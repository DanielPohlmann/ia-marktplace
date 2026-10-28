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
- **Event store** — with event sourcing, projections subscribe to the stream directly.

Avoid updating the read store as a second write inside the command handler; a failure between the two writes leaves the views silently wrong.

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
