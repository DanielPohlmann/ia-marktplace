# Hygiene Rules

Best practices and rules for Hygiene.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Treat all data as untrusted | MEDIUM | [`hygiene-treat-all-data-as-untrusted.md`](hygiene-treat-all-data-as-untrusted.md) |
| 2 | Canonicalize before validating | CRITICAL | [`hygiene-canonicalize-before-validating.md`](hygiene-canonicalize-before-validating.md) |
| 3 | Encode at the point of use | MEDIUM | [`hygiene-encode-at-the-point-of-use.md`](hygiene-encode-at-the-point-of-use.md) |
| 4 | Validate on both sides of every boundary | HIGH | [`hygiene-validate-on-both-sides-of-every-boundary.md`](hygiene-validate-on-both-sides-of-every-boundary.md) |
| 5 | Use allowlists over denylists | MEDIUM | [`hygiene-use-allowlists-over-denylists.md`](hygiene-use-allowlists-over-denylists.md) |
| 6 | Fail closed | MEDIUM | [`hygiene-fail-closed.md`](hygiene-fail-closed.md) |
| 7 | Apply the same rigor to outbound data | CRITICAL | [`hygiene-apply-the-same-rigor-to-outbound-data.md`](hygiene-apply-the-same-rigor-to-outbound-data.md) |
| 8 | Automate hygiene checks | MEDIUM | [`hygiene-automate-hygiene-checks.md`](hygiene-automate-hygiene-checks.md) |
| 9 | Document trust boundaries | HIGH | [`hygiene-document-trust-boundaries.md`](hygiene-document-trust-boundaries.md) |
| 10 | Review ORM and framework escape hatches | HIGH | [`hygiene-review-orm-and-framework-escape-hatches.md`](hygiene-review-orm-and-framework-escape-hatches.md) |

---

---
title: "Apply the same rigor to outbound data"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Apply the same rigor to outbound data

Apply the same rigor to outbound data: log injection, email header injection, and downstream API injection are just as real as XSS.

---

---
title: "Automate hygiene checks"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Automate hygiene checks

Automate hygiene checks: use linters, SAST rules (Semgrep, CodeQL), and code review checklists to catch missing validation and encoding at component boundaries.

---

---
title: "Canonicalize before validating"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Canonicalize before validating

Canonicalize before validating: decode, normalize, and resolve data to its simplest form before applying security checks.

---

---
title: "Document trust boundaries"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Document trust boundaries

Document trust boundaries: make them explicit in architecture diagrams and threat models so every developer knows where hygiene enforcement is required.

---

---
title: "Encode at the point of use"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Encode at the point of use

, not at the point of storage — the correct encoding depends on where the data is going, not where it came from.

---

---
title: "Fail closed"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Fail closed

Fail closed: if data fails validation, reject it entirely rather than attempting to "fix" it and proceeding.

---

---
title: "Review ORM and framework escape hatches"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Review ORM and framework escape hatches

`dangerouslySetInnerHTML`, raw SQL, `HtmlString`, `@Html.Raw()`, `mark_safe()`, and similar constructs bypass built-in protections and require manual encoding.

---

---
title: "Treat all data as untrusted"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Treat all data as untrusted

Treat all data as untrusted: regardless of source — user input, databases, caches, queues, APIs, config, and files all deserve the same scrutiny.

---

---
title: "Use allowlists over denylists"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Use allowlists over denylists

Use allowlists over denylists: it is safer to define what is permitted than to try to enumerate everything that is dangerous.

---

---
title: "Validate on both sides of every boundary"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: hygiene, security, data-hygiene, sanitization, canonicalization
---

## Validate on both sides of every boundary

Validate on both sides of every boundary: the producer should validate what it sends and the consumer should validate what it receives.
