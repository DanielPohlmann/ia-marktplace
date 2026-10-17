<!-- Part of the specs-diagramming-erd skill. Loaded on demand from SKILL.md. -->

# Mermaid ERD Syntax

Mermaid provides native support for ER diagrams using Crow's Foot-style notation.

## Relationship Symbols

| Symbol | Meaning |
|--------|---------|
| `\|\|` | Exactly one |
| `o\|` | Zero or one |
| `\|{` | One or many |
| `o{` | Zero or many |

Relationships are written as: `EntityA <relationship> EntityB : "label"`

## Attribute Types

Mermaid ERD attributes support type, name, and constraint markers:

```
erDiagram
    ENTITY {
        type attribute_name PK "comment"
        type attribute_name FK
        type attribute_name UK "unique key"
    }
```

## Complete Mermaid ERD Example: E-Commerce Database

```mermaid
erDiagram
    CUSTOMER {
        int customer_id PK
        string first_name
        string last_name
        string email UK
        string phone
        date created_at
    }

    ADDRESS {
        int address_id PK
        int customer_id FK
        string street
        string city
        string state
        string zip_code
        string country
        boolean is_primary
    }

    ORDER {
        int order_id PK
        int customer_id FK
        int shipping_address_id FK
        datetime order_date
        string status
        decimal total_amount
    }

    ORDER_ITEM {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
        decimal line_total
    }

    PRODUCT {
        int product_id PK
        int category_id FK
        string name
        string description
        decimal price
        int stock_quantity
        string sku UK
    }

    CATEGORY {
        int category_id PK
        int parent_category_id FK
        string name
        string description
    }

    PAYMENT {
        int payment_id PK
        int order_id FK
        string payment_method
        decimal amount
        string status
        datetime payment_date
        string transaction_ref UK
    }

    REVIEW {
        int review_id PK
        int product_id FK
        int customer_id FK
        int rating
        string comment
        datetime review_date
    }

    CUSTOMER ||--o{ ADDRESS : "has"
    CUSTOMER ||--o{ ORDER : "places"
    CUSTOMER ||--o{ REVIEW : "writes"
    ORDER ||--|{ ORDER_ITEM : "contains"
    ORDER ||--o{ PAYMENT : "paid via"
    ORDER }o--|| ADDRESS : "shipped to"
    ORDER_ITEM }o--|| PRODUCT : "references"
    PRODUCT ||--o{ REVIEW : "receives"
    PRODUCT }o--|| CATEGORY : "belongs to"
    CATEGORY ||--o{ CATEGORY : "parent of"
```

## Mermaid ERD Relationship Syntax Reference

```
erDiagram
    %% One-to-one (both mandatory)
    PERSON ||--|| PASSPORT : "holds"

    %% One-to-many (mandatory on both sides)
    DEPARTMENT ||--|{ EMPLOYEE : "employs"

    %% One-to-many (optional on many side)
    CUSTOMER ||--o{ ORDER : "places"

    %% Many-to-many (resolved via junction table)
    STUDENT }o--o{ COURSE : "enrolls in"

    %% One-to-zero-or-one
    EMPLOYEE ||--o| PARKING_SPOT : "assigned"
```
