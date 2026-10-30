<!-- Part of the dev-architecture-event-driven skill. Loaded on demand from SKILL.md. -->

# Event-Driven Architecture, Event Sourcing & CQRS — details

## Eventual Consistency

When using EDA, event sourcing, or CQRS, the system is eventually consistent -- updates propagate asynchronously and read models may temporarily be stale.

### Managing Eventual Consistency

| Strategy | Description |
|----------|-------------|
| **Causal consistency** | Ensure events are processed in causal order (use stream position / version) |
| **Read-your-own-writes** | After a command, query the write model directly (bypass read model) or wait for projection to catch up |
| **UI optimistic update** | Update the UI immediately; reconcile when the read model catches up |
| **Polling / subscription** | Client subscribes to updates or polls until the read model reflects the change |
| **Version stamping** | Include a version in responses; client retries if version is stale |

### Never Validate Commands Against the Read Model

Read-your-own-writes is about what the *user sees*; command validation is about what the *system allows*. The read model may not yet reflect the last write, so checks such as "enough balance", "seat still free" or "name not taken" made against it can approve a command that the write side would reject. Validate on the write side: the rehydrated aggregate (event sourcing) or the current state read in the same transaction (state-based), protected by optimistic concurrency or a unique constraint. Use the read model only for UX pre-checks that the write side re-validates.
