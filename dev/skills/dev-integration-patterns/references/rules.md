# Integration Patterns Rules

Best practices and rules for Integration Patterns.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Learn the pattern language before choosing a framework --... | MEDIUM | [`integration-patterns-learn-the-pattern-language-before-choosing-a-framework.md`](integration-patterns-learn-the-pattern-language-before-choosing-a-framework.md) |
| 2 | Prefer idempotent message handlers; at-least-once delivery... | LOW | [`integration-patterns-prefer-idempotent-message-handlers-at-least-once-delivery.md`](integration-patterns-prefer-idempotent-message-handlers-at-least-once-delivery.md) |
| 3 | Design messages as immutable, self-describing contracts... | MEDIUM | [`integration-patterns-design-messages-as-immutable-self-describing-contracts.md`](integration-patterns-design-messages-as-immutable-self-describing-contracts.md) |
| 4 | Keep channels focused on a single data type or purpose... | MEDIUM | [`integration-patterns-keep-channels-focused-on-a-single-data-type-or-purpose.md`](integration-patterns-keep-channels-focused-on-a-single-data-type-or-purpose.md) |
| 5 | Use Dead Letter Channels for every queue -- never silently... | CRITICAL | [`integration-patterns-use-dead-letter-channels-for-every-queue-never-silently.md`](integration-patterns-use-dead-letter-channels-for-every-queue-never-silently.md) |
| 6 | Instrument messaging with Wire Taps and Message Stores from... | MEDIUM | [`integration-patterns-instrument-messaging-with-wire-taps-and-message-stores-from.md`](integration-patterns-instrument-messaging-with-wire-taps-and-message-stores-from.md) |
| 7 | Start with the simplest topology (point-to-point) and... | MEDIUM | [`integration-patterns-start-with-the-simplest-topology-point-to-point-and.md`](integration-patterns-start-with-the-simplest-topology-point-to-point-and.md) |

---

---
title: "Design messages as immutable, self-describing contracts..."
impact: MEDIUM
impactDescription: "general best practice"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Design messages as immutable, self-describing contracts...

Design messages as immutable, self-describing contracts with schema versioning.

---

---
title: "Instrument messaging with Wire Taps and Message Stores from..."
impact: MEDIUM
impactDescription: "general best practice"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Instrument messaging with Wire Taps and Message Stores from...

Instrument messaging with Wire Taps and Message Stores from day one; debugging async flows without observability is painful.

---

---
title: "Keep channels focused on a single data type or purpose..."
impact: MEDIUM
impactDescription: "general best practice"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Keep channels focused on a single data type or purpose...

Keep channels focused on a single data type or purpose (Datatype Channel).

---

---
title: "Learn the pattern language before choosing a framework --..."
impact: MEDIUM
impactDescription: "general best practice"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Learn the pattern language before choosing a framework --...

Learn the pattern language before choosing a framework -- the vocabulary transcends any single implementation.

---

---
title: "Prefer idempotent message handlers; at-least-once delivery..."
impact: LOW
impactDescription: "recommended but situational"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Prefer idempotent message handlers; at-least-once delivery...

Prefer idempotent message handlers; at-least-once delivery is the norm.

---

---
title: "Start with the simplest topology (point-to-point) and..."
impact: MEDIUM
impactDescription: "general best practice"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Start with the simplest topology (point-to-point) and...

Start with the simplest topology (point-to-point) and evolve toward pub-sub or content-based routing only when the need is proven.

---

---
title: "Use Dead Letter Channels for every queue -- never silently..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: integration-patterns, dev, enterprise-integration-patterns, messaging-architecture, choosing-integration-patterns
---

## Use Dead Letter Channels for every queue -- never silently...

Use Dead Letter Channels for every queue -- never silently drop messages.
