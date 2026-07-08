# Messaging Channels Rules

Best practices and rules for Messaging Channels.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always configure a Dead Letter Channel for every production... | CRITICAL | [`messaging-channels-always-configure-a-dead-letter-channel-for-every-production.md`](messaging-channels-always-configure-a-dead-letter-channel-for-every-production.md) |
| 2 | Use Datatype Channels to keep consumers simple and avoid... | HIGH | [`messaging-channels-use-datatype-channels-to-keep-consumers-simple-and-avoid.md`](messaging-channels-use-datatype-channels-to-keep-consumers-simple-and-avoid.md) |
| 3 | Enable Guaranteed Delivery for any message whose loss has... | MEDIUM | [`messaging-channels-enable-guaranteed-delivery-for-any-message-whose-loss-has.md`](messaging-channels-enable-guaranteed-delivery-for-any-message-whose-loss-has.md) |
| 4 | Prefer Publish-Subscribe for events and Point-to-Point for... | LOW | [`messaging-channels-prefer-publish-subscribe-for-events-and-point-to-point-for.md`](messaging-channels-prefer-publish-subscribe-for-events-and-point-to-point-for.md) |
| 5 | Use Channel Adapters to isolate legacy integration code... | MEDIUM | [`messaging-channels-use-channel-adapters-to-isolate-legacy-integration-code.md`](messaging-channels-use-channel-adapters-to-isolate-legacy-integration-code.md) |
| 6 | Monitor channel depth and throughput; a growing queue... | MEDIUM | [`messaging-channels-monitor-channel-depth-and-throughput-a-growing-queue.md`](messaging-channels-monitor-channel-depth-and-throughput-a-growing-queue.md) |
| 7 | Name channels after the message type or business purpose,... | MEDIUM | [`messaging-channels-name-channels-after-the-message-type-or-business-purpose.md`](messaging-channels-name-channels-after-the-message-type-or-business-purpose.md) |

---

---
title: "Always configure a Dead Letter Channel for every production..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Always configure a Dead Letter Channel for every production...

Always configure a Dead Letter Channel for every production queue.

---

---
title: "Enable Guaranteed Delivery for any message whose loss has..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Enable Guaranteed Delivery for any message whose loss has...

Enable Guaranteed Delivery for any message whose loss has business impact.

---

---
title: "Monitor channel depth and throughput; a growing queue..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Monitor channel depth and throughput; a growing queue...

Monitor channel depth and throughput; a growing queue signals a consumer that cannot keep up.

---

---
title: "Name channels after the message type or business purpose,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Name channels after the message type or business purpose,...

Name channels after the message type or business purpose, not the producer or consumer.

---

---
title: "Prefer Publish-Subscribe for events and Point-to-Point for..."
impact: LOW
impactDescription: "recommended but situational"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Prefer Publish-Subscribe for events and Point-to-Point for...

Prefer Publish-Subscribe for events and Point-to-Point for commands.

---

---
title: "Use Channel Adapters to isolate legacy integration code..."
impact: MEDIUM
impactDescription: "general best practice"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Use Channel Adapters to isolate legacy integration code...

Use Channel Adapters to isolate legacy integration code from business logic.

---

---
title: "Use Datatype Channels to keep consumers simple and avoid..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: messaging-channels, dev, integration-patterns, choosing-channel-types, point-to-point-vs-pub-sub, guaranteed-delivery
---

## Use Datatype Channels to keep consumers simple and avoid...

Use Datatype Channels to keep consumers simple and avoid content inspection.
