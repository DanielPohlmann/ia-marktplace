---
name: dev-frontend-ssr
description: Use when choosing or implementing server rendering. USE FOR: SSR vs SSG vs ISR, islands, streaming SSR, React Server Components, Nuxt, Next.js, Remix, SvelteKit, Astro, SEO-critical pages. DO NOT USE FOR: client-only SPAs (use dev-frontend-spa), PWAs (use dev-frontend-pwa), micro-frontends (use dev-frontend-micro-frontends).
---

# Server-Side Rendering (SSR)

## Overview
Server-Side Rendering generates HTML on the server for each request, sending a fully-formed page to the browser. The client then "hydrates" the HTML — attaching event listeners and making it interactive. SSR combines the SEO and fast First Contentful Paint of traditional server-rendered pages with the rich interactivity of Single Page Applications. Beyond classic SSR, the modern landscape includes SSG, ISR, Islands Architecture, Streaming SSR, and React Server Components — each a different point on the spectrum between server and client rendering.

## SSR vs SSG vs ISR Decision Table

| Criteria | SSR | SSG | ISR |
|----------|-----|-----|-----|
| **Content Freshness** | Always fresh (per-request) | Stale until rebuild | Fresh within revalidation window |
| **TTFB** | Slower (server compute per request) | Fastest (CDN-served static) | Fast (CDN-served, revalidates async) |
| **Server Cost** | Higher (compute per request) | Minimal (CDN only) | Low (occasional revalidation) |
| **Dynamic Content** | Full support | None (build-time only) | Partial (revalidation delay) |
| **Personalization** | Full (cookies, auth) | None without client JS | None without client JS |
| **Scale** | Requires server infrastructure | Infinite (CDN) | Near-infinite (CDN + edge revalidation) |
| **Build Time** | None | Grows with page count | Grows initially, then on-demand |
| **Best For** | Authenticated dashboards, personalized content | Blogs, docs, marketing | E-commerce catalogs, news sites |

## Best Practices
- Default to SSG for content that does not change per request — it is the fastest and cheapest strategy.
- Use ISR for content that changes but does not need to be real-time (product catalogs, blog posts) — you get CDN speed with eventual freshness.
- Reserve full SSR for personalized or authenticated content that must be fresh on every request.
- Use streaming SSR to avoid blocking the entire page on the slowest data source — Suspense boundaries let fast parts render immediately.
- Prefer React Server Components for data fetching — they eliminate client-server waterfalls and ship zero JS for non-interactive UI.
- Consider Astro's Islands Architecture for content-heavy sites — shipping zero JS by default and hydrating only interactive components is a dramatic performance win.
- When using SSR, cache aggressively at the CDN/edge layer — not every request needs to hit your origin server.
- Avoid hydration mismatches — the server-rendered HTML and client render must produce identical output, or React will throw errors and re-render the entire tree.
- Test with JavaScript disabled to verify your SSR output is meaningful — if the page is blank without JS, your SSR is not doing its job.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/rendering-strategies.md](references/rendering-strategies.md) | Rendering Strategies — SSR — Server-Side Rendering, SSG — Static Site Generation, ISR — Incremental Static Regeneration, Islands Architecture, Streaming SSR, React Server Components (RSC) |
| [references/framework-deep-dives.md](references/framework-deep-dives.md) | Framework Deep Dives — Next.js (React), Nuxt (Vue), Remix (React), SvelteKit (Svelte), Astro (Islands Architecture) |
| [references/details.md](references/details.md) | Streaming SSR (React 18+) |

## References

- [web.dev — Rendering on the Web](https://web.dev/articles/rendering-on-the-web)
- [Next.js Documentation](https://nextjs.org/docs)

See references/rules.md for the full rule catalog.
