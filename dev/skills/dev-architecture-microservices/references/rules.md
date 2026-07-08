# Microservices Rules

Best practices and rules for Microservices.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Design for failure from day one | MEDIUM | [`microservices-design-for-failure-from-day-one.md`](microservices-design-for-failure-from-day-one.md) |
| 2 | Own your data | MEDIUM | [`microservices-own-your-data.md`](microservices-own-your-data.md) |
| 3 | Make inter-service communication observable | MEDIUM | [`microservices-make-inter-service-communication-observable.md`](microservices-make-inter-service-communication-observable.md) |
| 4 | Use consumer-driven contract testing (Pact, Spring Cloud... | HIGH | [`microservices-use-consumer-driven-contract-testing-pact-spring-cloud.md`](microservices-use-consumer-driven-contract-testing-pact-spring-cloud.md) |
| 5 | Prefer asynchronous communication; use synchronous calls... | LOW | [`microservices-prefer-asynchronous-communication-use-synchronous-calls.md`](microservices-prefer-asynchronous-communication-use-synchronous-calls.md) |
| 6 | Keep services small enough to be owned by a single team,... | MEDIUM | [`microservices-keep-services-small-enough-to-be-owned-by-a-single-team.md`](microservices-keep-services-small-enough-to-be-owned-by-a-single-team.md) |
| 7 | Deploy independently, test independently, fail independently | MEDIUM | [`microservices-deploy-independently-test-independently-fail-independently.md`](microservices-deploy-independently-test-independently-fail-independently.md) |

---

---
title: "Deploy independently, test independently, fail independently"
impact: MEDIUM
impactDescription: "general best practice"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Deploy independently, test independently, fail independently

Deploy independently, test independently, fail independently.

---

---
title: "Design for failure from day one"
impact: MEDIUM
impactDescription: "general best practice"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Design for failure from day one

Design for failure from day one: circuit breakers, retries, timeouts, bulkheads.

---

---
title: "Keep services small enough to be owned by a single team,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Keep services small enough to be owned by a single team,...

Keep services small enough to be owned by a single team, but large enough to justify the operational overhead.

---

---
title: "Make inter-service communication observable"
impact: MEDIUM
impactDescription: "general best practice"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Make inter-service communication observable

Make inter-service communication observable: distributed tracing (OpenTelemetry), centralized logging, metrics.

---

---
title: "Own your data"
impact: MEDIUM
impactDescription: "general best practice"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Own your data

Own your data: one database per service, no shared database access.

---

---
title: "Prefer asynchronous communication; use synchronous calls..."
impact: LOW
impactDescription: "recommended but situational"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Prefer asynchronous communication; use synchronous calls...

Prefer asynchronous communication; use synchronous calls only when necessary.

---

---
title: "Use consumer-driven contract testing (Pact, Spring Cloud..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: microservices, dev, architecture, microservice-decomposition, inter-service-communication, service-mesh
---

## Use consumer-driven contract testing (Pact, Spring Cloud...

Use consumer-driven contract testing (Pact, Spring Cloud Contract) to prevent breaking changes.
