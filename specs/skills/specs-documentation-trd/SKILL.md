---
name: specs-documentation-trd
description: Use when writing a Technical Requirements Document that defines how to build a system. USE FOR: architecture description, API contracts, data models, security and performance requirements, dependencies, constraints, deployment plan. DO NOT USE FOR: product requirements (use specs-documentation-prd), business case (use specs-documentation-brd), single decisions (use specs-documentation-adr).
---

# Technical Requirements Document (TRD)

## Overview
A Technical Requirements Document (TRD) defines *how* a system or feature will be built. It translates the product requirements from the PRD into concrete technical specifications -- architecture, APIs, data models, security controls, performance targets, and deployment strategy. The TRD is the engineering team's blueprint for implementation.

The TRD sits downstream of the PRD and upstream of implementation:
```
PRD ("What are we building?") --> TRD ("How do we build it?") --> Implementation + ADRs
```

## Relationship to Other Documents

```
BRD (Business Requirements)
 |  Business case and justification
 v
PRD (Product Requirements)
 |  What to build, user stories, success metrics
 v
TRD (Technical Requirements)  <-- YOU ARE HERE
 |  How to build it -- architecture, APIs, data, deployment
 |
 +---> ADR (Architecture Decision Records)
 |     Individual decisions made during TRD creation
 |     (e.g., "Why PostgreSQL over MongoDB?")
 |
 +---> RFC (Request for Comments)
 |     Proposals for significant technical changes
 |     that need team-wide input before finalizing
 |
 v
Implementation
 |  Code guided by the TRD
 v
Gherkin / Gauge (Executable Specs)
    Verification that implementation meets requirements
```

## Best Practices

- **Reference the PRD** -- every technical decision should trace back to a product requirement. If a TRD section cannot be justified by the PRD, question whether it belongs.
- **Include diagrams** -- architecture diagrams (C4, sequence, ERD) communicate structure far better than prose alone. Use Mermaid for Markdown-native rendering.
- **Specify API contracts precisely** -- include request/response schemas, error codes, authentication, pagination, and rate limiting. Consider providing an OpenAPI spec as an appendix.
- **Define performance targets with percentiles** -- P50, P95, and P99 targets are more useful than averages, which hide tail latency.
- **Document the security model explicitly** -- authentication, authorization, encryption, input validation, and secrets management deserve dedicated sections, not afterthoughts.
- **Plan for failure** -- include rollback procedures, circuit breaker strategies, fallback behaviors, and disaster recovery in the deployment plan.
- **Record decisions as ADRs** -- when the TRD makes a significant technical choice (database, framework, architecture style), create a linked ADR to capture the context and trade-offs.
- **Keep it current** -- update the TRD as the system evolves. An outdated TRD is a liability, not an asset.
- **Review with the full engineering team** -- the TRD should be reviewed by backend, frontend, infrastructure, security, and QA engineers before implementation begins.
- **Use version control** -- store the TRD in the repository alongside the code it describes so it evolves with the system.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/complete-trd-template.md](references/complete-trd-template.md) | Complete TRD Template — 1.1 Purpose, 1.2 Scope, 1.3 Context, 2.1 Architecture Style, 2.2 Component Overview, 2.3 Technology Stack, … |
| [references/details.md](references/details.md) | Standard TRD Structure; TRD Example: Order Service |

## References

- [Software Requirements Specification — Wikipedia](https://en.wikipedia.org/wiki/Software_requirements_specification)

See references/rules.md for the full rule catalog.
