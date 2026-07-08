# Hexagonal Architecture Rules

Best practices and rules for Hexagonal Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Keep the domain model completely free of infrastructure... | MEDIUM | [`hexagonal-keep-the-domain-model-completely-free-of-infrastructure.md`](hexagonal-keep-the-domain-model-completely-free-of-infrastructure.md) |
| 2 | Define ports using domain language, not technology language | MEDIUM | [`hexagonal-define-ports-using-domain-language-not-technology-language.md`](hexagonal-define-ports-using-domain-language-not-technology-language.md) |
| 3 | Use dependency injection to wire adapters to ports at the... | CRITICAL | [`hexagonal-use-dependency-injection-to-wire-adapters-to-ports-at-the.md`](hexagonal-use-dependency-injection-to-wire-adapters-to-ports-at-the.md) |
| 4 | Write the majority of tests against ports (mock adapters),... | MEDIUM | [`hexagonal-write-the-majority-of-tests-against-ports-mock-adapters.md`](hexagonal-write-the-majority-of-tests-against-ports-mock-adapters.md) |
| 5 | Start with one adapter per port | MEDIUM | [`hexagonal-start-with-one-adapter-per-port.md`](hexagonal-start-with-one-adapter-per-port.md) |
| 6 | Use the hexagonal structure to enable incremental migration | MEDIUM | [`hexagonal-use-the-hexagonal-structure-to-enable-incremental-migration.md`](hexagonal-use-the-hexagonal-structure-to-enable-incremental-migration.md) |
| 7 | Combine with DDD (see... | MEDIUM | [`hexagonal-combine-with-ddd-see.md`](hexagonal-combine-with-ddd-see.md) |
| 8 | The hexagonal shape is a metaphor for symmetry -- there is... | MEDIUM | [`hexagonal-the-hexagonal-shape-is-a-metaphor-for-symmetry-there-is.md`](hexagonal-the-hexagonal-shape-is-a-metaphor-for-symmetry-there-is.md) |

---

---
title: "Combine with DDD (see..."
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Combine with DDD (see...

Combine with DDD (see `dev/architecture/domain-driven-design`) for rich domain modeling inside the hexagon.

---

---
title: "Define ports using domain language, not technology language"
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Define ports using domain language, not technology language

Define ports using domain language, not technology language. `IOrderRepository.Save(Order)`, not `IDatabaseContext.ExecuteCommand(SQL)`.

---

---
title: "Keep the domain model completely free of infrastructure..."
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Keep the domain model completely free of infrastructure...

Keep the domain model completely free of infrastructure dependencies. No ORM attributes, no HTTP concepts, no serialization annotations in the domain layer.

---

---
title: "Start with one adapter per port"
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Start with one adapter per port

Start with one adapter per port. Add additional adapters when you actually need them (e.g., switching databases, adding a CLI interface).

---

---
title: "The hexagonal shape is a metaphor for symmetry -- there is..."
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## The hexagonal shape is a metaphor for symmetry -- there is...

The hexagonal shape is a metaphor for symmetry -- there is no inherent "top" or "bottom." Any adapter on any side is equally first-class.

---

---
title: "Use dependency injection to wire adapters to ports at the..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Use dependency injection to wire adapters to ports at the...

Use dependency injection to wire adapters to ports at the composition root.

---

---
title: "Use the hexagonal structure to enable incremental migration"
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Use the hexagonal structure to enable incremental migration

Use the hexagonal structure to enable incremental migration: swap one adapter at a time without touching the domain.

---

---
title: "Write the majority of tests against ports (mock adapters),..."
impact: MEDIUM
impactDescription: "general best practice"
tags: hexagonal, dev, architecture, hexagonal-architecture, ports-and-adapters, onion-architecture
---

## Write the majority of tests against ports (mock adapters),...

Write the majority of tests against ports (mock adapters), not against infrastructure. This gives you fast, reliable tests.
