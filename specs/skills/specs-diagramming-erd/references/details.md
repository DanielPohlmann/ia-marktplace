<!-- Part of the specs-diagramming-erd skill. Loaded on demand from SKILL.md. -->

# Entity-Relationship Diagrams (ERD) — details

## Attributes

Attributes describe properties of an entity.

| Attribute Type | Description | Notation |
|---------------|-------------|----------|
| **Primary Key (PK)** | Uniquely identifies each entity instance | Underlined or marked PK |
| **Foreign Key (FK)** | References a primary key in another entity | Marked FK |
| **Required (NOT NULL)** | Must have a value for every instance | Typically no special mark (default) |
| **Nullable** | May have no value | Marked with optional indicator or (NULL) |
| **Composite** | Made up of multiple sub-attributes | e.g., Address = Street + City + State + Zip |
| **Derived** | Computed from other attributes | e.g., Age derived from BirthDate, shown with dashed oval or / prefix |
| **Multi-valued** | Can hold multiple values for one entity | e.g., PhoneNumbers (modeled as a separate table in relational design) |

## Chen Notation

Chen notation (original ER notation by Peter Chen, 1976) uses geometric shapes:

```
┌───────────┐          ┌──────────────┐         ┌───────────┐
│           │          │              │         │           │
│ CUSTOMER  │══════════◇   places     ◇════════│  ORDER    │
│           │  1       │              │   N     │           │
└─────┬─────┘          └──────────────┘         └─────┬─────┘
      │                                               │
   ┌──┴──┐                                        ┌──┴──┐
   │Name │                                        │Date │
   └─────┘                                        └─────┘
  (attribute)                                    (attribute)

   ┌─────────┐
   │_CustID_ │   ← underlined = Primary Key
   └─────────┘

Shapes:
  Rectangle     = Entity
  Diamond       = Relationship
  Oval          = Attribute
  Double rect   = Weak Entity
  Double diamond= Identifying Relationship (for weak entities)
  Double oval   = Multi-valued Attribute
  Dashed oval   = Derived Attribute
```

### Chen Notation Cardinality
- Numbers (1, N, M) are placed on the lines connecting entities to the relationship diamond
- Double lines indicate total (mandatory) participation
- Single lines indicate partial (optional) participation

## Crow's Foot Notation

Crow's Foot notation (also called IE notation or Martin notation) is the most widely used notation in database tools and is more compact than Chen notation.

### Crow's Foot Symbols

```
Cardinality Symbols (at the end of relationship lines):

    ──────||    Exactly one (mandatory one)
    ──────|O    Zero or one (optional one)
    ──────|<    One or many (mandatory many)
    ──────O<    Zero or many (optional many)

Where:
    ||  = "one and only one" (two bars)
    |O  = "zero or one" (bar + circle)
    |<  = "one or many" (bar + crow's foot)
    O<  = "zero or many" (circle + crow's foot)
```

### Crow's Foot Reading Convention

Read relationships from each entity's perspective:

```
┌──────────┐                      ┌──────────┐
│ CUSTOMER │ ──────||────────O< ──│  ORDER   │
└──────────┘                      └──────────┘

Reading left-to-right:
  "A CUSTOMER places zero or many ORDERs"

Reading right-to-left:
  "An ORDER is placed by exactly one CUSTOMER"
```

### Crow's Foot Full Example

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│  CUSTOMER    │         │   ORDER      │         │  PRODUCT     │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ PK CustomerID│──||──O<─│ PK OrderID   │         │ PK ProductID │
│    Name      │         │ FK CustomerID│   ┌─O<──│    Name      │
│    Email     │         │    OrderDate │   │     │    Price     │
│    Phone     │         │    Total     │   │     │    Category  │
└──────────────┘         └──────┬───────┘   │     └──────────────┘
                                │           │
                         ┌──────┴───────┐   │
                         │ ORDER_ITEM   │   │
                         ├──────────────┤   │
                         │ PK,FK OrderID│──||┘
                         │ PK,FK ProdID │
                         │    Quantity  │
                         │    UnitPrice │
                         └──────────────┘

Resolves the M:N between ORDER and PRODUCT
via the associative entity ORDER_ITEM.
```

## Design Process

A recommended workflow for database design using ERDs:

```
1. Identify Entities
   │  What are the core "things" the system manages?
   ▼
2. Define Attributes
   │  What properties describe each entity? Identify PKs.
   ▼
3. Identify Relationships
   │  How are entities related? Determine cardinality.
   ▼
4. Draw Conceptual ERD
   │  Entities and relationships only, no attributes.
   ▼
5. Refine to Logical ERD
   │  Add attributes, PKs, FKs, resolve M:N via junction tables.
   ▼
6. Normalize (1NF → 2NF → 3NF)
   │  Eliminate redundancy and anomalies.
   ▼
7. Denormalize Selectively
   │  Add calculated columns or merge tables for performance.
   ▼
8. Create Physical ERD
   │  Specify data types, indexes, constraints for target DBMS.
```
