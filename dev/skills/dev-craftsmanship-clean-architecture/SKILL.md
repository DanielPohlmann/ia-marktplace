---
name: dev-craftsmanship-clean-architecture
description: Use when designing or checking layer boundaries and dependency direction (Robert C. Martin's Clean Architecture). USE FOR: the Dependency Rule, entities/use cases/adapters/frameworks layers, humble objects, screaming architecture, keeping domain free of infrastructure. DO NOT USE FOR: readability (use dev-craftsmanship-clean-code), ports/adapters (use dev-architecture-hexagonal), SOLID (use dev-craftsmanship-solid).
---

# Clean Architecture

## Overview
*Clean Architecture: A Craftsman's Guide to Software Structure and Design* by Robert C. Martin presents a set of principles for organizing software so that it is testable, independent of frameworks, independent of the UI, independent of the database, and independent of any external agency.

The central idea: **The Dependency Rule** — source code dependencies must point only inward, toward higher-level policies.

## Screaming Architecture

> "A good architecture screams the intent of the system."

When you look at the top-level directory structure, it should tell you what the system **does**, not what framework it uses.

```
# Bad — screams "Rails" or "Express"
src/
  controllers/
  models/
  views/
  routes/
  middleware/

# Good — screams "Health Clinic"
src/
  patients/
  appointments/
  prescriptions/
  billing/
  shared/
```

Each top-level folder represents a use case area or a bounded context, not a technical layer.

## Clean Architecture vs. Related Patterns

| Pattern | Relationship |
|---------|-------------|
| Hexagonal Architecture (Ports & Adapters) | Clean Architecture is a generalization. Ports are the interfaces in the Use Case layer; Adapters are the implementations in the outer layer. |
| Onion Architecture | Nearly identical in structure. Clean Architecture adds the concept of Screaming Architecture and the Humble Object. |
| Domain-Driven Design (DDD) | Clean Architecture's Entities map to DDD's Domain Model. Bounded Contexts often align with top-level Clean Architecture modules. |
| SOLID Principles | Clean Architecture is the architectural expression of SOLID, especially the Dependency Inversion Principle. |

## Typical Project Structure

```
src/
  domain/                      # Entities — enterprise business rules
    entities/
    value-objects/
    domain-events/
  application/                 # Use Cases — application business rules
    use-cases/
    ports/                     # Interfaces for outbound dependencies
    dto/                       # Request/Response data structures
  adapters/                    # Interface Adapters
    controllers/               # Inbound (driving) adapters
    gateways/                  # Outbound (driven) adapters
    presenters/
    mappers/
  infrastructure/              # Frameworks & Drivers
    database/
    web/
    messaging/
    config/
```

## Best Practices
- Enforce the Dependency Rule with linter rules or architectural tests (e.g., ArchUnit, dependency-cruiser).
- Defer framework decisions as long as possible. The architecture should work without Express, React, or PostgreSQL.
- Keep Use Cases as pure orchestrators — they call Entities and Ports but contain minimal logic themselves.
- Use the Humble Object pattern at every boundary to maximize testable code.
- Name modules after business capabilities, not technical layers — let the architecture scream.
- Test inner layers with unit tests (fast, no I/O). Test boundaries with integration tests. Test the outermost layer with end-to-end tests sparingly.
- When in doubt about which layer something belongs to, ask: "If I change the database / framework / UI, does this need to change?" If yes, it belongs in an outer layer.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/the-four-layers.md](references/the-four-layers.md) | The Four Layers — 1. Entities (Enterprise Business Rules), 2. Use Cases (Application Business Rules), 3. Interface Adapters (Controllers, Gateways, Presenters), 4. Frameworks & Drivers |
| [references/details.md](references/details.md) | The Concentric Circles; The Dependency Rule; Crossing Boundaries; The Humble Object Pattern; Boundaries |

## References

- [The Clean Architecture — Robert C. Martin (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Clean Architecture — Robert C. Martin (Book)](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/)

See references/rules.md for the full rule catalog.
