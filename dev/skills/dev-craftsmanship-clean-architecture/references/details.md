<!-- Part of the dev-craftsmanship-clean-architecture skill. Loaded on demand from SKILL.md. -->

# Clean Architecture — details

## The Concentric Circles

```
┌─────────────────────────────────────────────────────────┐
│                 Frameworks & Drivers                     │
│      Web, UI, DB, Devices, External Interfaces          │
│  ┌─────────────────────────────────────────────────┐    │
│  │            Interface Adapters                    │    │
│  │    Controllers, Gateways, Presenters            │    │
│  │  ┌─────────────────────────────────────────┐    │    │
│  │  │          Application Business Rules      │    │    │
│  │  │              (Use Cases)                 │    │    │
│  │  │  ┌─────────────────────────────────┐    │    │    │
│  │  │  │  Enterprise Business Rules      │    │    │    │
│  │  │  │        (Entities)               │    │    │    │
│  │  │  └─────────────────────────────────┘    │    │    │
│  │  └─────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘

         Dependencies point INWARD  ──────>
         Nothing in an inner circle can know about
         anything in an outer circle.
```

## The Dependency Rule

> Source code dependencies must point only inward, toward higher-level policies.

- **Entities** know nothing about Use Cases, Adapters, or Frameworks.
- **Use Cases** know about Entities, but nothing about Controllers, the Web, or the Database.
- **Interface Adapters** know about Use Cases, but not about which framework delivers HTTP requests.
- **Frameworks & Drivers** are the outermost layer and may know about everything inward, but inner layers never reference them.

The rule is absolute: **names declared in an outer circle must not be mentioned in an inner circle.** This includes functions, classes, variables, and any other software entity.

## Crossing Boundaries

When control flow needs to go from an inner layer to an outer layer (e.g., a Use Case needs to call a Repository), apply the **Dependency Inversion Principle**:

1. Define an **interface** in the inner layer (Use Cases).
2. Implement that interface in the outer layer (Adapters/Frameworks).
3. Use dependency injection to provide the implementation at runtime.

```
Use Case Layer           Adapter Layer
┌──────────────┐         ┌─────────────────────────┐
│ PlaceOrder   │         │ PostgresOrderRepository  │
│              │         │                          │
│ uses ──> OrderRepository <── implements           │
│ (interface)  │         │                          │
└──────────────┘         └─────────────────────────┘

Source code dependency: Adapter depends on Use Case (points inward).
Control flow: Use Case calls Adapter at runtime (points outward).
```

This is the key insight: **the source code dependency opposes the flow of control** at the boundary, achieved through polymorphism.

## The Humble Object Pattern

The Humble Object pattern splits a behavior into two parts:
1. A **humble** part that is hard to test (it touches the framework, UI, or database).
2. A **testable** part that contains all the interesting logic.

The humble part delegates immediately to the testable part with as little logic as possible.

**Example — Presenter / ViewModel:**

```typescript
// The testable part — pure logic, no UI dependency
class OrderPresenter {
    present(order: Order): OrderViewModel {
        return {
            orderId: order.id().toString(),
            totalDisplay: order.total().formatAsCurrency(),
            itemCount: `${order.items().length} item(s)`,
            canShip: order.canBeShipped(),
            statusColor: order.canBeShipped() ? "green" : "gray",
        };
    }
}

// The humble part — thin UI glue
class OrderView {
    constructor(private presenter: OrderPresenter) {}

    render(order: Order): void {
        const vm = this.presenter.present(order);
        document.getElementById("total").textContent = vm.totalDisplay;
        document.getElementById("status").style.color = vm.statusColor;
    }
}
```

The `OrderPresenter` is trivially testable. The `OrderView` is so thin that it barely needs testing.

## Boundaries

Boundaries are the lines you draw in the system to separate things that matter from things that are details. Every boundary follows the Dependency Rule.

**Identifying boundaries:**
- Between business rules and the database
- Between business rules and the UI
- Between business rules and external services
- Between independently deployable components
- Between teams or organizational units

**Boundary-crossing rule:** Data that crosses a boundary should be in the form most convenient for the inner layer. The outer layer is responsible for converting its data into the form the inner layer expects.

```typescript
// The inner layer defines what it needs
interface PlaceOrderRequest {
    items: Array<{ productId: string; quantity: number }>;
    paymentMethod: PaymentMethod;
}

// The outer layer maps HTTP/JSON into that format
function mapHttpBodyToRequest(body: any): PlaceOrderRequest {
    return {
        items: body.lineItems.map((li: any) => ({
            productId: li.sku,
            quantity: parseInt(li.qty, 10),
        })),
        paymentMethod: parsePaymentMethod(body.payment),
    };
}
```
