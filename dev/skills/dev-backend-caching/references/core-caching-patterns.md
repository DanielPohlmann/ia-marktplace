<!-- Part of the dev-backend-caching skill. Loaded on demand from SKILL.md. -->

# Core Caching Patterns

## Cache-Aside (Lazy Loading)

The application manages the cache explicitly. On a read, the application checks the cache first. On a miss, it loads from the database, stores the result in cache, and returns it.

```
Read path:
  1. App checks cache for key
  2. Cache HIT → return cached value
  3. Cache MISS → query database
  4. Store result in cache with TTL
  5. Return result

Write path:
  1. App writes to database
  2. App invalidates (deletes) the cache key
```

**Pros:** Simple to implement; cache only contains data that is actually requested; works with any database.
**Cons:** First request always hits the database (cold start); potential for stale data between write and invalidation.

**Ordering matters.** Delete the key *after* the database transaction commits. Deleting first (or inside the transaction) opens a window where a reader misses, loads the still-old row and caches it with a full TTL.

**The read/invalidate race remains even after commit:**

```
Reader A: cache miss → reads row v1 from DB ......... (slow) ... writes v1 to cache
Writer B:                 updates row to v2 → commit → deletes key
Result: cache holds v1 until TTL expires
```

Mitigations, cheapest first: a short TTL so the stale window is bounded; versioned keys (`product:42:v7`) where the writer bumps the version so stale entries are simply never read; a second delayed delete shortly after the first; or conditional set (only write to the cache if the stored version is not newer).

**Best for:** General-purpose caching where the application can tolerate brief staleness.

## Read-Through

The cache sits in front of the database and loads data transparently on a miss. The application always reads from the cache -- it never talks to the database directly for reads.

```
Read path:
  1. App reads from cache
  2. Cache HIT → return cached value
  3. Cache MISS → cache loads from database automatically
  4. Cache stores result, returns to app
```

**Pros:** Cleaner application code (no cache miss handling); cache warms itself.
**Cons:** Requires a cache layer that supports read-through (or a wrapper); first request still slow.

**Best for:** Workloads where you want the caching logic decoupled from application code.

## Write-Through

Writes go to the cache first, and the cache synchronously writes to the database before confirming the write to the application.

```
Write path:
  1. App writes to cache
  2. Cache writes to database synchronously
  3. Cache confirms write to app
```

**Pros:** Read-after-write on the happy path — a value just written is served from cache on the next read.
**Cons:** Higher write latency (two writes in series); cache may contain data that is never read. It is still two writes to two systems: unless a single provider performs both atomically, a crash or timeout between them, or two concurrent writers interleaving, leaves cache and database disagreeing. There is no atomicity — keep a TTL and treat the database as the source of truth.

**Best for:** Read-heavy workloads where recently written data is read back immediately and write volume is moderate.

## Write-Behind (Write-Back)

Writes go to the cache immediately, and the cache asynchronously flushes changes to the database in the background.

```
Write path:
  1. App writes to cache
  2. Cache confirms write to app immediately
  3. Cache asynchronously flushes to database (batched, periodic)
```

**Pros:** Very low write latency; writes can be batched for efficiency; absorbs write spikes.
**Cons:** Risk of data loss if the cache fails before flushing; eventual consistency with the database; complex to implement correctly.

**Best for:** Write-heavy workloads where write latency matters more than durability guarantees (e.g., analytics counters, session updates).

## Write-Around

Writes go directly to the database, bypassing the cache entirely. The cache is populated only on subsequent reads (via cache-aside or read-through).

```
Write path:
  1. App writes directly to database (cache not involved)

Read path:
  1. App reads from cache
  2. Cache MISS → load from database, populate cache
```

**Pros:** Avoids polluting the cache with data that may never be read; simple write path.
**Cons:** Recently written data always misses the cache on first read.

**Best for:** Write-heavy workloads where most written data is rarely read immediately (e.g., log ingestion, audit trails).
