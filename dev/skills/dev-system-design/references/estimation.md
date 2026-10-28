# Back-of-the-Envelope Estimation

Estimation exists to make a decision, not to produce a precise number. Round aggressively, keep one significant figure, and stop as soon as the answer changes nothing.

## Useful constants

| Quantity | Approximation |
|---|---|
| Seconds per day | 86,400 ≈ 10^5 (use 100k for mental math; it underestimates QPS by ~15%) |
| Seconds per month | ~2.6 million |
| Seconds per year | ~31.5 million |
| 1 million requests/day | ≈ 12 requests/s average |
| 1 billion requests/day | ≈ 12k requests/s average |
| Byte sizes | KB 10^3, MB 10^6, GB 10^9, TB 10^12, PB 10^15 |

Rough single-node capacities (order of magnitude only; measure your own stack):

| Component | Comfortable range |
|---|---|
| Relational DB on decent hardware, simple indexed writes | low thousands of writes/s |
| Relational DB, indexed point reads | ~10k reads/s, more with good caching |
| In-memory key-value store | ~100k ops/s per node |
| Stateless app server | hundreds to a few thousand requests/s, depending on the work |
| One connection server holding idle WebSockets | tens of thousands to a few hundred thousand connections |

## Formulas

**Average QPS** = daily operations ÷ 86,400

**Peak QPS** = average QPS × peak factor. Typical factors: 2–3× for steady consumer traffic, 10× or more for events (launches, sales, match kick-off, end-of-month batch). If the business has a known spike, estimate the spike directly ("200k users will hit Buy within the first minute").

**Read/write split**: estimate writes and reads separately; reads often dominate by 10:1 to 100:1. The two numbers drive different solutions (replicas and caches for reads, partitioning and queues for writes).

**Storage** = items per day × item size × retention days × replication factor. Add indexes (often 20–50% on top) and growth.

**Bandwidth** = QPS × payload size. Compute both ingress and egress; egress for media is what usually costs money and motivates a CDN.

**Key-space size** = base^length. Base62 with 7 characters gives 62^7 ≈ 3.5 × 10^12 values. Collisions on random keys start to appear around the square root of the key space and reach ~50% at about 1.18·√S (birthday bound): ~2.2 × 10^6 keys for 62^7 if you never check for collisions. So either check-and-retry on insert or use a counter-derived key.

## Worked mini-examples

### A. Event ticketing writes
- 1 million tickets sold per day across all events.
- Average: 1,000,000 ÷ 86,400 ≈ 12 writes/s.
- Normal peak factor 3× → ~35 writes/s.
- **Decision:** one relational primary handles this easily. The real problem is not volume but contention on the same seats during a hot on-sale — that is a concurrency problem, not a database-size problem.

### B. Hot on-sale spike
- 500k users arrive in the first 5 minutes for a single popular event.
- 500,000 ÷ 300 s ≈ 1,700 arrivals/s, each doing several page loads and polls → ~10k+ requests/s.
- **Decision:** the reads must be served from cache/CDN; the purchase path needs a waiting room that admits users at a rate the inventory service can take.

### C. URL shortener
- 100M new links/month → 100,000,000 ÷ 2.6M s ≈ 40 writes/s.
- Reads at 100:1 → ~4k reads/s average, maybe 20k at peak.
- Storage: 100M × 12 months × 5 years × ~500 bytes ≈ 3 TB before replication.
- **Decision:** writes fit one primary; reads are served by a cache plus replicas; 3 TB is large-ish for one node but well within a single managed database. Sharding is not needed on day one.

### D. Metrics ingestion
- 50,000 devices emitting one sample every 10 s → 5,000 writes/s sustained, no idle periods.
- 100 bytes/sample → 0.5 MB/s → ~43 GB/day → ~16 TB/year.
- **Decision:** sustained writes plus unbounded growth point to a time-series or wide-column store, time-based partitions, and retention/downsampling policies.

### E. Chat fan-out
- 10M daily active users, 50 messages each → 500M messages/day ≈ 6k messages/s average, maybe 30k peak.
- Average group size 20 → up to 600k deliveries/s at peak.
- **Decision:** the bottleneck is fan-out to connection servers, not storage writes; use pub/sub behind the connection tier.

## Pitfalls
- Spending ten minutes on precision that changes nothing.
- Forgetting the peak, or forgetting that the peak may be concentrated on a single key.
- Quoting storage without retention and replication.
- Confusing "users" with "requests": each active user produces many requests.
