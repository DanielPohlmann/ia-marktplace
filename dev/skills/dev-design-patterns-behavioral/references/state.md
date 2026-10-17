<!-- Part of the dev-design-patterns-behavioral skill. Loaded on demand from SKILL.md. -->

# 7. State

## Intent
Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Structure

```
┌──────────────────┐        ┌──────────────────┐
│    Context        │───────▶│     State         │
├──────────────────┤ has-a  │    (interface)    │
│ - state: State    │        ├──────────────────┤
│ + request()       │        │ + handle(ctx)     │
└──────────────────┘        └──────┬───────────┘
                                   │ implements
                            ┌──────┼──────────┐
                            ▼      ▼          ▼
                     ┌─────────┐┌─────────┐┌─────────┐
                     │ StateA   ││ StateB   ││ StateC   │
                     └─────────┘└─────────┘└─────────┘
```

## Participants
- **Context** — maintains an instance of a ConcreteState subclass that defines the current state
- **State** — defines an interface for encapsulating the behavior associated with a particular state
- **ConcreteState** — each subclass implements behavior associated with a state of the Context

## When to Use
- An object's behavior depends on its state, and it must change behavior at runtime
- Operations have large multipart conditional statements that depend on the object's state

## TypeScript Example

```typescript
// State interface
interface OrderState {
  next(order: Order): void;
  cancel(order: Order): void;
  toString(): string;
}

// Context
class Order {
  private state: OrderState;

  constructor(public readonly id: string) {
    this.state = new PendingState();
  }

  setState(state: OrderState): void {
    console.log(`  Order ${this.id}: ${this.state} -> ${state}`);
    this.state = state;
  }

  next(): void { this.state.next(this); }
  cancel(): void { this.state.cancel(this); }
  getStatus(): string { return this.state.toString(); }
}

// Concrete states
class PendingState implements OrderState {
  next(order: Order): void { order.setState(new PaidState()); }
  cancel(order: Order): void { order.setState(new CancelledState()); }
  toString(): string { return "PENDING"; }
}

class PaidState implements OrderState {
  next(order: Order): void { order.setState(new ShippedState()); }
  cancel(order: Order): void {
    console.log(`  Refunding order ${order.id}...`);
    order.setState(new CancelledState());
  }
  toString(): string { return "PAID"; }
}

class ShippedState implements OrderState {
  next(order: Order): void { order.setState(new DeliveredState()); }
  cancel(order: Order): void {
    console.log(`  Cannot cancel — order ${order.id} already shipped`);
  }
  toString(): string { return "SHIPPED"; }
}

class DeliveredState implements OrderState {
  next(order: Order): void {
    console.log(`  Order ${order.id} already delivered`);
  }
  cancel(order: Order): void {
    console.log(`  Cannot cancel — order ${order.id} already delivered`);
  }
  toString(): string { return "DELIVERED"; }
}

class CancelledState implements OrderState {
  next(order: Order): void {
    console.log(`  Order ${order.id} is cancelled — no further transitions`);
  }
  cancel(order: Order): void {
    console.log(`  Order ${order.id} is already cancelled`);
  }
  toString(): string { return "CANCELLED"; }
}

// Usage
const order = new Order("ORD-001");
order.next();   // PENDING -> PAID
order.next();   // PAID -> SHIPPED
order.cancel(); // Cannot cancel — already shipped
order.next();   // SHIPPED -> DELIVERED
```

---
