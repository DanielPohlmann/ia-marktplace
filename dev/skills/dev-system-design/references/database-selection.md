# Database Selection

Pick a datastore by its access patterns and its consistency/latency behaviour, not by the "SQL vs NoSQL" label. Many products end up with a relational system of record plus one or two specialised stores (search index, cache, object storage).

## Start from access patterns
Answer these before naming a product:
1. What are the main queries? Point lookups by key, range scans, joins, full-text, aggregations, time windows?
2. Read/write ratio and peak QPS for each (see `estimation.md`).
3. Which operations need transactions across multiple records?
4. Which operations need strong consistency and which tolerate staleness?
5. How large will the data get and how fast does it grow?
6. Is the schema stable or evolving per record?

## CAP, stated correctly
CAP concerns a distributed system **during a network partition**. When nodes cannot talk to each other, the system must either:
- refuse or delay some requests to stay consistent (**CP behaviour**), or
- keep answering from whatever node is reachable, accepting divergent data (**AP behaviour**).

Partitions are not optional in a distributed system, so "CA" is not a meaningful choice for one; it only describes a single node, which is not partition-tolerant because it is not distributed. Do not label databases as "CA". Many products are configurable and behave differently per operation.

## PACELC adds the normal case
PACELC: if there is a **P**artition, choose **A** or **C**; **E**lse, choose **L**atency or **C**onsistency. The "else" half matters more day to day: even with a healthy network, waiting for replicas to confirm a write costs latency.

| Behaviour | Partition | Normal operation | Typical example |
|---|---|---|---|
| PC/EC | Consistency | Consistency | Single-leader relational with synchronous replicas, consensus-based stores |
| PA/EL | Availability | Latency | Leaderless/Dynamo-style stores with default (low) quorum settings |
| PA/EC | Availability | Consistency | Some document stores depending on configuration |
| PC/EL | Consistency | Latency | Rare; systems that serve fast local reads normally but block writes during a partition |

## Tunable consistency (quorums)
With N replicas, a write waits for W acknowledgements and a read queries R replicas.
- **R + W > N**: every read set overlaps the latest write set, so reads see the latest acknowledged write (absent concurrent-write edge cases).
- N=3, W=2, R=2: balanced, tolerates one node down for both reads and writes.
- N=3, W=1, R=1: fastest, may read stale data.
- N=3, W=3, R=1: fast reads, but any node down blocks writes.
Choose per operation: e.g. strong reads for account balance, fast reads for profile views.

## Store families

| Family | Good fit | Poor fit |
|---|---|---|
| Relational | Transactions, joins, constraints, evolving queries over well-structured data; most systems of record | Massive write throughput beyond one primary without sharding; highly variable schemas |
| Document | Aggregates read and written as a whole; per-record schema variation | Many-to-many relationships and cross-document transactions as the main workload |
| Wide-column | Very high write throughput, known query patterns, time-ordered data per partition key | Ad-hoc queries, joins, frequently changing access patterns |
| Key-value | Sessions, caches, counters, feature flags, rate-limit buckets | Queries by anything other than the key |
| Search index | Full-text search, faceting, relevance ranking, log exploration | System of record; strong consistency; frequent updates to the same document |
| Object storage | Files, media, backups, data lake; huge and cheap | Low-latency small random updates, transactional queries |
| Time-series | Metrics, sensor data, append-mostly by time, retention and downsampling | General entity data, frequent updates to old points |
| Graph | Multi-hop relationship traversal (recommendations, fraud rings) | Bulk aggregations, simple CRUD |

## Decision heuristics
- Default to a relational database for the system of record until a requirement rules it out with numbers.
- Add a search index for text search rather than forcing `LIKE '%term%'` on the primary; keep the primary as source of truth and feed the index asynchronously.
- Put blobs in object storage and keep only metadata and the object key in the database.
- Pick wide-column or time-series when sustained write rates and data growth are the dominant constraint and queries are known up front.
- Every additional store needs a synchronisation story (CDC, outbox, dual-write avoidance) and an owner on call.
