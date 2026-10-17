---
name: dev-backend-caching
description: Use when choosing a caching strategy for a workload. USE FOR: cache-aside, read/write-through, write-behind, invalidation, stampede prevention, TTL/eviction, CDN and HTTP caching, multi-tier caches. DO NOT USE FOR: Redis commands and locks (use stack-redis), schema design (use dev-backend-data-modeling), API design (use dev-backend-api-design).
---

# Caching Strategies & Patterns

## Overview
Caching is the practice of storing copies of data in a faster storage layer so that future requests for that data are served more quickly. Effective caching can reduce database load by orders of magnitude, cut response latency dramatically, and improve system resilience -- but incorrect caching introduces stale data, consistency bugs, and operational complexity. Choosing the right caching strategy is a critical backend architecture decision.

## Choosing a Caching Strategy

| Criterion | Cache-Aside | Read-Through | Write-Through | Write-Behind | Write-Around |
|-----------|-------------|--------------|---------------|--------------|--------------|
| **Read latency (after warm)** | Low | Low | Low | Low | Low |
| **Write latency** | Normal (DB only) | Normal (DB only) | Higher (cache + DB) | Very low (cache only) | Normal (DB only) |
| **Consistency** | Eventual | Eventual | Strong | Eventual | Eventual |
| **Data loss risk** | None | None | None | Yes (cache failure) | None |
| **Cache pollution** | Low (demand-filled) | Low (demand-filled) | Higher (all writes cached) | Higher (all writes cached) | Lowest |
| **Implementation complexity** | Low | Medium | Medium | High | Low |
| **Best workload** | General purpose | Read-heavy | Read-heavy + consistency | Write-heavy + low latency | Write-heavy + rarely re-read |

**Decision heuristic:**
- Start with **cache-aside** -- it is the simplest and most widely applicable pattern.
- Use **write-through** when you need strong consistency between cache and database.
- Use **write-behind** when write latency is critical and you can tolerate potential data loss.
- Use **write-around** when most writes are not read back immediately.
- Use **read-through** when you want to keep caching logic out of your application code.

## Cache Invalidation Strategies

Cache invalidation is one of the two hard problems in computer science (along with naming things and off-by-one errors).

| Strategy | Mechanism | Trade-off |
|----------|-----------|-----------|
| **TTL (Time-To-Live)** | Cache entries expire after a fixed duration | Simple; data can be stale up to TTL; good baseline |
| **Event-based** | Invalidate cache when a domain event fires (e.g., `order.updated`) | Near-real-time consistency; requires event infrastructure |
| **Version-based** | Cache key includes a version number; bump version on write | No stale reads; requires version tracking |
| **Tag-based** | Associate cache entries with tags; invalidate all entries with a tag | Good for related data; supported by some cache frameworks |

**Recommendation:** Use TTL as a safety net on every cache entry (even with event-based invalidation). This ensures that stale data eventually expires even if an invalidation event is lost.

## HTTP Caching

### ETag and Last-Modified

```
Response:
  ETag: "abc123"
  Last-Modified: Tue, 15 Jan 2024 10:00:00 GMT

Subsequent request:
  If-None-Match: "abc123"
  If-Modified-Since: Tue, 15 Jan 2024 10:00:00 GMT

Server response if unchanged:
  304 Not Modified (no body, saves bandwidth)
```

- **ETag** -- opaque identifier for a specific version of a resource (hash of content or version number).
- **Last-Modified** -- timestamp of last change.
- Both enable conditional requests that save bandwidth when content has not changed.

## Best Practices
- Always set a TTL on every cache entry -- even if you also use event-based invalidation. TTL is your safety net against stale data from missed events.
- Monitor cache hit rates. A hit rate below 80% suggests the cache is not well-tuned for actual access patterns. Investigate and adjust.
- Design for cache failure gracefully: the system must function (possibly with degraded performance) when the cache is unavailable.
- Never cache sensitive data (credentials, tokens, PII) without encryption and strict TTLs.
- Use consistent hashing for distributed cache clusters to minimize key redistribution when nodes are added or removed.
- Prefer cache-aside as the starting pattern. Only move to more complex patterns (write-through, write-behind) when you have measured evidence that they are needed.
- Implement cache stampede protection (locking or probabilistic refresh) for any high-traffic cache keys with expensive recomputation.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/core-caching-patterns.md](references/core-caching-patterns.md) | Core Caching Patterns — Cache-Aside (Lazy Loading), Read-Through, Write-Through, Write-Behind (Write-Back), Write-Around |
| [references/details.md](references/details.md) | Cache Stampede / Thundering Herd; CDN Caching; Application Caching; Multi-Tier Caching |

## References

- [MDN Web Docs — HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
- [Cache (Computing) — Wikipedia](https://en.wikipedia.org/wiki/Cache_(computing))

See references/rules.md for the full rule catalog.
