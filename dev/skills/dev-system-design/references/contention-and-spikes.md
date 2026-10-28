# Contention and Traffic Spikes

Two related problems: many actors competing for the same scarce thing (seats, stock, usernames), and sudden bursts that exceed normal capacity (launches, sales, ticket drops).

## Reserving scarce inventory

Typical flow: user selects an item, has a few minutes to pay, then the purchase is confirmed or the item returns to the pool.

| Approach | How | Pros | Cons |
|---|---|---|---|
| Long DB transaction / row lock until payment | Lock the row for the whole checkout | Simple to reason about | Holds locks for minutes; does not scale; abandoned sessions block items |
| Status column + expiry timestamp | `status = 'held', held_until = now + 10 min`, a job or query treats expired holds as free | Durable, no extra store | Extra writes to the primary; expiry handling needed |
| Short-lived hold in a fast store | Atomic set-if-absent with TTL (e.g. `hold:seat:123` for 10 min) | Fast, expiry is automatic | Store is not the source of truth; must still be confirmed in the DB |

Recommended pattern: **hold in a fast store with TTL, and let the database be the final arbiter.** The confirmation write uses a unique constraint (one ticket per seat per event) or a conditional update (`UPDATE ... SET status='sold' WHERE id=? AND status='available'` and check the affected row count). If the fast store loses a hold or two clients race past it, the database constraint still prevents double-selling.

## Optimistic vs pessimistic concurrency

| | Optimistic | Pessimistic |
|---|---|---|
| Mechanism | Read a version, write `WHERE version = ?`, retry on conflict | `SELECT ... FOR UPDATE` or explicit locks |
| Best when | Conflicts are rare | Conflicts are frequent and retries are expensive |
| Failure mode | Retry storms under heavy contention | Lock waits, deadlocks, reduced throughput |
| Lock duration | None held between read and write | Held for the transaction |

Keep pessimistic locks short and acquire them in a consistent order to avoid deadlocks. Never hold a database lock across a call to an external service (payment gateway).

## Idempotency keys
Networks fail after the server has done the work, so clients retry. Without protection, a retry charges the card twice.
- Client generates a unique key per logical operation and sends it with every attempt.
- Server stores `key → result` (with a uniqueness constraint) within the same transaction as the effect, or before calling the external side effect.
- A repeat with the same key returns the stored result; a repeat with a different payload under the same key is rejected.
- Expire keys after a window longer than the client's retry horizon.
Consumers of queues need the same property: deduplicate by message ID or make the operation naturally idempotent (set, not increment).

## Absorbing spikes

### Virtual waiting room
Instead of letting 500k users hit checkout at once, place them in a queue and admit them at a rate the backend can handle.
- Issue a signed position/admission token at the edge.
- Admit N users per second; admitted users get a time-limited token to reach the protected flow.
- Serve the waiting page and status polls from cache/CDN so the queue itself is cheap.
- Communicate position and estimated wait; fairness matters as much as capacity.

### Queue-based load levelling
For work that does not need an immediate answer, accept the request, enqueue it, return `202 Accepted` with a status URL, and process at a steady rate. The queue depth becomes the buffer.

### Rate limiting

| Algorithm | Behaviour | Use for |
|---|---|---|
| Fixed window | N requests per clock window | Simple quotas; allows bursts at window edges |
| Sliding window | Smooths the edge effect | Fairer API limits |
| Token bucket | Steady refill, allows bursts up to bucket size | General API limiting |
| Leaky bucket | Constant outflow rate | Smoothing traffic to a fragile downstream |

Limit per user/API key/IP at the edge, return `429` with `Retry-After`, and keep counters in a shared fast store so limits hold across nodes.

### Other tools
- **Load shedding**: reject low-priority requests early when saturated, rather than slowing everything.
- **Pre-scaling**: for known events, scale up beforehand; autoscaling reacts too slowly for a spike measured in seconds.
- **Static and cached reads**: event pages, seat maps and availability summaries served from cache, refreshed every few seconds.
- **Circuit breakers and timeouts** so a slow dependency does not consume every thread.

## Checklist
- [ ] Database constraint or conditional update guarantees no double allocation.
- [ ] Holds expire automatically.
- [ ] Every mutating endpoint that clients retry is idempotent.
- [ ] A known spike has a waiting room or queue and pre-scaled capacity.
- [ ] Rate limits exist per client and at the edge.
