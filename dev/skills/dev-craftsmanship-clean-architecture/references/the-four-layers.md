<!-- Part of the dev-craftsmanship-clean-architecture skill. Loaded on demand from SKILL.md. -->

# The Four Layers

## 1. Entities (Enterprise Business Rules)
Entities encapsulate the most general and high-level business rules. They are the least likely to change when something external changes. An Entity can be an object with methods, or a set of data structures and functions.

```typescript
// entities/Order.ts — no framework imports, no database references
class Order {
    private items: OrderItem[] = [];

    addItem(product: Product, quantity: number): void {
        if (quantity <= 0) throw new InvalidQuantityError(quantity);
        this.items.push(new OrderItem(product, quantity));
    }

    total(): Money {
        return this.items.reduce(
            (sum, item) => sum.add(item.subtotal()),
            Money.zero()
        );
    }

    canBeShipped(): boolean {
        return this.items.length > 0 && this.total().isPositive();
    }
}
```

## 2. Use Cases (Application Business Rules)
Use Cases contain application-specific business rules. They orchestrate the flow of data to and from the Entities and direct them to use their enterprise-wide rules.

```typescript
// use-cases/PlaceOrder.ts
interface OrderRepository {
    save(order: Order): Promise<void>;
}

interface PaymentGateway {
    charge(amount: Money, paymentMethod: PaymentMethod): Promise<PaymentResult>;
}

class PlaceOrder {
    constructor(
        private orderRepo: OrderRepository,
        private paymentGateway: PaymentGateway,
        private notifier: OrderNotifier
    ) {}

    async execute(request: PlaceOrderRequest): Promise<PlaceOrderResponse> {
        const order = new Order();
        for (const item of request.items) {
            order.addItem(item.product, item.quantity);
        }

        const paymentResult = await this.paymentGateway.charge(
            order.total(), request.paymentMethod
        );

        if (!paymentResult.isSuccessful()) {
            return PlaceOrderResponse.failed(paymentResult.reason());
        }

        await this.orderRepo.save(order);
        await this.notifier.orderPlaced(order);
        return PlaceOrderResponse.success(order.id());
    }
}
```

Note: `OrderRepository`, `PaymentGateway`, and `OrderNotifier` are **interfaces defined in this layer**. Their implementations live in the outer layers.

## 3. Interface Adapters (Controllers, Gateways, Presenters)
This layer converts data from the form most convenient for Use Cases and Entities to the form most convenient for some external agency (database, web, etc.).

```typescript
// adapters/controllers/OrderController.ts
class OrderController {
    constructor(private placeOrder: PlaceOrder) {}

    async handlePost(httpRequest: HttpRequest): Promise<HttpResponse> {
        const request = this.mapToPlaceOrderRequest(httpRequest.body);
        const response = await this.placeOrder.execute(request);
        return this.mapToHttpResponse(response);
    }

    private mapToPlaceOrderRequest(body: any): PlaceOrderRequest { /* ... */ }
    private mapToHttpResponse(result: PlaceOrderResponse): HttpResponse { /* ... */ }
}

// adapters/gateways/PostgresOrderRepository.ts
class PostgresOrderRepository implements OrderRepository {
    async save(order: Order): Promise<void> {
        const row = this.mapToRow(order);
        await this.db.query("INSERT INTO orders ...", row);
    }
}
```

## 4. Frameworks & Drivers
The outermost layer. This is where all the details go — the web framework, the database driver, the UI framework. This layer is glue code that connects the outer world to the inner architecture.

```typescript
// frameworks/express/routes.ts
import express from "express";
import { OrderController } from "../../adapters/controllers/OrderController";

const router = express.Router();
const controller = new OrderController(/* injected use case */);

router.post("/orders", (req, res) => controller.handlePost(req).then(r => res.status(r.status).json(r.body)));
```
