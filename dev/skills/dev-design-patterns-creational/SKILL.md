---
name: dev-design-patterns-creational
description: Use when implementing any of the 5 GoF Creational patterns (Factory Method, Abstract Factory, Builder, Prototype, Singleton). USE FOR: decoupling instantiation from usage, factory hierarchies, fluent builders for complex objects, prototype cloning, controlled singleton instances DO NOT USE FOR: composing or adapting existing objects (use dev-design-patterns-structural), inter-object communication and algorithm encapsulation (use dev-design-patterns-behavioral), pattern family selection (use dev-design-patterns)
---

# Creational Design Patterns

## Overview
Creational patterns abstract the instantiation process. They help make a system independent of how its objects are created, composed, and represented. As systems evolve to depend more on object composition than class inheritance, the emphasis shifts from hard-coding fixed sets of behaviors toward defining a smaller set of fundamental behaviors that can be composed into more complex ones — and that requires flexible object creation.

> **Full per-pattern implementations, structure, code examples, and trade-offs live in [references/patterns.md](references/patterns.md).** Consult it when you need the detail for a specific pattern; the tables and decision guide below are enough to choose one.

---

## Comparison Table

| Pattern | Scope | Key Benefit | Typical Use Case |
|---------|-------|-------------|-----------------|
| **Factory Method** | Class | Defers creation to subclasses | Frameworks that define interfaces but let apps decide implementations |
| **Abstract Factory** | Object | Creates families of related objects | Cross-platform UI toolkits, themed component libraries |
| **Builder** | Object | Step-by-step construction with fluent API | Complex objects with many optional parameters (HTTP requests, queries) |
| **Prototype** | Object | Cloning pre-configured instances | Game units, document templates, expensive-to-create objects |
| **Singleton** | Object | Guarantees single instance | Configuration, connection pools (prefer DI singleton lifetime) |

## Decision Guide

```
Do you need to create objects?
│
├─ One product, varies by subclass?
│  └─▶ Factory Method
│
├─ Families of related products?
│  └─▶ Abstract Factory
│
├─ Complex object with many parts/options?
│  └─▶ Builder
│
├─ Copy an existing configured object?
│  └─▶ Prototype
│
└─ Exactly one instance, globally accessible?
   └─▶ Singleton (but strongly consider DI singleton lifetime instead)
```

## References

- [Refactoring.Guru — Creational Design Patterns](https://refactoring.guru/design-patterns/creational-patterns)
- [Creational Pattern — Wikipedia](https://en.wikipedia.org/wiki/Creational_pattern)
