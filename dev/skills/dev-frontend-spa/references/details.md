<!-- Part of the dev-frontend-spa skill. Loaded on demand from SKILL.md. -->

# Single Page Applications (SPA) — details

## SPA Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Browser (Client)                      │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │  Router   │  │  State   │  │  Component Tree       │  │
│  │  (URL ↔   │  │  Store   │  │  (Virtual DOM /       │  │
│  │   View)   │  │          │  │   Reactive Updates)   │  │
│  └──────────┘  └──────────┘  └──────────────────────┘  │
│       │              │               │                    │
│       └──────────────┼───────────────┘                    │
│                      │                                    │
│              ┌───────▼───────┐                            │
│              │  Data Fetching │                            │
│              │  (API Client)  │                            │
│              └───────┬───────┘                            │
└──────────────────────┼────────────────────────────────────┘
                       │ HTTP/WebSocket
              ┌────────▼────────┐
              │   Backend API    │
              │  (REST/GraphQL)  │
              └─────────────────┘
```

### How It Works
1. Browser requests `index.html` — a minimal shell with a `<div id="root">` and a `<script>` tag
2. JavaScript bundle loads, initializes the router, and renders the initial view
3. User clicks a link — the router intercepts it, updates the URL (History API), and renders the new view without a page reload
4. Data is fetched asynchronously from APIs and rendered into the component tree
5. All subsequent navigation happens client-side — the server is never contacted for HTML again

## Client-Side Routing

### React Router (v6+)
```tsx
import { BrowserRouter, Routes, Route, Link, Outlet } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/dashboard">Dashboard</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<DashboardLayout />}>
          <Route index element={<Overview />} />
          <Route path="settings" element={<Settings />} />
        </Route>
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

function DashboardLayout() {
  return (
    <div>
      <Sidebar />
      <Outlet /> {/* Nested route renders here */}
    </div>
  );
}
```

### Vue Router
```typescript
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: () => import('./views/Home.vue') },
    {
      path: '/dashboard',
      component: () => import('./views/Dashboard.vue'),
      children: [
        { path: '', component: () => import('./views/Overview.vue') },
        { path: 'settings', component: () => import('./views/Settings.vue') },
      ],
    },
  ],
});
```

### Angular Router
```typescript
const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: 'dashboard',
    component: DashboardComponent,
    children: [
      { path: '', component: OverviewComponent },
      { path: 'settings', component: SettingsComponent },
    ],
    canActivate: [AuthGuard],
  },
  { path: '**', component: NotFoundComponent },
];
```

## Code Splitting and Lazy Loading

### Route-Based Splitting (React)
```tsx
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));
const Analytics = lazy(() => import('./pages/Analytics'));

function App() {
  return (
    <Suspense fallback={<PageSkeleton />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}
```

### Component-Level Splitting
```tsx
const HeavyChart = lazy(() => import('./components/HeavyChart'));

function AnalyticsPage() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <HeavyChart />
        </Suspense>
      )}
    </div>
  );
}
```

### Prefetching on Hover
```tsx
function NavLink({ to, children }: { to: string; children: React.ReactNode }) {
  const prefetch = () => {
    // Trigger dynamic import on hover — browser caches the chunk
    if (to === '/analytics') import('./pages/Analytics');
    if (to === '/settings') import('./pages/Settings');
  };

  return (
    <Link to={to} onMouseEnter={prefetch}>
      {children}
    </Link>
  );
}
```

## Bundle Optimization

### Vite Configuration
```typescript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom'],
          query: ['@tanstack/react-query'],
          ui: ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
        },
      },
    },
    chunkSizeWarningLimit: 500, // warn if chunk > 500KB
    sourcemap: true,
  },
});
```

### Tree Shaking Best Practices
- Use ES module imports (`import { map } from 'lodash-es'` not `import _ from 'lodash'`)
- Mark packages as `sideEffects: false` in `package.json` when safe
- Avoid barrel files (`index.ts` re-exports) in large libraries — they defeat tree shaking
- Use `import()` for anything not needed on initial render

## SEO Challenges and Solutions

| Challenge | Solution |
|-----------|----------|
| Empty HTML (JS-rendered content) | Prerendering at build time (react-snap, prerender-spa-plugin) |
| Search engines can't crawl SPA routes | SSG fallback for public pages |
| No meta tags until JS loads | React Helmet, Vue Meta, or SSR |
| Slow FCP hurts rankings | Code splitting + skeleton screens |
| Dynamic content not indexed | Server-side rendering for critical pages |

### Hybrid Approach
Many modern apps use a hybrid: SSR or SSG for public-facing pages (marketing, docs, blog) and SPA for authenticated dashboard/application pages. Frameworks like Next.js make this easy with per-page rendering strategies.

## Performance Considerations

| Metric | Target | Why It Matters |
|--------|--------|---------------|
| **First Contentful Paint (FCP)** | < 1.8s | User perceives the page is loading |
| **Time to Interactive (TTI)** | < 3.5s | User can actually interact with the page |
| **Total Blocking Time (TBT)** | < 200ms | Main thread responsiveness |
| **Bundle Size (initial, gzipped)** | < 150KB | Directly impacts FCP and TTI |
| **Largest Contentful Paint (LCP)** | < 2.5s | Core Web Vital — primary content visible |

### Performance Checklist
- [ ] Route-based code splitting enabled
- [ ] Vendor chunks separated from application code
- [ ] Images lazy-loaded below the fold
- [ ] Tree shaking verified (no dead code in bundle)
- [ ] Compression enabled (gzip or Brotli)
- [ ] Service Worker caching static assets (see `dev-frontend-pwa`)
- [ ] Bundle analyzer run (webpack-bundle-analyzer or rollup-plugin-visualizer)
- [ ] Core Web Vitals measured with real user data (CrUX, web-vitals library)
