---
name: dev-frontend-micro-frontends
description: Use when splitting a frontend across independently deployed apps or teams. USE FOR: Module Federation (Webpack 5/Rspack), single-spa, import maps, iframes, web components, shared deps, cross-app events, independent pipelines. DO NOT USE FOR: single-team SPAs (use dev-frontend-spa), SSR (use dev-frontend-ssr), backend decomposition (use dev-architecture-microservices).
---

# Micro-Frontend Architecture

## Overview
Micro-frontends extend the microservices idea to the frontend: independently developed, tested, and deployed frontend applications that are composed into a single, cohesive user experience. Each team owns a vertical slice of the product — from the UI layer down through the API — with autonomy over their tech stack, build pipeline, and release cadence. The approach trades simplicity for team scalability.

## Tradeoffs

| Dimension | Benefit | Cost |
|-----------|---------|------|
| **Team Autonomy** | Teams choose their own framework, tooling, release cadence | Inconsistent UX without strong design system governance |
| **Independent Deployment** | Ship features without coordinating with other teams | Versioning complexity, integration testing burden |
| **Tech-Stack Freedom** | Adopt new frameworks incrementally, avoid full rewrites | Multiple frameworks = larger aggregate bundle, more to learn |
| **Fault Isolation** | One micro-frontend crashing does not bring down the page | Error boundaries and fallbacks add complexity |
| **Bundle Size** | Each team optimizes their own bundle | Duplicate dependencies if sharing is not configured correctly |
| **Routing** | Each team owns their routes | Cross-app navigation, deep linking, and shared layouts are harder |
| **Shared Dependencies** | Module Federation singleton sharing reduces duplication | Version mismatches can cause subtle runtime errors |
| **Organizational Fit** | Scales with the number of teams (Conway's Law) | Overkill for small teams — adds overhead without benefit |

## When to Use Micro-Frontends

**Use when**:
- Multiple teams (3+) work on the same user-facing application
- Teams need independent deployment and release cadences
- You are migrating a large legacy frontend incrementally (strangler fig pattern)
- Different parts of the app have fundamentally different requirements (e.g., a dashboard vs. a content editor)

**Do not use when**:
- A single team owns the entire frontend
- The application is small to medium in scope
- You can solve the problem with a well-organized monorepo and code splitting
- You lack the infrastructure for independent builds, deployments, and integration testing

## Best Practices
- Establish a shared design system (component library, tokens, CSS variables) — team autonomy does not mean visual chaos.
- Use Module Federation's `singleton: true` for critical shared dependencies (React, router) to avoid duplicate instances.
- Define clear contracts between micro-frontends — custom events with typed payloads, not ad-hoc DOM coupling.
- Invest in integration testing — test the composed page, not just individual micro-frontends in isolation.
- Start with a monolith and extract micro-frontends only when organizational pain (release coordination, merge conflicts, team coupling) justifies the architectural complexity.
- Use a shell/host application that owns the layout, authentication, and top-level routing — micro-frontends own their content area only.
- Monitor aggregate bundle size — without vigilance, micro-frontends will independently add dependencies until the total payload dwarfs a monolith.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/composition-approaches.md](references/composition-approaches.md) | Composition Approaches — Build-Time Composition, Runtime Composition — Module Federation, Runtime Composition — Import Maps, Runtime Composition — iframes, Server-Side Composition |
| [references/details.md](references/details.md) | Module Federation (Webpack 5 / Rspack); single-spa; Web Components as Micro-Frontend Boundaries; Shared State and Communication |

## References

- [Martin Fowler — Micro Frontends](https://martinfowler.com/articles/micro-frontends.html)
- [Micro-Frontends — Wikipedia](https://en.wikipedia.org/wiki/Microfrontend)

See references/rules.md for the full rule catalog.
