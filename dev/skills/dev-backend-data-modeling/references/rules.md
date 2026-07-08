# Data Modeling & Database Architecture Rules

Best practices and rules for Data Modeling & Database Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Model around access patterns, not just entity relationships | MEDIUM | [`data-modeling-model-around-access-patterns-not-just-entity-relationships.md`](data-modeling-model-around-access-patterns-not-just-entity-relationships.md) |
| 2 | Start normalized (3NF) for relational databases;... | MEDIUM | [`data-modeling-start-normalized-3nf-for-relational-databases.md`](data-modeling-start-normalized-3nf-for-relational-databases.md) |
| 3 | In document databases, embed what you read together and... | MEDIUM | [`data-modeling-in-document-databases-embed-what-you-read-together-and.md`](data-modeling-in-document-databases-embed-what-you-read-together-and.md) |
| 4 | For DynamoDB and Cassandra, know your access patterns... | MEDIUM | [`data-modeling-for-dynamodb-and-cassandra-know-your-access-patterns.md`](data-modeling-for-dynamodb-and-cassandra-know-your-access-patterns.md) |
| 5 | Use expand-contract migrations for any schema change in a... | HIGH | [`data-modeling-use-expand-contract-migrations-for-any-schema-change-in-a.md`](data-modeling-use-expand-contract-migrations-for-any-schema-change-in-a.md) |
| 6 | Time-series data needs retention policies from day one | MEDIUM | [`data-modeling-time-series-data-needs-retention-policies-from-day-one.md`](data-modeling-time-series-data-needs-retention-policies-from-day-one.md) |
| 7 | In microservices, prefer database-per-service for... | LOW | [`data-modeling-in-microservices-prefer-database-per-service-for.md`](data-modeling-in-microservices-prefer-database-per-service-for.md) |

---

---
title: "For DynamoDB and Cassandra, know your access patterns..."
impact: MEDIUM
impactDescription: "general best practice"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## For DynamoDB and Cassandra, know your access patterns...

For DynamoDB and Cassandra, know your access patterns before designing the table schema -- retrofitting is painful.

---

---
title: "In document databases, embed what you read together and..."
impact: MEDIUM
impactDescription: "general best practice"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## In document databases, embed what you read together and...

In document databases, embed what you read together and reference what you update independently.

---

---
title: "In microservices, prefer database-per-service for..."
impact: LOW
impactDescription: "recommended but situational"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## In microservices, prefer database-per-service for...

In microservices, prefer database-per-service for independence, and accept the complexity of cross-service data coordination.

---

---
title: "Model around access patterns, not just entity relationships"
impact: MEDIUM
impactDescription: "general best practice"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## Model around access patterns, not just entity relationships

Model around access patterns, not just entity relationships. The best schema depends on how you query, not just what you store.

---

---
title: "Start normalized (3NF) for relational databases;..."
impact: MEDIUM
impactDescription: "general best practice"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## Start normalized (3NF) for relational databases;...

Start normalized (3NF) for relational databases; denormalize only when you have measured evidence of read-path bottlenecks.

---

---
title: "Time-series data needs retention policies from day one"
impact: MEDIUM
impactDescription: "general best practice"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## Time-series data needs retention policies from day one

Time-series data needs retention policies from day one. Without them, storage costs grow unbounded.

---

---
title: "Use expand-contract migrations for any schema change in a..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: data-modeling, dev, backend, database-schema-design, data-modeling-patterns, normalizationdenormalization
---

## Use expand-contract migrations for any schema change in a...

Use expand-contract migrations for any schema change in a system that requires zero-downtime deployments.
