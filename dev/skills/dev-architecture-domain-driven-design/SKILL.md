---
name: dev-architecture-domain-driven-design
description: Use when modeling a complex domain with DDD. USE FOR: bounded contexts, context maps, subdomain classification, ubiquitous language, aggregates, entities, value objects, domain services, repositories. DO NOT USE FOR: event sourcing mechanics (use dev-architecture-event-driven), service decomposition (use dev-architecture-microservices), ports/adapters (use dev-architecture-hexagonal).
---

# Domain-Driven Design (DDD)

## Overview
Domain-Driven Design is a software design approach that centers the development process on the core business domain. It provides both strategic patterns for organizing large systems and tactical patterns for modeling individual domains. DDD is especially valuable for complex domains where the business logic is the primary source of difficulty.

The canonical reference is Eric Evans' *Domain-Driven Design: Tackling Complexity in the Heart of Software* (2003), supplemented by Vaughn Vernon's *Implementing Domain-Driven Design* (2013) and *Domain-Driven Design Distilled* (2016).

**Core premise:** The structure of the software should mirror the structure of the business domain. The language used by developers should be the same language used by domain experts.

## Strategic + Tactical DDD Together

```
Strategic (System Level):
  Identify Subdomains → Define Bounded Contexts → Map Context Relationships

Tactical (Within Each Context):
  Model Aggregates → Define Entities & Value Objects →
  Publish Domain Events → Implement Repositories & Services
```

## Common DDD Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Anemic Domain Model** | Entities are just data bags; logic lives in services | Move behavior into entities and value objects |
| **God Aggregate** | One massive aggregate with many entities | Break into smaller aggregates; use eventual consistency |
| **Shared Database across Contexts** | Bounded contexts lose independence | Each context owns its data; integrate through events or APIs |
| **Ubiquitous Language mismatch** | Code uses different terms than domain experts | Refactor code to match the domain language exactly |
| **DDD everywhere** | Applying DDD to simple CRUD domains | Use DDD for core subdomains; use simpler approaches for generic/supporting |

## Best Practices
- Apply DDD only where the domain complexity justifies it (core subdomains). For CRUD-heavy generic subdomains, simpler approaches are fine.
- Invest heavily in ubiquitous language. If developers and domain experts use different words, the design will drift.
- Keep aggregates small. The default should be a single entity as the aggregate root. Add more only when invariants require it.
- Reference other aggregates by identity, never by direct object reference.
- Use domain events for cross-aggregate and cross-context communication.
- Collaborate with domain experts continuously -- DDD is not a solo developer activity.
- Draw context maps early and revisit them as the system evolves.
- Bounded context boundaries often align well with microservice boundaries (see `dev-architecture-microservices`), but they don't have to -- a modular monolith can also respect bounded contexts (see `dev-architecture-monoliths`).

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/strategic-ddd.md](references/strategic-ddd.md) | Strategic DDD — Ubiquitous Language, Bounded Contexts, Subdomains, Context Maps, Context Mapping Patterns |
| [references/tactical-ddd.md](references/tactical-ddd.md) | Tactical DDD — Entities, Value Objects, Aggregates and Aggregate Roots, Aggregate Design Rules, Aggregate Design Example, Domain Events, … |

## References

- [Martin Fowler — Domain-Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html)
- [Domain-Driven Design — Wikipedia](https://en.wikipedia.org/wiki/Domain-driven_design)

See references/rules.md for the full rule catalog.
