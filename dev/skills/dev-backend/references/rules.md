# Backend Architecture Rules

Best practices and rules for Backend Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with a monolith and extract services only when... | MEDIUM | [`backend-start-with-a-monolith-and-extract-services-only-when.md`](backend-start-with-a-monolith-and-extract-services-only-when.md) |
| 2 | Choose boring technology by default | MEDIUM | [`backend-choose-boring-technology-by-default.md`](backend-choose-boring-technology-by-default.md) |
| 3 | Design for failure | MEDIUM | [`backend-design-for-failure.md`](backend-design-for-failure.md) |
| 4 | Make operations idempotent wherever possible -- especially... | MEDIUM | [`backend-make-operations-idempotent-wherever-possible-especially.md`](backend-make-operations-idempotent-wherever-possible-especially.md) |
| 5 | Instrument everything from day one | MEDIUM | [`backend-instrument-everything-from-day-one.md`](backend-instrument-everything-from-day-one.md) |
| 6 | Treat API contracts as public commitments | CRITICAL | [`backend-treat-api-contracts-as-public-commitments.md`](backend-treat-api-contracts-as-public-commitments.md) |

---

---
title: "Choose boring technology by default"
impact: MEDIUM
impactDescription: "general best practice"
tags: backend, dev, backend-architecture-decisions, choosing-api-styles, choosing-database-types
---

## Choose boring technology by default

Choose boring technology by default. PostgreSQL, Redis, and a well-designed REST API solve the vast majority of backend problems.

---

---
title: "Design for failure"
impact: MEDIUM
impactDescription: "general best practice"
tags: backend, dev, backend-architecture-decisions, choosing-api-styles, choosing-database-types
---

## Design for failure

Design for failure: every network call can fail, every database can be slow. Use timeouts, retries with backoff, circuit breakers, and fallbacks.

---

---
title: "Instrument everything from day one"
impact: MEDIUM
impactDescription: "general best practice"
tags: backend, dev, backend-architecture-decisions, choosing-api-styles, choosing-database-types
---

## Instrument everything from day one

Instrument everything from day one. Adding observability retroactively is far more expensive than building it in.

---

---
title: "Make operations idempotent wherever possible -- especially..."
impact: MEDIUM
impactDescription: "general best practice"
tags: backend, dev, backend-architecture-decisions, choosing-api-styles, choosing-database-types
---

## Make operations idempotent wherever possible -- especially...

Make operations idempotent wherever possible -- especially for writes, background jobs, and event handlers.

---

---
title: "Start with a monolith and extract services only when..."
impact: MEDIUM
impactDescription: "general best practice"
tags: backend, dev, backend-architecture-decisions, choosing-api-styles, choosing-database-types
---

## Start with a monolith and extract services only when...

Start with a monolith and extract services only when complexity demands it -- premature microservices add coordination cost without proportional benefit.

---

---
title: "Treat API contracts as public commitments"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: backend, dev, backend-architecture-decisions, choosing-api-styles, choosing-database-types
---

## Treat API contracts as public commitments

Treat API contracts as public commitments: version explicitly, deprecate gracefully, never break existing clients without a migration path.
