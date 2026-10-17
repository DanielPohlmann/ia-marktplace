<!-- Part of the dev-architecture-domain-driven-design skill. Loaded on demand from SKILL.md. -->

# Tactical DDD

Tactical DDD provides the building blocks for modeling a single bounded context.

## Entities
Objects defined by their **identity**, not their attributes. Two entities with the same attributes but different IDs are different entities. Entities have a lifecycle and mutable state.

```
// An Order is identified by its OrderId, not its contents
public class Order
{
    public OrderId Id { get; }
    public CustomerId CustomerId { get; }
    public List<OrderLine> Lines { get; }
    public OrderStatus Status { get; private set; }

    public void Confirm() { ... }
    public void Cancel() { ... }
}
```

## Value Objects
Objects defined by their **attributes**, not by identity. Two value objects with the same attributes are equal. Value objects are immutable.

```
// A Money value is defined by its amount and currency
public record Money(decimal Amount, string Currency)
{
    public Money Add(Money other)
    {
        if (Currency != other.Currency)
            throw new CurrencyMismatchException();
        return new Money(Amount + other.Amount, Currency);
    }
}
```

**Prefer value objects over entities.** Most concepts in a domain are values, not entities. Using value objects reduces bugs (immutability) and improves clarity.

## Aggregates and Aggregate Roots

An aggregate is a cluster of entities and value objects treated as a single unit for data changes. The **aggregate root** is the entry point -- all external access goes through the root. The root enforces invariants (business rules) for the entire aggregate.

```
┌──────────────────────────────────────┐
│  Order Aggregate                      │
│                                       │
│  ┌────────────────┐                  │
│  │ Order          │ ◄── Aggregate    │
│  │ (Root)         │     Root         │
│  │                │                  │
│  │ - orderId      │                  │
│  │ - status       │                  │
│  │ - totalAmount  │                  │
│  └───┬────────────┘                  │
│      │ contains                      │
│      │                               │
│  ┌───▼────────────┐  ┌───────────┐  │
│  │ OrderLine      │  │ Money     │  │
│  │ (Entity)       │  │ (Value)   │  │
│  │ - lineId       │  │ - amount  │  │
│  │ - productId    │  │ - currency│  │
│  │ - quantity     │  │           │  │
│  └────────────────┘  └───────────┘  │
│                                       │
│  Invariant: total = sum of lines      │
│  Invariant: max 20 lines per order    │
└──────────────────────────────────────┘
```

## Aggregate Design Rules

1. **Reference other aggregates by identity only.** An Order aggregate holds a `CustomerId`, not a `Customer` object.
2. **Keep aggregates small.** Large aggregates cause contention, slow loading, and complex invariants. Prefer small aggregates with eventual consistency between them.
3. **One transaction per aggregate.** Modify only one aggregate per transaction. Use domain events for cross-aggregate coordination.
4. **Protect invariants within the aggregate boundary.** Business rules that span multiple aggregates must be handled via eventual consistency (domain events, sagas).

## Aggregate Design Example

```
// GOOD: Small aggregates, reference by ID, domain events

public class Order    // Aggregate root
{
    public OrderId Id { get; }
    private List<OrderLine> _lines = new();

    public void AddLine(ProductId productId, int quantity, Money price)
    {
        if (_lines.Count >= 20)
            throw new TooManyLinesException();
        _lines.Add(new OrderLine(productId, quantity, price));
        AddDomainEvent(new OrderLineAdded(Id, productId, quantity));
    }

    public void Confirm()
    {
        if (!_lines.Any()) throw new EmptyOrderException();
        Status = OrderStatus.Confirmed;
        AddDomainEvent(new OrderConfirmed(Id, TotalAmount));
    }
}

public class Inventory    // Separate aggregate
{
    public ProductId ProductId { get; }
    public int AvailableQuantity { get; private set; }

    // Reacts to OrderConfirmed event (eventual consistency)
    public void Reserve(int quantity)
    {
        if (AvailableQuantity < quantity)
            throw new InsufficientStockException();
        AvailableQuantity -= quantity;
        AddDomainEvent(new StockReserved(ProductId, quantity));
    }
}
```

## Domain Events
Events that represent something significant that happened in the domain. Domain events enable loose coupling between aggregates and bounded contexts.

**Naming convention:** Past tense, describing what happened -- `OrderPlaced`, `PaymentReceived`, `ShipmentDispatched`.

See `dev-architecture-event-driven` for event sourcing and event-driven architecture patterns.

## Repositories
Provide collection-like access to aggregates. One repository per aggregate root. Repositories abstract the persistence mechanism.

```
public interface IOrderRepository
{
    Task<Order?> GetById(OrderId id);
    Task Save(Order order);
    Task Delete(OrderId id);
    // No query methods here -- queries belong in the read model (CQRS)
}
```

## Domain Services
Operations that don't naturally belong to any single entity or value object. Domain services are stateless and express domain logic.

```
// Pricing logic that spans multiple aggregates
public class PricingService
{
    public Money CalculateDiscount(
        Order order, CustomerTier tier, IReadOnlyList<Promotion> activePromotions)
    {
        // Complex pricing logic that doesn't belong in Order or Customer
    }
}
```

## Application Services
Orchestrate use cases by coordinating domain objects, repositories, and infrastructure concerns. Application services are the entry point from the outside world (API controllers, message handlers) into the domain.

```
public class PlaceOrderHandler
{
    public async Task Handle(PlaceOrderCommand command)
    {
        var order = new Order(command.CustomerId);
        foreach (var item in command.Items)
            order.AddLine(item.ProductId, item.Quantity, item.Price);
        order.Confirm();
        await _orderRepository.Save(order);
        await _eventPublisher.Publish(order.DomainEvents);
    }
}
```

## Factories
Encapsulate complex aggregate creation logic. Use factories when object construction involves business rules, validation, or coordination.
