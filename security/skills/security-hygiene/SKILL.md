---
name: security-hygiene
description: Use when treating data as untrusted at every component boundary, including internal DBs, caches, queues, and service calls. USE FOR: trust boundaries, sanitization, canonicalization, output encoding, zero-trust data handling, defense in depth. DO NOT USE FOR: injection rules at the edge (use security-input-validation), OWASP classification (use security-owasp), .NET-specific code (use stack-hygiene).
---

# Hygiene — Trust No Data

## Overview

Security hygiene is the discipline of treating **all data as untrusted** at every component boundary — not just data from end users. Internal databases, caches, message queues, partner APIs, configuration stores, and even your own microservices can deliver data that is malformed, stale, tampered with, or injected. A compromised internal system, a poisoned cache entry, or a corrupted database row can be just as dangerous as a malicious HTTP request.

The core principle: **sanitize, validate, and encode at the boundary of every component**, not just at the perimeter.

> "The Jenga tower of trust collapses when any single block is compromised. Don't assume the block below you is sound — verify it."

## Component Boundary Checklist

For every component boundary (inbound or outbound), verify:

| # | Check | Applies To |
|---|-------|-----------|
| 1 | **Type validation** — Is the data the expected type? | All inputs |
| 2 | **Format validation** — Does it match the expected pattern? | Strings, IDs, dates, emails |
| 3 | **Range validation** — Is it within acceptable bounds? | Numbers, dates, string lengths |
| 4 | **Canonicalization** — Is the data in its simplest canonical form? | Paths, URLs, Unicode strings |
| 5 | **Allowlist check** — Is the value in the set of permitted values? | Enums, status codes, roles |
| 6 | **Sanitization** — Have dangerous characters been removed or escaped? | All text inputs |
| 7 | **Output encoding** — Is data encoded for the destination context? | All outputs |
| 8 | **Size limits** — Is the data within acceptable size bounds? | Files, payloads, strings |

## Anti-Patterns

| Anti-Pattern | Why It's Dangerous | Correct Approach |
|-------------|-------------------|-----------------|
| "It's from our database, so it's safe" | Database can contain injected content from any entry point | Encode database values for the output context |
| "We validated it on the way in, so it's clean" | Output context may differ from input context; data may be modified in transit | Encode for the specific output context at point of use |
| "It's an internal API, so we trust it" | Internal services can be compromised or misconfigured | Validate response schema and sanitize values |
| "We use an ORM, so SQL injection is impossible" | Raw queries, dynamic column names, and ORDER BY bypass ORM protections | Always parameterize; review ORM escape hatches |
| "The cache just stores what we put in" | Cache can be poisoned via shared keys, race conditions, or unauthenticated access | Validate and encode cache values on read |
| "Config values are set by operators" | Environment variables and config stores can be compromised | Validate config values at startup; never pass raw to shell or template |

## Best Practices

- **Treat all data as untrusted** regardless of source — user input, databases, caches, queues, APIs, config, and files all deserve the same scrutiny.
- **Canonicalize before validating** — decode, normalize, and resolve data to its simplest form before applying security checks.
- **Encode at the point of use**, not at the point of storage — the correct encoding depends on where the data is going, not where it came from.
- **Validate on both sides of every boundary** — the producer should validate what it sends and the consumer should validate what it receives.
- **Use allowlists over denylists** — it is safer to define what is permitted than to try to enumerate everything that is dangerous.
- **Fail closed** — if data fails validation, reject it entirely rather than attempting to "fix" it and proceeding.
- **Apply the same rigor to outbound data** — log injection, email header injection, and downstream API injection are just as real as XSS.
- **Automate hygiene checks** — use linters, SAST rules (Semgrep, CodeQL), and code review checklists to catch missing validation and encoding at component boundaries.
- **Document trust boundaries** — make them explicit in architecture diagrams and threat models so every developer knows where hygiene enforcement is required.
- **Review ORM and framework escape hatches** — `dangerouslySetInnerHTML`, raw SQL, `HtmlString`, `@Html.Raw()`, `mark_safe()`, and similar constructs bypass built-in protections and require manual encoding.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/the-trust-boundary-model.md](references/the-trust-boundary-model.md) | The Trust Boundary Model — Why Internal Sources Are Untrusted |
| [references/canonicalization.md](references/canonicalization.md) | Canonicalization — Common Bypass Techniques Prevented by Canonicalization, Canonicalization Order, Language Examples |
| [references/output-encoding.md](references/output-encoding.md) | Output Encoding — Context-Specific Encoding, Encoding Data From Internal Sources |
| [references/details.md](references/details.md) | Sanitization |

## References

- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org)

See references/rules.md for the full rule catalog.
