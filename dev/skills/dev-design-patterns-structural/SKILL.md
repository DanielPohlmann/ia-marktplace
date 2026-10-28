---
name: dev-design-patterns-structural
description: Use when implementing a GoF structural pattern: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. USE FOR: adapting third-party APIs, adding behavior by wrapping, subsystem facades, trees, memory sharing, access proxies. DO NOT USE FOR: creation (use dev-design-patterns-creational), communication (use dev-design-patterns-behavioral), picking a family (use dev-design-patterns).
---

# Structural Design Patterns

## Overview
Structural patterns are concerned with how classes and objects are composed to form larger structures. Structural class patterns use inheritance to compose interfaces or implementations. Structural object patterns describe ways to compose objects to realize new functionality — the added flexibility of object composition comes from the ability to change the composition at runtime.

---

## Comparison Table

| Pattern | Key Mechanism | Problem It Solves | Key Distinction |
|---------|--------------|-------------------|-----------------|
| **Adapter** | Wraps one interface into another | Incompatible interfaces | Changes the interface of an existing object |
| **Bridge** | Separates abstraction from implementation | Two independent dimensions of variation | Designed up-front to let abstraction and implementation vary |
| **Composite** | Tree of uniform components | Part-whole hierarchies | Lets clients treat single objects and compositions uniformly |
| **Decorator** | Wraps an object, adds behavior | Adding responsibilities dynamically | Adds behavior without changing the interface |
| **Facade** | Simplified interface to a subsystem | Complex subsystem with many classes | Provides a new, simpler interface |
| **Flyweight** | Shares intrinsic state | Too many fine-grained objects in memory | Reduces object count by sharing common parts |
| **Proxy** | Controls access to an object | Controlled access, caching, lazy loading | Same interface as the real object but controls access |

## Decision Guide

```
Do you need to compose or wrap objects?
│
├─ Make incompatible interfaces work together?
│  └──▶ Adapter
│
├─ Vary abstraction and implementation independently?
│  └──▶ Bridge
│
├─ Represent tree / part-whole hierarchies?
│  └──▶ Composite
│
├─ Add or remove behavior dynamically?
│  └──▶ Decorator
│
├─ Simplify a complex subsystem interface?
│  └──▶ Facade
│
├─ Reduce memory for many similar objects?
│  └──▶ Flyweight
│
└─ Control access, cache, or lazy-load?
   └──▶ Proxy
```

## Review Signals

Use during code review: the middle column suggests the pattern is missing, the right column suggests it is misapplied.

| Pattern | Signals in code (pattern is needed) | When NOT to use (anti-signals / overuse) |
|---------|-------------------------------------|------------------------------------------|
| **Adapter** | Third-party or legacy types (SDK clients, DTOs, exceptions, enums) leak into domain code; vendor-specific conversions repeated at every call site; swapping a vendor would touch the domain | The external API already matches your abstraction; an adapter that only renames methods 1:1 and adds no translation or isolation is noise |
| **Bridge** | A class hierarchy multiplying along two axes (`PdfEmailReport`, `PdfSlackReport`, `CsvEmailReport`, …) | Only one axis actually varies; building the split up-front "for later" |
| **Composite** | Client code type-checks nodes (`if (x is Folder) … else …`) and recurses by hand over a tree | The structure is flat, or leaves and containers genuinely need different operations — a uniform interface would force meaningless methods on leaves |
| **Decorator** | Optional behavior switched on by flags inside a method (`if (enableCache) … if (enableRetry) …`); boolean constructor parameters such as `withLogging`; subclasses like `LoggingRetryingCachingClient` | One fixed combination that never changes; deep stacks whose behavior depends on wrapping order (retry outside vs inside cache, auth before or after logging) — make the order explicit in one composition root and test it |
| **Facade** | Callers repeat the same multi-step orchestration over several subsystem classes; controllers know the internal call order of a subsystem | A facade over a trivial one-step flow is an extra hop with no value. Watch growth: a facade that accumulates unrelated operations becomes a god object — split it per use case |
| **Flyweight** | Memory profiling shows huge counts of objects with identical immutable parts (glyphs, tiles, map markers) | No measured memory problem; shared state that must be mutable — sharing it creates cross-object bugs |
| **Proxy** | Cache lookups, permission checks, lazy loading or logging mixed into business methods, often copied across several methods | No shared interface between proxy and real object — clients must know which one they hold, so it is a wrapper, not a proxy; one-off concern better handled by the framework's middleware/interceptors |


## Commonly Confused Pairs

### Adapter vs Facade
- **Adapter** makes an existing interface conform to another existing interface (1:1 wrapping)
- **Facade** creates a new simplified interface over multiple subsystem classes (1:many simplification)

### Decorator vs Proxy
- **Decorator** adds new behavior (the client knows it is decorating)
- **Proxy** controls access to existing behavior (the client treats it identically to the real object)

### Composite vs Decorator
- Both use recursive composition, but **Composite** aggregates children (one-to-many) while **Decorator** wraps a single component (one-to-one) to add behavior

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/adapter.md](references/adapter.md) | 1. Adapter — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/bridge.md](references/bridge.md) | 2. Bridge — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/composite.md](references/composite.md) | 3. Composite — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/decorator.md](references/decorator.md) | 4. Decorator — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/facade.md](references/facade.md) | 5. Facade — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/flyweight.md](references/flyweight.md) | 6. Flyweight — Intent, Structure, Participants, When to Use, TypeScript Example |
| [references/proxy.md](references/proxy.md) | 7. Proxy — Intent, Structure, Participants, Proxy Variants, When to Use, TypeScript Example |

## References

- [Refactoring.Guru — Structural Design Patterns](https://refactoring.guru/design-patterns/structural-patterns)
- [Structural Pattern — Wikipedia](https://en.wikipedia.org/wiki/Structural_pattern)
