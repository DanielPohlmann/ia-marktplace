---
name: dev-architecture-hexagonal
description: Use when isolating domain logic from technology with Ports and Adapters or Onion architecture. USE FOR: port interfaces, driving/driven adapters, adapter-based testing, boundary inversion of control. DO NOT USE FOR: Clean Architecture layers (use dev-craftsmanship-clean-architecture), service boundaries (use dev-architecture-microservices), domain modeling (use dev-architecture-domain-driven-design).
---

# Hexagonal Architecture (Ports and Adapters)

## Overview
Hexagonal Architecture, introduced by Alistair Cockburn in 2005, organizes an application so that the core domain logic is isolated from external concerns (databases, APIs, UIs, message brokers) through **ports** (interfaces) and **adapters** (implementations). The goal is to make the application equally drivable by users, programs, automated tests, or batch scripts -- and equally connected to any external system.

The architecture is also known as **Ports and Adapters**. It shares the same fundamental principle as Onion Architecture (Jeffrey Palermo, 2008) and Clean Architecture (Robert C. Martin): **dependencies point inward; the domain depends on nothing external.**

## Code Structure Example

```
src/
  OrderService/
    Domain/                          # Pure domain model (no dependencies)
      Order.cs
      OrderLine.cs
      Money.cs
      OrderStatus.cs

    Ports/
      Primary/                       # What the app offers
        IOrderService.cs
        Commands/
          PlaceOrderCommand.cs
          CancelOrderCommand.cs
        Queries/
          GetOrderQuery.cs
      Secondary/                     # What the app needs
        IOrderRepository.cs
        IPaymentGateway.cs
        IInventoryClient.cs
        IEventPublisher.cs

    Application/                     # Use case orchestration
      OrderApplicationService.cs     # Implements IOrderService

    Adapters/
      Primary/                       # Driving adapters
        Rest/
          OrdersController.cs
        Grpc/
          OrderGrpcService.cs
        Cli/
          OrderCliCommand.cs
      Secondary/                     # Driven adapters
        Persistence/
          PostgresOrderRepository.cs
        Payment/
          StripePaymentGateway.cs
        Messaging/
          KafkaEventPublisher.cs

    Composition/                     # Wires everything together (DI)
      ServiceRegistration.cs
```

## Comparison: Hexagonal vs. Onion vs. Clean Architecture

| Aspect | Hexagonal (Cockburn) | Onion (Palermo) | Clean (Martin) |
|--------|---------------------|-----------------|----------------|
| **Core idea** | Ports and Adapters | Concentric layers | Dependency Rule |
| **Visualization** | Hexagon with ports | Concentric circles | Concentric circles |
| **Inner layer** | Domain Model | Domain Model | Entities |
| **Boundary definition** | Ports (interfaces) | Layer interfaces | Use Case boundaries |
| **Outer layer** | Adapters | Infrastructure | Frameworks & Drivers |
| **Key emphasis** | Symmetry between driving/driven | Layer discipline | Use cases as central organizing concept |
| **Dependency direction** | Inward | Inward | Inward |

**They are the same fundamental idea expressed differently.** All three:
- Isolate the domain from infrastructure.
- Use interfaces (ports) at boundaries.
- Enforce the dependency rule: inner layers never reference outer layers.
- Enable technology swaps without changing business logic.

The practical differences are in emphasis and vocabulary, not in principle.

### Onion Architecture Layers (Palermo)

```
┌─────────────────────────────────────────┐
│  Infrastructure & UI (outermost)         │
│  ┌─────────────────────────────────┐    │
│  │  Application Services           │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │  Domain Services        │    │    │
│  │  │  ┌─────────────────┐    │    │    │
│  │  │  │  Domain Model   │    │    │    │
│  │  │  │  (Entities,     │    │    │    │
│  │  │  │   Value Objects)│    │    │    │
│  │  │  └─────────────────┘    │    │    │
│  │  └─────────────────────────┘    │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| **Domain imports framework** | Domain coupled to infrastructure; hard to test | Remove all framework dependencies from domain layer |
| **Adapter logic in domain** | Business logic leaks into controllers or repositories | Move logic to domain model or application service |
| **Port too broad** | Interface with 20 methods; hard to mock, violates ISP | Split into focused interfaces (Interface Segregation Principle) |
| **Skipping ports for "simplicity"** | Application calls database directly; loses swappability and testability | Always define a port even if you only have one adapter |
| **Anemic domain + fat service** | Domain model is just data; all logic in application service | Enrich the domain model with behavior (see `dev-architecture-domain-driven-design`) |

## Best Practices
- Keep the domain model completely free of infrastructure dependencies. No ORM attributes, no HTTP concepts, no serialization annotations in the domain layer.
- Define ports using domain language, not technology language. `IOrderRepository.Save(Order)`, not `IDatabaseContext.ExecuteCommand(SQL)`.
- Use dependency injection to wire adapters to ports at the composition root.
- Write the majority of tests against ports (mock adapters), not against infrastructure. This gives you fast, reliable tests.
- Start with one adapter per port. Add additional adapters when you actually need them (e.g., switching databases, adding a CLI interface).
- Use the hexagonal structure to enable incremental migration: swap one adapter at a time without touching the domain.
- Combine with DDD (see `dev-architecture-domain-driven-design`) for rich domain modeling inside the hexagon.
- The hexagonal shape is a metaphor for symmetry -- there is no inherent "top" or "bottom." Any adapter on any side is equally first-class.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/core-concepts.md](references/core-concepts.md) | Core Concepts — Ports (Interfaces), Adapters (Implementations), Driving vs. Driven Side |
| [references/details.md](references/details.md) | The Hexagonal Diagram; The Dependency Rule; Testability: The Primary Benefit |

## References

- [Alistair Cockburn — Hexagonal Architecture (Ports and Adapters)](https://alistair.cockburn.us/hexagonal-architecture/)
- [Hexagonal Architecture — Wikipedia](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))

See references/rules.md for the full rule catalog.
