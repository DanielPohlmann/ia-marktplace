<!-- Part of the dev-architecture-event-driven skill. Loaded on demand from SKILL.md. -->

# Event Sourcing

Instead of storing the current state of an entity, store the **sequence of events** that led to the current state. The current state is derived by replaying the events.

## When to Use — and When Not

The trigger is the domain itself: the business already thinks in terms of facts that happened (ledger entries, bookings, claims moving through states), or you must reconstruct **past states** — what the system believed at a given moment and why.

| Need | Cheaper answer | Event sourcing? |
|------|----------------|-----------------|
| "Who changed what, when" | Append-only history/audit table written in the same transaction, or a temporal (system-versioned) table | No |
| Show previous versions of a record | Temporal table or versioned rows | No |
| Expensive joins on reads | Indexes, a projection/materialised view (CQRS without event sourcing) | No — join cost never justifies it |
| Decisions depend on the sequence of facts; past states must be rebuilt and explained; new views of old history keep appearing | — | Yes |

If the only argument is "we need history", stop at the audit table: it keeps the familiar state model, needs no projections, and answers the same questions.

## Traditional State vs. Event Sourcing

```
Traditional (State-based):
┌─────────────────────┐
│  Account             │
│  balance: $750       │  ← Only current state; history lost
│  status: active      │
└─────────────────────┘

Event Sourcing (Event Log):
┌─────────────────────────────────────────────────────┐
│  Event Store (Account #42)                           │
│                                                       │
│  1. AccountOpened    { balance: $0 }        2024-01  │
│  2. MoneyDeposited   { amount: $1000 }      2024-01  │
│  3. MoneyWithdrawn   { amount: $200 }       2024-02  │
│  4. MoneyWithdrawn   { amount: $50 }        2024-03  │
│                                                       │
│  Current state: replay events → balance: $750         │
└─────────────────────────────────────────────────────┘
```

## Event Store Structure

An event store is an append-only log organized by stream (typically one stream per aggregate):

| Column | Type | Description |
|--------|------|-------------|
| `stream_id` | string | Aggregate/entity identifier (e.g., `account-42`) |
| `event_id` | UUID | Unique event identifier |
| `event_type` | string | Event name (e.g., `MoneyDeposited`) |
| `data` | JSON/binary | Event payload |
| `metadata` | JSON | Correlation ID, causation ID, actor, schema version, effective time |
| `version` | integer | Sequence number within the stream (for optimistic concurrency) |
| `position` | bigint | Global, store-wide order; subscriptions use it as their checkpoint |
| `timestamp` | datetime | Recorded time: when the event was appended |

```sql
CREATE TABLE event_store (
    position     BIGINT GENERATED ALWAYS AS IDENTITY,
    stream_id    VARCHAR(255) NOT NULL,
    version      INTEGER NOT NULL,
    event_id     UUID NOT NULL,
    event_type   VARCHAR(255) NOT NULL,
    data         JSONB NOT NULL,
    metadata     JSONB,
    timestamp    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (stream_id, version),
    UNIQUE (position)
);
```

## Stream Design

- **One stream per aggregate**, named `<category>-<id>` (`account-42`, `order-9f1c`). The category prefix lets subscribers filter by aggregate type; the id keeps each stream small enough to load in one read.
- **Keep streams short-lived where the domain allows.** Model natural cut-offs ("closing the books"): an account ledger per accounting period, a cart per checkout. The closing event carries the balances forward and the next period starts a new stream. This beats snapshots for streams that would otherwise grow forever.
- **Events are immutable facts**: past-tense names (`FundsWithdrawn`, not `WithdrawFunds` or `AccountUpdated`), one explicit type per business fact, a JSON payload holding only what the fact needs.
- **Metadata travels with every event**: correlation id (the end-to-end flow), causation id (the command or event that caused this one), actor, schema version, and two times — **recorded time** (when the store appended it) and **effective time** (when it happened in the business, e.g. a backdated adjustment).

## Event Store Implementations

| Technology | Type | Notes |
|-----------|------|-------|
| **EventStoreDB** | Purpose-built | Native event sourcing database; subscriptions, projections |
| **Marten** | .NET library | Event sourcing + document DB on top of PostgreSQL |
| **Axon Framework** | Java framework | Event sourcing + CQRS + saga support |
| **PostgreSQL + custom table** | DIY | Simple; use the schema above |
| **Apache Kafka** | Log-based | Only with infinite retention and **no** compaction (compaction keeps the last record per key and destroys history). Lacks per-stream append-with-expected-version and efficient per-aggregate reads — better as a distribution log fed from the event store than as the store itself |
| **DynamoDB + streams** | AWS | Single-table design with event streams |

## Appending with Optimistic Concurrency

Every append states the version the decision was based on: "append these events to `account-42`, expecting version 7". The store rejects the write if the stream has moved on (the `(stream_id, version)` primary key above enforces it).

```
load account-42          → state at v7, balance 100
decide Withdraw(80)      → FundsWithdrawn{80}
append expecting v7      → ok, stream now at v8
concurrent Withdraw(80)  → also read v7 → append rejected
  reload (v8, balance 20), decide again → rejected: insufficient funds
```

Without the expected version, two concurrent commands read the same state, both pass validation and both append — a double withdrawal. On conflict, reload, re-decide and retry a bounded number of times; frequent conflicts mean the aggregate is too hot or too coarse.

## Decide on the Write Side, Never on the Read Model

Validate commands against the aggregate rehydrated from the store (latest snapshot plus the events after it), inside the load-decide-append cycle that the expected version protects. Projections lag behind the store: a balance read from a projection may not yet include the withdrawal appended a moment ago, and deciding on it lets a customer overspend. Read models answer queries; they never authorise commands.

## Snapshots

A snapshot caches the folded state of one aggregate at a given version, so loading reads the snapshot plus the events after it.

- **Purpose:** aggregate rehydration latency only. Projections do not use them — a projection rebuild still reads the events.
- **When:** only after measuring load latency and finding it too slow. Then the application writes one every N events, with N taken from that measurement (e.g. every 200), after a successful append.
- **Versioned and disposable:** store the fold/state version with each snapshot. When the fold logic or state shape changes, ignore and delete the old snapshots and let them be rebuilt from events. A snapshot is never the source of truth.
- Prefer short-lived streams (see *Stream Design*) before reaching for snapshots.

## Fixing Past Mistakes

Never edit or delete events to correct a mistake. Append a **compensating event** that states the correction (`FeeRefunded` after a wrongly charged `FeeCharged`), then rebuild the projections that consumed the original fact. History shows both the error and its fix, which is exactly what an audit needs.

**Replay must not re-trigger side effects.** Emails, payments and outbound messages belong to subscribers or process managers that record what they already did; rehydrating an aggregate or rebuilding a projection only folds data. If a handler could do both, give it an explicit replay mode that skips the side effects.

## Temporal Queries (Time Travel)

"What was the balance on March 15?" is answered by folding the stream up to a point — but first decide which time you mean:

- **Recorded time** — what the system *knew* then: fold events recorded on or before the date. Use for audits and "why did we decide that".
- **Effective time** — what was *true in the business* on that date, including corrections recorded later: fold all events, filtering on effective time. Use for statements and recalculations.

Backdated corrections make the two answers differ; store both times so both questions stay answerable.

## Schema Evolution

Stored events live forever, so readers must handle every version ever written:

- **Additive changes first** — new optional fields; readers ignore what they do not know and default what is missing (tolerant reader / weak schema). This covers most changes.
- **Upcasting** for breaking changes — transform old events into the current shape on read, before the aggregate or projection sees them; the stored bytes stay untouched.

```
upcast(event):
  if event.type == "FundsWithdrawn" and event.schemaVersion == 1:
      # v1 stored a bare number; v2 stores amount + currency
      return event with data.amount = { value: data.amount, currency: data.currency ?? "USD" },
                        schemaVersion = 2
  return event
```

- **New event type** when the meaning changed, not just the shape.
- **Internal vs integration events.** Stored events are the private persistence format of one service and can be upcast freely. Events published to other services are a public contract: translate stored events into separate integration events at the boundary, and apply schema registries, compatibility checks and contract tests there.

## Personal Data

An immutable log collides with erasure requests, so design for them up front:

- Keep personal data out of events where possible — reference a subject id and keep the details in a regular, deletable store.
- When events must carry it, use **crypto-shredding**: encrypt the personal fields with a per-subject key held in a key store. Deleting the key makes every copy unreadable — including backups and downstream logs — without rewriting events. Readers must handle a missing key by rendering the field as erased.

## Event Sourcing Benefits

- **Complete audit trail** -- Every change is recorded as an immutable event.
- **Temporal queries** -- "What was the account balance on March 15?" Fold the stream up to that point, choosing recorded or effective time (see *Temporal Queries*).
- **Event replay** -- Rebuild read models, fix projections, or populate new services by replaying events — without re-running side effects such as emails, payments or outbound messages.
- **Debugging** -- Reproduce any state by replaying the event sequence.
- **Domain richness** -- Events capture business intent, not just data changes.

## Event Sourcing Challenges

- **Event schema evolution** -- Events are immutable, but their schema must evolve. Use tolerant readers and upcasting (see *Schema Evolution*).
- **Rehydration latency** -- Long streams are slow to load. Prefer short-lived streams; add versioned, disposable **snapshots** at a measured threshold (see *Snapshots*).
- **Eventual consistency** -- Read models (projections) are updated asynchronously and lag behind the write model, so never validate commands against them.
- **Complexity** -- Significantly more complex than CRUD for simple domains.
- **Storage growth** -- Event stores grow continuously. Close streams per period and archive closed ones.
- **Personal data** -- Immutable events collide with erasure rights; keep PII out or crypto-shred it (see *Personal Data*).
