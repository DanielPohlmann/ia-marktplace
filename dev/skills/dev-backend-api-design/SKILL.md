---
name: dev-backend-api-design
description: Use when designing REST, GraphQL, gRPC, or WebSocket APIs. USE FOR: resource naming, HTTP semantics, versioning, pagination, error shapes, idempotency, OpenAPI contracts, gateway patterns. DO NOT USE FOR: storage design (use dev-backend-data-modeling), auth design (use dev-backend-authentication), Scalar/Swashbuckle wiring (use stack-openapi), API hardening (use security-api-security).
---

# API Design Patterns

## Overview
API design determines how clients interact with backend services. A well-designed API is intuitive, consistent, evolvable, and resilient. This skill covers the four major API styles -- REST, GraphQL, gRPC, and WebSocket -- along with cross-cutting concerns like versioning, pagination, rate limiting, and idempotency.

## Best Practices
- Design APIs for the consumer, not the database schema. Resource models should reflect use cases, not table structures.
- Be consistent: once you pick conventions for naming, pagination, error format, and versioning, apply them uniformly across all endpoints.
- Use pagination on every list endpoint from day one. Unpaginated lists become production incidents.
- Prefer cursor-based pagination for any data that changes or grows.
- Always set and propagate deadlines/timeouts. An API call without a timeout is a resource leak waiting to happen.
- Include correlation IDs in every request/response for end-to-end tracing.
- Document your API with OpenAPI (REST) or SDL (GraphQL) and keep the spec in version control alongside the code.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/rest-api-design.md](references/rest-api-design.md) | REST API Design — Resource Naming Conventions, HTTP Methods & Status Codes, HATEOAS (Hypermedia As The Engine Of Application State), Pagination, Filtering & Sorting, Versioning Strategies, … |
| [references/graphql-schema-design.md](references/graphql-schema-design.md) | GraphQL Schema Design — Schema Example (Schema-First / SDL), The N+1 Problem & DataLoader, Schema-First vs. Code-First, Federation |
| [references/grpc-service-design.md](references/grpc-service-design.md) | gRPC Service Design — Protobuf Service Definition, Communication Patterns, gRPC Best Practices |
| [references/details.md](references/details.md) | WebSocket Protocol Design; Cross-Cutting API Concerns |

## References

- [OpenAPI Specification](https://www.openapis.org/)
- [GraphQL Official Documentation](https://graphql.org/)
- [gRPC Official Documentation](https://grpc.io/)

See references/rules.md for the full rule catalog.
