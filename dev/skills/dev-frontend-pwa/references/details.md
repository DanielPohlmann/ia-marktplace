<!-- Part of the dev-frontend-pwa skill. Loaded on demand from SKILL.md. -->

# Progressive Web Apps (PWA) — details

## PWA Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Browser                               │
│                                                              │
│  ┌────────────────────┐    ┌──────────────────────────────┐ │
│  │  Web App            │    │  Service Worker (SW)          │ │
│  │  (HTML/CSS/JS)      │    │  (Background thread)          │ │
│  │                     │    │                                │ │
│  │  Registers SW ──────┼───▶│  Intercepts fetch requests    │ │
│  │  Requests data ─────┼───▶│  Manages cache                │ │
│  │  Receives push ◀────┼────│  Handles push notifications   │ │
│  │                     │    │  Background sync               │ │
│  └────────────────────┘    └──────────┬───────────────────┘ │
│                                       │                      │
│                              ┌────────▼────────┐             │
│                              │  Cache Storage    │             │
│                              │  (CacheAPI)       │             │
│                              └──────────────────┘             │
└───────────────────────────────────────┼──────────────────────┘
                                        │ Network (when available)
                               ┌────────▼────────┐
                               │  Server / CDN    │
                               └─────────────────┘
```

## Caching Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| **Cache First** | Check cache first, fall back to network | Static assets (CSS, JS, images, fonts) |
| **Network First** | Try network first, fall back to cache | API calls, dynamic content |
| **Stale-While-Revalidate** | Serve from cache immediately, update cache from network in background | Frequently updated but non-critical content |
| **Network Only** | Always fetch from network, never cache | Real-time data, authentication |
| **Cache Only** | Only serve from cache, never hit network | Precached app shell, offline-only assets |

### Cache First
```javascript
self.addEventListener('fetch', (event) => {
  if (event.request.destination === 'image') {
    event.respondWith(
      caches.match(event.request).then((cached) => {
        return cached || fetch(event.request).then((response) => {
          const clone = response.clone();
          caches.open('images-v1').then((cache) => cache.put(event.request, clone));
          return response;
        });
      })
    );
  }
});
```

### Network First
```javascript
async function networkFirst(request, cacheName) {
  try {
    const networkResponse = await fetch(request);
    const cache = await caches.open(cacheName);
    cache.put(request, networkResponse.clone());
    return networkResponse;
  } catch (error) {
    const cached = await caches.match(request);
    return cached || new Response('Offline', { status: 503 });
  }
}
```

### Stale-While-Revalidate
```javascript
async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);

  const networkFetch = fetch(request).then((response) => {
    cache.put(request, response.clone());
    return response;
  });

  return cached || networkFetch;
}
```

## Web App Manifest

### manifest.json
```json
{
  "name": "My Progressive Web App",
  "short_name": "MyPWA",
  "description": "A production-ready progressive web application",
  "start_url": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#1a73e8",
  "background_color": "#ffffff",
  "scope": "/",
  "icons": [
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ],
  "screenshots": [
    {
      "src": "/screenshots/home.png",
      "sizes": "1280x720",
      "type": "image/png",
      "form_factor": "wide"
    },
    {
      "src": "/screenshots/mobile.png",
      "sizes": "750x1334",
      "type": "image/png",
      "form_factor": "narrow"
    }
  ],
  "shortcuts": [
    {
      "name": "New Task",
      "short_name": "New",
      "url": "/new",
      "icons": [{ "src": "/icons/new-task.png", "sizes": "96x96" }]
    }
  ],
  "categories": ["productivity"],
  "lang": "en-US",
  "dir": "ltr"
}
```

### Linking the Manifest
```html
<head>
  <link rel="manifest" href="/manifest.json" />
  <meta name="theme-color" content="#1a73e8" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="default" />
  <meta name="apple-mobile-web-app-title" content="MyPWA" />
  <link rel="apple-touch-icon" href="/icons/icon-192x192.png" />
</head>
```

## Installability Criteria

For a PWA to be installable (show the browser's install prompt), it must meet these requirements:

1. **HTTPS** — Served over a secure connection (localhost is exempt for development)
2. **Web App Manifest** — Valid `manifest.json` with:
   - `name` or `short_name`
   - `start_url`
   - `display` set to `standalone`, `fullscreen`, or `minimal-ui`
   - At least one icon (192x192 and 512x512 recommended)
3. **Service Worker** — A registered service worker with a `fetch` event handler
4. **No blocking install criteria** — No already-installed version of the app

### Install Prompt Handling
```javascript
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (event) => {
  event.preventDefault();
  deferredPrompt = event;
  showInstallButton(); // show your custom UI
});

async function handleInstallClick() {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  console.log(`User ${outcome === 'accepted' ? 'installed' : 'dismissed'} the app`);
  deferredPrompt = null;
}

window.addEventListener('appinstalled', () => {
  console.log('App installed successfully');
  hideInstallButton();
});
```

## App Shell Model

The app shell is the minimal HTML, CSS, and JavaScript required to render the UI "frame" — navigation, header, sidebar — without any content. Content is loaded dynamically after the shell renders.

```
┌─────────────────────────────────────┐
│  App Shell (cached, loads instantly) │
│  ┌───────────────────────────────┐  │
│  │  Header / Navigation          │  │
│  ├───────────────────────────────┤  │
│  │  Sidebar  │  ┌─────────────┐ │  │
│  │           │  │  Content     │ │  │
│  │           │  │  (loaded     │ │  │
│  │           │  │   from API   │ │  │
│  │           │  │   or cache)  │ │  │
│  │           │  └─────────────┘ │  │
│  ├───────────────────────────────┤  │
│  │  Footer                       │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Push Notifications

### Subscribing
```javascript
async function subscribeToPush(registration) {
  const permission = await Notification.requestPermission();
  if (permission !== 'granted') return;

  const subscription = await registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY),
  });

  // Send subscription to your server
  await fetch('/api/push/subscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(subscription),
  });
}
```

### Handling Push Events (in Service Worker)
```javascript
// sw.js
self.addEventListener('push', (event) => {
  const data = event.data?.json() ?? {};
  const { title, body, icon, url } = data;

  event.waitUntil(
    self.registration.showNotification(title, {
      body,
      icon: icon || '/icons/icon-192x192.png',
      badge: '/icons/badge-72x72.png',
      data: { url },
      actions: [
        { action: 'open', title: 'Open' },
        { action: 'dismiss', title: 'Dismiss' },
      ],
    })
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  if (event.action === 'dismiss') return;

  const url = event.notification.data?.url || '/';
  event.waitUntil(clients.openWindow(url));
});
```

## Background Sync

```javascript
// In your app — register a sync event
async function saveDataWithSync(data) {
  // Store data in IndexedDB first
  await saveToIndexedDB('outbox', data);

  // Register background sync
  const registration = await navigator.serviceWorker.ready;
  await registration.sync.register('sync-outbox');
}

// sw.js — handle the sync event
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-outbox') {
    event.waitUntil(syncOutbox());
  }
});

async function syncOutbox() {
  const items = await getFromIndexedDB('outbox');
  for (const item of items) {
    try {
      await fetch('/api/data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(item),
      });
      await deleteFromIndexedDB('outbox', item.id);
    } catch (error) {
      // Will retry on next sync opportunity
      throw error;
    }
  }
}
```
