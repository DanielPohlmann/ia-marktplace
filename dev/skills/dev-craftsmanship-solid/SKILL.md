---
name: dev-craftsmanship-solid
description: Use when applying or auditing SOLID at class and interface level. USE FOR: SRP audits, OCP extension points, LSP violations, interface segregation, dependency inversion, coupling and testability. DO NOT USE FOR: layer boundaries (use dev-craftsmanship-clean-architecture), pattern selection (use dev-design-patterns), refactoring mechanics (use dev-craftsmanship-refactoring).
---

# SOLID Principles

## Overview
SOLID is a mnemonic for five object-oriented design principles collected by Robert C. Martin. They guide code toward being easier to change and to test. Use them as **review guardrails**: each principle below lists what to look for in code, how to correct it, and when the principle should *not* be applied.

| Letter | Principle | One-Line Summary |
|--------|-----------|------------------|
| **S** | Single Responsibility | A module should have one reason to change — one actor it answers to. |
| **O** | Open/Closed | Add behavior by adding code, not by editing working code. |
| **L** | Liskov Substitution | A subtype must be usable wherever its base type is expected. |
| **I** | Interface Segregation | No client should depend on methods it does not use. |
| **D** | Dependency Inversion | Policy should not depend on details; both depend on abstractions. |

Worked violation → correction examples for every principle are in [references/examples.md](references/examples.md).

---

## S — Single Responsibility

A "reason to change" is an **actor**: a person, team or external authority that can request a change. If two actors can drive changes into the same class, a change for one can break the other.

**Signals in code**
- Two groups of methods that change for unrelated business reasons (e.g. pricing rules and a regulatory export format) in the same class.
- A shared private helper used by both groups — the classic place where one actor's change leaks into the other's behavior.
- Merge conflicts on the same file from unrelated features.

**Correction:** split along actor lines; keep a thin orchestrator if a workflow needs both.

**When not to apply:** splitting by *technical step* (validate / save / notify / log) is separation of concerns, not SRP. If one actor owns every step, a single cohesive class is often simpler. SRP means one reason to change, not one method per class.

---

## O — Open/Closed

New variants should be added as new code rather than by editing a conditional that already works.

**Signals in code**
- `switch`/`if` chains on a type code, string or enum, with business rules in each branch.
- The same type-code conditional repeated in several places.
- Method families like `ApplyRegularDiscount`, `ApplyVipDiscount`.

**Correction:** move each branch into a polymorphic type (Strategy, State, subclass). The selection does not vanish — it **moves to a single place at the edge**: a factory, a registry map or the DI container. One place that knows every variant is the goal, not zero.

**When not to apply:** only one variant exists, or the conditional is a simple, stable mapping with no behavior per branch. Wait for the second real variant before introducing the abstraction.

---

## L — Liskov Substitution

Code written against a base type must keep working, unchanged, when handed any subtype. Subtypes must honor the base type's contract:
- **Preconditions** cannot be strengthened (a subtype cannot reject input the base accepts).
- **Postconditions** cannot be weakened (a subtype cannot return less, or something with different meaning).
- **Invariants** of the base type must be preserved.
- **History constraint:** a subtype must not allow state changes the base type forbids.

**Signals in code**
- Clients checking the concrete type: `instanceof`, `is`/`as`, `GetType() ==`, followed by special handling.
- Overrides that throw `NotSupportedException` / `NotImplementedException` or silently do nothing.
- Overrides that validate more strictly than the base (size limits, extra required fields).
- Overrides that return a value with different meaning — `null` where the base returns an empty collection, different units, different rounding.
- Tests written for the base type fail when run against the subtype.

**Correction:** if the contract cannot be honored, the types are not substitutable — break the hierarchy (share an interface for what really is common, or use composition). Do not patch clients with type checks.

**When not to apply:** LSP concerns behavioral subtyping. Value objects and DTOs without polymorphic use do not need it.

---

## I — Interface Segregation

**Signals in code**
- Implementations with methods that throw "not supported" or are left empty.
- An interface that grows every time a new variant appears.
- Clients that use one or two methods of a large interface.
- Capability-check methods such as `supportsFax()` next to the methods they guard.

**Correction:** split interfaces by **client need** (role interfaces). Often the root cause is a wrong abstraction — two different concepts forced under one name — so rethink the concept, not just the method list.

**When not to apply:** do not create one interface per method. Group methods that the same clients always use together.

---

## D — Dependency Inversion

High-level policy should not construct or reference low-level details directly. Both depend on an abstraction owned by the policy side.

**Signals in code**
- `new` of infrastructure inside domain or service code: database connections, HTTP clients, SDK clients, file system access.
- Static calls to volatile details: `DateTime.Now`, `Guid.NewGuid()`, environment variables, static service locators.
- Unit tests that need a real database, network or clock to run.

**Correction, in two steps**
1. **Own the dependency:** inject it through the constructor and wrap third-party APIs in a class you own, so the rest of the code depends on your vocabulary, not the vendor's.
2. **Invert with an interface** when at least one of these holds:
   - you need to fake it in tests (database, HTTP, clock, file system, message broker);
   - a second implementation exists or is concretely planned;
   - the abstraction marks a module boundary that another team or package depends on.

**When not to apply:** an interface with a single implementation and none of the reasons above is speculative — a concrete injected class is enough, and extracting the interface later is cheap. Stable dependencies (standard library, pure utility code) can be referenced directly. DIP (who owns the abstraction) is not the same as DI (how instances are wired); constructor injection is the default mechanism for both.

---

## Reporting a SOLID finding

1. Quote the code and name the principle.
2. State the concrete cost: what the next change will break or require.
3. Apply the "when not to apply" check before reporting — if it matches, drop the finding or downgrade it to a note.
4. Propose the smallest correction that removes the cost.

## Common Pitfalls

| Pitfall | Description |
|---------|-------------|
| Micro-classes in the name of SRP | Splitting every method into its own class. SRP is about actors, not method count. |
| Premature OCP | Strategy/plugin structures for code with one variant. |
| Patching LSP in clients | Adding `is`/`instanceof` checks instead of fixing the hierarchy. |
| Interface per method | ISP groups by client need, not one interface per method. |
| Interface for everything | DIP without a reason (tests, second implementation, boundary) adds indirection only. |

## Best Practices
- Apply SOLID during code review, as guardrails, not as upfront design mandates.
- When adding a feature feels harder than it should, ask which principle the friction points to.
- Use constructor injection as the default mechanism for dependencies.
- Balance SOLID with YAGNI: introduce an abstraction when the second real variation appears.
- Class names ending in `Manager`, `Helper`, or containing `And` deserve an SRP look.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/examples.md](references/examples.md) | Violation → correction code for each principle, including SRP by actors, where the OCP selection lives, a real-world LSP precondition violation and DIP in two steps |
| [references/how-solid-relates-to-other-concepts.md](references/how-solid-relates-to-other-concepts.md) | How SOLID Relates to Other Concepts — SOLID and Clean Architecture, SOLID and Design Patterns, SOLID and Testability |

## References

- [Robert C. Martin — The Principles of OOD](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod)
- [SOLID — Wikipedia](https://en.wikipedia.org/wiki/SOLID)

See references/rules.md for the full rule catalog.
