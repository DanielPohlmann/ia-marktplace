# Object Calisthenics — Nine Rules as Review Alarms

Object calisthenics is a set of nine deliberately strict constraints, originally proposed as a **practice exercise**: write a small program obeying all nine and you are forced to discover small objects, value types and behavior placed next to data. In production code they are **alarms, not laws**. When a rule is broken, ask what the break is hiding — a missing concept, a misplaced responsibility — and report that, not the rule number. Findings based on these rules are at most **suggestions**, and they must pass the YAGNI gate in `SKILL.md`.

| # | Rule | Alarm points to |
|---|---|---|
| 1 | One level of indentation per method | Method doing several things |
| 2 | Don't use `else` | Tangled branching; missing guard clauses or polymorphism |
| 3 | Wrap all primitives and strings | Primitive obsession |
| 4 | First-class collections | Collection rules scattered around |
| 5 | One dot per line | Reaching through collaborators |
| 6 | Don't abbreviate | A name too long because the class does too much |
| 7 | Keep all entities small | Low cohesion |
| 8 | Limit instance variables (classic form: two) | Missing sub-objects |
| 9 | No getters/setters/properties | Behavior living outside the data owner |

---

## 1. One level of indentation per method

- **Intent:** each method works at one level of abstraction, so it can be read at a glance.
- **Signal:** loops inside conditionals inside loops; a method you must scroll to understand.
- **Correction:** extract the inner block into a well-named method; replace nested loops with a collection pipeline where that is clearer.
- **When not to apply:** algorithmic code (parsers, matrix work, tight loops) where nesting mirrors the problem and extraction scatters the logic. One level is the exercise; two or three is normal in production.

## 2. Don't use `else`

- **Intent:** make the main path obvious and push edge cases to the top.
- **Signal:** `if/else` ladders, especially deep or repeated ones; the happy path buried in the last branch.
- **Correction:** guard clauses with early return/throw; for type-based branching, polymorphism or a lookup map; for absent values, a null object or an optional type.
- **When not to apply:** a genuine two-way choice with similar weight (`return x > 0 ? a : b`) is clearer with `else` or a ternary. Do not contort code to avoid the keyword.

## 3. Wrap all primitives and strings

- **Intent:** give domain concepts a type, so validation and rules live in one place and the compiler catches mix-ups.
- **Signal:** the same validation repeated for a string or number; methods taking several parameters of the same primitive type in a row; units implied by variable names (`timeoutMs`, `amountCents`).
- **Correction:** a value object (C# `record`, Java `record`, TS class with `equals`), validated in its constructor. Typed ids for entity keys.
- **When not to apply:** a primitive with no rules used in one place; DTO and persistence layers (map to value objects at the boundary); hot paths where allocation measurably matters — prefer value types (`readonly record struct`) there instead of dropping the idea.

## 4. First-class collections

- **Intent:** a collection with rules (uniqueness, limits, totals) deserves its own class so the rules are not reimplemented by every caller.
- **Signal:** `order.Items.Where(...).Sum(...)` repeated in several services; callers adding to a list after checking a limit themselves.
- **Correction:** wrap the collection (`OrderLines`) with methods such as `Add`, `Total`, `ContainsProduct`; expose a read-only view if callers need iteration.
- **When not to apply:** a plain list with no rules, or collections inside DTOs. The classic form also bans other fields in that class — treat that part as optional.

## 5. One dot per line

- **Intent:** avoid depending on the structure of objects you do not own directly (Law of Demeter).
- **Signal:** `a.GetB().GetC().DoD()` chains that reach through collaborators' internals.
- **Correction:** move the behavior to the object that owns the data (tell, don't ask), or pass in the object you actually need. A delegating getter that returns the same data only hides the chain.
- **When not to apply:** fluent APIs and builders, LINQ/stream pipelines, string and date method chains, and navigating plain data trees in mapping code. The rule is about knowledge of collaborators, not punctuation.

## 6. Don't abbreviate

- **Intent:** names are read far more than written; an abbreviation is usually a sign the name was too long.
- **Signal:** `custMgrSvc`, `calcTotAmt`, or very long names like `processOrderAndSendEmailAndUpdateStock`.
- **Correction:** if the full name is too long, the unit does too much — split it. Otherwise spell the word out.
- **When not to apply:** abbreviations that are the domain's own vocabulary (`Http`, `Id`, `Url`, `Vat`) and conventional loop indices or lambda parameters in short scopes.

## 7. Keep all entities small

- **Intent:** small classes and packages are easier to name, test and reuse. The exercise suggests around 50 lines per class and about 10 files per package.
- **Signal:** a class whose fields split into groups that methods use separately; a name that needs `And` or `Manager`.
- **Correction:** extract the cohesive groups into their own classes (Extract Class), then let the original delegate.
- **When not to apply:** never block on line counts. A long class that is cohesive (one concept, methods using the same fields) is fine. Generated code, mappings and configuration are exempt.

## 8. Limit instance variables

- **Intent:** a class with many fields usually hides smaller concepts. The exercise uses a limit of two, which forces decomposition.
- **Signal:** fields that always change together (`street`, `city`, `zip`); fields only used by a subset of methods.
- **Correction:** group related fields into objects (`Address`), move the methods that use them along.
- **When not to apply:** the numeric limit is a training device. In production, look for clumps, not counts. Services with several injected dependencies are a different signal — too many dependencies suggests SRP, but count alone is not a finding.

## 9. No getters/setters/properties

- **Intent:** tell objects what to do rather than pulling their data out and deciding for them; keeps invariants inside the class.
- **Signal:** services that read several properties of an entity, compute, and write the result back via setters; public setters on state with rules.
- **Correction:** move the computation into the entity (`account.Withdraw(amount)` instead of `account.Balance -= amount`); keep read-only getters where display or queries need them; make setters private.
- **When not to apply:** DTOs, view models, API contracts, messages, query projections and configuration objects are data on purpose. ORM entities may require settable or virtual members — encapsulate what the ORM allows and stop there. Properties in C# and TypeScript getters are idiomatic; the target is *public mutation and logic outside the owner*, not the syntax.

---

## Using the rules in a review
- Mention a rule only together with the concrete cost it exposes ("the limit check is duplicated in three callers").
- Prefer the underlying principle's name when there is one (Demeter, primitive obsession, tell-don't-ask) — it is easier to discuss than "rule 5".
- As a team exercise (kata), applying all nine strictly is valuable precisely because it is uncomfortable; do not carry that strictness into production review.
