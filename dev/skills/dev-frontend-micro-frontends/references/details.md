<!-- Part of the dev-frontend-micro-frontends skill. Loaded on demand from SKILL.md. -->

# Micro-Frontend Architecture — details

## Module Federation (Webpack 5 / Rspack)

### Remote Configuration
```javascript
// webpack.config.js — Remote (Product Team)
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  output: {
    publicPath: 'https://product.example.com/',
    uniqueName: 'product',
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'product',
      filename: 'remoteEntry.js',
      exposes: {
        './ProductList': './src/components/ProductList',
        './ProductDetail': './src/components/ProductDetail',
        './productApi': './src/api/products',
      },
      shared: {
        react: { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
        '@tanstack/react-query': { singleton: true },
      },
    }),
  ],
};
```

### Host Configuration
```javascript
// webpack.config.js — Host (Shell Application)
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        product: 'product@https://product.example.com/remoteEntry.js',
        cart: 'cart@https://cart.example.com/remoteEntry.js',
        profile: 'profile@https://profile.example.com/remoteEntry.js',
      },
      shared: {
        react: { singleton: true, eager: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true, eager: true, requiredVersion: '^18.0.0' },
        '@tanstack/react-query': { singleton: true },
      },
    }),
  ],
};
```

### Dynamic Remotes
```typescript
// Load remotes dynamically based on configuration
async function loadRemoteModule(scope: string, module: string) {
  // Initialize sharing scope
  await __webpack_init_sharing__('default');

  const container = window[scope];
  await container.init(__webpack_share_scopes__.default);

  const factory = await container.get(module);
  return factory();
}

// Usage — load a remote component at runtime
const ProductList = React.lazy(() =>
  loadRemoteModule('product', './ProductList')
);

function App() {
  return (
    <Suspense fallback={<Skeleton />}>
      <ProductList />
    </Suspense>
  );
}
```

## single-spa

single-spa is a framework-agnostic micro-frontend orchestrator. It manages the lifecycle of multiple frontend applications (called "applications" or "parcels") within a single page.

### Core Concepts
- **Applications**: Full page-level micro-frontends mounted/unmounted based on URL routes
- **Parcels**: Framework-agnostic components that can be mounted anywhere, regardless of route
- **Layout Engine**: Declarative HTML-based routing for micro-frontends

### Root Config
```javascript
// root-config.js
import { registerApplication, start } from 'single-spa';

registerApplication({
  name: '@org/navbar',
  app: () => System.import('@org/navbar'),
  activeWhen: () => true, // always active
});

registerApplication({
  name: '@org/products',
  app: () => System.import('@org/products'),
  activeWhen: '/products',
  customProps: { authToken: getAuthToken() },
});

registerApplication({
  name: '@org/checkout',
  app: () => System.import('@org/checkout'),
  activeWhen: '/checkout',
});

start();
```

### single-spa Application (React)
```javascript
// @org/products — single-spa-react wrapper
import React from 'react';
import ReactDOMClient from 'react-dom/client';
import singleSpaReact from 'single-spa-react';
import App from './App';

const lifecycles = singleSpaReact({
  React,
  ReactDOMClient,
  rootComponent: App,
  errorBoundary(err, info, props) {
    return <div>Error loading Products module</div>;
  },
});

export const { bootstrap, mount, unmount } = lifecycles;
```

## Web Components as Micro-Frontend Boundaries

Web Components provide native browser encapsulation (Shadow DOM) that makes them excellent micro-frontend boundaries — each team ships a custom element that encapsulates its framework and styles.

```typescript
// Product team ships a custom element
class ProductCard extends HTMLElement {
  private root: ShadowRoot;

  constructor() {
    super();
    this.root = this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    const productId = this.getAttribute('product-id');
    // Mount React/Vue/Svelte inside the shadow DOM
    this.render(productId);
  }

  disconnectedCallback() {
    // Cleanup framework instance
  }

  static get observedAttributes() {
    return ['product-id'];
  }

  attributeChangedCallback(name: string, oldVal: string, newVal: string) {
    if (name === 'product-id') this.render(newVal);
  }

  private render(productId: string | null) {
    // Render framework component into shadow root
  }
}

customElements.define('product-card', ProductCard);
```

Usage in any framework or plain HTML:
```html
<product-card product-id="abc-123"></product-card>
```

## Shared State and Communication

Micro-frontends are independently deployed, so they cannot share in-memory state directly. Communication strategies:

### Custom Events (Recommended)
```typescript
// Publishing micro-frontend
window.dispatchEvent(
  new CustomEvent('cart:item-added', {
    detail: { productId: 'abc-123', quantity: 1 },
  })
);

// Consuming micro-frontend
window.addEventListener('cart:item-added', (event: CustomEvent) => {
  const { productId, quantity } = event.detail;
  updateCartBadge(productId, quantity);
});
```

### Shared Observable (Event Bus)
```typescript
// shared-state.ts — published as a shared package
import { BehaviorSubject } from 'rxjs';

export interface AppState {
  user: User | null;
  cartCount: number;
  theme: 'light' | 'dark';
}

export const appState$ = new BehaviorSubject<AppState>({
  user: null,
  cartCount: 0,
  theme: 'light',
});

// Any micro-frontend can subscribe
appState$.subscribe((state) => {
  console.log('Cart count:', state.cartCount);
});

// Any micro-frontend can update
appState$.next({ ...appState$.value, cartCount: 5 });
```

### URL-Based Communication
Use URL search params or path segments as shared state. Each micro-frontend reads from and writes to the URL — the URL becomes the single source of truth.

```typescript
// Product micro-frontend sets filter
const url = new URL(window.location.href);
url.searchParams.set('category', 'electronics');
url.searchParams.set('sort', 'price-asc');
window.history.pushState({}, '', url);

// Sidebar micro-frontend reads filter
const params = new URLSearchParams(window.location.search);
const category = params.get('category');
const sort = params.get('sort');
```
