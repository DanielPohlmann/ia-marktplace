<!-- Part of the specs-documentation-rfc skill. Loaded on demand from SKILL.md. -->

# RFC Example: Migrate from REST to GraphQL

```markdown
# RFC: Migrate Customer Portal API from REST to GraphQL

| Field          | Value                     |
|----------------|---------------------------|
| Author         | Jordan Developer          |
| Status         | In Review                 |
| Created        | 2025-01-10                |
| Review Deadline| 2025-01-24                |
| Reviewers      | Frontend Team, API Team, Tech Lead |
| Decision Maker | VP Engineering            |

## Summary

Migrate the Customer Portal's backend-for-frontend (BFF) API from
REST to GraphQL to reduce over-fetching, eliminate the need for
multiple round-trips on dashboard pages, and improve frontend
developer productivity.

## Motivation

## Problem Statement
The Customer Portal dashboard currently makes 7 separate REST API
calls to render the main page. This causes:
- **Slow page loads**: average 2.8s FCP due to sequential API calls
- **Over-fetching**: the /users endpoint returns 42 fields when the
  dashboard only needs 6
- **Tight coupling**: every new UI component requires a new REST
  endpoint or BFF aggregation layer change
- **Mobile performance**: mobile users on slow connections experience
  5s+ load times due to payload size

## Why Now?
The Customer Portal redesign (PRD-042) adds 3 new dashboard widgets
that would require 4 additional REST endpoints. This is the right
time to address the underlying architectural issue.

## Goals
- Reduce dashboard FCP from 2.8s to < 1.5s
- Enable frontend teams to query exactly the data they need
- Eliminate the need for new REST endpoints for UI changes

## Non-Goals
- Migrating internal service-to-service APIs (those remain REST/gRPC)
- Replacing the existing public REST API (external consumers keep REST)

## Detailed Design

## Overview
Introduce a GraphQL gateway (Apollo Server) as the BFF layer between
the React frontend and the existing microservices. The gateway
federates data from User Service, Order Service, and Product Service.

## Schema Design
```graphql
type Query {
  me: User!
  orders(first: Int, after: String): OrderConnection!
  product(id: ID!): Product
}

type User {
  id: ID!
  name: String!
  email: String!
  recentOrders(first: Int): [Order!]!
}

type Order {
  id: ID!
  status: OrderStatus!
  total: Money!
  items: [OrderItem!]!
  createdAt: DateTime!
}
```

## Migration Strategy
1. Deploy GraphQL gateway alongside existing REST BFF (weeks 1-2)
2. Migrate dashboard page to GraphQL (weeks 3-4)
3. Migrate remaining pages incrementally (weeks 5-8)
4. Deprecate REST BFF endpoints with sunset headers (week 9)
5. Decommission REST BFF (week 12)

## Alternatives Considered

## Alternative 1: Optimize REST with Sparse Fieldsets
Use JSON:API sparse fieldsets (`?fields[user]=id,name,email`).

Pros: No new technology; smaller change.
Cons: Does not solve N+1 round-trip problem; limited query flexibility.
Why not chosen: Addresses over-fetching but not under-fetching or
round-trip issues.

## Alternative 2: BFF Aggregation Endpoints
Create purpose-built aggregation endpoints (e.g., /dashboard-data).

Pros: Simple; no new technology.
Cons: Tight coupling between UI and API; every UI change needs a
backend change.
Why not chosen: Does not scale with the rate of UI iteration planned
for the portal redesign.

## Alternative 3: Do Nothing
Maintain current REST BFF.

Why not chosen: Dashboard performance will worsen as new widgets
are added, and frontend team velocity will decrease.

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| N+1 query performance in resolvers | High | Medium | DataLoader batching from day 1 |
| Team unfamiliar with GraphQL | Medium | Medium | 2-day workshop + pair programming |
| Cache invalidation complexity | Medium | Medium | Apollo cache policies + persisted queries |

## Open Questions

- [ ] Should we use Apollo Federation or schema stitching?
- [ ] Do we need a persisted query allowlist for production?
- [ ] What is the deprecation timeline for the REST BFF?

## Timeline

| Phase | Duration | Description |
|-------|----------|-------------|
| RFC Review | 2 weeks | Team feedback |
| Prototype | 1 week | Validate Apollo Federation with 2 services |
| Phase 1 | 2 weeks | GraphQL gateway + dashboard migration |
| Phase 2 | 4 weeks | Remaining page migrations |
| Deprecation | 4 weeks | REST BFF sunset period |
```
