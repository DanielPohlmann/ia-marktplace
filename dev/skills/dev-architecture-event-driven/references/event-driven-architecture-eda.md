<!-- Part of the dev-architecture-event-driven skill. Loaded on demand from SKILL.md. -->

# Event-Driven Architecture (EDA)

In EDA, components produce and consume events. An event represents something that happened -- a fact. Events are immutable and past-tense (OrderPlaced, PaymentReceived, InventoryReserved).

## Event Types

| Type | Description | Example |
|------|-------------|---------|
| **Event Notification** | A thin signal that something happened; consumer fetches details if needed | `{ "type": "OrderPlaced", "orderId": "123" }` |
| **Event-Carried State Transfer** | Event carries the full state needed by consumers | `{ "type": "OrderPlaced", "orderId": "123", "items": [...], "total": 99.95 }` |
| **Domain Event** | A significant occurrence in the domain model (DDD) | `OrderPlaced`, `PaymentFailed`, `ShipmentDispatched` |

## EDA Topology

**Broker topology** (most common): Events flow through a central broker (Kafka, RabbitMQ, AWS EventBridge, Azure Service Bus).

```
┌──────────┐    ┌──────────────┐    ┌──────────────┐
│ Producer  │───▶│  Event       │───▶│  Consumer A  │
│           │    │  Broker      │───▶│  Consumer B  │
│           │    │  (Kafka,     │───▶│  Consumer C  │
└──────────┘    │  RabbitMQ)   │    └──────────────┘
                └──────────────┘
```

**Mediator topology**: A central mediator orchestrates event flow (used when processing order matters).

## EDA Benefits and Tradeoffs

| Benefit | Tradeoff |
|---------|----------|
| Loose coupling between producers and consumers | Harder to trace and debug end-to-end flows |
| Independent scalability per component | Eventual consistency; no immediate confirmation |
| Temporal decoupling (producer doesn't wait) | Event ordering and deduplication challenges |
| Natural fit for audit trails | Schema evolution and versioning complexity |
| Easy to add new consumers without changing producers | Error handling is more complex (dead letters, retries) |
