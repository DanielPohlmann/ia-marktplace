---
name: dev-frontend-spa
description: Use when designing a single-page application. USE FOR: client-side routing, state management (Pinia, Redux), data fetching, code splitting, lazy loading, bundle size, SPA vs MPA. DO NOT USE FOR: SSR/SSG (use dev-frontend-ssr), PWAs (use dev-frontend-pwa), micro-frontends (use dev-frontend-micro-frontends).
---

# Single Page Applications (SPA)

## Overview
A Single Page Application loads a single HTML shell, then uses JavaScript to dynamically render content and handle navigation entirely in the browser. The server provides JSON APIs; the client handles routing, rendering, and state. SPAs deliver rich, app-like experiences — think Gmail, Figma, or Notion — but come with tradeoffs in SEO, initial load performance, and complexity.

## SPA vs MPA Decision

| Factor | SPA | MPA (Multi-Page App) |
|--------|-----|---------------------|
| **Navigation** | Instant (client-side) | Full page reload |
| **Initial Load** | Slower (large JS bundle) | Faster (server HTML) |
| **SEO** | Challenging (needs prerendering or SSR) | Native |
| **Interactivity** | Rich, app-like | Page-based, simpler |
| **Offline** | Possible (with Service Workers) | Difficult |
| **State Persistence** | Survives navigation | Lost on page reload |
| **Complexity** | Higher (routing, state, hydration) | Lower |
| **Best For** | Dashboards, SaaS, tools | Content sites, blogs, e-commerce |

**Rule of thumb**: If your app feels like a *document*, use an MPA or SSR. If it feels like an *application*, use a SPA.

## Best Practices
- Treat server data as a cache, not as state — use TanStack Query or SWR instead of putting API responses in Redux.
- Split state by concern: URL state (router), server state (query library), UI state (local component state), global UI state (theme, auth — Zustand/Context).
- Code-split at the route level at minimum; split large components and heavy libraries on demand.
- Prefetch likely next routes on hover or viewport proximity to make navigation feel instant.
- Measure bundle size in CI — set budgets and fail the build if they are exceeded.
- Consider SSR or SSG for any pages that need SEO — a pure SPA is almost never the right choice for public content.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/state-management.md](references/state-management.md) | State Management — State Management Landscape, Zustand (Modern React State), Pinia (Vue State) |
| [references/data-fetching.md](references/data-fetching.md) | Data Fetching — The Server State Problem, TanStack Query (React Query), SWR (Vercel), Apollo Client (GraphQL) |
| [references/details.md](references/details.md) | SPA Architecture; Client-Side Routing; Code Splitting and Lazy Loading; Bundle Optimization; SEO Challenges and Solutions; Performance Considerations |

## References

- [MDN Web Docs — Single-Page Applications](https://developer.mozilla.org/en-US/docs/Glossary/SPA)
- [Single-Page Application — Wikipedia](https://en.wikipedia.org/wiki/Single-page_application)

See references/rules.md for the full rule catalog.
