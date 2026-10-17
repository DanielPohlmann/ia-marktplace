---
name: specs-documentation-gherkin
description: Use when looking up Gherkin syntax and tooling for BDD specifications. USE FOR: Feature, Rule, Scenario Outline, Examples, Background, tags, data tables, doc strings, step definitions, Cucumber/SpecFlow/Reqnroll/Behave, declarative style. DO NOT USE FOR: domain-driven acceptance criteria from user stories (use bdd-gherkin), Gauge specs (use specs-documentation-gauge), requirements (use specs-documentation-prd).
---

# Gherkin

## Overview
Gherkin is a structured, plain-language syntax for writing executable specifications in Behavior-Driven Development (BDD). It bridges the communication gap between business stakeholders, testers, and developers by expressing expected behavior in a human-readable format that also drives automated tests.

Gherkin files use the `.feature` extension and follow a strict keyword-based grammar that test runners (Cucumber, SpecFlow, Reqnroll, Behave) parse to execute step definitions written in code.

## Declarative vs Imperative Style

### Imperative (avoid)
Imperative scenarios describe the exact UI interactions -- they are brittle and hard to maintain.

```gherkin
Scenario: Login
  Given the user navigates to "https://app.example.com/login"
  And the user types "alice@example.com" into the field with id "email"
  And the user types "Str0ng!Pass" into the field with id "password"
  And the user clicks the button with id "login-btn"
  Then the page URL should be "https://app.example.com/dashboard"
  And the element with id "welcome-msg" should contain "Hello, Alice"
```

### Declarative (prefer)
Declarative scenarios describe the intended behavior without prescribing how the UI works.

```gherkin
Scenario: Login
  Given a registered user "Alice" with valid credentials
  When Alice logs in
  Then Alice should see her personalized dashboard
```

The step definitions handle the implementation details. When the UI changes, only step definitions need updating -- the feature file remains stable.

## Best Practices

- **One Feature per file** -- name the file after the feature (e.g., `shopping_cart.feature`).
- **Write declarative, not imperative scenarios** -- describe *what* should happen, not *how* the UI works.
- **Keep scenarios independent** -- no scenario should depend on the outcome of another. Use `Background` for shared setup.
- **Use Scenario Outline for data-driven tests** -- avoid duplicating scenarios that differ only in input/output values.
- **Limit steps per scenario** -- aim for 3-7 steps. If a scenario needs more, consider splitting it or abstracting steps.
- **Avoid conjunctive steps** -- a step like `Given the user is logged in and has items in the cart` should be two steps.
- **Use domain language, not technical jargon** -- feature files are a communication tool for the whole team.
- **Tag strategically** -- use tags for test suites (`@smoke`), priority (`@critical`), and feature areas (`@payments`), not for test management metadata.
- **Reuse steps across scenarios** -- write generic, parameterized step definitions that compose well.
- **Background should be short** -- if it grows beyond 3-4 steps, consider reorganizing the feature file.
- **Use Rules (Gherkin 6+)** to group scenarios by business rule within a feature.
- **Put feature files in a directory structure mirroring the application** -- e.g., `features/authentication/`, `features/cart/`, `features/checkout/`.

## Project Structure

```
features/
  authentication/
    login.feature
    registration.feature
  cart/
    add_to_cart.feature
    checkout.feature
  step_definitions/
    authentication_steps.js
    cart_steps.js
  support/
    hooks.js
    world.js
```

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/core-keywords.md](references/core-keywords.md) | Core Keywords — Feature, Scenario, Steps: Given / When / Then / And / But, Background, Scenario Outline (Scenario Template), Data Tables, … |
| [references/step-definitions.md](references/step-definitions.md) | Step Definitions — Cucumber (Java), SpecFlow / Reqnroll (C#), Behave (Python), Cucumber.js (JavaScript/TypeScript) |
| [references/complete-feature-file-example.md](references/complete-feature-file-example.md) | Complete Feature File Example |
| [references/details.md](references/details.md) | Test Runners |

## References

- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)
- [Cucumber Official Documentation](https://cucumber.io/docs/)

See references/rules.md for the full rule catalog.
