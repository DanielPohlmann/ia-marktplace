# API Design Patterns Rules

Best practices and rules for API Design Patterns.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Design APIs for the consumer, not the database schema | MEDIUM | [`api-design-design-apis-for-the-consumer-not-the-database-schema.md`](api-design-design-apis-for-the-consumer-not-the-database-schema.md) |
| 2 | Be consistent | MEDIUM | [`api-design-be-consistent.md`](api-design-be-consistent.md) |
| 3 | Use pagination on every list endpoint from day one | CRITICAL | [`api-design-use-pagination-on-every-list-endpoint-from-day-one.md`](api-design-use-pagination-on-every-list-endpoint-from-day-one.md) |
| 4 | Prefer cursor-based pagination for any data that changes or... | LOW | [`api-design-prefer-cursor-based-pagination-for-any-data-that-changes-or.md`](api-design-prefer-cursor-based-pagination-for-any-data-that-changes-or.md) |
| 5 | Always set and propagate deadlines/timeouts | CRITICAL | [`api-design-always-set-and-propagate-deadlines-timeouts.md`](api-design-always-set-and-propagate-deadlines-timeouts.md) |
| 6 | Include correlation IDs in every request/response for... | MEDIUM | [`api-design-include-correlation-ids-in-every-request-response-for.md`](api-design-include-correlation-ids-in-every-request-response-for.md) |
| 7 | Document your API with OpenAPI (REST) or SDL (GraphQL) and... | MEDIUM | [`api-design-document-your-api-with-openapi-rest-or-sdl-graphql-and.md`](api-design-document-your-api-with-openapi-rest-or-sdl-graphql-and.md) |

---

---
title: "Always set and propagate deadlines/timeouts"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Always set and propagate deadlines/timeouts

Always set and propagate deadlines/timeouts. An API call without a timeout is a resource leak waiting to happen.

---

---
title: "Be consistent"
impact: MEDIUM
impactDescription: "general best practice"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Be consistent

Be consistent: once you pick conventions for naming, pagination, error format, and versioning, apply them uniformly across all endpoints.

---

---
title: "Design APIs for the consumer, not the database schema"
impact: MEDIUM
impactDescription: "general best practice"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Design APIs for the consumer, not the database schema

Design APIs for the consumer, not the database schema. Resource models should reflect use cases, not table structures.

---

---
title: "Document your API with OpenAPI (REST) or SDL (GraphQL) and..."
impact: MEDIUM
impactDescription: "general best practice"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Document your API with OpenAPI (REST) or SDL (GraphQL) and...

Document your API with OpenAPI (REST) or SDL (GraphQL) and keep the spec in version control alongside the code.

---

---
title: "Include correlation IDs in every request/response for..."
impact: MEDIUM
impactDescription: "general best practice"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Include correlation IDs in every request/response for...

Include correlation IDs in every request/response for end-to-end tracing.

---

---
title: "Prefer cursor-based pagination for any data that changes or..."
impact: LOW
impactDescription: "recommended but situational"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Prefer cursor-based pagination for any data that changes or...

Prefer cursor-based pagination for any data that changes or grows.

---

---
title: "Use pagination on every list endpoint from day one"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-design, dev, backend, rest-api-design, graphql-schema-design, grpc-service-definition
---

## Use pagination on every list endpoint from day one

Use pagination on every list endpoint from day one. Unpaginated lists become production incidents.
