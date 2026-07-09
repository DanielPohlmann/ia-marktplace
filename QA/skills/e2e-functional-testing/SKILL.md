---
name: e2e-functional-testing
description: Use when assessing, writing, or fixing end-to-end functional tests for LinkDaily that boot the whole distributed app via Aspire and drive a real browser to simulate a user — the suite in tests/E2E/LinkDaily.E2E.Tests. USE FOR: deciding if an E2E test is even warranted (analyze the spec + PR/diff first — a trigger is not a mandate), xUnit + Microsoft.Playwright (.NET) + Aspire.Hosting.Testing tests, booting the full stack with DistributedApplicationTestingBuilder, waiting for resources healthy, valid-scenario user journeys (admin/professional on admin-spa, client on public-nuxt), happy-path + main error flows, Page Objects, web-first assertions, auth reuse via storage state, deterministic test data, tracing/screenshots on failure. DO NOT USE FOR: driving a browser ad-hoc for exploration (use playwright-cli), authoring Gherkin/.feature specs (use bdd-gherkin), .NET unit/handler tests (use dotnet-test:code-testing-generator), Vue component tests with Vitest (use vue-testing-best-practices).
---

# E2E Functional Testing (Aspire + Playwright .NET)

## Overview

Write **black-box functional tests** that boot the entire LinkDaily distributed
system and drive a real browser as a real user would. The suite lives in
`tests/E2E/LinkDaily.E2E.Tests` and uses **xUnit + Microsoft.Playwright (.NET) +
Aspire.Hosting.Testing**.

**Core principle:** a functional E2E test proves *a user can complete a valuable
flow against the real system* — real Postgres, Redis, RabbitMQ, `api`, `worker`,
and the real frontends. It asserts on what the user sees, never on internal state.
If the assertion needs a `DbContext`, a mock, or a private method, it is a unit or
integration test, not this.

This skill covers **HOW to design and write** those tests. Driving a browser
interactively is `playwright-cli`; writing the business spec is `bdd-gherkin`.

## First: decide whether an E2E test is warranted

**Being invoked is not a mandate to write a test.** E2E is the most expensive
level of testing — it boots the entire stack and runs a real browser. Every time
this skill triggers, apply critical, situational judgment *before* writing a line:
do the analysis, justify the level, and if a cheaper test gives the same
confidence — or no test is needed — say so and stop. Never write an E2E test just
to satisfy the trigger.

Analyze four things, in order:

1. **The specification / acceptance criteria.** What observable behavior is
   actually claimed? Read the `.feature` file, user story, or task. No spec?
   Establish (or confirm with the requester) the intended behavior first —
   never invent it.
2. **The PR / diff, if one exists.** What *actually* changed, and does it alter a
   **runtime, user-facing flow**? A change to domain logic, a config file, a
   comment, or a backend contract with no UI path does not, by itself, justify an
   E2E test. Read the diff — do not assume from the task title.
3. **The existing suite and the plan — review before adding.** Read the current
   E2E tests and any planned coverage. Is this behavior *already exercised*? A
   broader journey traverses every step inside it: if a "client books and pays"
   test exists, a separate "client opens the profile" test is redundant. Never add
   a test whose risk is already covered by a larger one.
4. **The right test level.** E2E earns its cost only when the value is the
   **integration itself** — a complete flow crossing frontend → API → infra that
   no cheaper test can cover with confidence, and that no existing flow subsumes.

**Prefer the fewest tests that cover the risk.** One meaningful journey that
traverses several steps beats many granular tests for each step. Larger flows
subsume the smaller ones they pass through — reach for a smaller, focused test only
when it isolates a distinct risk (a specific error case, an edge condition) the
larger flow does not already prove. When a smaller test adds nothing, take another
path: fold it into the larger flow, cover it one level cheaper, or skip it.

**Write an E2E test when:** a user-usable flow is complete end-to-end, spans the
real frontend + API + infrastructure, its correctness depends on that integration,
and no existing journey already covers it (a client books an appointment; a
professional signs in and publishes a profile; a plan limit blocks a booking).

**Do NOT write an E2E test — recommend the cheaper level and stop — when:**

| Situation | Right level instead |
|---|---|
| Pure domain / handler / service logic | unit (`dotnet-test:code-testing-generator`) |
| API contract, status codes, payload shape | in-memory API (`Microsoft.AspNetCore.Mvc.Testing`) |
| A single Vue component's behavior | Vitest (`vue-testing-best-practices`) |
| The flow isn't usable end-to-end yet | wait — E2E covers complete features, not stubs |
| A broader journey already traverses this step | covered — don't add a granular duplicate |
| The journey is already covered by an existing E2E | extend/adjust it, don't duplicate |
| The smaller flow adds no distinct risk | fold it into the larger flow or cover it cheaper |
| Nothing runtime/user-facing changed (docs, config, comments) | no test needed — say so |

**State your conclusion before writing code:** what changed, what the existing
suite already covers, which level is right, and why E2E is (or is not) justified
here. If it is not justified, do not proceed — recommend the appropriate level,
point to the flow that already covers it, or explain why no test is warranted. Only
when E2E is the right level *and adds coverage no existing flow provides* do you
continue to the sections below.

## When to use

- Adding a test for a completed end-to-end feature (usable by a real user).
- Simulating the **professional/admin** on `admin-spa` or the **client** on
  `public-nuxt` through a full journey.
- Covering a happy path plus its main error cases at the UI level.
- Fixing flaky/slow E2E: startup races, hard waits, brittle selectors.

**When NOT to use:**

| Situation | Use instead |
|---|---|
| Exploring the UI / one-off browser driving | `playwright-cli` |
| Writing Given/When/Then `.feature` specs | `bdd-gherkin` |
| Backend handler/service/domain logic | `dotnet-test:code-testing-generator` |
| In-memory API contract test (no browser) | `Microsoft.AspNetCore.Mvc.Testing` |
| Vue component in isolation | `vue-testing-best-practices` |

## The system under test

The harness boots the real `LinkDaily.AppHost`. The two user-facing apps are the
personas your tests simulate:

| Persona | Aspire resource | App | Anchor routes |
|---|---|---|---|
| **Professional / admin** | `admin-spa` | Vue 3 SPA (naive-ui, Pinia, vue-i18n) | `/account/login`, `/account/register`, dashboard |
| **Client / public** | `public-nuxt` | Nuxt "link in bio" | `/{slug}` (public profile), `/login`, `/admin` (auth-guarded) |

Backend resources (`api`, `worker`, `postgres`, `redis`, `rabbitmq`, …) are
started too. **Never hardcode ports** — resolve every URL from the running app.

## Golden rules

0. **Justify the test before writing it.** Analyze the spec, the PR/diff, and the
   existing suite; confirm E2E is the right level and that no larger flow already
   covers it (see the gate above). Being triggered ≠ writing. Fewest tests that
   cover the risk.
1. **Boot the app once, wait until it is HEALTHY, then test.** Never race a
   frontend that is still starting.
2. **Resolve URLs from Aspire.** `app.GetEndpoint("admin-spa", "http")` — never a
   literal `http://localhost:7000`.
3. **Web-first assertions only.** `await Expect(locator).ToBeVisibleAsync()`
   auto-waits and retries. **No `Thread.Sleep`, no `WaitForTimeout`.**
4. **User-facing locators.** Prefer `GetByRole` / `GetByLabel` / `GetByText`;
   `GetByTestId` when semantics are absent; CSS/XPath as a last resort.
5. **Test the user's outcome**, in the ubiquitous language (professional, client,
   appointment, slug, take-rate) — never internal database state.
6. **Deterministic, isolated data.** Each test seeds and owns its own data via the
   API; never depend on another test's leftovers or on execution order.
7. **Capture evidence on failure.** Trace + screenshot for every failing test.

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
            .CreateAsync<Projects.LinkDaily_AppHost>(["--environment=Testing"]);

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

**LinkDaily reality:** most components (e.g. the admin login form) render naive-ui
inputs with **i18n labels and no `data-testid`**. Prefer `GetByLabel` / `GetByRole`
against the rendered label today; when a flow has no stable semantic anchor, add a
`data-testid` to the component in the same PR rather than reaching for a brittle
CSS chain. Playwright's `GetByTestId` matches `data-testid` by default (align on it;
change globally only via `Playwright.Selectors.SetTestIdAttribute` if the app uses
another attribute).

## Web-first assertions — never hard-wait

```csharp
using static Microsoft.Playwright.Assertions;

// ✅ auto-waits & retries until the app catches up, or fails with a clear diff
await Expect(page.GetByRole(AriaRole.Heading, new() { Name = "Appointment confirmed" }))
    .ToBeVisibleAsync();
await Expect(page).ToHaveURLAsync(new Regex("/dashboard"));

// ❌ flaky and slow — bans:
await Task.Delay(2000);
await page.WaitForTimeoutAsync(2000);
(await page.GetByRole(...).IsVisibleAsync()).Should().BeTrue(); // no retry
```

Actions (`ClickAsync`, `FillAsync`) already auto-wait for actionability — you do
not need to check visibility before acting.

## Page Object Model

Wrap each screen in a Page Object so selectors and flow live in one place and
tests read as user intent.

```csharp
public sealed class AdminLoginPage(IPage page, Uri baseUrl)
{
    public async Task GotoAsync() => await page.GotoAsync($"{baseUrl}account/login");

    public async Task SignInAsync(string email, string password)
    {
        await page.GetByLabel("Email").FillAsync(email);
        await page.GetByLabel("Password").FillAsync(password);
        await page.GetByRole(AriaRole.Button, new() { Name = "Login" }).ClickAsync();
    }
}
```

Page Objects expose **actions and queries**, not assertions — keep `Expect(...)`
in the test so the failure points at the behavior under test.

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

## Test data: deterministic and isolated

- **Seed through the API**, not by clicking. Use `_appHost.CreateHttpClient("api")`
  to arrange preconditions (a professional, a bookable slot) fast and reliably.
- **Own your data.** Generate unique identifiers per test (unique email/slug) so
  parallel tests never collide. Never assert on data another test created.
- **Assert on outcomes**, e.g. "the appointment is confirmed" as shown to the
  client — never by querying the database directly.
- Prefer **realistic** data (real names, amounts, dates, slugs), except when
  deliberately exercising invalid input.

## Structure & naming (match the repo)

- Test classes are `sealed`; one `[Collection("AppHost")]` so all tests share the
  single booted app; `IClassFixture<PlaywrightFixture>` for the browser.
- Method naming mirrors the codebase: `Flow_GivenCondition_ShouldOutcome`
  (e.g. `Client_GivenAvailableSlot_ShouldConfirmAppointment`).
- Folder by persona/area: `Browser/Admin/…`, `Browser/Public/…`.
- Cover the **happy path first**, then the main **error cases** of the same flow
  (rejected booking, plan limit reached, invalid credentials).

## Parallelization with one shared app

The app boots once (`ICollectionFixture`), so all E2E tests belong to the
`"AppHost"` collection and run **sequentially by default** (xUnit disables
parallelism within a collection). That is intentional — a single running stack
plus shared external state (Postgres, RabbitMQ) makes cross-test parallelism a
source of flakiness. Get isolation from **unique data + a fresh browser context
per test**, not from parallel collections.

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

## Common mistakes

| ❌ Mistake | ✅ Fix |
|---|---|
| Testing before frontends are ready | `WaitForResourceHealthyAsync` in the fixture, with a timeout |
| `http://localhost:7000` hardcoded | `appHost.GetEndpoint("admin-spa")` |
| `Thread.Sleep` / `WaitForTimeout` to "let it load" | web-first `Expect(...).ToBeVisibleAsync()` |
| `IsVisibleAsync().Should().BeTrue()` | `Expect(locator).ToBeVisibleAsync()` (retries) |
| Brittle CSS chains (`.n-form > div:nth-child(2) input`) | `GetByLabel` / `GetByRole`, add `data-testid` if needed |
| Asserting on DB rows / internal state | assert on what the user sees |
| Tests depend on each other's data or order | unique data per test, own your preconditions |
| Logging in via UI in every test | reuse `StorageState` |
| Silent failures with no evidence | trace + screenshot on failure |
| One giant test doing browse→book→pay→review | one valuable flow per test (happy path, then error cases) |
| Expecting a `PageTest` base class in xUnit | own the browser lifecycle in a fixture (PageTest is NUnit/MSTest only) |
| Booting the full Aspire app per test class | boot once per `ICollectionFixture`; classes share it |
| Recording video/trace for every run | keep artifacts only on failure |

## Validation checklist

- [ ] Analyzed spec + PR/diff + existing suite; confirmed E2E is the right level,
      not a cheaper test, and not already covered/subsumed by a larger flow.
- [ ] App booted once via `DistributedApplicationTestingBuilder`, waited healthy.
- [ ] Every URL resolved from Aspire (`GetEndpoint` / `CreateHttpClient`).
- [ ] Only web-first `Expect(...)` assertions; zero `Sleep`/`WaitForTimeout`.
- [ ] Locators are role/label/text first; `data-testid` added where needed.
- [ ] Fresh browser context per test; data unique and self-seeded.
- [ ] Assertions are on user-visible outcomes in the ubiquitous language.
- [ ] Class `sealed`, in `[Collection("AppHost")]`, `Flow_GivenCondition_ShouldOutcome`.
- [ ] Trace + screenshot captured on failure.
- [ ] Happy path plus the flow's main error cases covered.
- [ ] Browsers installed once: `pwsh bin/Debug/net10.0/playwright.ps1 install`.

## References

**.NET Aspire testing** (docs live on `aspire.dev`; `learn.microsoft.com/dotnet/aspire/*` redirects here)
- Write your first test — https://aspire.dev/testing/write-your-first-test/
- Accessing resources from tests — https://aspire.dev/testing/accessing-resources/
- Manage the AppHost lifecycle — https://aspire.dev/testing/manage-app-host/
- Testing in CI/CD — https://aspire.dev/testing/testing-in-ci/

**Playwright**
- Best Practices — https://playwright.dev/docs/best-practices
- Locators (.NET) — https://playwright.dev/dotnet/docs/locators
- Authentication / storage state (.NET) — https://playwright.dev/dotnet/docs/auth
- Trace Viewer (.NET) — https://playwright.dev/dotnet/docs/trace-viewer
- Playwright Test Agents (planner / generator / healer) — https://playwright.dev/docs/test-agents

**Skill / prompt guides worth borrowing from (market references)**
- Anthropic — Agent skill authoring best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic — public skills repository — https://github.com/anthropics/skills
- obra/superpowers — test-driven-development & testing-anti-patterns skills — https://github.com/obra/superpowers/tree/main/skills/test-driven-development
- github/awesome-copilot — Playwright .NET instructions — https://github.com/github/awesome-copilot/blob/main/instructions/playwright-dotnet.instructions.md
- aaronontheweb/dotnet-skills — "aspire-integration-testing" — https://agentskills.so/skills/aaronontheweb-dotnet-skills-aspire-integration-testing
- xUnit — shared context (collection fixtures) — https://xunit.net/docs/shared-context

**Sibling LinkDaily QA skills**
- `playwright-cli` — drive the browser interactively / debug a failing flow.
- `bdd-gherkin` — author the Given/When/Then spec these tests satisfy.
