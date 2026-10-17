---
name: security-authentication
description: Use when assessing authentication and authorization threats and mitigations. USE FOR: OAuth 2.0/OIDC security, RBAC/ABAC/ReBAC, Zero Trust, session security, MFA threats, JWT security, SSO, federation. DO NOT USE FOR: ASP.NET Core Identity code (use stack-aspnet-identity), TLS and crypto (use security-cryptography), auth architecture design (use dev-backend-authentication).
---

# Authentication & Authorization

## Overview

Authentication (AuthN) and authorization (AuthZ) are distinct but tightly coupled security concerns. Authentication answers the question "Who are you?" by verifying a user's or service's identity through credentials, tokens, or certificates. Authorization answers the question "What are you allowed to do?" by determining whether an authenticated identity has permission to access a resource or perform an action. A secure system requires both: authentication without authorization means anyone who logs in can do anything, while authorization without authentication means permissions are assigned to identities that have not been verified. This skill covers the protocols, patterns, and best practices for implementing both concerns across all platforms and frameworks.

## JWT Best Practices

JSON Web Tokens (JWTs) are widely used for stateless authentication and authorization. Improper use of JWTs is a common source of security vulnerabilities.

- **Signing algorithms**: Use asymmetric algorithms (`RS256`, `ES256`) for tokens that are verified by multiple services. Use `HS256` only when the same service both signs and verifies. Never allow `"alg": "none"`.
- **Expiry**: Always set the `exp` (expiration) claim. Access tokens should be short-lived (5-15 minutes). Use refresh tokens for longer sessions.
- **Audience and issuer**: Always set and validate the `aud` (audience) and `iss` (issuer) claims to prevent token misuse across services.
- **Claims**: Include only the minimum necessary claims in the payload. JWTs are signed, not encrypted by default -- their contents are readable by anyone with the token.
- **Never store sensitive data in the payload**: Do not include passwords, secrets, PII, or other sensitive information in JWT claims. Use the token as a reference to server-side state if sensitive data is needed.
- **Token revocation**: JWTs are stateless and cannot be individually revoked. Implement a token deny-list (blocklist) for critical revocation scenarios, or use short expiry times with refresh token rotation.
- **Key rotation**: Rotate signing keys periodically. Use the `kid` (Key ID) header to support multiple active keys during rotation. Publish public keys via a JWKS (JSON Web Key Set) endpoint.

## Best Practices

- **Use established protocols**: implement OAuth 2.0 and OpenID Connect rather than designing custom authentication schemes. Custom auth is almost always less secure than battle-tested standards.
- **Always use PKCE**: regardless of client type, use PKCE with the Authorization Code flow. It adds protection against code interception attacks at negligible implementation cost.
- **Enforce MFA for all privileged accounts**: at minimum, require MFA for administrators, operators, and any account with access to sensitive data or infrastructure. Prefer phishing-resistant methods (WebAuthn/FIDO2).
- **Implement token rotation**: use short-lived access tokens paired with longer-lived refresh tokens that are rotated on each use (refresh token rotation). Detect and revoke token families on reuse.
- **Centralize identity management**: use a dedicated identity provider (IdP) rather than implementing authentication in each service. This provides a single point for policy enforcement, auditing, and credential management.
- **Apply least privilege at every layer**: combine RBAC or ABAC with resource-level authorization checks. Never rely solely on role membership -- validate that the specific user has access to the specific resource being requested.
- **Secure the session lifecycle end-to-end**: regenerate session identifiers after login, enforce idle and absolute timeouts, invalidate sessions on both client and server during logout, and use secure cookie attributes on every session cookie.
- **Log all authentication events**: record successful logins, failed attempts, token issuance, refresh, revocation, and privilege changes. Feed these events into monitoring systems to detect credential stuffing, brute force attacks, and anomalous access patterns.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | OAuth 2.0 Flows; OpenID Connect (OIDC); Access Control Models; Zero Trust Architecture; Session Management; Multi-Factor Authentication (MFA) |

## References

- [OAuth 2.0 Authorization Framework (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)
- [OpenID Connect Specification](https://openid.net/developers/specs/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

See references/rules.md for the full rule catalog.
