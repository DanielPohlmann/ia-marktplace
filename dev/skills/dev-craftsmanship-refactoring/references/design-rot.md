# Design Rot

Code smells describe a single spot. Design rot describes how the *system* resists change. Robert C. Martin named four symptoms; they are useful because each one can be observed in ordinary work — a diff, a bug report, an estimate — instead of argued about in the abstract.

## The four symptoms

| Symptom | What you observe | Typical root cause |
|---|---|---|
| **Rigidity** | A small requirement change touches many files or modules. Estimates grow because "it is never just one place". | Logic duplicated across modules; high-level policy depending on low-level details. |
| **Fragility** | A change in one place breaks something in an apparently unrelated place. Bug fixes generate new bugs. | Hidden coupling — shared mutable state, implicit ordering, the same rule implemented twice with drift. |
| **Immobility** | A piece that would be useful elsewhere cannot be reused without dragging half the codebase with it, so it gets copied instead. | Business logic tangled with infrastructure (database, HTTP, file system) or with UI. |
| **Viscosity** | Doing it the right way is harder than doing a hack, so hacks win. Also applies to the environment: slow builds and tests push people toward skipping them. | Design that fights the change direction; missing seams; slow feedback loops. |

## Detecting them in review

| Signal in a PR or in history | Likely symptom |
|---|---|
| A one-line requirement produced a diff across 5+ files that each repeat the same edit | Rigidity |
| The PR fixes a regression introduced by the previous PR on a different feature | Fragility |
| A class or function was copied into a new module "with small changes" | Immobility |
| The change adds a special case (`if (customer == X)`) instead of extending the abstraction that already exists | Viscosity |
| Tests were skipped or disabled "because they take too long" | Viscosity (environment) |

## Using the symptoms to decide when to refactor

- **Refactor now** when the task at hand is paying the rot tax: if the feature needs the same edit in many places, unify those places first, then make the edit once.
- **Refactor now** when a bug fix exposes fragility: fix the coupling that let the bug travel, not only the bug.
- **Record and defer** when the rot is real but the current task does not touch it — open a ticket that names the symptom and the evidence (files, PRs).
- **Leave it** when the code is stable and nobody needs to change it; rot only costs something when change happens.

## Reporting a finding

Name the symptom, show the evidence, and state the cost in terms of the next change:

> Rigidity: adding the new tax rule required the same edit in `InvoiceService`, `QuoteService` and `RefundService`. Extracting the rule into one policy object makes the next rule a one-file change.

Avoid reporting rot without evidence ("this code is rigid"). The point of the vocabulary is that each symptom is observable.
