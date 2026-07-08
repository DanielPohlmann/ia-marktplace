# API Security Rules

Best practices and rules for API Security.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Enforce HTTPS everywhere | CRITICAL | [`api-security-enforce-https-everywhere.md`](api-security-enforce-https-everywhere.md) |
| 2 | Validate all input on the server side | CRITICAL | [`api-security-validate-all-input-on-the-server-side.md`](api-security-validate-all-input-on-the-server-side.md) |
| 3 | Use the principle of least privilege for API scopes | HIGH | [`api-security-use-the-principle-of-least-privilege-for-api-scopes.md`](api-security-use-the-principle-of-least-privilege-for-api-scopes.md) |
| 4 | Implement defense in depth | CRITICAL | [`api-security-implement-defense-in-depth.md`](api-security-implement-defense-in-depth.md) |
| 5 | Return minimal error information | CRITICAL | [`api-security-return-minimal-error-information.md`](api-security-return-minimal-error-information.md) |
| 6 | Log all security-relevant events | CRITICAL | [`api-security-log-all-security-relevant-events.md`](api-security-log-all-security-relevant-events.md) |
| 7 | Version your APIs and deprecate securely | CRITICAL | [`api-security-version-your-apis-and-deprecate-securely.md`](api-security-version-your-apis-and-deprecate-securely.md) |
| 8 | Audit third-party API integrations | CRITICAL | [`api-security-audit-third-party-api-integrations.md`](api-security-audit-third-party-api-integrations.md) |

---

---
title: "Audit third-party API integrations"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Audit third-party API integrations

Audit third-party API integrations: review the security posture of external APIs your application depends on; validate their responses, enforce timeouts, and implement circuit breakers to prevent cascading failures.

---

---
title: "Enforce HTTPS everywhere"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Enforce HTTPS everywhere

Enforce HTTPS everywhere: never allow plaintext HTTP for any API endpoint; use HSTS headers to prevent downgrade attacks and configure TLS 1.2 as the minimum supported version.

---

---
title: "Implement defense in depth"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Implement defense in depth

Implement defense in depth: combine multiple security layers (gateway, authentication, authorization, input validation, rate limiting, monitoring) so that no single control failure results in a breach.

---

---
title: "Log all security-relevant events"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Log all security-relevant events

Log all security-relevant events: record authentication attempts, authorization failures, rate limit hits, and input validation rejections; feed logs into a SIEM for real-time alerting.

---

---
title: "Return minimal error information"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Return minimal error information

Return minimal error information: never expose stack traces, internal paths, or database error messages in API responses; use generic error messages with correlation IDs for debugging.

---

---
title: "Use the principle of least privilege for API scopes"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: api-security, security, rate-limiting, cors
---

## Use the principle of least privilege for API scopes

Use the principle of least privilege for API scopes: issue tokens with the minimum scopes and permissions required for the specific operation; avoid wildcard or admin scopes for routine operations.

---

---
title: "Validate all input on the server side"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Validate all input on the server side

Validate all input on the server side: never trust client-side validation alone; validate request bodies against schemas, enforce type and length constraints, and reject unexpected fields.

---

---
title: "Version your APIs and deprecate securely"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: api-security, security, rate-limiting, cors
---

## Version your APIs and deprecate securely

Version your APIs and deprecate securely: maintain security patches across all supported versions; when deprecating, provide clear timelines and ensure old versions are eventually decommissioned.
