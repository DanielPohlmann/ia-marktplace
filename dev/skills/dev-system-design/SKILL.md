---
name: dev-system-design
description: Use when designing or reviewing a system facing high volume, traffic spikes, live updates or data growth, or for design-interview practice. USE FOR: requirements, estimation, scaling ladder, load balancing, database choice, sharding, WebSockets/SSE, contention, large uploads, ID generation. DO NOT USE FOR: style selection (use dev-architecture), service decomposition (use dev-architecture-microservices), cache patterns (use dev-backend-caching), schema design (use dev-backend-data-modeling).
---

# System Design

## Overview
System design is the work of turning a set of use cases and load expectations into components, data flows and trade-offs that will survive production. This skill gives a repeatable procedure for designing a new system or reviewing an existing one when the hard parts are volume, bursts, live updates or growing data. The same procedure works as a structure for design-interview practice.

The procedure is deliberately incremental: a naive design that works comes first, and every piece of extra machinery must be justified by a specific problem with a number attached.

## The Procedure

### 1. Functional requirements
List the 3–5 use cases that define the product ("user uploads a file", "viewer sees the live score", "buyer reserves a seat"). Name what is explicitly out of scope. More than five usually means the scope is not yet understood.

### 2. Non-functional requirements — with numbers
Each one needs a value, otherwise it cannot drive a decision:
- **Availability** target (99.9% ≈ 8.8 h/year of downtime; 99.99% ≈ 53 min/year).
- **Latency** target, stated as a percentile (p99 < 200 ms for reads).
- **Consistency per operation** — "reserving a seat must never double-book" is strong; "the like counter may lag a few seconds" is eventual. Decide per operation, not per system.
- **Load**: average and peak, read/write ratio, expected growth.
- **Durability**: what may never be lost, and for how long it is retained.

### 3. Back-of-the-envelope estimation
Estimate only as far as needed to make a decision: QPS (average and peak), storage over the retention window, bandwidth. Stop once the numbers tell you whether one machine, a replica set, or a partitioned cluster is needed. See `references/estimation.md`.

### 4. Core entities
Name the nouns the system stores and moves (User, Event, Ticket, Reservation, File). Note which ones are hot, which grow without bound, and which need strong consistency.

### 5. API
Define the endpoints or messages for each functional requirement: method, path, key parameters, response. Push identity into auth context, not into request bodies. For live updates, name the channel (SSE stream, WebSocket topic).

### 6. High-level design, built incrementally
1. Draw the simplest design that satisfies every functional requirement: client → service → database.
2. Walk each non-functional requirement against it and write down where it breaks ("one DB at 5k reads/s peak", "users must refresh to see updates", "two buyers can grab the same seat").
3. That list of problems is the agenda for the deep dives.

### 7. Deep dives, one bottleneck at a time
For each problem: state it, give two or three options, pick one, and say explicitly what is being given up (latency, consistency, cost, operational complexity). Never solve two bottlenecks with one unexplained component.

### 8. Review
Ask: what fails first as load doubles? What happens when each dependency is down? What is the next scaling step and what metric triggers it? Record the decisions (an ADR per significant trade-off).

## Key Rules
- **Make the naive version work before scaling it.** A correct simple design is a better starting point than a complex one with gaps in the core flow.
- **Every component answers a named problem.** If you cannot say which requirement a cache, queue or shard exists for, remove it.
- **Numbers drive decisions.** ~35 writes/s fits comfortably in a single relational database; it does not justify a distributed store. 50k writes/s sustained is a different conversation.
- **Trade-offs are per operation.** Payments and inventory want strong consistency; feeds, counters and search can be eventually consistent in the same system.
- **Prefer boring technology** until a measured limit forces otherwise. Each new datastore is a new failure mode and an on-call burden.
- **Design for the peak, pay for the average.** Use autoscaling, queues and load shedding so the peak does not set the permanent bill.

## Scaling Ladder (summary)
Climb one rung only when a metric shows the current rung is exhausted:

| Rung | Move | Climb when |
|---|---|---|
| 1 | Bigger machine (vertical) | CPU/RAM saturated, still affordable |
| 2 | Separate app and database hosts | App and DB compete for resources |
| 3 | Stateless app + load balancer | One app node cannot serve peak, or you need redundancy |
| 4 | Read replicas | Reads dominate and the primary is saturated, or a hot standby is needed for availability |
| 5 | Cache-aside | Repeated reads of the same hot data |
| 6 | Queues for async work | Slow work in the request path, or bursty writes to level |
| 7 | Partitioning / sharding | Write volume or dataset exceeds one primary |
| 8 | Multi-region | Regional outage tolerance or global latency targets |

Details and criteria: `references/scaling-ladder.md`.

## Decision Cheat-Sheet

| Situation | Usual answer | Reference |
|---|---|---|
| Is this load "big"? | Divide daily volume by ~86,400, apply a peak factor | `estimation.md` |
| HTTP routing, path-based rules | L7 load balancer | `load-balancing.md` |
| Requests with very uneven duration | Least-connections balancing | `load-balancing.md` |
| Choosing a datastore | Start from access patterns and PACELC, not "SQL vs NoSQL" | `database-selection.md` |
| Single primary can no longer take the writes | Shard by a high-cardinality key with query affinity | `sharding.md` |
| Data is mostly appended by time | Time-based partitioning inside one database first | `sharding.md` |
| Server pushes updates only | Server-Sent Events | `real-time.md` |
| Bidirectional, low latency | WebSockets + pub/sub fan-out | `real-time.md` |
| Many users compete for scarce items | Short TTL hold + DB constraint as final arbiter | `contention-and-spikes.md` |
| Sudden spike (launch, sale) | Waiting room / queue + rate limiting | `contention-and-spikes.md` |
| Client retries can duplicate writes | Idempotency keys | `contention-and-spikes.md` |
| Large uploads/downloads | Object storage, pre-signed URLs, multipart, CDN | `large-files-and-ids.md` |
| Unique IDs across nodes | Time-ordered IDs (Snowflake-style, UUIDv7) | `large-files-and-ids.md` |

## Common Pitfalls
- Jumping to microservices, Kafka and sharding before computing the load.
- Stating "highly available and strongly consistent" for the whole system without saying which operation needs which.
- Adding a cache without an invalidation story or a TTL.
- Sticky sessions hiding state that should live in a shared store.
- Ignoring the hot key: even a perfectly sharded system melts when one key gets most of the traffic.
- Treating the happy path as the design; never asking what happens on retry, timeout or partial failure.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/estimation.md](references/estimation.md) | QPS from daily volume, peak factor, read/write ratio, storage, bandwidth, key-space sizing, worked examples ending in decisions |
| [references/scaling-ladder.md](references/scaling-ladder.md) | Each scaling rung, the signal to climb it, replication lag and sync vs async replicas |
| [references/load-balancing.md](references/load-balancing.md) | L4 vs L7, balancing algorithms, consistent hashing, sticky sessions, health checks |
| [references/database-selection.md](references/database-selection.md) | CAP and PACELC done correctly, tunable consistency and quorums, store families with fits and anti-fits |
| [references/sharding.md](references/sharding.md) | When to shard, shard key criteria, hash vs range, resharding, hot keys, cross-shard queries and sagas, time partitioning |
| [references/real-time.md](references/real-time.md) | Short/long polling, SSE, WebSockets, pub/sub fan-out, common streaming pitfalls |
| [references/contention-and-spikes.md](references/contention-and-spikes.md) | Inventory holds with TTL, optimistic vs pessimistic concurrency, idempotency keys, waiting rooms, rate limiting |
| [references/large-files-and-ids.md](references/large-files-and-ids.md) | Pre-signed URLs, multipart/resumable uploads, CDN delivery, ID generation strategies, base62, collision math, 301 vs 302 |

## References

- [Martin Kleppmann — Designing Data-Intensive Applications](https://dataintensive.net/)
- [The System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [AWS Well-Architected — Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
