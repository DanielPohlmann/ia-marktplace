# SOLID — Worked Examples

Violation → correction for each principle. Examples are in TypeScript; the shape is the same in C#, Java or Kotlin.

---

## S — Single Responsibility

### Violation: two actors, one class

```typescript
class Invoice {
    // Rules owned by the billing team
    total(): number {
        return round(this.items.reduce((sum, i) => sum + i.price * i.qty, 0));
    }

    // Layout owned by the tax authority's specification
    toTaxDocument(): string {
        return this.items
            .map(i => `${i.code};${round(i.price * i.qty)}`)
            .join("\n");
    }
}

// Shared helper — the trap
function round(value: number): number {
    return Math.round(value * 100) / 100;
}
```

The tax authority changes its rounding rule to truncation. A developer edits `round()` to satisfy the tax document — and every customer total silently changes. Two **actors** (billing and the tax authority) request changes for different reasons, and the shared code couples them.

### Correction

```typescript
class InvoiceTotals {
    total(invoice: Invoice): number { /* billing rounding */ }
}

class TaxDocumentRenderer {
    render(invoice: Invoice): string { /* tax-authority rounding */ }
}
```

Each class now changes only when its own actor asks. `Invoice` keeps the data and the invariants that both actors agree on.

### Technical layers are not actors

Splitting a `createUser` method into validator / repository / email sender / logger is often a good separation of concerns, but it is not what SRP measures. Use the actor question to decide **which** split matters: if the same person or team requests every change to validation, persistence and the welcome email, one cohesive class with private methods may be the simpler design.

---

## O — Open/Closed

### Violation

```typescript
class DiscountCalculator {
    calculate(order: Order): number {
        switch (order.customerType) {
            case "regular": return 0;
            case "premium": return order.total * 0.1;
            case "vip":     return order.total * 0.2;
            default:        return 0;
        }
    }
}
```

Every new customer type edits the calculator and every test around it.

### Correction — and where the choice now lives

```typescript
interface DiscountStrategy {
    calculate(order: Order): number;
}

class RegularDiscount implements DiscountStrategy { calculate() { return 0; } }
class PremiumDiscount implements DiscountStrategy { calculate(o: Order) { return o.total * 0.1; } }
class VipDiscount     implements DiscountStrategy { calculate(o: Order) { return o.total * 0.2; } }

// The selection did not disappear — it moved to one place at the edge
const discountByCustomerType: Record<CustomerType, DiscountStrategy> = {
    regular: new RegularDiscount(),
    premium: new PremiumDiscount(),
    vip:     new VipDiscount(),
};

class DiscountCalculator {
    constructor(private readonly strategies: Record<CustomerType, DiscountStrategy>) {}

    calculate(order: Order): number {
        return this.strategies[order.customerType].calculate(order);
    }
}
```

Adding a customer type now means a new class plus one registry entry, and the calculator never changes. The registry (or a factory, or the DI container) is the single place that still knows every variant — that is expected. The goal is one such place, not zero.

---

## L — Liskov Substitution

### Violation

```typescript
class Rectangle {
    constructor(protected width: number, protected height: number) {}
    setWidth(w: number) { this.width = w; }
    setHeight(h: number) { this.height = h; }
    area() { return this.width * this.height; }
}

class Square extends Rectangle {
    setWidth(w: number)  { this.width = w; this.height = w; }
    setHeight(h: number) { this.width = h; this.height = h; }
}

function resize(rect: Rectangle) {
    rect.setWidth(5);
    rect.setHeight(4);
    // Callers of Rectangle expect 20; a Square returns 16
}
```

### Correction

```typescript
interface Shape { area(): number; }

class Rectangle implements Shape {
    constructor(private readonly width: number, private readonly height: number) {}
    area() { return this.width * this.height; }
}

class Square implements Shape {
    constructor(private readonly side: number) {}
    area() { return this.side * this.side; }
}
```

### A more common real-world violation

```csharp
public class FileStorage {
    public virtual void Save(string path, byte[] data) { /* accepts any size */ }
}

public class CloudStorage : FileStorage {
    public override void Save(string path, byte[] data) {
        if (data.Length > 5_000_000)
            throw new ArgumentException("Max 5 MB");   // stronger precondition
        // ...
    }
}
```

Any caller written against `FileStorage` can now fail when handed a `CloudStorage`. Either the base contract states the limit, or the two are not substitutable and should not share a hierarchy.

---

## I — Interface Segregation

### Violation

```typescript
interface Printer {
    print(doc: Document): void;
    scan(doc: Document): void;
    fax(doc: Document): void;
}

class SimplePrinter implements Printer {
    print(doc: Document) { /* works */ }
    scan(): void { throw new Error("Not supported"); }
    fax(): void  { throw new Error("Not supported"); }
}
```

### Correction

```typescript
interface Printable { print(doc: Document): void; }
interface Scannable { scan(doc: Document): void; }
interface Faxable   { fax(doc: Document): void; }

class SimplePrinter implements Printable { print(doc: Document) { /* works */ } }

class MultiFunctionPrinter implements Printable, Scannable, Faxable {
    print(doc: Document) { /* works */ }
    scan(doc: Document)  { /* works */ }
    fax(doc: Document)   { /* works */ }
}
```

---

## D — Dependency Inversion

### Violation

```typescript
class OrderService {
    private readonly db = new MySqlDatabase();   // concrete infrastructure inside policy

    createOrder(order: Order) {
        this.db.save(order.toRecord());
    }
}
```

`OrderService` cannot be tested without MySQL and cannot outlive a database change.

### Step 1 — own the dependency

```typescript
class OrderRepository {
    constructor(private readonly db: MySqlDatabase) {}
    save(order: Order) { /* mapping lives here */ }
}

class OrderService {
    constructor(private readonly repo: OrderRepository) {}
    createOrder(order: Order) { this.repo.save(order); }
}
```

The service no longer constructs infrastructure, and the mapping has one home. This is often enough.

### Step 2 — invert, when there is a reason

```typescript
interface OrderRepository {             // owned by the high-level module
    save(order: Order): Promise<void>;
}

class MySqlOrderRepository implements OrderRepository { /* ... */ }

const service = new OrderService(new MySqlOrderRepository());   // composition root
```

Take step 2 when you need to fake the dependency in tests, when a second implementation exists, or when the abstraction marks a module boundary. See the DIP section of `SKILL.md` for the full rule.
