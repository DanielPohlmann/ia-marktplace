# Monoliths Rules

Best practices and rules for Monoliths.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | If you choose a monolith, invest in modular structure from... | MEDIUM | [`monoliths-if-you-choose-a-monolith-invest-in-modular-structure-from.md`](monoliths-if-you-choose-a-monolith-invest-in-modular-structure-from.md) |
| 2 | Enforce module boundaries with architecture tests... | HIGH | [`monoliths-enforce-module-boundaries-with-architecture-tests.md`](monoliths-enforce-module-boundaries-with-architecture-tests.md) |
| 3 | Keep modules loosely coupled | MEDIUM | [`monoliths-keep-modules-loosely-coupled.md`](monoliths-keep-modules-loosely-coupled.md) |
| 4 | Make each module independently testable | MEDIUM | [`monoliths-make-each-module-independently-testable.md`](monoliths-make-each-module-independently-testable.md) |
| 5 | Monitor module complexity (cyclomatic complexity, coupling... | MEDIUM | [`monoliths-monitor-module-complexity-cyclomatic-complexity-coupling.md`](monoliths-monitor-module-complexity-cyclomatic-complexity-coupling.md) |
| 6 | When migrating, use the Strangler Fig pattern | CRITICAL | [`monoliths-when-migrating-use-the-strangler-fig-pattern.md`](monoliths-when-migrating-use-the-strangler-fig-pattern.md) |
| 7 | A monolith that is well-structured and maintainable is... | MEDIUM | [`monoliths-a-monolith-that-is-well-structured-and-maintainable-is.md`](monoliths-a-monolith-that-is-well-structured-and-maintainable-is.md) |

---

---
title: "A monolith that is well-structured and maintainable is..."
impact: MEDIUM
impactDescription: "general best practice"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## A monolith that is well-structured and maintainable is...

A monolith that is well-structured and maintainable is better than microservices that are poorly understood and operationally fragile.

---

---
title: "Enforce module boundaries with architecture tests..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## Enforce module boundaries with architecture tests...

Enforce module boundaries with architecture tests (ArchUnit, NetArchTest).

---

---
title: "If you choose a monolith, invest in modular structure from..."
impact: MEDIUM
impactDescription: "general best practice"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## If you choose a monolith, invest in modular structure from...

If you choose a monolith, invest in modular structure from day one. A Big Ball of Mud is a choice, not an inevitability.

---

---
title: "Keep modules loosely coupled"
impact: MEDIUM
impactDescription: "general best practice"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## Keep modules loosely coupled

Keep modules loosely coupled: depend on interfaces, not implementations.

---

---
title: "Make each module independently testable"
impact: MEDIUM
impactDescription: "general best practice"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## Make each module independently testable

Make each module independently testable.

---

---
title: "Monitor module complexity (cyclomatic complexity, coupling..."
impact: MEDIUM
impactDescription: "general best practice"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## Monitor module complexity (cyclomatic complexity, coupling...

Monitor module complexity (cyclomatic complexity, coupling metrics) as early warnings for when extraction may be needed.

---

---
title: "When migrating, use the Strangler Fig pattern"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: monoliths, dev, architecture, monolith-first-strategy, modular-monolith-design, monolith-decomposition
---

## When migrating, use the Strangler Fig pattern

When migrating, use the Strangler Fig pattern. Never attempt a big-bang rewrite.
