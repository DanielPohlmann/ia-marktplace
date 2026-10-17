<!-- Part of the dev-integration-patterns-transactional-outbox skill. Loaded on demand from SKILL.md. -->

# Outbox relay implementations

## Outbox table

```sql
-- PostgreSQL
CREATE TABLE outbox (
    id              uuid        PRIMARY KEY,          -- message id, used for dedupe downstream
    seq             bigserial   NOT NULL UNIQUE,      -- commit-order cursor for the relay
    aggregate_type  text        NOT NULL,             -- routing: topic/exchange
    aggregate_id    text        NOT NULL,             -- partition / routing key (ordering scope)
    type            text        NOT NULL,             -- e.g. 'OrderPlaced.v1'
    payload         jsonb       NOT NULL,             -- serialized at write time, immutable
    headers         jsonb       NOT NULL DEFAULT '{}',-- correlation_id, causation_id, tenant
    occurred_at     timestamptz NOT NULL DEFAULT now(),
    sent_at         timestamptz NULL,
    attempts        int         NOT NULL DEFAULT 0,
    last_error      text        NULL
);

-- only unsent rows are scanned by the relay
CREATE INDEX outbox_unsent ON outbox (seq) WHERE sent_at IS NULL;
```

`seq` gives a total order of inserts. Note that sequence values are assigned at
insert, not commit: a long transaction can commit a lower `seq` after a higher one
was already relayed. Ordering only matters **per aggregate**, so publish with
`aggregate_id` as the key and let consumers tolerate cross-aggregate reordering.

## Polling publisher

### Safe concurrent batch (PostgreSQL)

```sql
BEGIN;
SELECT id, aggregate_type, aggregate_id, type, payload, headers
FROM outbox
WHERE sent_at IS NULL AND attempts < 10
ORDER BY seq
LIMIT 100
FOR UPDATE SKIP LOCKED;          -- other relay instances skip these rows

-- publish each row (broker confirm / ack required before marking)

UPDATE outbox SET sent_at = now() WHERE id = ANY(:published_ids);
UPDATE outbox SET attempts = attempts + 1, last_error = :err WHERE id = ANY(:failed_ids);
COMMIT;
```

- Hold the batch lock only for the publish round-trip; keep batches small.
- Require **publisher confirms** (RabbitMQ) / `acks=all` (Kafka) before marking sent.
- A crash after publish and before `COMMIT` republishes the batch → consumers dedupe.
- `SKIP LOCKED` with multiple instances can reorder rows **of the same aggregate**
  across instances. When strict per-aggregate order matters, either run a single
  relay (leader election / advisory lock) or shard relays by `hash(aggregate_id)`.

### SQL Server equivalent

```sql
SELECT TOP (100) *
FROM outbox WITH (UPDLOCK, READPAST, ROWLOCK)
WHERE sent_at IS NULL
ORDER BY seq;
```

### Loop shape

```
loop:
  rows = fetch_batch()
  if rows empty: sleep(backoff)  # 100ms → 1s → 5s, reset on work
  else: publish(rows); mark(rows)
```

Optional latency trick: `LISTEN/NOTIFY` (PostgreSQL) or an in-process signal after
commit wakes the relay immediately; polling stays as the safety net.

### Cleanup

```sql
DELETE FROM outbox WHERE sent_at < now() - interval '7 days';
```

At high volume, partition `outbox` by `occurred_at` (daily) and drop old partitions
instead of deleting.

## Transaction log tailing (CDC)

Debezium reads the database log (PostgreSQL WAL via logical replication, MySQL
binlog, SQL Server CDC) and routes outbox inserts to Kafka topics.

```properties
connector.class=io.debezium.connector.postgresql.PostgresConnector
table.include.list=public.outbox
plugin.name=pgoutput
transforms=outbox
transforms.outbox.type=io.debezium.transforms.outbox.EventRouter
transforms.outbox.table.field.event.id=id
transforms.outbox.table.field.event.key=aggregate_id
transforms.outbox.table.field.event.type=type
transforms.outbox.table.field.event.payload=payload
transforms.outbox.route.by.field=aggregate_type
transforms.outbox.route.topic.replacement=events.${routedByValue}
```

- No `sent_at` bookkeeping: the connector offset is the cursor. Rows can be deleted
  right after insert (same transaction even) — the log still carries them.
- Events arrive in **commit order**, fixing the `seq` caveat above.
- Operate the replication slot: a stopped connector makes PostgreSQL retain WAL
  indefinitely. Alert on slot lag and set `max_slot_wal_keep_size`.
- Snapshot mode for the outbox table is usually `never`/`no_data`.

## Relay comparison

| Concern | Polling publisher | Log tailing (Debezium) |
|---|---|---|
| Latency | Poll interval (100ms–seconds) | Sub-second |
| DB load | Repeated queries on outbox | Reads the log; near zero query load |
| Ordering | Insert order; per-aggregate with care | Commit order |
| Infra | Code in the service or a sidecar | Kafka Connect + Debezium + slot ops |
| Broker | Any (RabbitMQ, SQS, Service Bus, Kafka) | Kafka-centric (Debezium Server for others) |
| Failure mode | Backlog grows in outbox table | WAL retention grows on DB disk |
