---
name: dev-craftsmanship-oo-review
description: Use when reviewing or refactoring classes for OO design flaws (C#, Java, TypeScript). USE FOR: type-code conditionals, anemic entities, infrastructure new in domain code, static singletons, fat interfaces, suspicious overrides, primitive obsession, Law of Demeter, object calisthenics. DO NOT USE FOR: principle explanations (use dev-craftsmanship-solid), naming/readability (use dev-craftsmanship-clean-code), refactoring mechanics (use dev-craftsmanship-refactoring), pattern catalog (use dev-design-patterns).
---

# Object-Oriented Design Review

## Overview
A checklist for reviewing class-level design in OO code (C#, Java, TypeScript and similar). It maps **signals you can see in a diff** to the principle behind them and the **smallest correction** that removes the cost. It is a review tool, not a design method: every finding must pass the YAGNI gate before it is reported.

Principles are only named here — for the reasoning behind each one, load `dev-craftsmanship-solid`. For step-by-step transformations, load `dev-craftsmanship-refactoring`.

## Review workflow
1. Scan the diff for the signals in the table below.
2. For each hit, run the **YAGNI gate**. Drop or downgrade findings that fail it.
3. Check the **language exceptions** — many apparent violations are idiomatic.
4. Assign a **severity** and write the finding in the **finding format**.
5. When arguing "why now and not later", use the design-rot vocabulary (rigidity, fragility, immobility, viscosity) from `dev-craftsmanship-refactoring` — see its `references/design-rot.md`.

## Signal → principle → minimal correction

| # | Signal in code | Principle | Minimal correction |
|---|---|---|---|
| 1 | `switch`/`if` on a type code, enum or string, with business rules per branch | OCP | One Strategy per branch; selection moves to a single factory, registry map or DI registration |
| 2 | Clients doing `is`/`instanceof`/`as` checks before calling, or overrides that throw `NotSupported`/do nothing | LSP | Break the hierarchy: shared interface for what is truly common, composition for the rest |
| 3 | Interface methods implemented as "not supported"; interface grows with each new variant | ISP | Split into role interfaces by client need; rethink a forced abstraction |
| 4 | `new` of DB/HTTP/SDK clients, `DateTime.Now`, `Guid.NewGuid()`, env reads inside domain code | DIP | Own the dependency first (inject a concrete class you own); add an interface only for tests, a second implementation or a module boundary |
| 5 | Hand-written static singleton holding mutable state | DIP / testability | Register as a singleton lifetime in the DI container, or `Lazy<T>` for a pure, immutable value |
| 6 | Status string/enum with a public setter; transition checks scattered across services | Encapsulation / State | Private setter plus intention-revealing methods (`Approve()`, `Cancel()`) that guard transitions; State pattern only if per-state behavior grows |
| 7 | Entity with only getters/setters; every rule about it lives in services (anemic model) | Tell, don't ask | Move behavior to the class that owns the data |
| 8 | Primitives for domain concepts (email, money, tax documents, typed ids) validated in many places | Primitive obsession | Value object that validates once at construction |
| 9 | `a.B.C.D.DoSomething()` navigation through collaborators | Law of Demeter | Move the behavior to the object that owns the data (tell, don't ask); a delegating getter only hides the chain |
| 10 | Deep `else` cascades, nesting three or more levels | Readability of control flow | Guard clauses and early return |
| 11 | Same creation `if`/`switch` copied in several places | DRY / creation | One injectable factory or registry (avoid static factory methods — they block test substitution) |
| 12 | Parallel classes repeating the same sequence of steps with small differences | DRY / OCP | Template method, or composition of a fixed pipeline with injected steps |
| 13 | Optional behavior switched on by boolean flags or constructor options | OCP / SRP | Decorator per optional behavior |
| 14 | Logging, caching, retries, authorization or transactions inside business methods | SRP | Proxy/decorator, middleware or pipeline behavior |
| 15 | Long parameter lists, the same group of arguments traveling together | Cohesion | Parameter object (often becomes a value object) |

Before/after sketches for every row are in [references/signals-catalog.md](references/signals-catalog.md).

## YAGNI gate (apply before every finding)
Ask three questions. At least one must be **yes** to report the finding as a suggestion or blocker:

1. **Second real variant** — does a second implementation, branch or variant exist today (or is it in the current backlog, not imagined)?
2. **Concrete pain** — is there a bug, a change that had to be made in several places, or code that cannot be tested where tests are expected?
3. **Boundary** — does the code sit on a module, package, process or team boundary where decoupling is valuable by itself?

If all three are "no", drop the finding or downgrade it to a note. The reverse also holds: **a single implementation behind an interface with no test, second-implementation or boundary reason is itself a finding** — speculative indirection costs navigation and reading time.

## Severity guide

| Severity | Use for |
|---|---|
| **Blocking** | LSP violations that make existing callers fail or misbehave; shared mutable static state reachable from several threads/requests; infrastructure constructed inside domain code that prevents tests the team requires |
| **Suggestion** | OCP when variants are actively growing; introducing value objects; Demeter; object calisthenics rules; parameter objects; guard clauses |
| **Note** | Findings that failed the YAGNI gate but are worth recording |

Never block a change on line counts, method counts or parameter counts alone. A count is a prompt to look for the real problem (mixed responsibilities, missing concept); report that problem, not the number.

## Language and framework exceptions
- **Fluent APIs, builders, LINQ and stream pipelines** chain calls on the same or a freshly returned object — they are not Demeter violations. Demeter is about reaching through collaborators' internals.
- **DTOs, view models, API contracts and messages** are data holders on purpose. Getters/setters without behavior are correct there.
- **ORM-mapped entities** may need parameterless constructors, `virtual` members (lazy-loading proxies) or settable properties. Encapsulate behavior where the ORM allows (protected/private setters, backing fields, domain methods); do not fight the ORM to reach purity.
- **Value objects in C#**: modern C# `record`/`record struct` give value equality for free. In older C# versions write `Equals`/`GetHashCode` (and `==`) by hand. Java has `record` from 16+; in TypeScript compare explicitly with an `equals` method.
- **.NET naming**: keep the `I` prefix on interfaces; language conventions beat generic advice.
- **Static is fine** for pure, stateless functions and constants. The problem is static *mutable* state or static access to volatile infrastructure.

## Finding format
Every finding contains five parts:

1. **Code excerpt** — the smallest snippet that shows the signal, with file and line.
2. **Principle** — the name from the table above.
3. **Cost of not fixing** — concrete and tied to the next change: "adding a new carrier requires editing `ShippingService`, `QuoteService` and `LabelPrinter`".
4. **Smallest correction** — what to change now, not the ideal redesign.
5. **YAGNI justification** — which gate question answered yes, with evidence.

Example:

> **Suggestion — OCP** (`FeeCalculator.cs:42`)
> `switch (account.Type)` with distinct fee rules in each of four branches; the same switch appears in `StatementBuilder.cs:88`.
> Cost: the next account type needs coordinated edits in two files that already drifted (branch `Premium` rounds differently).
> Correction: extract `IFeePolicy` with one class per type, resolved in one registry.
> YAGNI: second real variant exists (four), concrete pain (drift between copies).

## Common pitfalls

| Pitfall | Why it hurts |
|---|---|
| Reporting a pattern name instead of a cost | The author cannot judge the trade-off; state what the next change costs |
| Interfaces "for future flexibility" | Fails the YAGNI gate and adds indirection |
| Flagging DTOs as anemic | DTOs carry data by design |
| Treating object calisthenics as rules | They are training constraints and review alarms, not laws |
| Proposing the full redesign in a review | Suggest the smallest correction that removes the cost; larger changes go to a separate ticket |

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/signals-catalog.md](references/signals-catalog.md) | Expanded signal table: each of the 15 signals with a short before/after sketch (TypeScript and C#), when to skip it and severity hints |
| [references/object-calisthenics.md](references/object-calisthenics.md) | The nine object calisthenics rules — intent, signal, correction technique and when not to apply each one, framed as an exercise and review alarms |
