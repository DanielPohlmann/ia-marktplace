# Entity-Relationship Diagrams Rules

Best practices and rules for Entity-Relationship Diagrams.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with a conceptual ERD. | MEDIUM | [`erd-start-with-a-conceptual-erd.md`](erd-start-with-a-conceptual-erd.md) |
| 2 | Normalize to 3NF by default. | MEDIUM | [`erd-normalize-to-3nf-by-default.md`](erd-normalize-to-3nf-by-default.md) |
| 3 | Use Crow's Foot notation for implementation. | MEDIUM | [`erd-use-crow-s-foot-notation-for-implementation.md`](erd-use-crow-s-foot-notation-for-implementation.md) |
| 4 | Use Chen notation for teaching and conceptual design. | MEDIUM | [`erd-use-chen-notation-for-teaching-and-conceptual-design.md`](erd-use-chen-notation-for-teaching-and-conceptual-design.md) |
| 5 | Resolve many-to-many relationships. | CRITICAL | [`erd-resolve-many-to-many-relationships.md`](erd-resolve-many-to-many-relationships.md) |
| 6 | Name entities as singular nouns. | MEDIUM | [`erd-name-entities-as-singular-nouns.md`](erd-name-entities-as-singular-nouns.md) |
| 7 | Name relationships with verbs. | MEDIUM | [`erd-name-relationships-with-verbs.md`](erd-name-relationships-with-verbs.md) |
| 8 | Mark all keys explicitly. | CRITICAL | [`erd-mark-all-keys-explicitly.md`](erd-mark-all-keys-explicitly.md) |
| 9 | Document cardinality from both directions. | MEDIUM | [`erd-document-cardinality-from-both-directions.md`](erd-document-cardinality-from-both-directions.md) |
| 10 | Use Mermaid for ERDs in documentation. | MEDIUM | [`erd-use-mermaid-for-erds-in-documentation.md`](erd-use-mermaid-for-erds-in-documentation.md) |
| 11 | Validate with sample data. | HIGH | [`erd-validate-with-sample-data.md`](erd-validate-with-sample-data.md) |
| 12 | Separate read models from write models. | MEDIUM | [`erd-separate-read-models-from-write-models.md`](erd-separate-read-models-from-write-models.md) |

---

---
title: "Document cardinality from both directions."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Document cardinality from both directions.

"A CUSTOMER places zero or many ORDERs" AND "An ORDER is placed by exactly one CUSTOMER." Both sides matter.

---

---
title: "Mark all keys explicitly."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Mark all keys explicitly.

Every entity must have a PK. Every relationship should be traceable through FKs. Mark nullable vs required for each attribute.

---

---
title: "Name entities as singular nouns."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Name entities as singular nouns.

Use `CUSTOMER` not `CUSTOMERS`. The entity represents the concept, not a collection.

---

---
title: "Name relationships with verbs."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Name relationships with verbs.

"places", "contains", "belongs to" — not "has" (which is vague) or "link" (which is meaningless).

---

---
title: "Normalize to 3NF by default."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Normalize to 3NF by default.

Denormalize only when you have a measured performance problem. Premature denormalization causes data integrity issues.

---

---
title: "Resolve many-to-many relationships."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Resolve many-to-many relationships.

Every M:N relationship must be resolved into two 1:N relationships via an associative (junction) entity before physical implementation.

---

---
title: "Separate read models from write models."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Separate read models from write models.

In CQRS or event-sourced systems, the write-side schema should be normalized, while the read-side can be denormalized for query performance.

---

---
title: "Start with a conceptual ERD."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Start with a conceptual ERD.

Identify entities and relationships before worrying about attributes, types, or keys. Get agreement on the conceptual model first.

---

---
title: "Use Chen notation for teaching and conceptual design."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Use Chen notation for teaching and conceptual design.

Its explicit shapes make it easier to explain ER concepts to non-technical stakeholders.

---

---
title: "Use Crow's Foot notation for implementation."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Use Crow's Foot notation for implementation.

It is the most widely supported notation in database tools and maps directly to physical schemas.

---

---
title: "Use Mermaid for ERDs in documentation."
impact: MEDIUM
impactDescription: "general best practice"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Use Mermaid for ERDs in documentation.

Mermaid ERD syntax renders natively on GitHub, GitLab, and most documentation platforms, keeping your data models version-controlled alongside code.

---

---
title: "Validate with sample data."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: erd, specs, diagramming, database-schema-design, data-modeling, entity-relationship-diagrams
---

## Validate with sample data.

After drawing an ERD, populate it with 3-5 rows of realistic sample data per entity. This quickly reveals modeling errors.
