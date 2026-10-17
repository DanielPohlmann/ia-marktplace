<!-- Part of the dev-architecture-event-driven skill. Loaded on demand from SKILL.md. -->

# Event Sourcing

Instead of storing the current state of an entity, store the **sequence of events** that led to the current state. The current state is derived by replaying the events.

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
| `metadata` | JSON | Correlation ID, causation ID, user, timestamp |
| `version` | integer | Sequence number within the stream (for optimistic concurrency) |
| `timestamp` | datetime | When the event was appended |

```sql
CREATE TABLE event_store (
    stream_id    VARCHAR(255) NOT NULL,
    version      INTEGER NOT NULL,
    event_id     UUID NOT NULL,
    event_type   VARCHAR(255) NOT NULL,
    data         JSONB NOT NULL,
    metadata     JSONB,
    timestamp    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (stream_id, version)
);
```

## Event Store Implementations

| Technology | Type | Notes |
|-----------|------|-------|
| **EventStoreDB** | Purpose-built | Native event sourcing database; subscriptions, projections |
| **Marten** | .NET library | Event sourcing + document DB on top of PostgreSQL |
| **Axon Framework** | Java framework | Event sourcing + CQRS + saga support |
| **PostgreSQL + custom table** | DIY | Simple; use the schema above |
| **Apache Kafka** | Log-based | Can serve as event store; infinite retention + compaction |
| **DynamoDB + streams** | AWS | Single-table design with event streams |

## Event Sourcing Benefits

- **Complete audit trail** -- Every change is recorded as an immutable event.
- **Temporal queries** -- "What was the account balance on March 15?" Replay events up to that date.
- **Event replay** -- Rebuild read models, fix projections, or populate new services by replaying events.
- **Debugging** -- Reproduce any state by replaying the event sequence.
- **Domain richness** -- Events capture business intent, not just data changes.

## Event Sourcing Challenges

- **Event schema evolution** -- Events are immutable, but their schema must evolve. Use upcasting or versioned deserializers.
- **Replay performance** -- Long event streams are slow to replay. Use **snapshots** to checkpoint state periodically.
- **Eventual consistency** -- Read models (projections) are updated asynchronously; they may lag behind the write model.
- **Complexity** -- Significantly more complex than CRUD for simple domains.
- **Storage growth** -- Event stores grow continuously. Archiving and retention policies are needed.
