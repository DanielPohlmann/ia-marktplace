# Sharding (Horizontal Partitioning)

Sharding splits one logical dataset across multiple independent databases. It raises write capacity and storage limits, and it permanently complicates queries, transactions and operations. Treat it as a late step.

## Exhaust these first
1. Missing or wrong indexes, N+1 queries, oversized result sets.
2. Query and schema tuning; denormalising a hot read path.
3. Caching hot reads.
4. Read replicas for read-heavy load.
5. Archiving or deleting cold data; time-based partitioning inside the same database.
6. A bigger primary.

If writes or dataset size still exceed one primary after this, shard.

## Choosing a shard key

| Criterion | Why it matters |
|---|---|
| High cardinality | Few distinct values cannot be spread across many shards |
| Even distribution of data and traffic | Avoids one shard doing most of the work |
| Query affinity | The most frequent queries should hit a single shard (e.g. all of a tenant's or user's data together) |
| Stability | Changing a record's key means moving it between shards |

Common choices: tenant ID for multi-tenant SaaS, user ID for user-centric apps, a composite (entity + time bucket) for high-volume streams.

## Hash vs range

| Strategy | Pros | Cons |
|---|---|---|
| Hash of key | Even spread, no hotspots from sequential keys | Range queries hit every shard |
| Range of key | Efficient range scans, easy to reason about | Monotonic keys (timestamps, auto-increment IDs) send all new writes to the last shard |
| Directory / lookup table | Full control, can move individual tenants | Lookup service becomes a critical dependency |

## Resharding with consistent hashing
With `hash(key) mod N`, changing N moves almost every key. Consistent hashing places shards and keys on a ring so adding a node moves only about 1/N of keys. Virtual nodes (many points per physical shard) smooth out the distribution. Alternatively, pre-split into many logical partitions (say 1,024) and map them to fewer physical nodes; rebalancing then moves whole logical partitions.

## Hot keys (the celebrity problem)
Even distribution of keys does not mean even distribution of traffic. One celebrity account, one viral item or one huge tenant can overload a single shard.
- Cache the hot key aggressively (and in multiple replicas).
- Split the key: append a suffix (`item#0..item#9`) for writes and aggregate on read, e.g. for counters.
- Give very large tenants dedicated shards.
- Detect hot keys with per-key metrics rather than discovering them during an incident.

## Cross-shard queries and transactions
- **Scatter-gather** queries hit all shards and merge; latency is the slowest shard. Avoid them on hot paths; maintain a secondary index or a denormalised read model instead.
- **Distributed transactions** (two-phase commit) are slow and fragile. Prefer designing so a transaction stays within one shard; when a workflow spans shards, use a **saga**: a sequence of local transactions with compensating actions on failure.
- **Global uniqueness** (e.g. unique email) needs a dedicated lookup table or a global unique-ID scheme.

## Reference / global tables
Small, rarely changing tables (countries, plans, configuration) are replicated to every shard so joins stay local. Updates must be propagated to all shards.

## Time-based partitioning as a lighter alternative
Most relational databases support native partitioning by range (e.g. month) inside one instance. It gives:
- Fast deletion of old data by dropping partitions.
- Partition pruning for time-bounded queries.
- Smaller indexes per partition.
It does not add write capacity beyond one machine, but for append-mostly data with retention rules it often postpones sharding indefinitely.

## Checklist before sharding
- [ ] Numbers show one primary cannot hold the write load or data, after tuning.
- [ ] Shard key supports the top queries on a single shard.
- [ ] Hot-key plan exists.
- [ ] Rebalancing plan exists (logical partitions or consistent hashing).
- [ ] Cross-shard workflows are designed as sagas or avoided.
- [ ] Backups, migrations and monitoring work per shard.
