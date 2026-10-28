---
name: dev-design-patterns-creational
description: Use when implementing a GoF creational pattern: Factory Method, Abstract Factory, Builder, Prototype, Singleton. USE FOR: decoupling instantiation, fluent builders, cloning, controlled single instances. DO NOT USE FOR: composing/adapting objects (use dev-design-patterns-structural), communication and algorithms (use dev-design-patterns-behavioral), picking a family (use dev-design-patterns).
---

# Creational Design Patterns

## Overview
Creational patterns abstract the instantiation process. They help make a system independent of how its objects are created, composed, and represented. As systems evolve to depend more on object composition than class inheritance, the emphasis shifts from hard-coding fixed sets of behaviors toward defining a smaller set of fundamental behaviors that can be composed into more complex ones — and that requires flexible object creation.

> **Full per-pattern implementations, structure, code examples, and trade-offs live in [references/patterns.md](references/patterns.md)** (see the Detailed reference table). The tables and decision guide below are enough to choose one and to review code.

---

## Comparison Table

| Pattern | Scope | Key Benefit | Typical Use Case |
|---------|-------|-------------|-----------------|
| **Factory Method** | Class | Defers creation to subclasses | Frameworks that define interfaces but let apps decide implementations |
| **Abstract Factory** | Object | Creates families of related objects | Cross-platform UI toolkits, themed component libraries |
| **Builder** | Object | Step-by-step construction with fluent API | Complex objects with many optional parameters (HTTP requests, queries) |
| **Prototype** | Object | Cloning pre-configured instances | Game units, document templates, expensive-to-create objects |
| **Singleton** | Object | Guarantees single instance | Configuration, connection pools (prefer DI singleton lifetime) |
| **Simple Factory** *(not GoF)* | Object | One place owns a creation conditional | Pick an implementation from a type code, config value or request field |

Simple Factory is an idiom, not one of the GoF patterns: a single method that holds the `if`/`switch` choosing which class to instantiate. It does not remove the Open/Closed violation — adding a variant still means editing the switch — it deliberately concentrates that violation in one place instead of letting it spread across call sites.

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
├─ Exactly one instance, globally accessible?
│  └─▶ Singleton (but strongly consider DI singleton lifetime instead)
│
└─ Same "which class do I create?" conditional repeated in many places?
   └─▶ Simple Factory (injectable), or a registry keyed by type code
```

## Review Signals

Use this table during code review: the left column is what suggests the pattern is missing, the right column is what suggests it is misapplied.

| Pattern | Signals in code (pattern is needed) | When NOT to use (anti-signals / overuse) |
|---------|-------------------------------------|------------------------------------------|
| **Simple Factory** | The same creation `if`/`switch` copied into several endpoints, handlers or jobs; each new variant requires a multi-file hunt | Only one call site creates the object; only one implementation exists. A `static` factory method is itself a smell — callers cannot substitute it in tests. Prefer an injectable factory interface or a registry (`Dictionary<key, Func<T>>`, keyed DI services) |
| **Factory Method** | A base class/framework hard-codes `new ConcreteX()` that subclasses or plugins need to change | A subclass hierarchy created only to vary one constructor call — pass a factory delegate or use DI instead |
| **Abstract Factory** | Code mixes products from different families (e.g. a light-theme button with a dark-theme dialog); conditionals on the "family" repeated per product | Only one family exists or products are unrelated; adding a product type forces edits to every factory — accept that cost only if families are stable |
| **Builder** | Telescoping constructors, many optional/boolean parameters, objects observable in a half-initialized state, the same multi-line setup copied in tests | Few required fields — a constructor, object initializer or record with named/default arguments is clearer; a builder that does no validation adds ceremony only |
| **Prototype** | Expensive setup repeated to produce near-identical objects; copy code that reads every field by hand | Objects are cheap to build; deep graphs with shared references or external handles where clone semantics (shallow vs deep) are ambiguous |
| **Singleton** | Hand-rolled `static Instance` / `getInstance()`; mutable global state; tests that pass alone but fail depending on execution order; hidden dependencies not declared in constructors | Almost always prefer a DI singleton lifetime. Never for state that differs per request, tenant or user |

### Singleton thread-safety

Hand-written lazy initialization (`if (instance == null) instance = new X();`) is not thread-safe: two threads can both pass the null check and create two instances, each holding different state (a check-then-create race). Ad-hoc double-checked locking is easy to get wrong. In .NET:

- Register the service with a **singleton lifetime in the DI container** (`services.AddSingleton<IX, X>()`) — the container guarantees one instance and keeps the dependency visible in constructors.
- When no container is available, use **`Lazy<T>`** (thread-safe by default) or a `static readonly` field initialized by the type initializer.
- Keep the instance immutable or internally synchronized; a singleton shared across threads is shared mutable state.

## Detailed reference

| File | Contents |
|---|---|
| [references/patterns.md](references/patterns.md) | Factory Method, Abstract Factory, Builder, Prototype, Singleton, Simple Factory — intent, structure, participants, when to use, TypeScript examples |

## References

- [Refactoring.Guru — Creational Design Patterns](https://refactoring.guru/design-patterns/creational-patterns)
- [Creational Pattern — Wikipedia](https://en.wikipedia.org/wiki/Creational_pattern)
