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
