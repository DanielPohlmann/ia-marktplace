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
