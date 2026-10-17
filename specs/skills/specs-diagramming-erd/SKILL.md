---
name: specs-diagramming-erd
description: Use when drawing entity-relationship diagrams for database design. USE FOR: entities, attributes, cardinality, Chen and Crow's Foot notation, normalization, logical vs physical models, Mermaid erDiagram. DO NOT USE FOR: application architecture (use specs-diagramming-c4-diagrams), behavior (use specs-diagramming-uml), schema trade-offs (use dev-backend-data-modeling).
---

# Entity-Relationship Diagrams (ERD)

## Overview
Entity-Relationship Diagrams model the structure of data by defining entities, their attributes, and the relationships between them. ERDs are the foundational tool for database design, used from early conceptual modeling through to physical schema implementation.

ERDs operate at three levels of abstraction:
- **Conceptual ERD** — High-level entities and relationships, no attributes. Used for business communication.
- **Logical ERD** — Entities, attributes, primary keys, and relationships with cardinality. Database-agnostic.
- **Physical ERD** — Table names, column types, indexes, constraints. Maps directly to a specific DBMS.

## Entity Types

An entity represents a "thing" or concept about which data is stored.

| Entity Type | Description | Example |
|------------|-------------|---------|
| **Strong Entity** | Exists independently, has its own primary key | Customer, Product, Order |
| **Weak Entity** | Cannot exist without a related strong entity; uses a partial key combined with the owner's key | OrderLineItem (depends on Order), DependentPerson (depends on Employee) |
| **Associative Entity** | Resolves a many-to-many relationship into a table with its own attributes | Enrollment (between Student and Course, with grade attribute) |

## Relationships

Relationships connect entities and describe how they are associated.

### Relationship Types

| Type | Description | Example |
|------|-------------|---------|
| **One-to-One (1:1)** | Each instance of A is associated with exactly one instance of B | Person 1:1 Passport |
| **One-to-Many (1:N)** | Each instance of A is associated with zero or more instances of B | Customer 1:N Order |
| **Many-to-Many (M:N)** | Each instance of A can be associated with many instances of B and vice versa | Student M:N Course |

### Participation (Optionality)

| Participation | Description | Notation |
|--------------|-------------|----------|
| **Mandatory (Total)** | Every entity instance must participate in the relationship | Double line (Chen) or bar (Crow's Foot) |
| **Optional (Partial)** | An entity instance may or may not participate | Single line (Chen) or circle (Crow's Foot) |

### Cardinality and Participation Combined

```
Cardinality:     Minimum .. Maximum

Examples:
  0..1    Zero or one (optional, at most one)
  1..1    Exactly one (mandatory, at most one)
  0..*    Zero or many (optional, unbounded)
  1..*    One or many (mandatory, at least one)
```

## Chen vs Crow's Foot Comparison

| Aspect | Chen Notation | Crow's Foot Notation |
|--------|--------------|---------------------|
| **Origin** | Peter Chen, 1976 | James Martin / Clive Finkelstein |
| **Shapes** | Rectangles, diamonds, ovals | Rectangles with line-end symbols |
| **Readability** | More explicit, good for teaching | More compact, good for production schemas |
| **Attributes** | Shown as ovals connected to entities | Listed inside entity rectangles |
| **Relationships** | Named diamond between entities | Named line between entities |
| **Cardinality** | Numbers on lines (1, N, M) | Symbols on line ends (crow's foot, bar, circle) |
| **Tool support** | Academic, some modeling tools | Most database tools (ERwin, MySQL Workbench, dbdiagram.io, Mermaid) |
| **Best for** | Conceptual modeling, teaching | Logical and physical modeling, implementation |

## Best Practices
- **Start with a conceptual ERD.** Identify entities and relationships before worrying about attributes, types, or keys. Get agreement on the conceptual model first.
- **Normalize to 3NF by default.** Denormalize only when you have a measured performance problem. Premature denormalization causes data integrity issues.
- **Use Crow's Foot notation for implementation.** It is the most widely supported notation in database tools and maps directly to physical schemas.
- **Use Chen notation for teaching and conceptual design.** Its explicit shapes make it easier to explain ER concepts to non-technical stakeholders.
- **Resolve many-to-many relationships.** Every M:N relationship must be resolved into two 1:N relationships via an associative (junction) entity before physical implementation.
- **Name entities as singular nouns.** Use `CUSTOMER` not `CUSTOMERS`. The entity represents the concept, not a collection.
- **Name relationships with verbs.** "places", "contains", "belongs to" — not "has" (which is vague) or "link" (which is meaningless).
- **Mark all keys explicitly.** Every entity must have a PK. Every relationship should be traceable through FKs. Mark nullable vs required for each attribute.
- **Document cardinality from both directions.** "A CUSTOMER places zero or many ORDERs" AND "An ORDER is placed by exactly one CUSTOMER." Both sides matter.
- **Use Mermaid for ERDs in documentation.** Mermaid ERD syntax renders natively on GitHub, GitLab, and most documentation platforms, keeping your data models version-controlled alongside code.
- **Validate with sample data.** After drawing an ERD, populate it with 3-5 rows of realistic sample data per entity. This quickly reveals modeling errors.
- **Separate read models from write models.** In CQRS or event-sourced systems, the write-side schema should be normalized, while the read-side can be denormalized for query performance.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/mermaid-erd-syntax.md](references/mermaid-erd-syntax.md) | Mermaid ERD Syntax — Relationship Symbols, Attribute Types, Complete Mermaid ERD Example: E-Commerce Database, Mermaid ERD Relationship Syntax Reference |
| [references/normalization.md](references/normalization.md) | Normalization — First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), Summary of Normal Forms, When to Denormalize |
| [references/details.md](references/details.md) | Attributes; Chen Notation; Crow's Foot Notation; Design Process |

## References

- [Entity-Relationship Model — Wikipedia](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
- [Peter Chen — The Entity-Relationship Model (Original Paper)](https://dl.acm.org/doi/10.1145/320434.320440)

See references/rules.md for the full rule catalog.
