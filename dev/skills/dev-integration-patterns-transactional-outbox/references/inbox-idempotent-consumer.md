<!-- Part of the dev-integration-patterns-transactional-outbox skill. Loaded on demand from SKILL.md. -->

# Inbox & idempotent consumers

The outbox gives **at-least-once** delivery. Duplicates are normal (relay crash
after publish, broker redelivery, consumer crash before ack). The consumer side
must turn at-least-once into **effectively-once**.

## Inbox table

```sql
CREATE TABLE inbox (
    message_id   uuid        NOT NULL,
    consumer     text        NOT NULL,   -- one row per handler; a message can fan out
    processed_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (message_id, consumer)
);
```

## Consumer transaction

```
on message m:
  BEGIN
    INSERT INTO inbox (message_id, consumer) VALUES (m.id, 'billing')
      ON CONFLICT DO NOTHING
    if 0 rows inserted:            # already processed
      COMMIT; ack(m); return
    apply business change
    (optional) INSERT INTO outbox ...   # chained events: inbox + outbox in one tx
  COMMIT
  ack(m)                           # ack only after commit
```

- Inbox insert, business change, and any new outbox rows share **one** local
  transaction — that is what makes the whole chain reliable.
- Ack **after** commit. Ack-before-commit loses messages on crash.
- The message id must be stable across redeliveries: use the outbox row `id`, never
  a broker-generated delivery id.

## Natural idempotency (no inbox)

Prefer operations that are idempotent by construction when possible:

| Technique | Example |
|---|---|
| Upsert by business key | `INSERT … ON CONFLICT (order_id) DO UPDATE` |
| Set, don't increment | `status = 'PAID'` instead of `balance = balance - x` |
| Version / sequence guard | `UPDATE … WHERE id = :id AND version < :event_version` |
| Unique constraint on effect | `UNIQUE (payment_id)` on the ledger entry |

Increments, appends, emails, and external API calls are **not** naturally
idempotent — use the inbox, or pass an idempotency key to the external API.

## Retention

Keep inbox rows longer than the maximum redelivery window (broker retention,
relay retry horizon, replay scenarios). Typical: 7–30 days, then delete or
partition-drop. Deleting too early reopens the duplicate window.

## Ordering on the consumer

- Consume one partition / session per aggregate key to keep per-aggregate order.
- With competing consumers on an unordered queue, guard with a version check and
  either park out-of-order messages or make handlers commutative.
- Never rely on cross-aggregate ordering.

## Poison messages

Count attempts per message; after N failures route to a dead-letter queue with the
error, and alert. Do not insert the inbox row for a failed attempt — the
transaction rolls back, so the retry is processed fresh.
