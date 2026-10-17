<!-- Part of the dev-frontend-pwa skill. Loaded on demand from SKILL.md. -->

# Service Workers

## Lifecycle

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ Register  │────▶│ Install   │────▶│ Activate  │────▶│ Running   │
│           │     │ (cache    │     │ (clean    │     │ (fetch    │
│           │     │  assets)  │     │  old      │     │  events)  │
│           │     │           │     │  caches)  │     │           │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                      │                                    │
                      │ waitUntil()                        │ Can be
                      │ self.skipWaiting()                 │ terminated
                      ▼                                    │ and restarted
                 On failure:                               │ by browser
                 SW not installed                          ▼
                                                     ┌──────────┐
                                                     │ Idle /    │
                                                     │ Terminated│
                                                     └──────────┘
```

## Service Worker Registration
```javascript
// main.js — register the service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', async () => {
    try {
      const registration = await navigator.serviceWorker.register('/sw.js', {
        scope: '/',
      });
      console.log('SW registered:', registration.scope);

      // Check for updates periodically
      setInterval(() => registration.update(), 60 * 60 * 1000); // hourly
    } catch (error) {
      console.error('SW registration failed:', error);
    }
  });
}
```

## Service Worker Implementation
```javascript
// sw.js
const CACHE_NAME = 'app-v1';
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/styles/main.css',
  '/scripts/app.js',
  '/images/logo.svg',
  '/offline.html',
];

// Install — precache app shell
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_URLS);
    })
  );
  self.skipWaiting(); // activate immediately
});

// Activate — clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    })
  );
  self.clients.claim(); // take control of all pages
});

// Fetch — serve from cache, fall back to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return cached || fetch(event.request).catch(() => {
        // Offline fallback for navigation requests
        if (event.request.mode === 'navigate') {
          return caches.match('/offline.html');
        }
      });
    })
  );
});
```
