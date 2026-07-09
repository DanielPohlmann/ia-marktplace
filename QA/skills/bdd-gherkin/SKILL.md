---
name: bdd-gherkin
description: Use when authoring Gherkin/Cucumber .feature files or BDD acceptance criteria for LinkDaily — translating business requirements and user stories into domain-driven Given/When/Then specifications. USE FOR: writing feature files, BDD scenarios, executable acceptance criteria, expressing a business rule as single-focused Given/When/Then scenarios in the ubiquitous language (professional, client, appointment, take-rate, review), data tables, backgrounds, scenario outlines. DO NOT USE FOR: running or executing tests or writing step-definition/automation glue code (use playwright-cli), .NET unit/integration test generation (use dotnet-test:code-testing-generator), Vue component tests (use vue-testing-best-practices).
---

# BDD with Gherkin

## Overview

Write Gherkin/Cucumber `.feature` files that read as **business specifications**,
not automation scripts. Scenarios describe observable behavior in the domain's
ubiquitous language so a professional, a product owner, and a developer all read
the same truth.

This skill **authors the specification**. Executing it is a different job:
`playwright-cli` drives the browser and step definitions; `dotnet-test` covers
.NET tests. Keep the `.feature` free of any automation mechanics.

**Core principle:** one behavior per scenario, expressed declaratively (WHAT
happens, never HOW the UI or API does it), in LinkDaily's language.

## When to use

- Turning a user story or business rule into acceptance criteria.
- Writing `.feature` files for Scheduling, Payments, Reviews, Presentation, etc.
- Documenting behavior as executable specification before automation exists.

**When NOT to use:** writing the step-definition glue or running tests
(`playwright-cli`), generating .NET tests (`dotnet-test:code-testing-generator`),
Vue component tests (`vue-testing-best-practices`).

## Ask before you write

Never invent business rules. Before generating scenarios, confirm:

1. **What capability is this?** — frames the `Feature`.
2. **Who is the actor?** — professional, client, admin (perspective of steps).
3. **What business value?** — decides the `As a / I want / So that` line.
4. **What are the rules and edge cases?** — becomes the scenarios.
5. **Any shared precondition?** — decides the `Background`.

Do **not** ask single-focused vs. journey — always default to single-focused
unless the user explicitly requests a journey / end-to-end flow.

## Core principles

### Domain-driven language

Use LinkDaily's ubiquitous language. Prioritize business actions, outcomes, and
rules; allow a minimal technical term only when it genuinely adds clarity.

**Good — business-focused:**
```gherkin
Given a professional on the Free plan with 4 appointments booked this month
When a client books an appointment
Then the booking is rejected
And the professional is prompted to upgrade the plan
```

**Bad — implementation leaking through:**
```gherkin
Given the appointments table has 4 rows where professional_id = 42
When a POST is sent to /api/appointments with JSON { "slot": "..." }
Then the HTTP response status code is 402
```

### Single-focused scenarios (default)

Each scenario proves **one** business rule and runs independently. Do not chain
capabilities into a journey unless the user explicitly asks for one.

### Declarative, not imperative

Say *what* the actor achieves ("the client books an appointment"), not the
click-by-click path ("clicks #book, waits for spinner, clicks Confirm").

## Given / When / Then

- **Given** — context and preconditions only. No actions. Present state / past
  fact: "a professional has…", "the appointment is confirmed".
- **When** — the single action under test. Prefer **exactly one `When`**. One
  behavior, one logical action per scenario; add an `And` under `When` only when
  a single action genuinely spans two steps. Push data and parameters into the
  `Given` context, never into extra action steps.
- **Then** — an observable, checkable business outcome. Present tense: "the
  booking is confirmed", "a 10% take-rate is applied". Never a vague "it works".
- **And / But** — chain additional context or assertions; keep it readable.

## Formatting standards

- File extension `*.feature`; filename in **kebab-case**
  (`appointment-booking.feature`), one `Feature` per file.
- Indent block bodies by **2 spaces**.
- Keep lines under **120 characters**.
- One blank line between the `Feature` header and `Background`/first scenario,
  and between adjacent scenarios. **No** blank lines between steps within a
  scenario or background.
- **No comments** — the scenario text must self-explain.

## Scenario structure rules

- Behavior-focused, single-line title (`Silver-tier professional keeps full
  take-rate`), not `Test 1`.
- Aim for **fewer than 10 steps**; scenarios execute chronologically top to
  bottom.
- Strict **Given → When → Then** order. Never repeat a phase (no second `Given`
  block after the `When`).
- No `Or` keyword — use separate scenarios or a `Scenario Outline`.
- Prefer meaningful starting **state** over navigation tours.
- Steps stay at the **domain level**: no selectors, XPath, DOM, `wait for`,
  scroll/click mechanics, no HTTP endpoints or SQL — unless the behavior is
  inherently at that layer (an API contract feature).
- Use **concrete, realistic** example data (real names, amounts, dates, slugs).
  Never `foo`, `bar`, `test`, `lorem` — except when deliberately testing
  invalid input.

## Data tables and doc strings

Use a data table when a step carries 2+ fields or would otherwise run long.

**Multiple records — horizontal headers:**
```gherkin
Given the following services are in the professional's catalog:
  | Service        | Duration | Price |
  | Haircut        | 45       | 80    |
  | Beard trim     | 20       | 40    |
  | Full grooming  | 75       | 150   |
```

**One entity, many fields — vertical key/value:**
```gherkin
Given a client books an appointment with the following details:
  | Service   | Haircut            |
  | Date      | 2026-07-15         |
  | Time      | 14:30              |
  | Address   | 120 Oak Street     |
```

**Don't** cram it inline:
```gherkin
Given a client books a Haircut on 2026-07-15 at 14:30 at 120 Oak Street with notes "please be on time"
```

Use a doc string for larger free text:
```gherkin
Given a client leaves this review for a completed appointment:
  """
  Arrived right on time and did a fantastic job.
  Booking through the profile link was effortless.
  """
When the review is submitted
Then the review is published on the professional's public profile
```

## Scenario Outlines

Prefer regular `Scenario`. Reach for an outline **only** when the identical
behavior must be proven across genuinely varying inputs — not to mass-generate
rows.

```gherkin
Scenario Outline: Take-rate decreases as the professional's plan tier rises
  Given a professional on the <plan> plan
  When a client pays 200 for an appointment
  Then the platform take-rate is <rate> percent

  Examples: Plan tiers
    | plan     | rate |
    | Free     | 15   |
    | Pro      | 10   |
    | Business | 5    |
```

## Tags and Background

- **Tags:** minimal. Only `@wip`, execution-filter needs, or when explicitly
  requested. Avoid reflexive `@smoke`/`@regression`/`@critical`.
- **Background:** use liberally when 2+ scenarios share setup — but only one
  `Background` per `Feature`, and not when a single scenario needs the setup.

## Feature file template

```gherkin
Feature: [Business capability]
  As a [professional | client | admin]
  I want [capability]
  So that [business value]

  Background:
    Given [precondition shared by all scenarios]

  Scenario: [happy-path behavior]
    Given [context]
    And [more context]
    When [the single action]
    Then [observable outcome]
    And [additional observable outcome]

  Scenario: [edge case or rule violation]
    Given [specific context]
    When [action that triggers the rule]
    Then [expected business behavior]
```

## Worked example (Scheduling)

```gherkin
Feature: Appointment booking within plan limits
  As a client
  I want to book an appointment with a professional
  So that I reserve a confirmed time slot

  Background:
    Given the professional accepts online bookings

  Scenario: Client books an available slot
    Given the professional has a free slot on 2026-07-15 at 14:30
    When a client books that slot
    Then the appointment is confirmed
    And the professional is notified of the booking

  Scenario: Booking is rejected when the monthly plan limit is reached
    Given the professional is on the Free plan
    And 5 appointments are already booked this month
    When a client books another appointment
    Then the booking is rejected
    And the client is told the professional is fully booked this month

  Scenario: Overlapping slot cannot be double-booked
    Given the professional has a confirmed appointment on 2026-07-15 at 14:30
    When another client books the 14:30 slot on 2026-07-15
    Then the booking is rejected
    And the slot is shown as unavailable
```

## Anti-patterns

**❌ Automation mechanics in steps**
```gherkin
When the client clicks "#book-btn" and the Selenium driver waits 2s
Then the API returns HTTP 200 and the row commits to the appointments table
```
**✓ Business action and outcome**
```gherkin
When the client books the slot
Then the appointment is confirmed
```

**❌ Multiple actions bundled into one scenario**
```gherkin
When the client enters the date
And enters the time
And enters the address
And submits the booking
```
**✓ One action, data in Given**
```gherkin
Given a client books an appointment with the following details:
  | Date    | 2026-07-15 |
  | Time    | 14:30      |
  | Address | 120 Oak St |
When the client confirms the booking
Then the appointment is confirmed
```

**❌ Scenario Outline with a single row / no real variation**
```gherkin
Scenario Outline: Book appointment
  When a client pays <amount>
  Examples:
    | amount |
    | 200    |
```
**✓ A plain scenario when inputs don't change behavior**
```gherkin
Scenario: Client pays for an appointment
  When the client pays for the appointment
  Then the payment is captured
```

**❌ Journey scenario when not requested** — chaining browse → book → pay →
review in one scenario. **✓** Split into single-focused scenarios.

**❌ Vague outcome** (`Then it works`) — **✓** state the observable signal
(`Then the appointment is confirmed`).

## Validation checklist

Before finalizing, verify every box:

- [ ] Domain/business language throughout; minimal technical terms.
- [ ] Each scenario is **single-focused** (no journey unless requested).
- [ ] Strict Given → When → Then order; no repeated phases.
- [ ] **One behavior, prefer a single `When`**; data lives in `Given`.
- [ ] Data tables used for `Given` steps with 2+ fields or long values.
- [ ] Regular `Scenario` by default; `Scenario Outline` only for real variation.
- [ ] Behavior-focused titles; fewer than 10 steps.
- [ ] Concrete, realistic data — no `foo`/`bar`.
- [ ] `Then` outcomes are observable and checkable.
- [ ] No selectors, XPath, HTTP, or SQL (unless an API-layer feature).
- [ ] `*.feature`, kebab-case, one `Feature`/file, 2-space indent, <120 chars.
- [ ] Tags minimal; `Background` used only for shared setup.
- [ ] Readable by a non-technical stakeholder.

## References

- angelo-v — bdd-gherkin skill:
  https://github.com/angelo-v/opencode-playground/blob/main/.opencode/skills/bdd-gherkin/SKILL.md
- AutomationPanda — Gherkin guidelines for AI:
  https://github.com/AutomationPanda/gherkin-guidelines-for-ai/blob/main/gherkin-guidelines.md
