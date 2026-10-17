<!-- Part of the specs-documentation-adr skill. Loaded on demand from SKILL.md. -->

# The Nygard Format (Original ADR)

Michael Nygard defined the original ADR format in his blog post "Documenting Architecture Decisions" (2011). It has five sections:

## Structure

```markdown
# [ADR-NNNN] [Short Title of Decision]

## Status

[Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]

## Context

[What is the issue that we are seeing that is motivating this decision
or change? Describe the forces at play -- technical, political,
social, project-specific. This section is factual, not opinionated.]

## Decision

[What is the change that we are proposing and/or doing?
State the decision in active voice: "We will..."]

## Consequences

[What becomes easier or more difficult to do because of this change?
Include both positive and negative consequences. Be honest about
trade-offs.]
```

## Complete Example (Nygard Format)

```markdown
# ADR-0007: Use PostgreSQL as the Primary Database

## Status

Accepted

## Context

The Order Service requires a persistent data store for order and
payment data. We need ACID transactions for financial operations,
strong consistency guarantees, and the ability to handle complex
queries involving joins across orders, items, and payments.

The team has evaluated three options:
1. **PostgreSQL** -- relational, ACID-compliant, mature ecosystem
2. **MongoDB** -- document store, flexible schema, eventual consistency
3. **CockroachDB** -- distributed SQL, strong consistency, higher cost

Key constraints:
- The operations team has production experience with PostgreSQL
- Our cloud provider offers managed PostgreSQL (RDS/Cloud SQL)
- Financial data requires ACID transactions (not eventual consistency)
- Budget does not support CockroachDB licensing for this phase

## Decision

We will use PostgreSQL as the primary database for the Order Service.

We will use the managed PostgreSQL offering from our cloud provider
(AWS RDS) to reduce operational burden. Schema migrations will be
managed with Entity Framework Core Migrations in the application
repository.

## Consequences

**Positive:**
- ACID transactions guarantee financial data integrity
- Rich query capabilities for reporting and analytics
- Team familiarity reduces onboarding and debugging time
- Managed service reduces operational burden
- Large ecosystem of tools, extensions, and community support

**Negative:**
- Vertical scaling limits compared to distributed databases
- Schema changes require migration management
- Horizontal scaling (read replicas, sharding) adds complexity
  if we outgrow a single instance
- Document-style data (order metadata) requires JSONB columns
  rather than native document storage

**Neutral:**
- We will revisit this decision if order volume exceeds 10,000
  transactions per second, which would require a distributed
  database strategy (see future ADR)
```
