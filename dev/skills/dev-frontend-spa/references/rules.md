# Single Page Applications Rules

Best practices and rules for Single Page Applications.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Treat server data as a cache, not as state | MEDIUM | [`spa-treat-server-data-as-a-cache-not-as-state.md`](spa-treat-server-data-as-a-cache-not-as-state.md) |
| 2 | Split state by concern | MEDIUM | [`spa-split-state-by-concern.md`](spa-split-state-by-concern.md) |
| 3 | Code-split at the route level at minimum; split large... | MEDIUM | [`spa-code-split-at-the-route-level-at-minimum-split-large.md`](spa-code-split-at-the-route-level-at-minimum-split-large.md) |
| 4 | Prefetch likely next routes on hover or viewport proximity... | MEDIUM | [`spa-prefetch-likely-next-routes-on-hover-or-viewport-proximity.md`](spa-prefetch-likely-next-routes-on-hover-or-viewport-proximity.md) |
| 5 | Measure bundle size in CI | MEDIUM | [`spa-measure-bundle-size-in-ci.md`](spa-measure-bundle-size-in-ci.md) |
| 6 | Consider SSR or SSG for any pages that need SEO | CRITICAL | [`spa-consider-ssr-or-ssg-for-any-pages-that-need-seo.md`](spa-consider-ssr-or-ssg-for-any-pages-that-need-seo.md) |

---

---
title: "Code-split at the route level at minimum; split large..."
impact: MEDIUM
impactDescription: "general best practice"
tags: spa, dev, frontend, spa-architecture, client-side-routing, state-management-patterns
---

## Code-split at the route level at minimum; split large...

Code-split at the route level at minimum; split large components and heavy libraries on demand.

---

---
title: "Consider SSR or SSG for any pages that need SEO"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: spa, dev, frontend, spa-architecture, client-side-routing, state-management-patterns
---

## Consider SSR or SSG for any pages that need SEO

Consider SSR or SSG for any pages that need SEO — a pure SPA is almost never the right choice for public content.

---

---
title: "Measure bundle size in CI"
impact: MEDIUM
impactDescription: "general best practice"
tags: spa, dev, frontend, spa-architecture, client-side-routing, state-management-patterns
---

## Measure bundle size in CI

Measure bundle size in CI — set budgets and fail the build if they are exceeded.

---

---
title: "Prefetch likely next routes on hover or viewport proximity..."
impact: MEDIUM
impactDescription: "general best practice"
tags: spa, dev, frontend, spa-architecture, client-side-routing, state-management-patterns
---

## Prefetch likely next routes on hover or viewport proximity...

Prefetch likely next routes on hover or viewport proximity to make navigation feel instant.

---

---
title: "Split state by concern"
impact: MEDIUM
impactDescription: "general best practice"
tags: spa, dev, frontend, spa-architecture, client-side-routing, state-management-patterns
---

## Split state by concern

Split state by concern: URL state (router), server state (query library), UI state (local component state), global UI state (theme, auth — Zustand/Context).

---

---
title: "Treat server data as a cache, not as state"
impact: MEDIUM
impactDescription: "general best practice"
tags: spa, dev, frontend, spa-architecture, client-side-routing, state-management-patterns
---

## Treat server data as a cache, not as state

Treat server data as a cache, not as state — use TanStack Query or SWR instead of putting API responses in Redux.
