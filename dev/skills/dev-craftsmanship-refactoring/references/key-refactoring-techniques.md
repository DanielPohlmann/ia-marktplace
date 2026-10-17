<!-- Part of the dev-craftsmanship-refactoring skill. Loaded on demand from SKILL.md. -->

# Key Refactoring Techniques

## Extract Method
The most common and most powerful refactoring. Turn a code fragment into a method whose name explains its purpose.

```typescript
// Before
function printOwing(invoice: Invoice): void {
    let outstanding = 0;

    console.log("***********************");
    console.log("**** Customer Owes ****");
    console.log("***********************");

    for (const order of invoice.orders) {
        outstanding += order.amount;
    }

    console.log(`name: ${invoice.customer}`);
    console.log(`amount: ${outstanding}`);
}

// After
function printOwing(invoice: Invoice): void {
    printBanner();
    const outstanding = calculateOutstanding(invoice);
    printDetails(invoice, outstanding);
}

function printBanner(): void {
    console.log("***********************");
    console.log("**** Customer Owes ****");
    console.log("***********************");
}

function calculateOutstanding(invoice: Invoice): number {
    return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice: Invoice, outstanding: number): void {
    console.log(`name: ${invoice.customer}`);
    console.log(`amount: ${outstanding}`);
}
```

## Inline Method
The inverse of Extract Method. When a method body is just as clear as its name, inline it.

```typescript
// Before
function getRating(): number {
    return moreThanFiveLateDeliveries() ? 2 : 1;
}

function moreThanFiveLateDeliveries(): boolean {
    return this.numberOfLateDeliveries > 5;
}

// After
function getRating(): number {
    return this.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

## Extract Class
When a class is doing the work of two, split it into two.

```typescript
// Before
class Person {
    name: string;
    officeAreaCode: string;
    officeNumber: string;

    telephoneNumber(): string {
        return `(${this.officeAreaCode}) ${this.officeNumber}`;
    }
}

// After
class Person {
    name: string;
    officeTelephone: TelephoneNumber;

    telephoneNumber(): string {
        return this.officeTelephone.toString();
    }
}

class TelephoneNumber {
    areaCode: string;
    number: string;

    toString(): string {
        return `(${this.areaCode}) ${this.number}`;
    }
}
```

## Move Method
When a method uses more features of another class than its own, move it to the class where it belongs.

```typescript
// Before — overdraftCharge uses Account's type more than it uses itself
class AccountType {
    isPremium: boolean;
}

class Account {
    type: AccountType;
    daysOverdrawn: number;

    overdraftCharge(): number {
        if (this.type.isPremium) {
            return 10 + (this.daysOverdrawn - 7) * 0.85;
        }
        return this.daysOverdrawn * 1.75;
    }
}

// After — moved to AccountType where it belongs
class AccountType {
    isPremium: boolean;

    overdraftCharge(daysOverdrawn: number): number {
        if (this.isPremium) {
            return 10 + (daysOverdrawn - 7) * 0.85;
        }
        return daysOverdrawn * 1.75;
    }
}

class Account {
    type: AccountType;
    daysOverdrawn: number;

    overdraftCharge(): number {
        return this.type.overdraftCharge(this.daysOverdrawn);
    }
}
```

## Replace Conditional with Polymorphism
Replace a conditional that dispatches on type with polymorphic method calls.

```typescript
// Before
function calculatePay(employee: Employee): number {
    switch (employee.type) {
        case "engineer":
            return employee.baseSalary;
        case "salesperson":
            return employee.baseSalary + employee.commission;
        case "manager":
            return employee.baseSalary + employee.bonus;
        default:
            throw new Error(`Unknown type: ${employee.type}`);
    }
}

// After
interface Employee {
    calculatePay(): number;
}

class Engineer implements Employee {
    constructor(private baseSalary: number) {}
    calculatePay(): number { return this.baseSalary; }
}

class Salesperson implements Employee {
    constructor(private baseSalary: number, private commission: number) {}
    calculatePay(): number { return this.baseSalary + this.commission; }
}

class Manager implements Employee {
    constructor(private baseSalary: number, private bonus: number) {}
    calculatePay(): number { return this.baseSalary + this.bonus; }
}
```

## Introduce Parameter Object
When several parameters always travel together, group them into an object.

```typescript
// Before
function amountInvoiced(startDate: Date, endDate: Date): number { /* ... */ }
function amountReceived(startDate: Date, endDate: Date): number { /* ... */ }
function amountOverdue(startDate: Date, endDate: Date): number { /* ... */ }

// After
class DateRange {
    constructor(readonly start: Date, readonly end: Date) {
        if (start > end) throw new Error("Start must precede end");
    }

    contains(date: Date): boolean {
        return date >= this.start && date <= this.end;
    }
}

function amountInvoiced(range: DateRange): number { /* ... */ }
function amountReceived(range: DateRange): number { /* ... */ }
function amountOverdue(range: DateRange): number { /* ... */ }
```

## Replace Temp with Query
Turn a temporary variable into a method call, so the logic is available to other methods and the code is more self-documenting.

```typescript
// Before
function calculateTotal(order: Order): number {
    const basePrice = order.quantity * order.itemPrice;
    const discountFactor = basePrice > 1000 ? 0.95 : 0.98;
    return basePrice * discountFactor;
}

// After
function calculateTotal(order: Order): number {
    return basePrice(order) * discountFactor(order);
}

function basePrice(order: Order): number {
    return order.quantity * order.itemPrice;
}

function discountFactor(order: Order): number {
    return basePrice(order) > 1000 ? 0.95 : 0.98;
}
```

---
