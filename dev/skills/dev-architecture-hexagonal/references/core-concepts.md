<!-- Part of the dev-architecture-hexagonal skill. Loaded on demand from SKILL.md. -->

# Core Concepts

## Ports (Interfaces)

Ports define the boundaries of the application. They are **interfaces** -- contracts that describe what the application can do (primary/driving) or what the application needs (secondary/driven).

| Port Type | Also Called | Direction | Purpose | Example |
|-----------|------------|-----------|---------|---------|
| **Primary Port** | Driving Port | Inbound | Defines what the app **offers** to the outside world | `IOrderService.PlaceOrder(...)` |
| **Secondary Port** | Driven Port | Outbound | Defines what the app **requires** from the outside world | `IOrderRepository.Save(...)`, `IPaymentGateway.Charge(...)` |

```
// Primary port — what the application offers
public interface IOrderService
{
    Task<OrderId> PlaceOrder(PlaceOrderCommand command);
    Task<OrderDto> GetOrder(OrderId id);
    Task CancelOrder(OrderId id);
}

// Secondary port — what the application needs
public interface IOrderRepository
{
    Task<Order?> FindById(OrderId id);
    Task Save(Order order);
}

// Secondary port — what the application needs
public interface IPaymentGateway
{
    Task<PaymentResult> Charge(Money amount, PaymentMethod method);
    Task Refund(PaymentId paymentId, Money amount);
}
```

## Adapters (Implementations)

Adapters are concrete implementations that connect ports to specific technologies. They live **outside** the domain core.

| Adapter Type | Also Called | Implements | Example |
|-------------|------------|------------|---------|
| **Primary Adapter** | Driving Adapter | Uses primary ports | REST controller, gRPC handler, CLI command, test harness |
| **Secondary Adapter** | Driven Adapter | Implements secondary ports | PostgreSQL repository, Stripe payment adapter, Kafka publisher |

```
// Primary adapter — REST controller drives the application
[ApiController]
public class OrdersController : ControllerBase
{
    private readonly IOrderService _orderService; // Primary port

    [HttpPost]
    public async Task<IActionResult> PlaceOrder(PlaceOrderRequest request)
    {
        var command = MapToCommand(request);
        var orderId = await _orderService.PlaceOrder(command);
        return Created($"/orders/{orderId}", new { orderId });
    }
}

// Secondary adapter — PostgreSQL implements the repository port
public class PostgresOrderRepository : IOrderRepository
{
    private readonly DbContext _db;

    public async Task<Order?> FindById(OrderId id)
    {
        return await _db.Orders
            .Include(o => o.Lines)
            .FirstOrDefaultAsync(o => o.Id == id);
    }

    public async Task Save(Order order) { ... }
}

// Secondary adapter — Stripe implements the payment port
public class StripePaymentGateway : IPaymentGateway
{
    private readonly StripeClient _stripe;

    public async Task<PaymentResult> Charge(Money amount, PaymentMethod method)
    {
        var intent = await _stripe.PaymentIntents.CreateAsync(...);
        return MapToResult(intent);
    }
}
```

## Driving vs. Driven Side

| Aspect | Driving (Primary) Side | Driven (Secondary) Side |
|--------|----------------------|------------------------|
| **Who initiates** | External actor drives the application | Application drives external systems |
| **Port direction** | Inbound (app receives calls) | Outbound (app makes calls) |
| **Adapter role** | Translates external input into domain calls | Translates domain calls into external system interactions |
| **Dependency direction** | Adapter depends on port (calls it) | Adapter implements port (the domain defines the interface) |
| **Examples** | HTTP controller, CLI, test, event consumer | Database, API client, message publisher, file system |
