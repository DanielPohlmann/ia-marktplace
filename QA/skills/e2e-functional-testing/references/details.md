<!-- Part of the e2e-functional-testing skill. Loaded on demand from SKILL.md. -->

# E2E Functional Testing (Aspire + Playwright .NET) — details

## Harness: boot the stack correctly

The current `AppHostFixture` starts the app but does **not** wait for health — the
first fix any test author should make. Boot, then wait for the resources the test
touches to be healthy, with a timeout.

```csharp
public sealed class AppHostFixture : IAsyncLifetime
{
    private DistributedApplication _app = null!;

    public Uri GetEndpoint(string resource, string endpoint = "http")
        => _app.GetEndpoint(resource, endpoint);

    public HttpClient CreateHttpClient(string resource, string endpoint = "http")
        => _app.CreateHttpClient(resource, endpoint);

    public string GetConnectionString(string resource)   // for DB-level test-data seeding
        => _app.GetConnectionStringAsync(resource).GetAwaiter().GetResult()!;

    public async Task InitializeAsync()
    {
        var appHost = await DistributedApplicationTestingBuilder
            .CreateAsync<Projects.MyApp_AppHost>(["--environment=Testing"]);

        appHost.Services.ConfigureHttpClientDefaults(c => c.AddStandardResilienceHandler());

        // Frontends (npm dev servers) are slow to boot — budget minutes, not seconds.
        using var cts = new CancellationTokenSource(TimeSpan.FromMinutes(5));

        _app = await appHost.BuildAsync(cts.Token);
        await _app.StartAsync(cts.Token);

        // Wait until the resources our tests exercise are actually usable (healthy,
        // not merely Running). A missing/mistyped resource name hangs to the timeout.
        await _app.ResourceNotifications.WaitForResourceHealthyAsync("api", cts.Token);
        await _app.ResourceNotifications.WaitForResourceHealthyAsync("admin-spa", cts.Token);
        await _app.ResourceNotifications.WaitForResourceHealthyAsync("public-nuxt", cts.Token);
    }

    public async Task DisposeAsync()
    {
        await _app.StopAsync();
        await _app.DisposeAsync();
    }
}

[CollectionDefinition("AppHost")]
public sealed class AppHostCollection : ICollectionFixture<AppHostFixture>;
```

**Frontend health pitfall:** `AddNpmApp` resources have no health check by
default, so `WaitForResourceHealthyAsync` waits only for *Running*, not *ready to
serve*. Add an HTTP health check to the frontends in the AppHost
(`.WithHttpHealthCheck("/")`) so "healthy" means the dev server actually answers.
Without it, fall back to `WaitForResourceAsync(resource, KnownResourceStates.Running)`
plus a short readiness poll with Playwright's own auto-waiting `GotoAsync`.

## Browser fixture: evidence on failure

Playwright ships a `PageTest` base class only for **NUnit and MSTest** — there is
no xUnit equivalent, so own the browser lifecycle yourself in a fixture. Give it a
factory that starts a trace and stops it into a per-test file, so a red test always
leaves a `trace.zip` you can open with `playwright show-trace`.

```csharp
public sealed class PlaywrightFixture : IAsyncLifetime
{
    public IBrowser Browser { get; private set; } = null!;
    private IPlaywright _pw = null!;

    public async Task InitializeAsync()
    {
        _pw = await Playwright.CreateAsync();
        Browser = await _pw.Chromium.LaunchAsync(new() { Headless = true });
    }

    // One isolated context per test → no cookie/localStorage bleed between tests.
    public async Task<(IBrowserContext, IPage)> NewPageAsync(string? storageState = null)
    {
        var context = await Browser.NewContextAsync(new()
        {
            StorageStatePath = storageState,
            IgnoreHTTPSErrors = true,
        });
        await context.Tracing.StartAsync(new() { Screenshots = true, Snapshots = true, Sources = true });
        return (context, await context.NewPageAsync());
    }

    public async Task DisposeAsync()
    {
        await Browser.DisposeAsync();
        _pw.Dispose();
    }
}
```

In the test, stop the trace only when it failed:

```csharp
var (context, page) = await _playwright.NewPageAsync();
try
{
    // ... the flow + assertions ...
}
catch
{
    await context.Tracing.StopAsync(new() { Path = $"traces/{nameof(SomeTest)}.zip" });
    await page.ScreenshotAsync(new() { Path = $"traces/{nameof(SomeTest)}.png" });
    throw;
}
finally { await context.DisposeAsync(); }
```

## Locators: priority order

Locate elements the way a user or assistive tech perceives them. This survives
CSS refactors and reads as intent.

| Priority | Locator | Use for |
|---|---|---|
| 1 | `GetByRole(AriaRole.Button, new() { Name = "Book" })` | buttons, links, headings, inputs by accessible name |
| 2 | `GetByLabel("Email")` | form fields tied to a `<label>` |
| 3 | `GetByPlaceholder`, `GetByText` | text with no better handle |
| 4 | `GetByTestId("book-appointment")` | when no semantic anchor exists |
| 5 | CSS / XPath | last resort only |

**Typical reality:** most components (e.g. the admin login form) render naive-ui
inputs with **i18n labels and no `data-testid`**. Prefer `GetByLabel` / `GetByRole`
against the rendered label today; when a flow has no stable semantic anchor, add a
`data-testid` to the component in the same PR rather than reaching for a brittle
CSS chain. Playwright's `GetByTestId` matches `data-testid` by default (align on it;
change globally only via `Playwright.Selectors.SetTestIdAttribute` if the app uses
another attribute).

## Auth reuse via storage state

Logging in through the UI on every test is slow and fragile. Sign in **once**,
save the storage state, and open authenticated contexts from it.

```csharp
// once (e.g. a collection fixture): drive the real login, then persist the session
await loginPage.SignInAsync("pro@example.com", "Str0ng!pass");
await Expect(page.GetByRole(AriaRole.Heading, new() { Name = "Dashboard" })).ToBeVisibleAsync();
await context.StorageStateAsync(new() { Path = "auth/professional.json" });

// each authenticated test:
var (context, page) = await _playwright.NewPageAsync(storageState: "auth/professional.json");
```

Keep **one** UI-login test that proves the login flow itself; everything else
reuses the saved state. Gitignore the `auth/` directory — the file holds live
cookies and tokens. Storage state captures cookies + localStorage + IndexedDB but
**not** sessionStorage; if a flow depends on sessionStorage, re-inject it with
`AddInitScriptAsync`.

## Worked example: client books an appointment

```csharp
[Collection("AppHost")]
public sealed class AppointmentBookingTests(AppHostFixture appHost, PlaywrightFixture playwright)
    : IClassFixture<PlaywrightFixture>
{
    [Fact]
    public async Task Client_GivenAvailableSlot_ShouldConfirmAppointment()
    {
        // Arrange — seed a professional with a bookable slot through the API
        var slug = $"maria-{Guid.NewGuid():N}";
        using var api = appHost.CreateHttpClient("api");
        await SeedProfessionalWithSlotAsync(api, slug, date: "2026-07-15", time: "14:30");

        var publicUrl = appHost.GetEndpoint("public-nuxt");
        var (context, page) = await playwright.NewPageAsync();
        try
        {
            // Act — the client journeys through the public profile
            await page.GotoAsync($"{publicUrl}{slug}");
            await page.GetByRole(AriaRole.Button, new() { Name = "Book" }).ClickAsync();
            await page.GetByRole(AriaRole.Button, new() { Name = "14:30" }).ClickAsync();
            await page.GetByRole(AriaRole.Button, new() { Name = "Confirm booking" }).ClickAsync();

            // Assert — the client sees a confirmed appointment
            await Expect(page.GetByText("Appointment confirmed")).ToBeVisibleAsync();
        }
        catch
        {
            await context.Tracing.StopAsync(new() { Path = "traces/book-appointment.zip" });
            throw;
        }
        finally { await context.DisposeAsync(); }
    }
}
```
