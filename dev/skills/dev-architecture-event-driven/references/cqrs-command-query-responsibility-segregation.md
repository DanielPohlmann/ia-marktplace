<!-- Part of the dev-architecture-event-driven skill. Loaded on demand from SKILL.md. -->

# CQRS (Command Query Responsibility Segregation)

CQRS separates the model used for updating (commands/writes) from the model used for reading (queries/reads). This allows each side to be optimized independently.

## CQRS Architecture

```
                    ┌──────────────────┐
                    │    Client        │
                    └────┬────────┬────┘
                         │        │
                   Commands    Queries
                         │        │
                    ┌────▼──┐  ┌──▼──────┐
                    │ Write │  │  Read    │
                    │ Model │  │  Model   │
                    │       │  │          │
                    │Command│  │ Query    │
                    │Handler│  │ Handler  │
                    └───┬───┘  └────▲────┘
                        │           │
                   ┌────▼───┐  ┌────┴────┐
                   │ Write  │  │  Read   │
                   │ Store  │──▶│  Store  │
                   │        │  │(Projec- │
                   └────────┘  │ tions)  │
                               └─────────┘
```

## Why Separate Read and Write Models?

| Concern | Write Model | Read Model |
|---------|-------------|------------|
| **Optimization** | Normalized; optimized for consistency | Denormalized; optimized for query performance |
| **Scaling** | Scale for write throughput | Scale for read throughput (often 10-100x more reads) |
| **Schema** | Domain model (aggregates, entities) | Flat, query-specific views (projections) |
| **Validation** | Complex business rules, invariants | No business rules; just serving data |
| **Storage** | Event store, relational DB | Document DB, search index, cache, materialized views |

## When CQRS Is Justified

| Signal | What it looks like |
|--------|--------------------|
| Read-heavy and read-expensive | Reads dominate traffic and each read joins or aggregates much more than a write touches |
| Workload contention | Reports or dashboards slow down command handling through shared locks, connections or I/O |
| Query shape mismatch | The UI needs denormalised, combined or searchable views that the normalised write model serves poorly |

What is **not** CQRS and should be tried first:

- Adding indexes, rewriting queries, caching hot reads, scaling hardware.
- A **read replica** — it offloads the same model to another node; it does not change the model. CQRS starts when the read side has its own schema designed for queries.

Scope it to individual flows. One projection for one painful screen is a valid CQRS adoption; converting every module is rarely worth the extra moving parts.

### Feeding the Read Store

The read store is derived data: it can be dropped and rebuilt at any time. Feed it from a reliable source of changes:

- **Transactional outbox** — the command handler writes the change and an outbox row in one transaction; a relay publishes to the projector (see `dev-integration-patterns-transactional-outbox`).
- **Change data capture** — a connector tails the write database's log and emits row changes.
- **Event store** — with event sourcing, projections subscribe to the event store (typically the all-streams or per-category feed) directly.

When the read store is a separate resource, avoid updating it as a second write inside the command handler; a failure between the two writes leaves the views silently wrong. Read tables in the same database, updated in the same transaction as the write, are atomic and a valid CQRS setup.

## Projections (Read Models)

Projections transform events into query-optimized read models. They subscribe to the event stream and update materialized views.

```
Event Stream:
  OrderPlaced { orderId: 1, customer: "Alice", total: $50 }
  OrderShipped { orderId: 1, trackingNumber: "XYZ123" }

Projection → Order Summary (Read Model):
  { orderId: 1, customer: "Alice", total: $50,
    status: "Shipped", tracking: "XYZ123" }
```

Multiple projections can be built from the same event stream for different query needs:
- **Order summary** -- For the customer dashboard
- **Revenue report** -- For the finance team
- **Shipping manifest** -- For the warehouse

### Projection Rules

- **At-least-once delivery.** Every feed above can redeliver after a crash or restart, so each handler must be idempotent: applying the same event twice leaves the read model unchanged (upsert by key, or skip events at or below the stored version).
- **Keep a checkpoint with the read model.** Store the last processed global position (or, per read-model row, the stream version) in the same database and the same transaction as the view update. A checkpoint kept elsewhere drifts: a crash between the two writes skips or double-applies events.
- **Ordering is per stream, not across streams.** Events of `order-1` arrive in order; there is no guarantee between `order-1` and `customer-7`. A projection joining several streams must tolerate either arriving first (e.g. create a placeholder row, fill in later).
- **Apply event data; do not re-run business rules.** The decision was made and recorded on the write side. A projection that recomputes discounts or eligibility will disagree with the write side as soon as the rules change, and replays will rewrite history.
- **Projections have no side effects.** Emails, payments and outbound messages live in separate subscribers that track what they already sent, so a rebuild can replay everything safely.

### Rebuilding a Projection

1. Deploy the new version as a **new** read model (new table/index) with its own checkpoint at position 0.
2. Let it catch up from the start of the log in parallel with the old one, which keeps serving reads.
3. When its lag is near zero, switch queries to it, then drop the old one.

Rebuilding in place (truncate and replay) leaves the screen empty or wrong for the duration; only do it for small views.
