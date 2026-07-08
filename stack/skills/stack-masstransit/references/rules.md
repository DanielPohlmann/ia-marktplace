# MassTransit Rules

Best practices and rules for MassTransit.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use `Publish` for events (fan-out to all interested... | MEDIUM | [`masstransit-use-publish-for-events-fan-out-to-all-interested.md`](masstransit-use-publish-for-events-fan-out-to-all-interested.md) |
| 2 | Enable the transactional outbox (`AddEntityFrameworkOutbox`... | MEDIUM | [`masstransit-enable-the-transactional-outbox-addentityframeworkoutbox.md`](masstransit-enable-the-transactional-outbox-addentityframeworkoutbox.md) |
| 3 | Design consumers to be idempotent so that retried or... | MEDIUM | [`masstransit-design-consumers-to-be-idempotent-so-that-retried-or.md`](masstransit-design-consumers-to-be-idempotent-so-that-retried-or.md) |
| 4 | Use `ITestHarness` from `MassTransit | MEDIUM | [`masstransit-use-itestharness-from-masstransit.md`](masstransit-use-itestharness-from-masstransit.md) |
| 5 | Configure message retry with exponential backoff on... | MEDIUM | [`masstransit-configure-message-retry-with-exponential-backoff-on.md`](masstransit-configure-message-retry-with-exponential-backoff-on.md) |
| 6 | Keep message contracts in a shared contract assembly... | HIGH | [`masstransit-keep-message-contracts-in-a-shared-contract-assembly.md`](masstransit-keep-message-contracts-in-a-shared-contract-assembly.md) |
| 7 | Use saga state machines for long-running workflows spanning... | MEDIUM | [`masstransit-use-saga-state-machines-for-long-running-workflows-spanning.md`](masstransit-use-saga-state-machines-for-long-running-workflows-spanning.md) |
| 8 | Set `PrefetchCount` and concurrency limits per consumer... | HIGH | [`masstransit-set-prefetchcount-and-concurrency-limits-per-consumer.md`](masstransit-set-prefetchcount-and-concurrency-limits-per-consumer.md) |
| 9 | Prefer the in-memory transport for local development and... | CRITICAL | [`masstransit-prefer-the-in-memory-transport-for-local-development-and.md`](masstransit-prefer-the-in-memory-transport-for-local-development-and.md) |
| 10 | Always call `ConfigureEndpoints(context)` on the bus... | CRITICAL | [`masstransit-always-call-configureendpoints-context-on-the-bus.md`](masstransit-always-call-configureendpoints-context-on-the-bus.md) |

---

---
title: "Always call `ConfigureEndpoints(context)` on the bus..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Always call `ConfigureEndpoints(context)` on the bus...

Always call `ConfigureEndpoints(context)` on the bus configuration to let MassTransit automatically wire consumer endpoints using conventions.

---

---
title: "Configure message retry with exponential backoff on..."
impact: MEDIUM
impactDescription: "general best practice"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Configure message retry with exponential backoff on...

Configure message retry with exponential backoff on consumers to handle transient failures without overwhelming downstream services.

---

---
title: "Design consumers to be idempotent so that retried or..."
impact: MEDIUM
impactDescription: "general best practice"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Design consumers to be idempotent so that retried or...

Design consumers to be idempotent so that retried or redelivered messages produce the same result without side effects.

---

---
title: "Enable the transactional outbox (`AddEntityFrameworkOutbox`..."
impact: MEDIUM
impactDescription: "general best practice"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Enable the transactional outbox (`AddEntityFrameworkOutbox`...

Enable the transactional outbox (`AddEntityFrameworkOutbox` + `UseBusOutbox`) to guarantee at-least-once delivery of messages published within a database transaction.

---

---
title: "Keep message contracts in a shared contract assembly..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Keep message contracts in a shared contract assembly...

Keep message contracts in a shared contract assembly referenced by both producer and consumer projects; avoid sharing implementation code.

---

---
title: "Prefer the in-memory transport for local development and..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Prefer the in-memory transport for local development and...

Prefer the in-memory transport for local development and unit tests; switch to a real broker (RabbitMQ, Azure SB) via configuration for staging and production.

---

---
title: "Set `PrefetchCount` and concurrency limits per consumer..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Set `PrefetchCount` and concurrency limits per consumer...

Set `PrefetchCount` and concurrency limits per consumer based on workload characteristics to avoid overwhelming databases or downstream APIs.

---

---
title: "Use `ITestHarness` from `MassTransit"
impact: MEDIUM
impactDescription: "general best practice"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Use `ITestHarness` from `MassTransit

Use `ITestHarness` from `MassTransit.Testing` for integration tests rather than mocking `IPublishEndpoint` or `IBus` directly.

---

---
title: "Use `Publish` for events (fan-out to all interested..."
impact: MEDIUM
impactDescription: "general best practice"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Use `Publish` for events (fan-out to all interested...

Use `Publish` for events (fan-out to all interested consumers) and `Send` for commands (point-to-point to a specific queue) to maintain clear messaging semantics.

---

---
title: "Use saga state machines for long-running workflows spanning..."
impact: MEDIUM
impactDescription: "general best practice"
tags: masstransit, dotnet, eventing, distributed-messaging, pubsub-consumers, requestresponse-over-message-brokers
---

## Use saga state machines for long-running workflows spanning...

Use saga state machines for long-running workflows spanning multiple messages rather than trying to coordinate state across independent consumers.
