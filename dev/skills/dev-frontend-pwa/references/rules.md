# Progressive Web Apps Rules

Best practices and rules for Progressive Web Apps.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with the app shell model | MEDIUM | [`pwa-start-with-the-app-shell-model.md`](pwa-start-with-the-app-shell-model.md) |
| 2 | Use Workbox instead of hand-coding service workers | MEDIUM | [`pwa-use-workbox-instead-of-hand-coding-service-workers.md`](pwa-use-workbox-instead-of-hand-coding-service-workers.md) |
| 3 | Choose caching strategies per resource type | CRITICAL | [`pwa-choose-caching-strategies-per-resource-type.md`](pwa-choose-caching-strategies-per-resource-type.md) |
| 4 | Always provide an offline fallback page | CRITICAL | [`pwa-always-provide-an-offline-fallback-page.md`](pwa-always-provide-an-offline-fallback-page.md) |
| 5 | Handle service worker updates gracefully | MEDIUM | [`pwa-handle-service-worker-updates-gracefully.md`](pwa-handle-service-worker-updates-gracefully.md) |
| 6 | Test offline behavior in Chrome DevTools (Application >... | MEDIUM | [`pwa-test-offline-behavior-in-chrome-devtools-application.md`](pwa-test-offline-behavior-in-chrome-devtools-application.md) |
| 7 | Size your app shell for sub-second loads on 3G | MEDIUM | [`pwa-size-your-app-shell-for-sub-second-loads-on-3g.md`](pwa-size-your-app-shell-for-sub-second-loads-on-3g.md) |
| 8 | Use Background Sync for data that must reach the server... | CRITICAL | [`pwa-use-background-sync-for-data-that-must-reach-the-server.md`](pwa-use-background-sync-for-data-that-must-reach-the-server.md) |

---

---
title: "Always provide an offline fallback page"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Always provide an offline fallback page

Always provide an offline fallback page — users should see something meaningful, not a browser error.

---

---
title: "Choose caching strategies per resource type"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Choose caching strategies per resource type

Choose caching strategies per resource type: Cache First for static assets, Network First for API data, Stale-While-Revalidate for non-critical content.

---

---
title: "Handle service worker updates gracefully"
impact: MEDIUM
impactDescription: "general best practice"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Handle service worker updates gracefully

Handle service worker updates gracefully — show a "New version available" banner rather than silently updating, which can break in-flight state.

---

---
title: "Size your app shell for sub-second loads on 3G"
impact: MEDIUM
impactDescription: "general best practice"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Size your app shell for sub-second loads on 3G

Size your app shell for sub-second loads on 3G — the shell should be under 50KB gzipped.

---

---
title: "Start with the app shell model"
impact: MEDIUM
impactDescription: "general best practice"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Start with the app shell model

Start with the app shell model — cache the UI frame so the app loads instantly, even offline.

---

---
title: "Test offline behavior in Chrome DevTools (Application >..."
impact: MEDIUM
impactDescription: "general best practice"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Test offline behavior in Chrome DevTools (Application >...

Test offline behavior in Chrome DevTools (Application > Service Workers > Offline checkbox).

---

---
title: "Use Background Sync for data that must reach the server..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Use Background Sync for data that must reach the server...

Use Background Sync for data that must reach the server eventually (form submissions, analytics) — do not lose user actions to network failures.

---

---
title: "Use Workbox instead of hand-coding service workers"
impact: MEDIUM
impactDescription: "general best practice"
tags: pwa, dev, frontend, progressive-web-apps, service-workers, offline-support
---

## Use Workbox instead of hand-coding service workers

Use Workbox instead of hand-coding service workers — it handles edge cases (cache versioning, routing, expiration) that are easy to get wrong.
