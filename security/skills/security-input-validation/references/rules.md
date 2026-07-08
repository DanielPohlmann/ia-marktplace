# Input Validation & Output Encoding Rules

Best practices and rules for Input Validation & Output Encoding.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Validate all input on the server side | CRITICAL | [`input-validation-validate-all-input-on-the-server-side.md`](input-validation-validate-all-input-on-the-server-side.md) |
| 2 | Use allowlist validation | MEDIUM | [`input-validation-use-allowlist-validation.md`](input-validation-use-allowlist-validation.md) |
| 3 | Normalize input before validation | MEDIUM | [`input-validation-normalize-input-before-validation.md`](input-validation-normalize-input-before-validation.md) |
| 4 | Encode output for its specific context | HIGH | [`input-validation-encode-output-for-its-specific-context.md`](input-validation-encode-output-for-its-specific-context.md) |
| 5 | Use parameterized queries for all database access | CRITICAL | [`input-validation-use-parameterized-queries-for-all-database-access.md`](input-validation-use-parameterized-queries-for-all-database-access.md) |
| 6 | Avoid shell execution with user input | HIGH | [`input-validation-avoid-shell-execution-with-user-input.md`](input-validation-avoid-shell-execution-with-user-input.md) |
| 7 | Deploy Content Security Policy (CSP) headers | CRITICAL | [`input-validation-deploy-content-security-policy-csp-headers.md`](input-validation-deploy-content-security-policy-csp-headers.md) |
| 8 | Audit framework escape hatches | MEDIUM | [`input-validation-audit-framework-escape-hatches.md`](input-validation-audit-framework-escape-hatches.md) |

---

---
title: "Audit framework escape hatches"
impact: MEDIUM
impactDescription: "general best practice"
tags: input-validation, security, output-encoding, xss-prevention
---

## Audit framework escape hatches

Audit framework escape hatches: review all uses of `dangerouslySetInnerHTML`, `Html.Raw()`, `|safe`, `th:utext`, and similar raw-output functions during code review.

---

---
title: "Avoid shell execution with user input"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: input-validation, security, output-encoding, xss-prevention
---

## Avoid shell execution with user input

Avoid shell execution with user input: use language-native APIs with argument arrays instead of constructing shell command strings.

---

---
title: "Deploy Content Security Policy (CSP) headers"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: input-validation, security, output-encoding, xss-prevention
---

## Deploy Content Security Policy (CSP) headers

CSP provides an additional layer of defense against XSS even when encoding is missed.

---

---
title: "Encode output for its specific context"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: input-validation, security, output-encoding, xss-prevention
---

## Encode output for its specific context

HTML, JavaScript, URL, CSS, and SQL each require different encoding; there is no universal encoder.

---

---
title: "Normalize input before validation"
impact: MEDIUM
impactDescription: "general best practice"
tags: input-validation, security, output-encoding, xss-prevention
---

## Normalize input before validation

Normalize input before validation: canonicalize Unicode, decode URL encoding, and trim whitespace before applying validation rules.

---

---
title: "Use allowlist validation"
impact: MEDIUM
impactDescription: "general best practice"
tags: input-validation, security, output-encoding, xss-prevention
---

## Use allowlist validation

Use allowlist validation: define what is permitted and reject everything else; denylist approaches are inherently incomplete.

---

---
title: "Use parameterized queries for all database access"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: input-validation, security, output-encoding, xss-prevention
---

## Use parameterized queries for all database access

Use parameterized queries for all database access: never concatenate user input into SQL, regardless of prior validation.

---

---
title: "Validate all input on the server side"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: input-validation, security, output-encoding, xss-prevention
---

## Validate all input on the server side

Validate all input on the server side: never rely on client-side validation for security.
