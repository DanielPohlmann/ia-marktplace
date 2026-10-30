# Event-Driven Architecture Rules

Best practices and rules for Event-Driven Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with EDA alone if you only need loose coupling and... | MEDIUM | [`event-driven-start-with-eda-alone-if-you-only-need-loose-coupling-and.md`](event-driven-start-with-eda-alone-if-you-only-need-loose-coupling-and.md) |
| 2 | Design events as first-class domain concepts | MEDIUM | [`event-driven-design-events-as-first-class-domain-concepts.md`](event-driven-design-events-as-first-class-domain-concepts.md) |
| 3 | Plan for event schema evolution from day one | MEDIUM | [`event-driven-plan-for-event-schema-evolution-from-day-one.md`](event-driven-plan-for-event-schema-evolution-from-day-one.md) |
| 4 | Build projections to be rebuildable | MEDIUM | [`event-driven-build-projections-to-be-rebuildable.md`](event-driven-build-projections-to-be-rebuildable.md) |
| 5 | Add snapshots only when measured rehydration latency demands it | MEDIUM | [`event-driven-use-snapshots-for-long-lived-event-streams-to-keep-replay.md`](event-driven-use-snapshots-for-long-lived-event-streams-to-keep-replay.md) |
| 6 | Handle idempotency in all event consumers | MEDIUM | [`event-driven-handle-idempotency-in-all-event-consumers.md`](event-driven-handle-idempotency-in-all-event-consumers.md) |
| 7 | Monitor projection lag (time between event publication and... | MEDIUM | [`event-driven-monitor-projection-lag-time-between-event-publication-and.md`](event-driven-monitor-projection-lag-time-between-event-publication-and.md) |
| 8 | Keep the write model focused on enforcing business... | MEDIUM | [`event-driven-keep-the-write-model-focused-on-enforcing-business.md`](event-driven-keep-the-write-model-focused-on-enforcing-business.md) |

---

---
title: "Build projections to be rebuildable"
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Build projections to be rebuildable

Build projections to be rebuildable: if a projection is corrupted or needs to change, replay events from the beginning.

---

---
title: "Design events as first-class domain concepts"
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Design events as first-class domain concepts

Design events as first-class domain concepts: past-tense, immutable, carrying business intent (not CRUD operations).

---

---
title: "Handle idempotency in all event consumers"
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Handle idempotency in all event consumers

Handle idempotency in all event consumers: at-least-once delivery is the norm.

---

---
title: "Keep the write model focused on enforcing business..."
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Keep the write model focused on enforcing business...

Keep the write model focused on enforcing business invariants; keep the read model focused on query performance.

---

---
title: "Monitor projection lag (time between event publication and..."
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Monitor projection lag (time between event publication and...

Monitor projection lag (time between event publication and read model update) as a key operational metric.

---

---
title: "Plan for event schema evolution from day one"
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Plan for event schema evolution from day one

Plan for event schema evolution from day one. Use a schema registry (Avro, Protobuf) for strong contracts.

---

---
title: "Start with EDA alone if you only need loose coupling and..."
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Start with EDA alone if you only need loose coupling and...

Start with EDA alone if you only need loose coupling and reactive behavior. Add event sourcing or CQRS only when you have a specific need.

---

---
title: "Add snapshots only when measured rehydration latency demands it"
impact: MEDIUM
impactDescription: "general best practice"
tags: event-driven, dev, architecture, event-driven-architecture, event-sourcing, cqrs
---

## Add snapshots only when measured rehydration latency demands it

Snapshots exist to cut aggregate rehydration latency, not to speed up projection rebuilds. Add them only after measuring load latency, have the application write one every N events (N taken from that measurement), and store a fold/state version with each snapshot. They are disposable: when the fold logic or state shape changes, discard them and rebuild from events. Prefer short-lived streams (closing the books per period) before reaching for snapshots.
