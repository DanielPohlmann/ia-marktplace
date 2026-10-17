<!-- Part of the dev-frontend-ssr skill. Loaded on demand from SKILL.md. -->

# Rendering Strategies

```
┌──────────────────────────────────────────────────────────────────┐
│                    Rendering Strategy Spectrum                     │
│                                                                   │
│  SSG ──────▶ ISR ──────▶ SSR ──────▶ Streaming ──────▶ RSC      │
│                                                                   │
│  Build-time    Build-time    Per-request   Per-request   Server-  │
│  HTML          + revalidate  HTML on       HTML streamed  only     │
│  Static CDN    on demand     every req     progressively components│
└──────────────────────────────────────────────────────────────────┘
```

## SSR — Server-Side Rendering
HTML is rendered on the server for **every request**. The client receives a complete page, then hydrates it with JavaScript for interactivity.

```
Browser request → Server renders HTML → Browser displays HTML → JS loads → Hydration → Interactive
```

## SSG — Static Site Generation
HTML is rendered at **build time**. Pages are pre-generated as static files and served from a CDN. Content is only as fresh as the last build.

```
Build step → HTML files generated → Deployed to CDN → Browser requests static file → Instant response
```

## ISR — Incremental Static Regeneration
A hybrid of SSG and SSR. Pages are statically generated but **revalidated** in the background after a configurable time interval. First popularized by Next.js.

```
First request → Serve cached static page → Background revalidation → Next request gets fresh page
```

## Islands Architecture
The page is mostly **static HTML** with isolated "islands" of interactivity. Only the interactive components ship JavaScript and hydrate independently. The rest of the page is zero-JS static HTML.

```
┌───────────────────────────────────────────────────┐
│  Static HTML (no JS)                               │
│  ┌─────────────┐                ┌──────────────┐  │
│  │  Island:     │                │  Island:      │  │
│  │  Search Bar  │  Static text   │  Add to Cart  │  │
│  │  (hydrated)  │  and images    │  (hydrated)   │  │
│  └─────────────┘  (no JS)       └──────────────┘  │
│                                                    │
│  Static HTML (no JS)                               │
│  ┌──────────────────────────────────────────────┐  │
│  │  Island: Image Carousel (hydrated)            │  │
│  └──────────────────────────────────────────────┘  │
│  Static HTML (no JS)                               │
└───────────────────────────────────────────────────┘
```

## Streaming SSR
Instead of waiting for the entire page to render, the server **streams** HTML to the browser as it becomes ready. React 18 Suspense boundaries define streaming chunks — fast parts render first, slow parts (data fetching) stream in later.

```
Server starts streaming HTML →
  [Header renders immediately]
  [Main content streams as data resolves]
  [Suspense fallback replaced by real content]
  [JavaScript hydrates progressively]
```

## React Server Components (RSC)
A paradigm shift: components that run **only on the server** and never ship JavaScript to the client. RSC can directly access databases, filesystems, and server-only APIs. Client Components (marked with `'use client'`) handle interactivity and ship JS. The two compose seamlessly in the same component tree.

```
┌──────────────────────────────────────────────────────┐
│  Server Component Tree (zero JS to client)            │
│  ┌────────────────────────────────────────────────┐  │
│  │  ServerLayout                                   │  │
│  │    ├── ServerHeader (DB query for user)         │  │
│  │    ├── ServerArticle (filesystem read)          │  │
│  │    │     └── ClientLikeButton ('use client')   │  │
│  │    └── ServerSidebar (API call for related)     │  │
│  │          └── ClientSearch ('use client')        │  │
│  └────────────────────────────────────────────────┘  │
│                                                       │
│  Only ClientLikeButton and ClientSearch ship JS       │
└──────────────────────────────────────────────────────┘
```
