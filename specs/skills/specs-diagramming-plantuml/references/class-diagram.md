<!-- Part of the specs-diagramming-plantuml skill. Loaded on demand from SKILL.md. -->

# Class Diagram

```plantuml
@startuml
title Domain Model

abstract class Entity<T> {
    - id: T
    - createdAt: DateTime
    - updatedAt: DateTime
    + getId(): T
}

interface IRepository<T extends Entity> {
    + findById(id: ID): T
    + findAll(): List<T>
    + save(entity: T): T
    + delete(id: ID): void
}

class User extends Entity {
    - email: String
    - name: String
    - passwordHash: String
    + getEmail(): String
    + verifyPassword(raw: String): Boolean
}

class Order extends Entity {
    - status: OrderStatus
    - total: BigDecimal
    + getTotal(): BigDecimal
    + addItem(item: OrderItem): void
    + cancel(): void
}

class OrderItem {
    - quantity: int
    - unitPrice: BigDecimal
    + getSubtotal(): BigDecimal
}

enum OrderStatus {
    PENDING
    CONFIRMED
    SHIPPED
    DELIVERED
    CANCELLED
}

User "1" -- "0..*" Order : places >
Order "1" *-- "1..*" OrderItem : contains
Order --> OrderStatus

IRepository <|.. UserRepository
IRepository <|.. OrderRepository

@enduml
```

## Relationship Syntax

| Syntax | Meaning |
|--------|---------|
| `A <\|-- B` | B extends A (inheritance) |
| `A <\|.. B` | B implements A (realization) |
| `A *-- B` | A is composed of B (composition) |
| `A o-- B` | A aggregates B (aggregation) |
| `A --> B` | A depends on / uses B (directed association) |
| `A -- B` | Association |
| `A ..> B` | Dependency |
| `A -- "label" B` | Association with label |
| `A "1" -- "0..*" B` | Association with multiplicity |

## Visibility Modifiers

| Symbol | Visibility |
|--------|-----------|
| `+` | Public |
| `-` | Private |
| `#` | Protected |
| `~` | Package |
| `{abstract}` | Abstract method |
| `{static}` | Static member |
