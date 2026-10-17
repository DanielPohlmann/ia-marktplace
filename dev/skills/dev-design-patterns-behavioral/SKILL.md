---
name: dev-design-patterns-behavioral
description: Use when implementing a GoF behavioral pattern: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor. USE FOR: pipelines, undo/redo, pub-sub, swappable algorithms, state machines. DO NOT USE FOR: creation (use dev-design-patterns-creational), composition (use dev-design-patterns-structural), picking a family (use dev-design-patterns).
---

# Behavioral Design Patterns

## Overview
Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. They describe not just patterns of objects or classes but also the patterns of communication between them. These patterns characterize complex control flow that is difficult to follow at run-time — they shift your focus away from flow of control to the way objects are interconnected.

---

## Commonly Confused Pairs

### Strategy vs State

| Aspect | Strategy | State |
|--------|----------|-------|
| **Intent** | Swap an algorithm from outside | Change behavior as internal state changes |
| **Who decides** | The client selects the strategy | The state objects trigger transitions |
| **Awareness** | Strategies are unaware of each other | States often know about sibling states |
| **Typical trigger** | Client calls `setStrategy()` | Internal condition triggers `setState()` |
| **Example** | Choose sort algorithm | Order status lifecycle (Pending -> Paid -> Shipped) |

**Rule of thumb**: If the client picks the behavior, it is Strategy. If the object changes its own behavior based on internal conditions, it is State.

### Command vs Memento

| Aspect | Command | Memento |
|--------|---------|---------|
| **Intent** | Encapsulate an action as an object | Capture a snapshot of state |
| **What it stores** | An operation + its parameters | An object's internal state |
| **Undo mechanism** | Reverse the operation (execute inverse) | Restore the saved state |
| **Scope** | One action at a time | Full state snapshot |
| **Example** | "Insert text at position 5" (undo = delete) | "Save entire document state" (undo = restore) |

**Rule of thumb**: Command stores *what to do* (and how to undo it). Memento stores *what things looked like* (so you can go back).

### Observer vs Mediator

| Aspect | Observer | Mediator |
|--------|----------|----------|
| **Direction** | One-to-many (subject -> observers) | Many-to-many (colleagues <-> mediator) |
| **Coupling** | Observers subscribe to a subject | Colleagues only know the mediator |
| **Awareness** | Subject does not know observer types | Mediator knows all colleague types |
| **Typical use** | Event notification, data binding | Complex UI interactions, chat rooms |
| **Distribution** | Distributed — each subject manages its list | Centralized — one mediator coordinates all |

**Rule of thumb**: Observer is for broadcasting events. Mediator is for coordinating complex interactions between many objects.

---

## Full Comparison Table

| Pattern | Key Mechanism | Problem It Solves |
|---------|--------------|-------------------|
| **Chain of Responsibility** | Linked handler chain | Decouple sender from receiver; multiple potential handlers |
| **Command** | Request as object | Parameterize, queue, log, undo operations |
| **Interpreter** | Grammar tree evaluation | Evaluate simple expressions and DSLs |
| **Iterator** | Sequential traversal interface | Access elements without exposing internals |
| **Mediator** | Central coordinator | Reduce N:M coupling between collaborating objects |
| **Memento** | State snapshot | Save/restore state without breaking encapsulation |
| **Observer** | Publish-subscribe | Notify dependents of state changes automatically |
| **State** | State-driven delegation | Change object behavior when state changes |
| **Strategy** | Algorithm delegation | Swap algorithms at runtime |
| **Template Method** | Skeleton + hooks | Reuse algorithm structure, vary individual steps |
| **Visitor** | Double dispatch | Add operations to class hierarchies without modifying them |

## Decision Guide

```
How do objects communicate or behave?
│
├─ Pass request along until someone handles it?
│  └──▶ Chain of Responsibility
│
├─ Encapsulate a request for undo/redo/queuing?
│  └──▶ Command
│
├─ Traverse a collection without exposing internals?
│  └──▶ Iterator
│
├─ Reduce coupling between many interacting objects?
│  └──▶ Mediator
│
├─ Save and restore object state?
│  └──▶ Memento
│
├─ Notify others when state changes?
│  └──▶ Observer
│
├─ Change behavior based on internal state?
│  └──▶ State
│
├─ Swap algorithms at runtime?
│  └──▶ Strategy
│
├─ Reuse algorithm skeleton, vary steps?
│  └──▶ Template Method
│
├─ Add operations across a class hierarchy?
│  └──▶ Visitor
│
└─ Evaluate simple grammar or expressions?
   └──▶ Interpreter (but consider a parser library first)
```

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/chain-of-responsibility.md](references/chain-of-responsibility.md) | 1. Chain of Responsibility — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/command.md](references/command.md) | 2. Command — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/iterator.md](references/iterator.md) | 3. Iterator — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/mediator.md](references/mediator.md) | 4. Mediator — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/memento.md](references/memento.md) | 5. Memento — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/observer.md](references/observer.md) | 6. Observer — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/state.md](references/state.md) | 7. State — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/strategy.md](references/strategy.md) | 8. Strategy — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/template-method.md](references/template-method.md) | 9. Template Method — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/visitor.md](references/visitor.md) | 10. Visitor — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/interpreter.md](references/interpreter.md) | 11. Interpreter — Intent, Note on Usage, Structure, When to Use, TypeScript Example |

## References

- [Refactoring.Guru — Behavioral Design Patterns](https://refactoring.guru/design-patterns/behavioral-patterns)
- [Behavioral Pattern — Wikipedia](https://en.wikipedia.org/wiki/Behavioral_pattern)
