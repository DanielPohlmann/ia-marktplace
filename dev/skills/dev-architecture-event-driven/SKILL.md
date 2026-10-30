---
name: dev-architecture-event-driven
description: Use when designing event-driven systems, event sourcing, or CQRS. USE FOR: domain vs integration events, projections, eventual consistency, compensating transactions, choreography vs orchestration, sagas. DO NOT USE FOR: channel topology (use dev-integration-patterns-messaging-channels), routing rules (use dev-integration-patterns-message-routing), reliable DB + publish (use dev-integration-patterns-transactional-outbox), MassTransit wiring (use stack-masstransit).
---

# Event-Driven Architecture, Event Sourcing & CQRS

## Overview
This skill covers three complementary but independent patterns that are frequently used together:

1. **Event-Driven Architecture (EDA)** -- A system design where components communicate through events rather than direct calls.
2. **Event Sourcing** -- A persistence pattern where state is stored as a sequence of events rather than as current state.
3. **CQRS (Command Query Responsibility Segregation)** -- A pattern that separates read and write models.

These patterns can be used independently or combined. Understanding when to use each -- and when to combine them -- is critical.

## Canonical Works

| Book | Author(s) | Relevant Coverage |
|------|-----------|-------------------|
| *Designing Data-Intensive Applications* | Martin Kleppmann | Event sourcing, stream processing, change data capture |
| *Implementing Domain-Driven Design* | Vaughn Vernon | Domain events, event sourcing with DDD, CQRS |
| *Building Event-Driven Microservices* | Adam Bellemare | EDA at scale, event mesh, stream processing |
| *Enterprise Integration Patterns* | Hohpe & Woolf | Messaging foundations (see `dev-integration-patterns`) |

## Relationship Between the Three Patterns

```
┌─────────────────────────────────────────────────────────┐
│                                                           │
│  Event-Driven Architecture (EDA)                          │
│  Components communicate through events                    │
│                                                           │
│    ┌──────────────────┐    ┌──────────────────┐          │
│    │  Event Sourcing   │    │      CQRS        │          │
│    │  Store state as   │    │  Separate read    │          │
│    │  event log        │    │  and write models │          │
│    └────────┬─────────┘    └────────┬─────────┘          │
│             │                       │                     │
│             └───────────┬───────────┘                     │
│                         │                                 │
│              Can be combined but                           │
│              are independent patterns                     │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

- **EDA without Event Sourcing:** Services publish events but store current state in a traditional database.
- **Event Sourcing without CQRS:** Store state as events and rebuild current state from the event log -- but use the same model for reads and writes.
- **CQRS without Event Sourcing:** Separate read and write models backed by a traditional database.
- **All three combined:** The most powerful but most complex combination.

## Compensating Transactions

In eventually consistent systems, you cannot roll back distributed changes with a traditional transaction. Instead, use **compensating transactions** -- actions that semantically undo the effect of a previous action.

```
Forward:   OrderPlaced → PaymentCharged → InventoryReserved → ShipmentCreated
Compensate: OrderCancelled ← PaymentRefunded ← InventoryReleased ← ShipmentCancelled
```

Compensating transactions are used in the saga pattern (see `dev-architecture-microservices` for choreography vs. orchestration).

## When to Use Each Pattern

| Pattern | Use When | Avoid When |
|---------|----------|------------|
| **EDA** | Multiple consumers need to react to changes; temporal decoupling needed; high scalability | Simple CRUD apps; strong consistency required; small systems with few components |
| **Event Sourcing** | The domain *is* a sequence of facts (ledgers, bookings, claims); past states must be reconstructed and explained | Only an audit trail or history is needed — an append-only history or temporal table is far cheaper; join cost alone; simple CRUD |
| **CQRS** | Concrete signals are present (see *Adopting CQRS* below) | Reads and writes are symmetric; indexes, query tuning and hardware are not yet exhausted; a read replica would do |
| **All three** | Fact-centric domains that rebuild past states, different read/write scaling needs, and reactive workflows | MVP or prototype; small team; simple domain; when any individual pattern would suffice |

### Adopting CQRS

Look for concrete signals, not a general feeling that the domain is complex:

- **Reads vastly outnumber writes and are expensive** — joins, aggregations or search that cost far more than the writes feeding them.
- **Read and write workloads contend** for the same locks, connections, CPU or I/O, so heavy reporting degrades command latency.
- **The shape the UI needs is a poor fit for the write model** — screens stitch together several aggregates, or need denormalised, pre-computed or searchable views. This is often the decisive signal.

Before adopting it:

- **A read replica is not CQRS.** A replica scales the same model; CQRS introduces a *different* read model. If the same queries just need more capacity, a replica is the cheaper answer.
- **Exhaust the cheap options first**: indexes, query rewrites, caching, more hardware.
- **Treat the read store as disposable.** It must be rebuildable from the write side (replaying events or re-projecting current state). Feed it from a transactional outbox (see `dev-integration-patterns-transactional-outbox`), change data capture or, with event sourcing, a subscription to the event store. A second write in the command handler is only safe when the read tables live in the same database and are updated in the same transaction; to a separate store it is a dual write.
- **Apply it per flow, never system-wide.** Use it for the one or two query paths that show the signals; the rest of the system stays plain CRUD.

## Log vs Queue Brokers

The broker type changes what consumers can rely on:

| | Log-based (Kafka-style) | Queue-based (RabbitMQ-style) |
|---|---|---|
| **Retention** | Events kept for a retention period after consumption | Message deleted once acknowledged |
| **Replay** | Yes — reset the consumer offset to rebuild a projection or onboard a new consumer | No — a new consumer sees only new messages |
| **Ordering per key** | Guaranteed within a partition; route by key to the same partition | Only with a single active consumer per queue, or consistent-hash routing to per-key queues |
| **Fits** | Event streams, projections, multiple independent readers | Work distribution, commands, per-message routing |

If projections must be rebuildable from the broker, you need a log; with a queue broker, rebuild from the write store or an event store instead.

## Publishing Reliably

Saving state and then publishing the event is a **dual write**: a crash between the two loses the event (or publishes one for a rolled-back change). Write the event to an outbox in the same transaction as the state change and relay it afterwards — see `dev-integration-patterns-transactional-outbox`. Consumers must still be idempotent, because the relay delivers at least once.

## Best Practices
- Start with EDA alone if you only need loose coupling and reactive behavior. Add event sourcing or CQRS only when you have a specific need.
- Design events as first-class domain concepts: past-tense, immutable, carrying business intent (not CRUD operations).
- Plan for event schema evolution from day one: upcast stored events on read; use a schema registry (Avro, Protobuf) for integration events published to other services.
- Build projections to be rebuildable: if a projection is corrupted or needs to change, replay events from the beginning.
- Validate commands against the write side (rehydrated aggregate), never against projections.
- Add snapshots only when measured rehydration latency demands it, every N events; keep them versioned and disposable.
- Handle idempotency in all event consumers: at-least-once delivery is the norm.
- Monitor projection lag (time between event publication and read model update) as a key operational metric.
- Keep the write model focused on enforcing business invariants; keep the read model focused on query performance.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/event-driven-architecture-eda.md](references/event-driven-architecture-eda.md) | Event-Driven Architecture (EDA) — Event Types, EDA Topology, EDA Benefits and Tradeoffs |
| [references/event-sourcing.md](references/event-sourcing.md) | Event Sourcing — when to use (vs audit/temporal tables), stream design, store schema, optimistic concurrency, deciding on the write side, snapshots, compensating events, temporal queries, schema evolution/upcasting, personal data, benefits & challenges |
| [references/cqrs-command-query-responsibility-segregation.md](references/cqrs-command-query-responsibility-segregation.md) | CQRS — architecture, when justified, feeding the read store, projections (idempotency, checkpoints, ordering, rebuild) |
| [references/details.md](references/details.md) | Eventual consistency — strategies, never validating commands against the read model |

## References

- [Martin Fowler — Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)
- [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html)
- [Martin Fowler — What Do You Mean by Event-Driven?](https://martinfowler.com/articles/201701-event-driven.html)

See references/rules.md for the full rule catalog.
