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
| **Event Sourcing** | Audit trail is critical; temporal queries needed; domain is event-centric; complex business rules | Simple CRUD domains; team unfamiliar with the pattern; high-volume writes with no audit need |
| **CQRS** | Read and write patterns differ significantly; need independent scaling; complex query requirements | Simple domains where reads and writes are symmetric; small systems; team unfamiliar with the pattern |
| **All three** | Complex domains with audit requirements, different read/write scaling needs, and reactive workflows | MVP or prototype; small team; simple domain; when any individual pattern would suffice |

## Best Practices
- Start with EDA alone if you only need loose coupling and reactive behavior. Add event sourcing or CQRS only when you have a specific need.
- Design events as first-class domain concepts: past-tense, immutable, carrying business intent (not CRUD operations).
- Plan for event schema evolution from day one. Use a schema registry (Avro, Protobuf) for strong contracts.
- Build projections to be rebuildable: if a projection is corrupted or needs to change, replay events from the beginning.
- Use snapshots for long-lived event streams to keep replay times reasonable.
- Handle idempotency in all event consumers: at-least-once delivery is the norm.
- Monitor projection lag (time between event publication and read model update) as a key operational metric.
- Keep the write model focused on enforcing business invariants; keep the read model focused on query performance.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/event-driven-architecture-eda.md](references/event-driven-architecture-eda.md) | Event-Driven Architecture (EDA) — Event Types, EDA Topology, EDA Benefits and Tradeoffs |
| [references/event-sourcing.md](references/event-sourcing.md) | Event Sourcing — Traditional State vs. Event Sourcing, Event Store Structure, Event Store Implementations, Event Sourcing Benefits, Event Sourcing Challenges |
| [references/cqrs-command-query-responsibility-segregation.md](references/cqrs-command-query-responsibility-segregation.md) | CQRS (Command Query Responsibility Segregation) — CQRS Architecture, Why Separate Read and Write Models?, Projections (Read Models) |
| [references/details.md](references/details.md) | Eventual Consistency |

## References

- [Martin Fowler — Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)
- [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html)
- [Martin Fowler — What Do You Mean by Event-Driven?](https://martinfowler.com/articles/201701-event-driven.html)

See references/rules.md for the full rule catalog.
