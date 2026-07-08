# Validot Rules

Best practices and rules for Validot.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Create `Validator<T>` instances once and register them as singletons | MEDIUM | [`validot-create-validator-t-instances-once-and-register-them-as.md`](validot-create-validator-t-instances-once-and-register-them-as.md) |
| 2 | Define specifications as `static readonly` fields in dedicated specification classes | MEDIUM | [`validot-define-specifications-as-static-readonly-fields-in.md`](validot-define-specifications-as-static-readonly-fields-in.md) |
| 3 | Use `.Member()` with nested specifications for object graph validation | HIGH | [`validot-use-member-with-nested-specifications-for-object-graph.md`](validot-use-member-with-nested-specifications-for-object-graph.md) |
| 4 | Use `.WithMessage()` on every rule to provide context-specific error messages | CRITICAL | [`validot-use-withmessage-on-every-rule-to-provide-context-specific.md`](validot-use-withmessage-on-every-rule-to-provide-context-specific.md) |
| 5 | Use `.Optional()` on nullable or optional members | MEDIUM | [`validot-use-optional-on-nullable-or-optional-members.md`](validot-use-optional-on-nullable-or-optional-members.md) |
| 6 | Check `result.AnyErrors` before accessing `result.MessageMap` | HIGH | [`validot-check-result-anyerrors-before-accessing-result-messagemap.md`](validot-check-result-anyerrors-before-accessing-result-messagemap.md) |
| 7 | Map `result.MessageMap` to ASP.NET Core's `Results.ValidationProblem(IDictionary<string, string[]>)` format | MEDIUM | [`validot-map-result-messagemap-to-asp-net-core-s-results.md`](validot-map-result-messagemap-to-asp-net-core-s-results.md) |
| 8 | Use `.Rule(predicate)` for custom validation logic | CRITICAL | [`validot-use-rule-predicate-for-custom-validation-logic.md`](validot-use-rule-predicate-for-custom-validation-logic.md) |
| 9 | Do not use Validot for validation that requires database lookups or external API calls | CRITICAL | [`validot-do-not-use-validot-for-validation-that-requires-database.md`](validot-do-not-use-validot-for-validation-that-requires-database.md) |
| 10 | Write unit tests that instantiate the validator, pass both valid and invalid objects, and assert on `result.AnyErrors` and specific paths in `result.MessageMap` | CRITICAL | [`validot-write-unit-tests-that-instantiate-the-validator-pass-both.md`](validot-write-unit-tests-that-instantiate-the-validator-pass-both.md) |

---

---
title: "Check `result.AnyErrors` before accessing `result.MessageMap`"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Check `result.AnyErrors` before accessing `result.MessageMap`

Check `result.AnyErrors` before accessing `result.MessageMap`: to avoid unnecessary enumeration; `AnyErrors` is a fast boolean check that does not allocate, while `MessageMap` builds a dictionary on access.

---

---
title: "Compose complex rules"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation
---

## Compose complex rules

Compose complex rules

---

---
title: "Consider performance"
impact: LOW
impactDescription: "recommended but situational"
tags: validot, dotnet, validation
---

## Consider performance

Consider performance

---

---
title: "Create reusable specifications"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation
---

## Create reusable specifications

Create reusable specifications

---

---
title: "Create `Validator<T>` instances once and register them as singletons"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Create `Validator<T>` instances once and register them as singletons

Create `Validator<T>` instances once and register them as singletons: in the DI container, because the factory method compiles the specification into an optimized validation plan with pre-allocated error templates; creating new validators per request wastes the compilation cost.

---

---
title: "Define specifications as `static readonly` fields in dedicated specification classes"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Define specifications as `static readonly` fields in dedicated specification classes

(e.g., `OrderSpecifications.CreateOrderSpec`) rather than inline in service constructors, so that specifications are discoverable, reusable across validators, and unit-testable independently.

---

---
title: "Do not use Validot for validation that requires database lookups or external API calls"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Do not use Validot for validation that requires database lookups or external API calls

Do not use Validot for validation that requires database lookups or external API calls: because Validot's validation pipeline is synchronous; use FluentValidation with `MustAsync` for rules that need async I/O, or split validation into a synchronous Validot pass for format checks and a separate async service call for uniqueness/existence checks.

---

---
title: "Map `result.MessageMap` to ASP.NET Core's `Results.ValidationProblem(IDictionary<string, string[]>)` format"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Map `result.MessageMap` to ASP.NET Core's `Results.ValidationProblem(IDictionary<string, string[]>)` format

Map `result.MessageMap` to ASP.NET Core's `Results.ValidationProblem(IDictionary<string, string[]>)` format: for API endpoints, so that front-end clients receive standard RFC 7807 problem details with per-field error arrays that integrate with form validation libraries.

---

---
title: "Use appropriate error messages"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation
---

## Use appropriate error messages

Use appropriate error messages

---

---
title: "Use `.Member()` with nested specifications for object graph validation"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Use `.Member()` with nested specifications for object graph validation

Use `.Member()` with nested specifications for object graph validation: and `.AsCollection()` for list properties, composing small specifications into larger ones; avoid writing a single monolithic specification that validates the entire request in one flat chain.

---

---
title: "Use `.Optional()` on nullable or optional members"
impact: MEDIUM
impactDescription: "general best practice"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Use `.Optional()` on nullable or optional members

Use `.Optional()` on nullable or optional members: before applying further rules, so that null values pass validation without triggering subsequent rules; without `.Optional()`, a null `Notes` field would fail a `.MaxLength()` check with a confusing null reference error.

---

---
title: "Use `.Rule(predicate)` for custom validation logic"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Use `.Rule(predicate)` for custom validation logic

Use `.Rule(predicate)` for custom validation logic: that Validot's built-in rules do not cover (e.g., password complexity, business-specific formats), keeping the predicate as a pure function without side effects so it can be safely invoked during the synchronous validation pass.

---

---
title: "Use `.WithMessage()` on every rule to provide context-specific error messages"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Use `.WithMessage()` on every rule to provide context-specific error messages

Use `.WithMessage()` on every rule to provide context-specific error messages: rather than relying on Validot's default messages, because default messages reference the rule type (e.g., "Must not be empty") without mentioning the field name, which is unhelpful in API responses.

---

---
title: "Validate at boundaries"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: validot, dotnet, validation
---

## Validate at boundaries

Validate at boundaries

---

---
title: "Write unit tests that instantiate the validator, pass both valid and invalid objects, and assert on `result.AnyErrors` and specific paths in `result.MessageMap`"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: validot, dotnet, validation, defining-high-performance-validation-specifications-using-validots-fluent-specification-builder-use-when-you-need-allocation-free-validation-with-reusable-specifications, fast-execution, and-detailed-error-output
---

## Write unit tests that instantiate the validator, pass both valid and invalid objects, and assert on `result.AnyErrors` and specific paths in `result.MessageMap`

, verifying that each rule produces the expected error at the expected path; do not rely solely on integration tests through the HTTP pipeline.
