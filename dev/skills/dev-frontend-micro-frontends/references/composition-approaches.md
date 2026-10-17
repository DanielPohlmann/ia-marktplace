<!-- Part of the dev-frontend-micro-frontends skill. Loaded on demand from SKILL.md. -->

# Composition Approaches

```
┌──────────────────────────────────────────────────────────────────┐
│                  Micro-Frontend Composition                       │
│                                                                   │
│  Build-Time             Runtime                  Server-Side      │
│  ┌──────────────┐       ┌──────────────────┐     ┌────────────┐  │
│  │ npm packages │       │ Module Federation│     │ ESI / SSI  │  │
│  │ Monorepo     │       │ Import Maps      │     │ SSR Comp.  │  │
│  │ imports      │       │ iframes          │     │ Tailor /   │  │
│  │              │       │ Web Components   │     │ Podium     │  │
│  └──────────────┘       └──────────────────┘     └────────────┘  │
│                                                                   │
│  + Type safety            + Independent deploy    + SEO-friendly  │
│  + Optimized bundle       + Tech-stack freedom    + Fast FCP      │
│  - Coupled releases       - Runtime overhead      - Complexity    │
│  - Single deploy          - Larger bundles        - Server infra  │
└──────────────────────────────────────────────────────────────────┘
```

## Build-Time Composition
Each micro-frontend is published as an npm package and consumed by a host application at build time.

```json
// package.json of the host/shell application
{
  "dependencies": {
    "@org/header": "^2.1.0",
    "@org/product-catalog": "^3.4.0",
    "@org/checkout": "^1.8.0",
    "@org/user-profile": "^2.0.0"
  }
}
```

**Tradeoff**: Strong type safety and optimized bundles, but all micro-frontends must be built and deployed together — defeating much of the independence benefit.

## Runtime Composition — Module Federation
Webpack 5 Module Federation (and Rspack) allows applications to share code at runtime. A "host" application dynamically loads "remote" modules from independently deployed bundles.

```
┌──────────────────────────────────────────────────────────┐
│  Host (Shell Application)                                 │
│                                                           │
│  Loads at runtime:                                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Remote A     │  │ Remote B     │  │ Remote C     │      │
│  │ (Product)    │  │ (Cart)       │  │ (Profile)    │      │
│  │ React 18     │  │ Vue 3        │  │ React 18     │      │
│  │ Port 3001    │  │ Port 3002    │  │ Port 3003    │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                           │
│  Shared: react, react-dom (singleton)                     │
└──────────────────────────────────────────────────────────┘
```

## Runtime Composition — Import Maps
Native browser import maps allow mapping bare module specifiers to URLs, enabling runtime loading without a bundler federation plugin.

```html
<script type="importmap">
{
  "imports": {
    "@org/header": "https://cdn.example.com/header/v2.1.0/index.js",
    "@org/product": "https://cdn.example.com/product/v3.4.0/index.js",
    "react": "https://cdn.example.com/react/18.2.0/react.production.min.js"
  }
}
</script>
```

## Runtime Composition — iframes
The simplest (and oldest) isolation approach. Each micro-frontend runs in its own iframe with full CSS and JS isolation. Drawbacks: no shared DOM, awkward communication, SEO-invisible, accessibility challenges.

## Server-Side Composition
Fragments are assembled on the server before sending HTML to the client. Approaches include Edge Side Includes (ESI), Server-Side Includes (SSI), and frameworks like Podium (Node.js) or Piral.
