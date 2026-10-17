---
name: security-api-security
description: Use when hardening REST API endpoints against common attacks. USE FOR: rate limiting, CORS, CSP, security headers, API keys, OAuth for APIs, gateway controls, HTTPS enforcement, request limits. DO NOT USE FOR: API contract design (use dev-backend-api-design), OpenAPI docs (use stack-openapi), auth protocol design (use security-authentication).
---

# API Security

## Overview

APIs are the primary attack surface of modern applications. As architectures shift toward microservices, serverless functions, and third-party integrations, the number of exposed API endpoints grows dramatically. Every endpoint is a potential entry point for attackers. Securing APIs requires a layered approach that includes transport security, authentication, authorization, input validation, rate limiting, and proper response handling. A single misconfigured header or overly permissive CORS policy can expose an entire system.

## Best Practices

- **Enforce HTTPS everywhere** — never allow plaintext HTTP for any API endpoint; use HSTS headers to prevent downgrade attacks and configure TLS 1.2 as the minimum supported version.
- **Validate all input on the server side** — never trust client-side validation alone; validate request bodies against schemas, enforce type and length constraints, and reject unexpected fields.
- **Use the principle of least privilege for API scopes** — issue tokens with the minimum scopes and permissions required for the specific operation; avoid wildcard or admin scopes for routine operations.
- **Implement defense in depth** — combine multiple security layers (gateway, authentication, authorization, input validation, rate limiting, monitoring) so that no single control failure results in a breach.
- **Return minimal error information** — never expose stack traces, internal paths, or database error messages in API responses; use generic error messages with correlation IDs for debugging.
- **Log all security-relevant events** — record authentication attempts, authorization failures, rate limit hits, and input validation rejections; feed logs into a SIEM for real-time alerting.
- **Version your APIs and deprecate securely** — maintain security patches across all supported versions; when deprecating, provide clear timelines and ensure old versions are eventually decommissioned.
- **Audit third-party API integrations** — review the security posture of external APIs your application depends on; validate their responses, enforce timeouts, and implement circuit breakers to prevent cascading failures.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/rate-limiting.md](references/rate-limiting.md) | Rate Limiting |
| [references/details.md](references/details.md) | Security Headers; CORS Configuration; Content Security Policy; API Authentication; API Gateway Security |

## References

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [MDN Web Docs: Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

See references/rules.md for the full rule catalog.
