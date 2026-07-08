# Authentication & Authorization Rules

Best practices and rules for Authentication & Authorization.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use established protocols | CRITICAL | [`authentication-use-established-protocols.md`](authentication-use-established-protocols.md) |
| 2 | Always use PKCE | CRITICAL | [`authentication-always-use-pkce.md`](authentication-always-use-pkce.md) |
| 3 | Enforce MFA for all privileged accounts | HIGH | [`authentication-enforce-mfa-for-all-privileged-accounts.md`](authentication-enforce-mfa-for-all-privileged-accounts.md) |
| 4 | Implement token rotation | MEDIUM | [`authentication-implement-token-rotation.md`](authentication-implement-token-rotation.md) |
| 5 | Centralize identity management | CRITICAL | [`authentication-centralize-identity-management.md`](authentication-centralize-identity-management.md) |
| 6 | Apply least privilege at every layer | CRITICAL | [`authentication-apply-least-privilege-at-every-layer.md`](authentication-apply-least-privilege-at-every-layer.md) |
| 7 | Secure the session lifecycle end-to-end | HIGH | [`authentication-secure-the-session-lifecycle-end-to-end.md`](authentication-secure-the-session-lifecycle-end-to-end.md) |
| 8 | Log all authentication events | CRITICAL | [`authentication-log-all-authentication-events.md`](authentication-log-all-authentication-events.md) |

---

---
title: "Always use PKCE"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Always use PKCE

Always use PKCE: regardless of client type, use PKCE with the Authorization Code flow. It adds protection against code interception attacks at negligible implementation cost.

---

---
title: "Apply least privilege at every layer"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Apply least privilege at every layer

Apply least privilege at every layer: combine RBAC or ABAC with resource-level authorization checks. Never rely solely on role membership -- validate that the specific user has access to the specific resource being requested.

---

---
title: "Centralize identity management"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Centralize identity management

Centralize identity management: use a dedicated identity provider (IdP) rather than implementing authentication in each service. This provides a single point for policy enforcement, auditing, and credential management.

---

---
title: "Enforce MFA for all privileged accounts"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Enforce MFA for all privileged accounts

Enforce MFA for all privileged accounts: at minimum, require MFA for administrators, operators, and any account with access to sensitive data or infrastructure. Prefer phishing-resistant methods (WebAuthn/FIDO2).

---

---
title: "Implement token rotation"
impact: MEDIUM
impactDescription: "general best practice"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Implement token rotation

Implement token rotation: use short-lived access tokens paired with longer-lived refresh tokens that are rotated on each use (refresh token rotation). Detect and revoke token families on reuse.

---

---
title: "Log all authentication events"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Log all authentication events

Log all authentication events: record successful logins, failed attempts, token issuance, refresh, revocation, and privilege changes. Feed these events into monitoring systems to detect credential stuffing, brute force attacks, and anomalous access patterns.

---

---
title: "Secure the session lifecycle end-to-end"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Secure the session lifecycle end-to-end

Secure the session lifecycle end-to-end: regenerate session identifiers after login, enforce idle and absolute timeouts, invalidate sessions on both client and server during logout, and use secure cookie attributes on every session cookie.

---

---
title: "Use established protocols"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: authentication, security, oauth-20, openid-connect, oidc
---

## Use established protocols

Use established protocols: implement OAuth 2.0 and OpenID Connect rather than designing custom authentication schemes. Custom auth is almost always less secure than battle-tested standards.
