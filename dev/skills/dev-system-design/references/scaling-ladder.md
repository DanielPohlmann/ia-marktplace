# The Scaling Ladder

Scale by climbing one rung at a time. Each rung adds cost and operational complexity, so each one needs a metric that says the previous rung is exhausted.

## Rungs and the signal to climb

| # | Step | What it buys | Signal to climb | New costs |
|---|---|---|---|---|
| 1 | Vertical scaling | More CPU/RAM/IOPS with zero code change | Sustained saturation on one host | Hardware ceiling, single point of failure |
| 2 | Separate app and DB | Independent sizing and tuning | App and DB contend for CPU/memory/disk | One more network hop |
| 3 | Stateless app + load balancer | Horizontal app capacity, rolling deploys, redundancy | One app node cannot carry peak; need zero-downtime deploys | Session state must leave the process |
| 4 | Read replicas | Read throughput; a standby for failover | Primary saturated by reads, or availability target needs a warm standby | Replication lag, failover procedures |
| 5 | Cache-aside | Very fast reads of hot data | Same data read repeatedly; DB load dominated by a few queries | Invalidation, stampedes, staleness |
| 6 | Queues and async work | Short request path, load levelling of bursts | Slow work in the request (email, image processing), or write bursts above DB capacity | Eventual completion, retries, idempotency, dead letters |
| 7 | Partitioning / sharding | Write throughput and dataset beyond one primary | Write volume or data size outgrows the biggest practical primary after tuning | Cross-shard queries, rebalancing, operational load |
| 8 | Multi-region | Survive a region loss; lower latency for distant users | Availability target requires it, or users are global with tight latency targets | Data replication across regions, conflict handling, cost |

## Notes per rung

### Vertical first
Modern hardware is large. A single well-tuned database server with plenty of RAM covers far more products than people expect. Vertical scaling is often the cheapest step in engineering time.

### Stateless application tier
Move sessions, uploads in progress and per-user caches to shared stores (key-value store, object storage). Once any app node can serve any request, scaling the tier is just adding nodes behind the load balancer.

### Read replicas and replication lag
- **Asynchronous replication**: the primary commits without waiting. Writes stay fast, but replicas can serve stale data, and a failover can lose the last few transactions.
- **Synchronous replication**: the primary waits for at least one replica. No data loss on failover, but write latency rises and an unavailable replica can block writes.
- **Read-your-writes**: after a user writes, route that user's reads to the primary for a short window, or carry a version/timestamp and wait until the replica has caught up.
- Replicas are not only about throughput. A synchronous or semi-synchronous standby is justified by availability and durability even when the primary is not busy.

### Cache before shard
A cache with a high hit rate on hot keys often removes the need for more database capacity. See the caching skill for patterns and invalidation.

### Queues
Queues decouple the rate at which work arrives from the rate at which it is processed. They turn a spike into a backlog, which is fine when the work is asynchronous and users accept delayed completion. Consumers must be idempotent because messages can be delivered more than once.

### Partitioning
Exhaust indexing, query tuning, caching, replicas and archiving first. Sharding is the most expensive rung to climb back down from. See `sharding.md`.

### Multi-region
Decide active-passive (simpler, failover takes time) versus active-active (lower latency, but concurrent writes to the same data in two regions need conflict resolution or a single home region per record).

## Quick decision table

| Symptom | Likely next rung |
|---|---|
| Primary CPU high, mostly SELECTs | Cache-aside, then replicas |
| Primary CPU high, mostly writes | Batch/queue writes, tune indexes, then partition |
| p99 latency dominated by a slow side task | Queue it |
| App nodes saturated, DB fine | More stateless app nodes |
| Disk growing without bound | Retention, archiving, time partitioning before sharding |
| One region outage takes everything down | Multi-AZ first, multi-region if the target demands it |
