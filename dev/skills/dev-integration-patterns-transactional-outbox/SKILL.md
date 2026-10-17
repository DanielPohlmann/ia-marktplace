---
name: dev-integration-patterns-transactional-outbox
description: Use when one operation must change a database and also notify another system (broker, cache, search index, external API) without losing or inventing events (the dual-write problem). USE FOR: transactional outbox, polling publisher, CDC/Debezium log tailing, inbox, idempotent consumers, listen-to-yourself, why not 2PC, ordering, relay concurrency, cleanup. DO NOT USE FOR: MassTransit outbox config (use stack-masstransit), general consumer patterns (use dev-integration-patterns-messaging-endpoints), event sourcing/CQRS design (use dev-architecture-event-driven).
---

# Transactional Outbox & Dual-Write Strategies

## Overview

A **dual write** is any operation that must update two systems that share no
transaction — typically "save the order in the database **and** publish
`OrderPlaced` to the broker". Every naive ordering breaks:

| Order of writes | Failure | Result |
|---|---|---|
| Commit DB → publish | Process crashes / broker down after commit | **Lost event** — state changed, nobody notified |
| Publish → commit DB | Commit fails (constraint, deadlock, timeout) | **Ghost event** — consumers act on something that never happened |
| Publish inside the open transaction | Transaction rolls back after publish | Ghost event (same as above) |
| Retry the failed side | Crash between attempts; retries are not durable | Lost event, just less often |

The fix is to make the second write **derive from the first durable one**:
commit the state change and the intent to notify atomically in **one** store,
then deliver asynchronously with retries. Delivery becomes **at-least-once**, so
consumers must be **idempotent**.

## When to use

- A command handler changes state **and** publishes an integration event.
- A write must also update a cache, search index, read model, or call a webhook.
- You see "published after `SaveChanges()`" or "send email then save" code.
- Incidents of missing downstream updates or events for rolled-back data.

Not needed when the side effect is in the **same** transactional store (same DB
transaction), or when loss is acceptable and cheap to reconcile (see strategy 7).

## Strategy decision matrix

| # | Strategy | How it works | Guarantee | Main cost | Pick when |
|---|---|---|---|---|---|
| 1 | **Outbox + polling publisher** | Insert event row in an `outbox` table in the same transaction; a relay polls, publishes, marks sent | At-least-once, ordered per key | Polling latency & DB load; relay to operate | **Default.** Any relational DB, moderate throughput |
| 2 | **Outbox + log tailing (CDC)** | Same outbox table; Debezium (or DB-native CDC) reads the transaction log and emits rows | At-least-once, commit order, low latency | Kafka Connect/Debezium infra, replication slots | High throughput, Kafka already present |
| 3 | **CDC on business tables** | Stream row changes of domain tables directly | At-least-once | Leaks internal schema as the public contract; no intent | Replicating data (search index, analytics), **not** domain events |
| 4 | **Event sourcing** | The event store *is* the state; subscribers read the stream | Exactly the stored events, ordered | Full paradigm shift | Already doing event sourcing (use dev-architecture-event-driven) |
| 5 | **Listen to yourself** | Publish only; the service consumes its own event to update its DB | At-least-once | No read-your-writes; validation before publish is weak | Write path can be fully async and state is rebuildable |
| 6 | **2PC / XA** | Distributed transaction across DB and broker | Atomic (in theory) | Blocking, coordinator failure, most brokers/clouds lack XA | Almost never — legacy MSDTC/JTA estates only |
| 7 | **Best effort + reconciliation** | Do both writes; a periodic job detects and repairs drift | Eventually consistent, gaps until sweep | Reconciler logic per pair | Low-value side effects: cache invalidation, notifications that may be late |

```
Need to notify another system after a DB change?
├─ Is the event store your source of truth? ──yes──> 4 Event sourcing
├─ Is it data replication, not a business event? ─yes─> 3 CDC on tables
├─ Is losing/duplicating briefly acceptable + repairable? ─yes─> 7 Reconcile
└─ Otherwise: Transactional outbox
     ├─ Kafka + CDC infra available, high volume ──> 2 Log tailing
     └─ else ──────────────────────────────────────> 1 Polling publisher
```

## Core pattern

```sql
-- same database, same transaction as the business change
BEGIN;
  UPDATE orders SET status = 'PLACED' WHERE id = :order_id;
  INSERT INTO outbox (id, aggregate_type, aggregate_id, type, payload, occurred_at)
  VALUES (:message_id, 'Order', :order_id, 'OrderPlaced.v1', :json, now());
COMMIT;
```

1. **Write** — handler persists state + outbox row in one local transaction.
2. **Relay** — a separate loop (or CDC connector) reads unsent rows in order,
   publishes with the row `id` as the **message id**, then marks them sent.
3. **Consume** — consumers record processed message ids in an **inbox** table in
   the same transaction as their own changes and skip duplicates.

The outbox row is the event contract: serialize the payload **at write time**
(immutable), version the type, and carry `message_id`, `aggregate_id`,
`correlation_id`, and `occurred_at`.

## Pitfalls checklist

- [ ] **Outbox insert uses the same connection/transaction** as the business write
      (same `DbContext`/unit of work) — otherwise you rebuilt the dual write.
- [ ] **Relay concurrency is controlled**: `FOR UPDATE SKIP LOCKED` batches or a
      single leader per partition; unguarded parallel relays duplicate and reorder.
- [ ] **Ordering is per aggregate**: read by sequence, publish with
      `aggregate_id` as the partition/routing key; never promise global order.
- [ ] **Consumers are idempotent** (inbox table, natural idempotency, or upserts) —
      the relay *will* republish after a crash between publish and mark-sent.
- [ ] **Partial index on unsent rows** and batched polling with backoff; no full scans.
- [ ] **Cleanup job** deletes or archives sent rows (or partition by day and drop).
- [ ] **Poison rows** get an attempt counter and a dead-letter state; one bad row
      must not block the partition forever.
- [ ] **Alert on outbox age** (oldest unsent `occurred_at`), not just row count.
- [ ] **CDC**: monitor replication-slot lag — a stopped connector makes Postgres
      retain WAL until the disk fills.
- [ ] **No external calls inside the business transaction** (HTTP, broker, email).
- [ ] Prefer the framework's outbox when one exists (MassTransit, NServiceBus,
      Wolverine, Spring Modulith) over a hand-rolled relay.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/relay-implementations.md](references/relay-implementations.md) | Outbox schema, polling publisher with `SKIP LOCKED` (PostgreSQL, SQL Server), Debezium outbox event router config, relay comparison |
| [references/inbox-idempotent-consumer.md](references/inbox-idempotent-consumer.md) | Inbox table, consumer transaction flow, natural idempotency, dedupe retention, ordering on the consumer side |
| [references/dotnet-examples.md](references/dotnet-examples.md) | EF Core hand-rolled outbox (SaveChanges interceptor + BackgroundService relay), when to switch to the MassTransit outbox |

## References

- Chris Richardson — [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), [Polling publisher](https://microservices.io/patterns/data/polling-publisher.html), [Transaction log tailing](https://microservices.io/patterns/data/transaction-log-tailing.html)
- [Debezium — Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
- Gunnar Morling — [Reliable Microservices Data Exchange With the Outbox Pattern](https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/)
- Martin Kleppmann — *Designing Data-Intensive Applications*, ch. 11 (derived data, CDC)
