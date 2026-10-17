<!-- Part of the dev-architecture-hexagonal skill. Loaded on demand from SKILL.md. -->

# Hexagonal Architecture (Ports and Adapters) — details

## The Hexagonal Diagram

```
                        Driving Side (Primary)
                     (things that USE the app)

                    REST    CLI    Tests   Events
                     │       │      │       │
                     ▼       ▼      ▼       ▼
               ┌─────────────────────────────────┐
               │        Primary Adapters          │
               │    (implement driving ports)      │
               │                                   │
         ┌─────┤─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤─────┐
         │     │        Primary Ports              │     │
         │     │    (interfaces the app exposes)   │     │
         │     │                                   │     │
         │     │     ┌───────────────────┐         │     │
         │     │     │                   │         │     │
         │     │     │   Domain Model    │         │     │
         │     │     │   (Pure Business  │         │     │
         │     │     │    Logic)         │         │     │
         │     │     │                   │         │     │
         │     │     └───────────────────┘         │     │
         │     │                                   │     │
         │     │       Secondary Ports             │     │
         │     │   (interfaces the app needs)      │     │
         └─────┤─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤─────┘
               │      Secondary Adapters           │
               │   (implement driven ports)        │
               └─────────────────────────────────┘
                     │       │       │       │
                     ▼       ▼       ▼       ▼
                  Postgres  Redis  Stripe  Kafka

                        Driven Side (Secondary)
                    (things the app USES)
```

## The Dependency Rule

The fundamental rule shared by Hexagonal, Onion, and Clean Architecture:

```
Dependencies point inward. Inner layers know nothing about outer layers.

┌─────────────────────────────────────────┐
│  Adapters (outermost)                    │
│  ┌─────────────────────────────────┐    │
│  │  Ports / Application            │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │  Domain Model           │    │    │
│  │  │  (innermost, no deps)   │    │    │
│  │  └─────────────────────────┘    │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘

  Outer depends on inner. Never the reverse.
```

- The **domain** has zero external dependencies. No framework imports, no database references, no HTTP concepts.
- **Ports** are defined by the domain/application layer using domain language.
- **Adapters** depend on ports (and on external libraries), never the reverse.
- **Composition root** (startup/DI configuration) wires adapters to ports.

## Testability: The Primary Benefit

The greatest practical benefit of hexagonal architecture is **testability**. Because the domain depends only on ports (interfaces), you can test business logic without any infrastructure.

```
// Test the domain using mock adapters — no database, no HTTP, no Stripe
[Test]
public async Task PlaceOrder_WithValidItems_ConfirmsOrder()
{
    // Arrange — mock secondary ports
    var orderRepo = new InMemoryOrderRepository();
    var paymentGateway = new FakePaymentGateway(alwaysSucceeds: true);
    var eventPublisher = new SpyEventPublisher();

    // The application service uses ports, not concrete adapters
    var service = new OrderApplicationService(
        orderRepo, paymentGateway, eventPublisher);

    // Act — drive through primary port
    var orderId = await service.PlaceOrder(new PlaceOrderCommand
    {
        CustomerId = "cust-1",
        Items = new[] { new OrderItem("prod-1", 2, 25.00m) }
    });

    // Assert — verify domain behavior
    var order = await orderRepo.FindById(orderId);
    Assert.Equal(OrderStatus.Confirmed, order.Status);
    Assert.Single(eventPublisher.PublishedEvents
        .OfType<OrderConfirmed>());
}
```

### Testing Strategy by Layer

| Layer | Test Type | What to Test | Infrastructure Needed |
|-------|-----------|-------------|----------------------|
| **Domain** | Unit tests | Business rules, invariants, calculations | None (pure logic) |
| **Application** | Unit tests with mocks | Use case orchestration, event publishing | Mock adapters |
| **Primary Adapters** | Integration tests | Request mapping, serialization, routing | HTTP test server |
| **Secondary Adapters** | Integration tests | Database queries, API calls, serialization | Real or containerized infrastructure |
| **Composition** | Smoke / E2E tests | Full system wiring, happy path | Full infrastructure |
