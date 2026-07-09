# Gherkin Rules

Best practices and rules for Gherkin.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | One Feature per file | MEDIUM | [`gherkin-one-feature-per-file.md`](gherkin-one-feature-per-file.md) |
| 2 | Write declarative, not imperative scenarios | MEDIUM | [`gherkin-write-declarative-not-imperative-scenarios.md`](gherkin-write-declarative-not-imperative-scenarios.md) |
| 3 | Keep scenarios independent | MEDIUM | [`gherkin-keep-scenarios-independent.md`](gherkin-keep-scenarios-independent.md) |
| 4 | Use Scenario Outline for data-driven tests | HIGH | [`gherkin-use-scenario-outline-for-data-driven-tests.md`](gherkin-use-scenario-outline-for-data-driven-tests.md) |
| 5 | Limit steps per scenario | LOW | [`gherkin-limit-steps-per-scenario.md`](gherkin-limit-steps-per-scenario.md) |
| 6 | Avoid conjunctive steps | HIGH | [`gherkin-avoid-conjunctive-steps.md`](gherkin-avoid-conjunctive-steps.md) |
| 7 | Use domain language, not technical jargon | MEDIUM | [`gherkin-use-domain-language-not-technical-jargon.md`](gherkin-use-domain-language-not-technical-jargon.md) |
| 8 | Tag strategically | CRITICAL | [`gherkin-tag-strategically.md`](gherkin-tag-strategically.md) |
| 9 | Reuse steps across scenarios | MEDIUM | [`gherkin-reuse-steps-across-scenarios.md`](gherkin-reuse-steps-across-scenarios.md) |
| 10 | Background should be short | LOW | [`gherkin-background-should-be-short.md`](gherkin-background-should-be-short.md) |
| 11 | Use Rules (Gherkin 6+) | MEDIUM | [`gherkin-use-rules-gherkin-6.md`](gherkin-use-rules-gherkin-6.md) |
| 12 | Put feature files in a directory structure mirroring the application | MEDIUM | [`gherkin-put-feature-files-in-a-directory-structure-mirroring-the.md`](gherkin-put-feature-files-in-a-directory-structure-mirroring-the.md) |

---

---
title: "Avoid conjunctive steps"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Avoid conjunctive steps

Avoid conjunctive steps: a step like `Given the user is logged in and has items in the cart` should be two steps.

---

---
title: "Background should be short"
impact: LOW
impactDescription: "recommended but situational"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Background should be short

Background should be short: if it grows beyond 3-4 steps, consider reorganizing the feature file.

---

---
title: "Keep scenarios independent"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Keep scenarios independent

Keep scenarios independent: no scenario should depend on the outcome of another. Use `Background` for shared setup.

---

---
title: "Limit steps per scenario"
impact: LOW
impactDescription: "recommended but situational"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Limit steps per scenario

Limit steps per scenario: aim for 3-7 steps. If a scenario needs more, consider splitting it or abstracting steps.

---

---
title: "One Feature per file"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## One Feature per file

One Feature per file: name the file after the feature (e.g., `shopping_cart.feature`).

---

---
title: "Put feature files in a directory structure mirroring the application"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Put feature files in a directory structure mirroring the application

Put feature files in a directory structure mirroring the application: e.g., `features/authentication/`, `features/cart/`, `features/checkout/`.

---

---
title: "Reuse steps across scenarios"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Reuse steps across scenarios

Reuse steps across scenarios: write generic, parameterized step definitions that compose well.

---

---
title: "Tag strategically"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Tag strategically

Tag strategically: use tags for test suites (`@smoke`), priority (`@critical`), and feature areas (`@payments`), not for test management metadata.

---

---
title: "Use domain language, not technical jargon"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Use domain language, not technical jargon

Use domain language, not technical jargon: feature files are a communication tool for the whole team.

---

---
title: "Use Rules (Gherkin 6+)"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Use Rules (Gherkin 6+)

Use Rules (Gherkin 6+): to group scenarios by business rule within a feature.

---

---
title: "Use Scenario Outline for data-driven tests"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Use Scenario Outline for data-driven tests

Use Scenario Outline for data-driven tests: avoid duplicating scenarios that differ only in input/output values.

---

---
title: "Write declarative, not imperative scenarios"
impact: MEDIUM
impactDescription: "general best practice"
tags: gherkin, specs, documentation, bdd-acceptance-criteria, executable-specifications, givenwhenthen-scenarios
---

## Write declarative, not imperative scenarios

Write declarative, not imperative scenarios: describe *what* should happen, not *how* the UI works.
