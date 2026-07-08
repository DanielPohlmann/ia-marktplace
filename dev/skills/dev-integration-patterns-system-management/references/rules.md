# System Management Rules

Best practices and rules for System Management.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Deploy Wire Taps from day one; adding observability after a... | CRITICAL | [`system-management-deploy-wire-taps-from-day-one-adding-observability-after-a.md`](system-management-deploy-wire-taps-from-day-one-adding-observability-after-a.md) |
| 2 | Propagate trace context (correlationId, traceId) through... | MEDIUM | [`system-management-propagate-trace-context-correlationid-traceid-through.md`](system-management-propagate-trace-context-correlationid-traceid-through.md) |
| 3 | Use the Control Bus pattern even if you implement it as... | MEDIUM | [`system-management-use-the-control-bus-pattern-even-if-you-implement-it-as.md`](system-management-use-the-control-bus-pattern-even-if-you-implement-it-as.md) |
| 4 | Store messages with enough metadata (messageId,... | MEDIUM | [`system-management-store-messages-with-enough-metadata-messageid.md`](system-management-store-messages-with-enough-metadata-messageid.md) |
| 5 | Implement Test Messages for critical business pipelines;... | CRITICAL | [`system-management-implement-test-messages-for-critical-business-pipelines.md`](system-management-implement-test-messages-for-critical-business-pipelines.md) |
| 6 | Protect Channel Purger behind access controls and audit... | CRITICAL | [`system-management-protect-channel-purger-behind-access-controls-and-audit.md`](system-management-protect-channel-purger-behind-access-controls-and-audit.md) |
| 7 | Detours are invaluable for debugging production issues;... | CRITICAL | [`system-management-detours-are-invaluable-for-debugging-production-issues.md`](system-management-detours-are-invaluable-for-debugging-production-issues.md) |
| 8 | Correlate messaging observability with application metrics... | MEDIUM | [`system-management-correlate-messaging-observability-with-application-metrics.md`](system-management-correlate-messaging-observability-with-application-metrics.md) |

---

---
title: "Correlate messaging observability with application metrics..."
impact: MEDIUM
impactDescription: "general best practice"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Correlate messaging observability with application metrics...

Correlate messaging observability with application metrics (error rates, latency) for a complete operational picture.

---

---
title: "Deploy Wire Taps from day one; adding observability after a..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Deploy Wire Taps from day one; adding observability after a...

Deploy Wire Taps from day one; adding observability after a production incident is too late.

---

---
title: "Detours are invaluable for debugging production issues;..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Detours are invaluable for debugging production issues;...

Detours are invaluable for debugging production issues; design pipelines with detour insertion points from the start.

---

---
title: "Implement Test Messages for critical business pipelines;..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Implement Test Messages for critical business pipelines;...

Implement Test Messages for critical business pipelines; silent failures are the most dangerous kind.

---

---
title: "Propagate trace context (correlationId, traceId) through..."
impact: MEDIUM
impactDescription: "general best practice"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Propagate trace context (correlationId, traceId) through...

Propagate trace context (correlationId, traceId) through every message header to enable distributed tracing.

---

---
title: "Protect Channel Purger behind access controls and audit..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Protect Channel Purger behind access controls and audit...

Protect Channel Purger behind access controls and audit logging; an accidental purge in production can cause data loss.

---

---
title: "Store messages with enough metadata (messageId,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Store messages with enough metadata (messageId,...

Store messages with enough metadata (messageId, correlationId, timestamp, source, type) to reconstruct any conversation.

---

---
title: "Use the Control Bus pattern even if you implement it as..."
impact: MEDIUM
impactDescription: "general best practice"
tags: system-management, dev, integration-patterns, messaging-observability, wire-tap, control-bus
---

## Use the Control Bus pattern even if you implement it as...

Use the Control Bus pattern even if you implement it as feature flags or admin API endpoints -- the principle of a separate management plane matters.
