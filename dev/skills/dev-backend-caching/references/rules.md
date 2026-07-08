# Caching Strategies & Patterns Rules

Best practices and rules for Caching Strategies & Patterns.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always set a TTL on every cache entry -- even if you also... | CRITICAL | [`caching-always-set-a-ttl-on-every-cache-entry-even-if-you-also.md`](caching-always-set-a-ttl-on-every-cache-entry-even-if-you-also.md) |
| 2 | Monitor cache hit rates | MEDIUM | [`caching-monitor-cache-hit-rates.md`](caching-monitor-cache-hit-rates.md) |
| 3 | Design for cache failure gracefully | CRITICAL | [`caching-design-for-cache-failure-gracefully.md`](caching-design-for-cache-failure-gracefully.md) |
| 4 | Never cache sensitive data (credentials, tokens, PII)... | CRITICAL | [`caching-never-cache-sensitive-data-credentials-tokens-pii.md`](caching-never-cache-sensitive-data-credentials-tokens-pii.md) |
| 5 | Use consistent hashing for distributed cache clusters to... | MEDIUM | [`caching-use-consistent-hashing-for-distributed-cache-clusters-to.md`](caching-use-consistent-hashing-for-distributed-cache-clusters-to.md) |
| 6 | Prefer cache-aside as the starting pattern | LOW | [`caching-prefer-cache-aside-as-the-starting-pattern.md`](caching-prefer-cache-aside-as-the-starting-pattern.md) |
| 7 | Implement cache stampede protection (locking or... | HIGH | [`caching-implement-cache-stampede-protection-locking-or.md`](caching-implement-cache-stampede-protection-locking-or.md) |

---

---
title: "Always set a TTL on every cache entry -- even if you also..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Always set a TTL on every cache entry -- even if you also...

Always set a TTL on every cache entry -- even if you also use event-based invalidation. TTL is your safety net against stale data from missed events.

---

---
title: "Design for cache failure gracefully"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Design for cache failure gracefully

Design for cache failure gracefully: the system must function (possibly with degraded performance) when the cache is unavailable.

---

---
title: "Implement cache stampede protection (locking or..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Implement cache stampede protection (locking or...

Implement cache stampede protection (locking or probabilistic refresh) for any high-traffic cache keys with expensive recomputation.

---

---
title: "Monitor cache hit rates"
impact: MEDIUM
impactDescription: "general best practice"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Monitor cache hit rates

Monitor cache hit rates. A hit rate below 80% suggests the cache is not well-tuned for actual access patterns. Investigate and adjust.

---

---
title: "Never cache sensitive data (credentials, tokens, PII)..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Never cache sensitive data (credentials, tokens, PII)...

Never cache sensitive data (credentials, tokens, PII) without encryption and strict TTLs.

---

---
title: "Prefer cache-aside as the starting pattern"
impact: LOW
impactDescription: "recommended but situational"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Prefer cache-aside as the starting pattern

Prefer cache-aside as the starting pattern. Only move to more complex patterns (write-through, write-behind) when you have measured evidence that they are needed.

---

---
title: "Use consistent hashing for distributed cache clusters to..."
impact: MEDIUM
impactDescription: "general best practice"
tags: caching, dev, backend, caching-strategy-selection, cache-invalidation, cache-aside-pattern
---

## Use consistent hashing for distributed cache clusters to...

Use consistent hashing for distributed cache clusters to minimize key redistribution when nodes are added or removed.
