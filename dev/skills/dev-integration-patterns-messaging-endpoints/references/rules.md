# Messaging Endpoints Rules

Best practices and rules for Messaging Endpoints.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Default to Event-Driven Consumer; use Polling Consumer only... | MEDIUM | [`messaging-endpoints-default-to-event-driven-consumer-use-polling-consumer-only.md`](messaging-endpoints-default-to-event-driven-consumer-use-polling-consumer-only.md) |
| 2 | Always implement Idempotent Receiver -- treat it as a... | CRITICAL | [`messaging-endpoints-always-implement-idempotent-receiver-treat-it-as-a.md`](messaging-endpoints-always-implement-idempotent-receiver-treat-it-as-a.md) |
| 3 | Use Competing Consumers for horizontal scaling, but be... | MEDIUM | [`messaging-endpoints-use-competing-consumers-for-horizontal-scaling-but-be.md`](messaging-endpoints-use-competing-consumers-for-horizontal-scaling-but-be.md) |
| 4 | Prefer Durable Subscriber for all production pub-sub... | CRITICAL | [`messaging-endpoints-prefer-durable-subscriber-for-all-production-pub-sub.md`](messaging-endpoints-prefer-durable-subscriber-for-all-production-pub-sub.md) |
| 5 | Use the Outbox Pattern as a practical alternative to... | MEDIUM | [`messaging-endpoints-use-the-outbox-pattern-as-a-practical-alternative-to.md`](messaging-endpoints-use-the-outbox-pattern-as-a-practical-alternative-to.md) |
| 6 | Service Activator is the pattern that keeps your business... | CRITICAL | [`messaging-endpoints-service-activator-is-the-pattern-that-keeps-your-business.md`](messaging-endpoints-service-activator-is-the-pattern-that-keeps-your-business.md) |
| 7 | Monitor consumer lag (the gap between published and... | MEDIUM | [`messaging-endpoints-monitor-consumer-lag-the-gap-between-published-and.md`](messaging-endpoints-monitor-consumer-lag-the-gap-between-published-and.md) |
| 8 | Set appropriate prefetch counts and concurrency limits;... | MEDIUM | [`messaging-endpoints-set-appropriate-prefetch-counts-and-concurrency-limits.md`](messaging-endpoints-set-appropriate-prefetch-counts-and-concurrency-limits.md) |

---

---
title: "Always implement Idempotent Receiver -- treat it as a..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Always implement Idempotent Receiver -- treat it as a...

Always implement Idempotent Receiver -- treat it as a non-negotiable baseline, not an optimisation.

---

---
title: "Default to Event-Driven Consumer; use Polling Consumer only..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Default to Event-Driven Consumer; use Polling Consumer only...

Default to Event-Driven Consumer; use Polling Consumer only when you need explicit rate control or batch processing.

---

---
title: "Monitor consumer lag (the gap between published and..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Monitor consumer lag (the gap between published and...

Monitor consumer lag (the gap between published and consumed messages) as a key health metric.

---

---
title: "Prefer Durable Subscriber for all production pub-sub..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Prefer Durable Subscriber for all production pub-sub...

Prefer Durable Subscriber for all production pub-sub subscriptions; non-durable subscriptions lose messages during deployments.

---

---
title: "Service Activator is the pattern that keeps your business..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Service Activator is the pattern that keeps your business...

Service Activator is the pattern that keeps your business logic testable -- it should never import messaging libraries.

---

---
title: "Set appropriate prefetch counts and concurrency limits;..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Set appropriate prefetch counts and concurrency limits;...

Set appropriate prefetch counts and concurrency limits; unbounded consumption can overwhelm downstream resources.

---

---
title: "Use Competing Consumers for horizontal scaling, but be..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Use Competing Consumers for horizontal scaling, but be...

Use Competing Consumers for horizontal scaling, but be aware of ordering implications.

---

---
title: "Use the Outbox Pattern as a practical alternative to..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-endpoints, dev, integration-patterns, consumer-patterns, polling-vs-event-driven-consumers, competing-consumers
---

## Use the Outbox Pattern as a practical alternative to...

Use the Outbox Pattern as a practical alternative to distributed transactions in Transactional Client scenarios.
