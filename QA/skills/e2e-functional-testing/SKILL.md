---
name: e2e-functional-testing
description: Use when assessing, writing, or fixing .NET end-to-end tests that boot a distributed app via Aspire and drive a real browser. USE FOR: deciding if an E2E test is warranted, xUnit + Microsoft.Playwright + Aspire.Hosting.Testing, DistributedApplicationTestingBuilder, user journeys, Page Objects, web-first assertions, storage-state auth, failure traces. DO NOT USE FOR: ad-hoc browser exploration (use playwright-cli), .feature specs (use bdd-gherkin), unit tests (use dotnet-test:code-testing-generator).
---

# E2E Functional Testing (Aspire + Playwright .NET)

## Overview

Write **black-box functional tests** that boot the entire distributed
system and drive a real browser as a real user would. A typical suite lives in
`tests/E2E/<App>.E2E.Tests` and uses **xUnit + Microsoft.Playwright (.NET) +
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

The harness boots the real `<App>.AppHost`. Map each user-facing app to the
persona your tests simulate (example from a scheduling SaaS):

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

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | Harness: boot the stack correctly; Browser fixture: evidence on failure; Locators: priority order; Auth reuse via storage state; Worked example: client books an appointment |

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

**Sibling QA skills**
- `playwright-cli` — drive the browser interactively / debug a failing flow.
- `bdd-gherkin` — author the Given/When/Then spec these tests satisfy.
