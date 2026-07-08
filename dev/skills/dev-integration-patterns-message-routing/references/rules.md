# Message Routing Rules

Best practices and rules for Message Routing.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use Content-Based Router when you have a small, stable set... | MEDIUM | [`message-routing-use-content-based-router-when-you-have-a-small-stable-set.md`](message-routing-use-content-based-router-when-you-have-a-small-stable-set.md) |
| 2 | Always pair a Splitter with an Aggregator to avoid orphaned... | CRITICAL | [`message-routing-always-pair-a-splitter-with-an-aggregator-to-avoid-orphaned.md`](message-routing-always-pair-a-splitter-with-an-aggregator-to-avoid-orphaned.md) |
| 3 | Aggregators need three things | MEDIUM | [`message-routing-aggregators-need-three-things.md`](message-routing-aggregators-need-three-things.md) |
| 4 | Prefer Routing Slip over Process Manager when steps are... | CRITICAL | [`message-routing-prefer-routing-slip-over-process-manager-when-steps-are.md`](message-routing-prefer-routing-slip-over-process-manager-when-steps-are.md) |
| 5 | Use Process Manager (Saga) when you need compensation logic... | MEDIUM | [`message-routing-use-process-manager-saga-when-you-need-compensation-logic.md`](message-routing-use-process-manager-saga-when-you-need-compensation-logic.md) |
| 6 | Scatter-Gather should always have a timeout; do not wait... | CRITICAL | [`message-routing-scatter-gather-should-always-have-a-timeout-do-not-wait.md`](message-routing-scatter-gather-should-always-have-a-timeout-do-not-wait.md) |
| 7 | Keep routing logic in the infrastructure layer, not in... | MEDIUM | [`message-routing-keep-routing-logic-in-the-infrastructure-layer-not-in.md`](message-routing-keep-routing-logic-in-the-infrastructure-layer-not-in.md) |
| 8 | Monitor router decisions with Wire Tap for debugging;... | MEDIUM | [`message-routing-monitor-router-decisions-with-wire-tap-for-debugging.md`](message-routing-monitor-router-decisions-with-wire-tap-for-debugging.md) |

---

---
title: "Aggregators need three things"
impact: MEDIUM
impactDescription: "general best practice"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Aggregators need three things

Aggregators need three things: a correlation key, a completion condition, and a timeout strategy.

---

---
title: "Always pair a Splitter with an Aggregator to avoid orphaned..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Always pair a Splitter with an Aggregator to avoid orphaned...

Always pair a Splitter with an Aggregator to avoid orphaned fragments.

---

---
title: "Keep routing logic in the infrastructure layer, not in..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Keep routing logic in the infrastructure layer, not in...

Keep routing logic in the infrastructure layer, not in business code -- this makes it visible and reconfigurable.

---

---
title: "Monitor router decisions with Wire Tap for debugging;..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Monitor router decisions with Wire Tap for debugging;...

Monitor router decisions with Wire Tap for debugging; complex routing is notoriously hard to troubleshoot.

---

---
title: "Prefer Routing Slip over Process Manager when steps are..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Prefer Routing Slip over Process Manager when steps are...

Prefer Routing Slip over Process Manager when steps are independent and do not require shared state.

---

---
title: "Scatter-Gather should always have a timeout; do not wait..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Scatter-Gather should always have a timeout; do not wait...

Scatter-Gather should always have a timeout; do not wait indefinitely for all replies.

---

---
title: "Use Content-Based Router when you have a small, stable set..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Use Content-Based Router when you have a small, stable set...

Use Content-Based Router when you have a small, stable set of routes; switch to Dynamic Router when rules change frequently.

---

---
title: "Use Process Manager (Saga) when you need compensation logic..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-routing, dev, integration-patterns, content-based-routing, message-filtering, splitteraggregator
---

## Use Process Manager (Saga) when you need compensation logic...

Use Process Manager (Saga) when you need compensation logic for failures in long-running workflows.
