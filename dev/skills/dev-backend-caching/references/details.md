<!-- Part of the dev-backend-caching skill. Loaded on demand from SKILL.md. -->

# Caching Strategies & Patterns — details

## Cache Stampede / Thundering Herd

When a popular cache key expires, many concurrent requests simultaneously miss the cache and hit the database, potentially overwhelming it.

### Solutions

| Solution | How It Works |
|----------|--------------|
| **Mutex / distributed lock** | First request that misses acquires a lock and rebuilds the cache; other requests wait or get stale data |
| **Probabilistic early expiration** | Each request has a small probability of refreshing the cache before TTL expires, spreading the refresh load |
| **Stale-while-revalidate** | Serve the stale value while asynchronously refreshing in the background |
| **Pre-warming** | Proactively refresh cache entries before they expire (scheduled or event-triggered) |
| **Request coalescing (single-flight)** | Concurrent misses for the same key in one process share a single in-flight load instead of each querying the source |
| **TTL jitter** | Add a random offset to each TTL (e.g. ±10%) so keys written together do not expire together |

```python
# Probabilistic early expiration (XFetch algorithm)
import random, time

def get_with_early_expiration(cache, key, ttl, beta=1.0):
    entry = cache.get(key)
    if entry is None:
        return recompute_and_cache(cache, key, ttl)

    value, expiry, delta = entry
    # delta = time it took to recompute last time
    # Probabilistically refresh before actual expiry
    if time.time() - delta * beta * random.random() >= expiry:
        return recompute_and_cache(cache, key, ttl)

    return value
```

## CDN Caching

Content Delivery Networks cache responses at edge locations close to users.

### Cache-Control Headers

```http
Cache-Control: public, max-age=3600, s-maxage=86400, stale-while-revalidate=60
```

| Directive | Meaning |
|-----------|---------|
| `public` | Any cache (CDN, proxy, browser) may store the response |
| `private` | Only the browser may cache (not CDN/proxies) |
| `max-age=N` | Browser cache TTL in seconds |
| `s-maxage=N` | CDN/proxy cache TTL (overrides max-age for shared caches) |
| `no-cache` | Must revalidate with origin before using cached copy |
| `no-store` | Do not cache at all (sensitive data) |
| `stale-while-revalidate=N` | Serve stale for N seconds while revalidating in background |
| `stale-if-error=N` | Serve stale for N seconds if origin returns an error |
| `immutable` | Content will never change (versioned assets) |

### Edge Caching Strategy
- Cache static assets with long TTLs and content-hash filenames (`app.a1b2c3.js` with `immutable`).
- Cache API responses at the CDN with `s-maxage` and `stale-while-revalidate`.
- Use cache tags or surrogate keys for targeted invalidation (supported by Fastly, CloudFront, Cloudflare).

## Application Caching

### Redis vs. Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data structures** | Strings, hashes, lists, sets, sorted sets, streams | Strings only |
| **Persistence** | RDB snapshots, AOF log | None |
| **Replication** | Built-in primary/replica | None (client-side sharding) |
| **Pub/Sub** | Yes | No |
| **Lua scripting** | Yes | No |
| **Max value size** | 512 MB | 1 MB |
| **Multi-threading** | Single-threaded (I/O threads in 6.0+) | Multi-threaded |

**Recommendation:** Use Redis unless you need only simple string caching and prefer Memcached's multi-threaded model for pure throughput at scale.

### In-Memory / Local Cache
- Fastest possible access (no network hop).
- Limited by process memory; not shared across instances.
- Use for extremely hot data with short TTLs (e.g., config, feature flags, rate limit counters).
- On a multi-instance deployment each node has its own copy, so instances diverge after a write until their entries expire. Keep TTLs short, put shared mutable data in a distributed cache, or publish invalidation messages that every instance subscribes to.
- Examples: Caffeine (Java), MemoryCache (.NET), node-cache (Node.js), lru-cache (Python).

## Multi-Tier Caching

```
┌─────────────┐    ┌─────────────────┐    ┌──────────┐    ┌──────────┐
│   Client     │───>│  CDN (L3)       │───>│ Redis    │───>│ Database │
│   Browser    │    │  Edge cache     │    │ (L2)     │    │          │
│   cache (L0) │    │                 │    │ Distrib. │    │          │
└─────────────┘    └─────────────────┘    │ cache    │    │          │
                                          └──────────┘    └──────────┘
                                               ▲
                                          ┌──────────┐
                                          │ In-proc  │
                                          │ cache(L1)│
                                          └──────────┘
```

| Tier | Location | Latency | Shared | Capacity |
|------|----------|---------|--------|----------|
| **L0 — Browser** | Client device | ~0 ms | No | Small |
| **L1 — In-process** | Application memory | ~0.01 ms | No (per-instance) | Small-Medium |
| **L2 — Distributed** | Redis / Memcached | ~1 ms | Yes (all instances) | Large |
| **L3 — CDN** | Edge PoP | ~10-50 ms | Yes (per-region) | Very large |
| **Origin** | Database | ~5-50 ms | Yes | Unlimited |

**Strategy:** Check L1 first, then L2, then L3, then origin. Write-through from origin to L2; let L1 fill on demand with short TTLs. CDN serves public, cacheable content.
