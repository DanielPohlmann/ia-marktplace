# Domain-Driven Design Rules

Best practices and rules for Domain-Driven Design.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Apply DDD only where the domain complexity justifies it... | MEDIUM | [`domain-driven-design-apply-ddd-only-where-the-domain-complexity-justifies-it.md`](domain-driven-design-apply-ddd-only-where-the-domain-complexity-justifies-it.md) |
| 2 | Invest heavily in ubiquitous language | MEDIUM | [`domain-driven-design-invest-heavily-in-ubiquitous-language.md`](domain-driven-design-invest-heavily-in-ubiquitous-language.md) |
| 3 | Keep aggregates small | HIGH | [`domain-driven-design-keep-aggregates-small.md`](domain-driven-design-keep-aggregates-small.md) |
| 4 | Reference other aggregates by identity, never by direct... | CRITICAL | [`domain-driven-design-reference-other-aggregates-by-identity-never-by-direct.md`](domain-driven-design-reference-other-aggregates-by-identity-never-by-direct.md) |
| 5 | Use domain events for cross-aggregate and cross-context... | MEDIUM | [`domain-driven-design-use-domain-events-for-cross-aggregate-and-cross-context.md`](domain-driven-design-use-domain-events-for-cross-aggregate-and-cross-context.md) |
| 6 | Collaborate with domain experts continuously -- DDD is not... | MEDIUM | [`domain-driven-design-collaborate-with-domain-experts-continuously-ddd-is-not.md`](domain-driven-design-collaborate-with-domain-experts-continuously-ddd-is-not.md) |
| 7 | Draw context maps early and revisit them as the system... | MEDIUM | [`domain-driven-design-draw-context-maps-early-and-revisit-them-as-the-system.md`](domain-driven-design-draw-context-maps-early-and-revisit-them-as-the-system.md) |
| 8 | Bounded context boundaries often align well with... | MEDIUM | [`domain-driven-design-bounded-context-boundaries-often-align-well-with.md`](domain-driven-design-bounded-context-boundaries-often-align-well-with.md) |

---

---
title: "Apply DDD only where the domain complexity justifies it..."
impact: MEDIUM
impactDescription: "general best practice"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Apply DDD only where the domain complexity justifies it...

Apply DDD only where the domain complexity justifies it (core subdomains). For CRUD-heavy generic subdomains, simpler approaches are fine.

---

---
title: "Bounded context boundaries often align well with..."
impact: MEDIUM
impactDescription: "general best practice"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Bounded context boundaries often align well with...

Bounded context boundaries often align well with microservice boundaries (see `dev/architecture/microservices`), but they don't have to -- a modular monolith can also respect bounded contexts (see `dev/architecture/monoliths`).

---

---
title: "Collaborate with domain experts continuously -- DDD is not..."
impact: MEDIUM
impactDescription: "general best practice"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Collaborate with domain experts continuously -- DDD is not...

Collaborate with domain experts continuously -- DDD is not a solo developer activity.

---

---
title: "Draw context maps early and revisit them as the system..."
impact: MEDIUM
impactDescription: "general best practice"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Draw context maps early and revisit them as the system...

Draw context maps early and revisit them as the system evolves.

---

---
title: "Invest heavily in ubiquitous language"
impact: MEDIUM
impactDescription: "general best practice"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Invest heavily in ubiquitous language

Invest heavily in ubiquitous language. If developers and domain experts use different words, the design will drift.

---

---
title: "Keep aggregates small"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Keep aggregates small

Keep aggregates small. The default should be a single entity as the aggregate root. Add more only when invariants require it.

---

---
title: "Reference other aggregates by identity, never by direct..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Reference other aggregates by identity, never by direct...

Reference other aggregates by identity, never by direct object reference.

---

---
title: "Use domain events for cross-aggregate and cross-context..."
impact: MEDIUM
impactDescription: "general best practice"
tags: domain-driven-design, dev, architecture, bounded-context-identification, context-mapping, aggregate-design
---

## Use domain events for cross-aggregate and cross-context...

Use domain events for cross-aggregate and cross-context communication.
