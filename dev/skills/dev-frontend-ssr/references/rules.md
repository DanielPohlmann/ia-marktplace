# Server-Side Rendering Rules

Best practices and rules for Server-Side Rendering.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Default to SSG for content that does not change per request | MEDIUM | [`ssr-default-to-ssg-for-content-that-does-not-change-per-request.md`](ssr-default-to-ssg-for-content-that-does-not-change-per-request.md) |
| 2 | Use ISR for content that changes but does not need to be... | MEDIUM | [`ssr-use-isr-for-content-that-changes-but-does-not-need-to-be.md`](ssr-use-isr-for-content-that-changes-but-does-not-need-to-be.md) |
| 3 | Reserve full SSR for personalized or authenticated content... | CRITICAL | [`ssr-reserve-full-ssr-for-personalized-or-authenticated-content.md`](ssr-reserve-full-ssr-for-personalized-or-authenticated-content.md) |
| 4 | Use streaming SSR to avoid blocking the entire page on the... | HIGH | [`ssr-use-streaming-ssr-to-avoid-blocking-the-entire-page-on-the.md`](ssr-use-streaming-ssr-to-avoid-blocking-the-entire-page-on-the.md) |
| 5 | Prefer React Server Components for data fetching | LOW | [`ssr-prefer-react-server-components-for-data-fetching.md`](ssr-prefer-react-server-components-for-data-fetching.md) |
| 6 | Consider Astro's Islands Architecture for content-heavy... | LOW | [`ssr-consider-astro-s-islands-architecture-for-content-heavy.md`](ssr-consider-astro-s-islands-architecture-for-content-heavy.md) |
| 7 | When using SSR, cache aggressively at the CDN/edge layer | MEDIUM | [`ssr-when-using-ssr-cache-aggressively-at-the-cdn-edge-layer.md`](ssr-when-using-ssr-cache-aggressively-at-the-cdn-edge-layer.md) |
| 8 | Avoid hydration mismatches | CRITICAL | [`ssr-avoid-hydration-mismatches.md`](ssr-avoid-hydration-mismatches.md) |
| 9 | Test with JavaScript disabled to verify your SSR output is... | MEDIUM | [`ssr-test-with-javascript-disabled-to-verify-your-ssr-output-is.md`](ssr-test-with-javascript-disabled-to-verify-your-ssr-output-is.md) |

---

---
title: "Avoid hydration mismatches"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Avoid hydration mismatches

Avoid hydration mismatches — the server-rendered HTML and client render must produce identical output, or React will throw errors and re-render the entire tree.

---

---
title: "Consider Astro's Islands Architecture for content-heavy..."
impact: LOW
impactDescription: "recommended but situational"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Consider Astro's Islands Architecture for content-heavy...

Consider Astro's Islands Architecture for content-heavy sites — shipping zero JS by default and hydrating only interactive components is a dramatic performance win.

---

---
title: "Default to SSG for content that does not change per request"
impact: MEDIUM
impactDescription: "general best practice"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Default to SSG for content that does not change per request

Default to SSG for content that does not change per request — it is the fastest and cheapest strategy.

---

---
title: "Prefer React Server Components for data fetching"
impact: LOW
impactDescription: "recommended but situational"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Prefer React Server Components for data fetching

Prefer React Server Components for data fetching — they eliminate client-server waterfalls and ship zero JS for non-interactive UI.

---

---
title: "Reserve full SSR for personalized or authenticated content..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Reserve full SSR for personalized or authenticated content...

Reserve full SSR for personalized or authenticated content that must be fresh on every request.

---

---
title: "Test with JavaScript disabled to verify your SSR output is..."
impact: MEDIUM
impactDescription: "general best practice"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Test with JavaScript disabled to verify your SSR output is...

Test with JavaScript disabled to verify your SSR output is meaningful — if the page is blank without JS, your SSR is not doing its job.

---

---
title: "Use ISR for content that changes but does not need to be..."
impact: MEDIUM
impactDescription: "general best practice"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Use ISR for content that changes but does not need to be...

Use ISR for content that changes but does not need to be real-time (product catalogs, blog posts) — you get CDN speed with eventual freshness.

---

---
title: "Use streaming SSR to avoid blocking the entire page on the..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## Use streaming SSR to avoid blocking the entire page on the...

Use streaming SSR to avoid blocking the entire page on the slowest data source — Suspense boundaries let fast parts render immediately.

---

---
title: "When using SSR, cache aggressively at the CDN/edge layer"
impact: MEDIUM
impactDescription: "general best practice"
tags: ssr, dev, frontend, server-side-rendering, ssg, isr
---

## When using SSR, cache aggressively at the CDN/edge layer

When using SSR, cache aggressively at the CDN/edge layer — not every request needs to hit your origin server.
