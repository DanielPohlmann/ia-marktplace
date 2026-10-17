---
name: dev-frontend-pwa
description: Use when adding PWA capabilities to a web app. USE FOR: service worker lifecycle, cache-first/network-first/stale-while-revalidate, offline, manifest, installability, push, background sync, Workbox. DO NOT USE FOR: SPA routing/state (use dev-frontend-spa), SSR (use dev-frontend-ssr), architecture choice (use dev-frontend).
---

# Progressive Web Apps (PWA)

## Overview
A Progressive Web App is a web application that uses modern web APIs and a progressive enhancement strategy to deliver a native app-like experience. PWAs are installable, work offline, can receive push notifications, and run in their own window — all while being distributed via URL, not an app store. The three technical pillars are: HTTPS, a Service Worker, and a Web App Manifest.

> **Detailed how-tos with full code (service workers, caching strategies, manifest, installability, app shell, push, background sync, Workbox) live in [references/guide.md](references/guide.md); project-specific rules are in [references/rules.md](references/rules.md).** The material below is enough to orient and choose an approach.

## Best Practices
- Start with the app shell model — cache the UI frame so the app loads instantly, even offline.
- Use Workbox instead of hand-coding service workers — it handles edge cases (cache versioning, routing, expiration) that are easy to get wrong.
- Choose caching strategies per resource type: Cache First for static assets, Network First for API data, Stale-While-Revalidate for non-critical content.
- Always provide an offline fallback page — users should see something meaningful, not a browser error.
- Handle service worker updates gracefully — show a "New version available" banner rather than silently updating, which can break in-flight state.
- Test offline behavior in Chrome DevTools (Application > Service Workers > Offline checkbox).
- Size your app shell for sub-second loads on 3G — the shell should be under 50KB gzipped.
- Use Background Sync for data that must reach the server eventually (form submissions, analytics) — do not lose user actions to network failures.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/service-workers.md](references/service-workers.md) | Service Workers — Lifecycle, Service Worker Registration, Service Worker Implementation |
| [references/workbox.md](references/workbox.md) | Workbox — Workbox Configuration (with Vite), Workbox Strategies (Manual) |
| [references/details.md](references/details.md) | PWA Architecture; Caching Strategies; Web App Manifest; Installability Criteria; App Shell Model; Push Notifications; Background Sync |

## References

- [web.dev — Learn PWA](https://web.dev/learn/pwa)
- [MDN Web Docs — Progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)

See references/rules.md for the full rule catalog.
