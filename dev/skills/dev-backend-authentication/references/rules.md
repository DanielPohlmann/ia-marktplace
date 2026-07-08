# Authentication & Authorization Patterns Rules

Best practices and rules for Authentication & Authorization Patterns.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use a managed identity provider (Auth0, Entra ID, Cognito,... | CRITICAL | [`authentication-use-a-managed-identity-provider-auth0-entra-id-cognito.md`](authentication-use-a-managed-identity-provider-auth0-entra-id-cognito.md) |
| 2 | Always use PKCE with the Authorization Code flow -- even... | CRITICAL | [`authentication-always-use-pkce-with-the-authorization-code-flow-even.md`](authentication-always-use-pkce-with-the-authorization-code-flow-even.md) |
| 3 | Keep access token lifetimes short (5-15 minutes) | MEDIUM | [`authentication-keep-access-token-lifetimes-short-5-15-minutes.md`](authentication-keep-access-token-lifetimes-short-5-15-minutes.md) |
| 4 | Check permissions, not roles, in your authorization code | MEDIUM | [`authentication-check-permissions-not-roles-in-your-authorization-code.md`](authentication-check-permissions-not-roles-in-your-authorization-code.md) |
| 5 | Implement row-level security or tenant-scoped queries as a... | CRITICAL | [`authentication-implement-row-level-security-or-tenant-scoped-queries-as-a.md`](authentication-implement-row-level-security-or-tenant-scoped-queries-as-a.md) |
| 6 | Set all security headers from day one | CRITICAL | [`authentication-set-all-security-headers-from-day-one.md`](authentication-set-all-security-headers-from-day-one.md) |
| 7 | Store secrets (API keys, client secrets, signing keys) in a... | CRITICAL | [`authentication-store-secrets-api-keys-client-secrets-signing-keys-in-a.md`](authentication-store-secrets-api-keys-client-secrets-signing-keys-in-a.md) |
| 8 | Rotate signing keys and refresh tokens regularly | MEDIUM | [`authentication-rotate-signing-keys-and-refresh-tokens-regularly.md`](authentication-rotate-signing-keys-and-refresh-tokens-regularly.md) |

---

---
title: "Always use PKCE with the Authorization Code flow -- even..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Always use PKCE with the Authorization Code flow -- even...

Always use PKCE with the Authorization Code flow -- even for server-side apps. It adds security with no meaningful cost.

---

---
title: "Check permissions, not roles, in your authorization code"
impact: MEDIUM
impactDescription: "general best practice"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Check permissions, not roles, in your authorization code

Check permissions, not roles, in your authorization code. This makes RBAC more granular and decouples business logic from role definitions.

---

---
title: "Implement row-level security or tenant-scoped queries as a..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Implement row-level security or tenant-scoped queries as a...

Implement row-level security or tenant-scoped queries as a defense-in-depth measure -- never rely solely on application-level tenant filtering.

---

---
title: "Keep access token lifetimes short (5-15 minutes)"
impact: MEDIUM
impactDescription: "general best practice"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Keep access token lifetimes short (5-15 minutes)

Keep access token lifetimes short (5-15 minutes). Use refresh tokens for longer sessions.

---

---
title: "Rotate signing keys and refresh tokens regularly"
impact: MEDIUM
impactDescription: "general best practice"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Rotate signing keys and refresh tokens regularly

Rotate signing keys and refresh tokens regularly. Implement token family revocation for refresh token reuse detection.

---

---
title: "Set all security headers from day one"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Set all security headers from day one

Set all security headers from day one. Adding HSTS, CSP, and CORS retroactively often breaks existing functionality.

---

---
title: "Store secrets (API keys, client secrets, signing keys) in a..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Store secrets (API keys, client secrets, signing keys) in a...

Store secrets (API keys, client secrets, signing keys) in a secrets manager (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault), never in code or environment variables in plain text.

---

---
title: "Use a managed identity provider (Auth0, Entra ID, Cognito,..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, dev, backend, authentication-design, authorization-models, oauth-20-flows
---

## Use a managed identity provider (Auth0, Entra ID, Cognito,...

Use a managed identity provider (Auth0, Entra ID, Cognito, Keycloak) instead of building authentication from scratch. Authentication is a security-critical function where the cost of getting it wrong is severe.
