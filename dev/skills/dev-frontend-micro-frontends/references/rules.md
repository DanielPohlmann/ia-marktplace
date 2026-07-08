# Micro-Frontend Architecture Rules

Best practices and rules for Micro-Frontend Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Establish a shared design system (component library,... | MEDIUM | [`micro-frontends-establish-a-shared-design-system-component-library.md`](micro-frontends-establish-a-shared-design-system-component-library.md) |
| 2 | Use Module Federation's `singleton | CRITICAL | [`micro-frontends-use-module-federation-s-singleton.md`](micro-frontends-use-module-federation-s-singleton.md) |
| 3 | Define clear contracts between micro-frontends | MEDIUM | [`micro-frontends-define-clear-contracts-between-micro-frontends.md`](micro-frontends-define-clear-contracts-between-micro-frontends.md) |
| 4 | Invest in integration testing | MEDIUM | [`micro-frontends-invest-in-integration-testing.md`](micro-frontends-invest-in-integration-testing.md) |
| 5 | Start with a monolith and extract micro-frontends only when... | MEDIUM | [`micro-frontends-start-with-a-monolith-and-extract-micro-frontends-only-when.md`](micro-frontends-start-with-a-monolith-and-extract-micro-frontends-only-when.md) |
| 6 | Use a shell/host application that owns the layout,... | MEDIUM | [`micro-frontends-use-a-shell-host-application-that-owns-the-layout.md`](micro-frontends-use-a-shell-host-application-that-owns-the-layout.md) |
| 7 | Monitor aggregate bundle size | MEDIUM | [`micro-frontends-monitor-aggregate-bundle-size.md`](micro-frontends-monitor-aggregate-bundle-size.md) |

---

---
title: "Define clear contracts between micro-frontends"
impact: MEDIUM
impactDescription: "general best practice"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Define clear contracts between micro-frontends

Define clear contracts between micro-frontends — custom events with typed payloads, not ad-hoc DOM coupling.

---

---
title: "Establish a shared design system (component library,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Establish a shared design system (component library,...

Establish a shared design system (component library, tokens, CSS variables) — team autonomy does not mean visual chaos.

---

---
title: "Invest in integration testing"
impact: MEDIUM
impactDescription: "general best practice"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Invest in integration testing

Invest in integration testing — test the composed page, not just individual micro-frontends in isolation.

---

---
title: "Monitor aggregate bundle size"
impact: MEDIUM
impactDescription: "general best practice"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Monitor aggregate bundle size

Monitor aggregate bundle size — without vigilance, micro-frontends will independently add dependencies until the total payload dwarfs a monolith.

---

---
title: "Start with a monolith and extract micro-frontends only when..."
impact: MEDIUM
impactDescription: "general best practice"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Start with a monolith and extract micro-frontends only when...

Start with a monolith and extract micro-frontends only when organizational pain (release coordination, merge conflicts, team coupling) justifies the architectural complexity.

---

---
title: "Use a shell/host application that owns the layout,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Use a shell/host application that owns the layout,...

Use a shell/host application that owns the layout, authentication, and top-level routing — micro-frontends own their content area only.

---

---
title: "Use Module Federation's `singleton"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: micro-frontends, dev, frontend, micro-frontend-architecture, module-federation, single-spa
---

## Use Module Federation's `singleton

Use Module Federation's `singleton: true` for critical shared dependencies (React, router) to avoid duplicate instances.
