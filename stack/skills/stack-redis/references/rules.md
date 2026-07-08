# Redis Rules

Best practices and rules for Redis.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Register `ConnectionMultiplexer` as a singleton and reuse... | MEDIUM | [`redis-register-connectionmultiplexer-as-a-singleton-and-reuse.md`](redis-register-connectionmultiplexer-as-a-singleton-and-reuse.md) |
| 2 | Set `AbortOnConnectFail = false` in `ConfigurationOptions`... | MEDIUM | [`redis-set-abortonconnectfail-false-in-configurationoptions.md`](redis-set-abortonconnectfail-false-in-configurationoptions.md) |
| 3 | Use `KeyExpireAsync` on every key that is not meant to live... | HIGH | [`redis-use-keyexpireasync-on-every-key-that-is-not-meant-to-live.md`](redis-use-keyexpireasync-on-every-key-that-is-not-meant-to-live.md) |
| 4 | Use hash operations (`HashSetAsync`, `HashGetAsync`) for... | MEDIUM | [`redis-use-hash-operations-hashsetasync-hashgetasync-for.md`](redis-use-hash-operations-hashsetasync-hashgetasync-for.md) |
| 5 | Release distributed locks using a Lua script that checks... | HIGH | [`redis-release-distributed-locks-using-a-lua-script-that-checks.md`](redis-release-distributed-locks-using-a-lua-script-that-checks.md) |
| 6 | Use `FireAndForget` command flags on non-critical write... | CRITICAL | [`redis-use-fireandforget-command-flags-on-non-critical-write.md`](redis-use-fireandforget-command-flags-on-non-critical-write.md) |
| 7 | Namespace all keys with a prefix (e | HIGH | [`redis-namespace-all-keys-with-a-prefix-e.md`](redis-namespace-all-keys-with-a-prefix-e.md) |
| 8 | Configure `SyncTimeout` and `AsyncTimeout` to values... | HIGH | [`redis-configure-synctimeout-and-asynctimeout-to-values.md`](redis-configure-synctimeout-and-asynctimeout-to-values.md) |
| 9 | Use pipelining by issuing multiple commands before awaiting... | MEDIUM | [`redis-use-pipelining-by-issuing-multiple-commands-before-awaiting.md`](redis-use-pipelining-by-issuing-multiple-commands-before-awaiting.md) |
| 10 | Monitor Redis memory usage and eviction policy... | CRITICAL | [`redis-monitor-redis-memory-usage-and-eviction-policy.md`](redis-monitor-redis-memory-usage-and-eviction-policy.md) |

---

---
title: "Configure `SyncTimeout` and `AsyncTimeout` to values..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Configure `SyncTimeout` and `AsyncTimeout` to values...

Configure `SyncTimeout` and `AsyncTimeout` to values appropriate for your latency requirements (typically 1-5 seconds) and handle `TimeoutException` with retries.

---

---
title: "Handle connection failures"
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data
---

## Handle connection failures

Handle connection failures

---

---
title: "Monitor Redis memory usage and eviction policy..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Monitor Redis memory usage and eviction policy...

Monitor Redis memory usage and eviction policy (`maxmemory-policy`) in production; use `allkeys-lru` for cache workloads and `noeviction` for data that must not be lost.

---

---
title: "Namespace all keys with a prefix (e"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Namespace all keys with a prefix (e

Namespace all keys with a prefix (e.g., `"myapp:session:{id}"`) to avoid collisions when multiple applications share the same Redis instance.

---

---
title: "Register `ConnectionMultiplexer` as a singleton and reuse..."
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Register `ConnectionMultiplexer` as a singleton and reuse...

Register `ConnectionMultiplexer` as a singleton and reuse it across the entire application; creating multiple multiplexers wastes connections and degrades performance.

---

---
title: "Release distributed locks using a Lua script that checks..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Release distributed locks using a Lua script that checks...

Release distributed locks using a Lua script that checks ownership before deleting to prevent accidentally releasing a lock acquired by another process after expiry.

---

---
title: "Set `AbortOnConnectFail = false` in `ConfigurationOptions`..."
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Set `AbortOnConnectFail = false` in `ConfigurationOptions`...

Set `AbortOnConnectFail = false` in `ConfigurationOptions` so the client retries connections gracefully rather than throwing an exception on the first failure.

---

---
title: "Set appropriate expiration"
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data
---

## Set appropriate expiration

Set appropriate expiration

---

---
title: "Use connection multiplexer singleton"
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data
---

## Use connection multiplexer singleton

Use connection multiplexer singleton

---

---
title: "Use `FireAndForget` command flags on non-critical write..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Use `FireAndForget` command flags on non-critical write...

Use `FireAndForget` command flags on non-critical write operations (e.g., analytics counters) to reduce latency by not waiting for the server acknowledgment.

---

---
title: "Use hash operations (`HashSetAsync`, `HashGetAsync`) for..."
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Use hash operations (`HashSetAsync`, `HashGetAsync`) for...

Use hash operations (`HashSetAsync`, `HashGetAsync`) for objects with many fields instead of serializing the entire object as a JSON string, enabling partial field updates.

---

---
title: "Use `KeyExpireAsync` on every key that is not meant to live..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Use `KeyExpireAsync` on every key that is not meant to live...

Use `KeyExpireAsync` on every key that is not meant to live forever to prevent unbounded memory growth in the Redis instance.

---

---
title: "Use pipelines for bulk operations"
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data
---

## Use pipelines for bulk operations

Use pipelines for bulk operations

---

---
title: "Use pipelining by issuing multiple commands before awaiting..."
impact: MEDIUM
impactDescription: "general best practice"
tags: redis, dotnet, data, distributed-caching, session-storage, real-time-pubsub-messaging
---

## Use pipelining by issuing multiple commands before awaiting...

Use pipelining by issuing multiple commands before awaiting any results (`batch = db.CreateBatch()`) to reduce network round trips for bulk operations.
