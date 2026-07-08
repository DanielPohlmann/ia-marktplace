# Frontend Architecture Rules

Best practices and rules for Frontend Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Choose the simplest architecture that meets your... | HIGH | [`frontend-choose-the-simplest-architecture-that-meets-your.md`](frontend-choose-the-simplest-architecture-that-meets-your.md) |
| 2 | Measure performance with real user metrics (Core Web... | MEDIUM | [`frontend-measure-performance-with-real-user-metrics-core-web.md`](frontend-measure-performance-with-real-user-metrics-core-web.md) |
| 3 | Use code splitting aggressively | CRITICAL | [`frontend-use-code-splitting-aggressively.md`](frontend-use-code-splitting-aggressively.md) |
| 4 | Treat server state and client state differently | MEDIUM | [`frontend-treat-server-state-and-client-state-differently.md`](frontend-treat-server-state-and-client-state-differently.md) |
| 5 | Design for progressive enhancement | MEDIUM | [`frontend-design-for-progressive-enhancement.md`](frontend-design-for-progressive-enhancement.md) |
| 6 | Consider the Islands Architecture for content-heavy sites... | LOW | [`frontend-consider-the-islands-architecture-for-content-heavy-sites.md`](frontend-consider-the-islands-architecture-for-content-heavy-sites.md) |

---

---
title: "Choose the simplest architecture that meets your..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: frontend, dev, frontend-architecture-selection, comparing-spa-vs-ssr-vs-micro-frontends, choosing-frontend-frameworks
---

## Choose the simplest architecture that meets your...

Choose the simplest architecture that meets your requirements — not every app needs SSR or micro-frontends.

---

---
title: "Consider the Islands Architecture for content-heavy sites..."
impact: LOW
impactDescription: "recommended but situational"
tags: frontend, dev, frontend-architecture-selection, comparing-spa-vs-ssr-vs-micro-frontends, choosing-frontend-frameworks
---

## Consider the Islands Architecture for content-heavy sites...

Consider the Islands Architecture for content-heavy sites that need sprinkles of interactivity.

---

---
title: "Design for progressive enhancement"
impact: MEDIUM
impactDescription: "general best practice"
tags: frontend, dev, frontend-architecture-selection, comparing-spa-vs-ssr-vs-micro-frontends, choosing-frontend-frameworks
---

## Design for progressive enhancement

Design for progressive enhancement — the page should be usable before JavaScript loads.

---

---
title: "Measure performance with real user metrics (Core Web..."
impact: MEDIUM
impactDescription: "general best practice"
tags: frontend, dev, frontend-architecture-selection, comparing-spa-vs-ssr-vs-micro-frontends, choosing-frontend-frameworks
---

## Measure performance with real user metrics (Core Web...

Measure performance with real user metrics (Core Web Vitals), not just Lighthouse scores.

---

---
title: "Treat server state and client state differently"
impact: MEDIUM
impactDescription: "general best practice"
tags: frontend, dev, frontend-architecture-selection, comparing-spa-vs-ssr-vs-micro-frontends, choosing-frontend-frameworks
---

## Treat server state and client state differently

Treat server state and client state differently — use TanStack Query or SWR for server state, not Redux.

---

---
title: "Use code splitting aggressively"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: frontend, dev, frontend-architecture-selection, comparing-spa-vs-ssr-vs-micro-frontends, choosing-frontend-frameworks
---

## Use code splitting aggressively

Use code splitting aggressively — no user should download JavaScript they will never execute.
