# Security Hygiene & Sanitization Rules

Best practices and rules for Security Hygiene & Sanitization.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Encode output for its specific rendering context | CRITICAL | [`hygiene-encode-output-for-its-specific-rendering-context.md`](hygiene-encode-output-for-its-specific-rendering-context.md) |
| 2 | Use parameterized queries everywhere without exception | CRITICAL | [`hygiene-use-parameterized-queries-everywhere-without-exception.md`](hygiene-use-parameterized-queries-everywhere-without-exception.md) |
| 3 | Validate input at the API boundary with allowlists | HIGH | [`hygiene-validate-input-at-the-api-boundary-with-allowlists.md`](hygiene-validate-input-at-the-api-boundary-with-allowlists.md) |
| 4 | Apply security headers via middleware early in the pipeline | CRITICAL | [`hygiene-apply-security-headers-via-middleware-early-in-the-pipeline.md`](hygiene-apply-security-headers-via-middleware-early-in-the-pipeline.md) |
| 5 | Set cookies with HttpOnly, Secure, and SameSite=Strict | HIGH | [`hygiene-set-cookies-with-httponly-secure-and-samesite-strict.md`](hygiene-set-cookies-with-httponly-secure-and-samesite-strict.md) |
| 6 | Use `Path.GetFullPath` and verify the canonical path prefix | HIGH | [`hygiene-use-path-getfullpath-and-verify-the-canonical-path-prefix.md`](hygiene-use-path-getfullpath-and-verify-the-canonical-path-prefix.md) |
| 7 | Never disable request validation or model binding validation | CRITICAL | [`hygiene-never-disable-request-validation-or-model-binding-validation.md`](hygiene-never-disable-request-validation-or-model-binding-validation.md) |
| 8 | Configure Content Security Policy to block inline scripts | CRITICAL | [`hygiene-configure-content-security-policy-to-block-inline-scripts.md`](hygiene-configure-content-security-policy-to-block-inline-scripts.md) |
| 9 | Log all validation failures with the source IP and input value | CRITICAL | [`hygiene-log-all-validation-failures-with-the-source-ip-and-input.md`](hygiene-log-all-validation-failures-with-the-source-ip-and-input.md) |
| 10 | Run static analysis with `dotnet format` and security analyzers | CRITICAL | [`hygiene-run-static-analysis-with-dotnet-format-and-security.md`](hygiene-run-static-analysis-with-dotnet-format-and-security.md) |

---

---
title: "Always validate and sanitize user input"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security
---

## Always validate and sanitize user input

Always validate and sanitize user input

---

---
title: "Apply security headers via middleware early in the pipeline"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Apply security headers via middleware early in the pipeline

Apply security headers via middleware early in the pipeline: register `UseSecurityHeaders()` before `UseRouting()` so every response, including error pages, includes protective headers.

---

---
title: "Configure Content Security Policy to block inline scripts"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Configure Content Security Policy to block inline scripts

Configure Content Security Policy to block inline scripts: use `script-src 'self'` without `'unsafe-inline'` and move all JavaScript to external files to prevent XSS through injected script tags.

---

---
title: "Encode output based on context (HTML, URL, JS)"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, dotnet, security
---

## Encode output based on context (HTML, URL, JS)

Encode output based on context (HTML, URL, JS)

---

---
title: "Encode output for its specific rendering context"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Encode output for its specific rendering context

Encode output for its specific rendering context: use `HtmlEncoder` for HTML bodies, `UrlEncoder` for URLs, and `JavaScriptEncoder` for inline scripts; never use a single encoding function for all contexts.

---

---
title: "Implement allowlists over blocklists"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, dotnet, security
---

## Implement allowlists over blocklists

Implement allowlists over blocklists

---

---
title: "Log all validation failures with the source IP and input value"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Log all validation failures with the source IP and input value

Log all validation failures with the source IP and input value: track rejected inputs for threat intelligence, but sanitize the logged values to prevent log injection attacks.

---

---
title: "Never disable request validation or model binding validation"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Never disable request validation or model binding validation

Never disable request validation or model binding validation: if `ModelState.IsValid` is false, return `ValidationProblem()` immediately; do not proceed with invalid data.

---

---
title: "Never trust client-side validation alone"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security
---

## Never trust client-side validation alone

Never trust client-side validation alone

---

---
title: "Run static analysis with `dotnet format` and security analyzers"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Run static analysis with `dotnet format` and security analyzers

Run static analysis with `dotnet format` and security analyzers: enable Roslyn security analyzers (`Microsoft.CodeAnalysis.NetAnalyzers`) to catch insecure patterns like string concatenation in SQL at compile time.

---

---
title: "Set cookies with HttpOnly, Secure, and SameSite=Strict"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Set cookies with HttpOnly, Secure, and SameSite=Strict

Set cookies with HttpOnly, Secure, and SameSite=Strict: prevent JavaScript access to cookies with `HttpOnly`, require HTTPS with `Secure`, and block cross-origin sends with `SameSite`.

---

---
title: "Use built-in sanitization libraries"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, dotnet, security
---

## Use built-in sanitization libraries

Use built-in sanitization libraries

---

---
title: "Use parameterized queries everywhere without exception"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Use parameterized queries everywhere without exception

Use parameterized queries everywhere without exception: even for queries that appear safe today, always use `@param` syntax to prevent SQL injection if the query evolves to include user input later.

---

---
title: "Use parameterized queries"
impact: MEDIUM
impactDescription: "general best practice"
tags: hygiene, dotnet, security
---

## Use parameterized queries

Use parameterized queries

---

---
title: "Use `Path.GetFullPath` and verify the canonical path prefix"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Use `Path.GetFullPath` and verify the canonical path prefix

Use `Path.GetFullPath` and verify the canonical path prefix: after resolving a user-supplied file name, confirm the full path starts with your allowed directory to prevent `../` traversal.

---

---
title: "Validate input at the API boundary with allowlists"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: hygiene, dotnet, security, preventing-xss-attacks, sql-injection-prevention, htmlurljavascript-encoding
---

## Validate input at the API boundary with allowlists

Validate input at the API boundary with allowlists: use `[RegularExpression]` and `[StringLength]` data annotations to define what valid input looks like rather than trying to blocklist dangerous characters.
