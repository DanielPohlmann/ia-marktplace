# Message Construction Rules

Best practices and rules for Message Construction.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Give every message a unique `messageId` -- it is the... | MEDIUM | [`message-construction-give-every-message-a-unique-messageid-it-is-the.md`](message-construction-give-every-message-a-unique-messageid-it-is-the.md) |
| 2 | Prefer Event Messages for cross-service communication; they... | LOW | [`message-construction-prefer-event-messages-for-cross-service-communication-they.md`](message-construction-prefer-event-messages-for-cross-service-communication-they.md) |
| 3 | Use Command Messages only when you intend exactly one... | MEDIUM | [`message-construction-use-command-messages-only-when-you-intend-exactly-one.md`](message-construction-use-command-messages-only-when-you-intend-exactly-one.md) |
| 4 | Always include a `correlationId` in replies so requestors... | CRITICAL | [`message-construction-always-include-a-correlationid-in-replies-so-requestors.md`](message-construction-always-include-a-correlationid-in-replies-so-requestors.md) |
| 5 | Set `expiration` on time-sensitive messages rather than... | MEDIUM | [`message-construction-set-expiration-on-time-sensitive-messages-rather-than.md`](message-construction-set-expiration-on-time-sensitive-messages-rather-than.md) |
| 6 | Version your message schemas from day one using Format... | MEDIUM | [`message-construction-version-your-message-schemas-from-day-one-using-format.md`](message-construction-version-your-message-schemas-from-day-one-using-format.md) |
| 7 | Keep message bodies lean -- carry references (IDs, URIs)... | MEDIUM | [`message-construction-keep-message-bodies-lean-carry-references-ids-uris.md`](message-construction-keep-message-bodies-lean-carry-references-ids-uris.md) |
| 8 | Include `timestamp` and `source` in every message for... | MEDIUM | [`message-construction-include-timestamp-and-source-in-every-message-for.md`](message-construction-include-timestamp-and-source-in-every-message-for.md) |

---

---
title: "Always include a `correlationId` in replies so requestors..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Always include a `correlationId` in replies so requestors...

Always include a `correlationId` in replies so requestors can match responses.

---

---
title: "Give every message a unique `messageId` -- it is the..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Give every message a unique `messageId` -- it is the...

Give every message a unique `messageId` -- it is the foundation of idempotency, deduplication, and correlation.

---

---
title: "Include `timestamp` and `source` in every message for..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Include `timestamp` and `source` in every message for...

Include `timestamp` and `source` in every message for observability and debugging.

---

---
title: "Keep message bodies lean -- carry references (IDs, URIs)..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Keep message bodies lean -- carry references (IDs, URIs)...

Keep message bodies lean -- carry references (IDs, URIs) rather than full object graphs when possible.

---

---
title: "Prefer Event Messages for cross-service communication; they..."
impact: LOW
impactDescription: "recommended but situational"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Prefer Event Messages for cross-service communication; they...

Prefer Event Messages for cross-service communication; they create the loosest coupling.

---

---
title: "Set `expiration` on time-sensitive messages rather than..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Set `expiration` on time-sensitive messages rather than...

Set `expiration` on time-sensitive messages rather than relying on consumers to check timestamps.

---

---
title: "Use Command Messages only when you intend exactly one..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Use Command Messages only when you intend exactly one...

Use Command Messages only when you intend exactly one receiver to act.

---

---
title: "Version your message schemas from day one using Format..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-construction, dev, integration-patterns, message-types, command-vs-event-vs-document-messages, request-reply
---

## Version your message schemas from day one using Format...

Version your message schemas from day one using Format Indicator; schema evolution is inevitable.
