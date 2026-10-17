---
name: dev-craftsmanship-refactoring
description: Use when code smells are present and you need safe, behavior-preserving refactoring (Fowler). USE FOR: smell catalog, named refactorings (Extract Method, Introduce Parameter Object, Replace Conditional with Polymorphism), incremental test-backed workflow, legacy code. DO NOT USE FOR: naming/readability alone (use dev-craftsmanship-clean-code), pattern choice (use dev-design-patterns), large restructuring (use dev-architecture).
---

# Refactoring

## Overview
*Refactoring: Improving the Design of Existing Code* by Martin Fowler defines refactoring as:

> "A disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior."

Refactoring is not rewriting. It is a sequence of small, behavior-preserving transformations that cumulatively produce a significant restructuring. Each transformation is tiny and "obviously correct," so the risk of introducing bugs is low.

## When to Refactor

| Trigger | Action |
|---------|--------|
| **The Rule of Three** | The first time you do something, just do it. The second time, wince. The third time, refactor. |
| **Before adding a feature** | If the existing structure makes the new feature awkward, refactor first so the addition is simple. |
| **During code review** | Smells spotted in review are refactoring opportunities. Address them before merging. |
| **While fixing a bug** | The bug often reveals a structural weakness. Fix the structure and the bug together (in separate commits). |
| **Boy Scout Rule** | Every time you read code and it takes a moment to understand, leave it clearer than you found it. |

## When NOT to Refactor

| Situation | Reason |
|-----------|--------|
| **No tests exist and you cannot write them** | Refactoring without tests is gambling. Write characterization tests first. |
| **A deadline is imminent** | Technical debt is a valid business decision when managed consciously. Refactor after the deadline. |
| **The code is going to be replaced** | Do not polish code that will be thrown away. |
| **The code works and nobody needs to change it** | Refactoring code that is never touched adds risk with no benefit. |

## Refactoring Techniques Quick Reference

| Technique | When to Use |
|-----------|-------------|
| Extract Method | Long method, duplicated fragment, comment explaining a block |
| Inline Method | Method body is as clear as its name, excessive delegation |
| Extract Class | Class with too many responsibilities, data clumps |
| Inline Class | Class does too little to justify its existence |
| Move Method | Method uses more features of another class |
| Move Field | Field is used more by another class |
| Rename Method/Variable | Name does not reveal intent |
| Replace Conditional with Polymorphism | Switch/if-else dispatching on type |
| Introduce Parameter Object | Multiple parameters that always appear together |
| Replace Temp with Query | Temporary variable obscures method decomposition |
| Preserve Whole Object | Pulling several values from an object to pass as separate parameters |
| Replace Magic Number with Constant | Literal numbers whose meaning is unclear |
| Decompose Conditional | Complex conditional expression |
| Consolidate Conditional Expression | Multiple conditionals with the same result |
| Remove Flag Argument | Boolean parameter that changes method behavior |
| Pull Up Method | Identical methods in sibling subclasses |
| Push Down Method | Method only relevant to one subclass |
| Collapse Hierarchy | Subclass is not different enough from its parent |

## Best Practices
- Name the refactoring you are applying. "I am doing an Extract Method" is clearer than "I am cleaning up this code."
- Commit after each successful refactoring step. Small commits make bisecting safe.
- Use IDE refactoring tools (rename, extract, inline) — they automate the mechanics and reduce errors.
- Never refactor and change behavior in the same step. Separate the two activities with separate commits.
- Track technical debt explicitly (TODO comments, issue tracker) so refactoring is planned, not ad hoc.
- Refactor toward the design you need for the next feature, not toward a theoretically ideal design.
- Pair on refactoring when possible — two sets of eyes catch more unintended behavior changes.
- If a refactoring takes more than an hour without completing, break it into smaller steps or reconsider the approach.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/code-smells-catalog.md](references/code-smells-catalog.md) | Code Smells Catalog — Bloaters, Object-Orientation Abusers, Change Preventers, Dispensables, Couplers |
| [references/key-refactoring-techniques.md](references/key-refactoring-techniques.md) | Key Refactoring Techniques — Extract Method, Inline Method, Extract Class, Move Method, Replace Conditional with Polymorphism, Introduce Parameter Object, … |
| [references/details.md](references/details.md) | The Refactoring Workflow; Refactoring and Testing |

## References

- [Refactoring.com — Catalog of Refactorings](https://refactoring.com/catalog/)
- [Martin Fowler — Refactoring (2nd Edition)](https://martinfowler.com/books/refactoring.html)
- [Refactoring.Guru — Refactoring](https://refactoring.guru/refactoring)

See references/rules.md for the full rule catalog.
