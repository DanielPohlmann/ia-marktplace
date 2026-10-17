---
name: dev-backend-authentication
description: Use when designing authentication and authorization at the architecture level. USE FOR: OAuth 2.0 flow choice (PKCE, client credentials, device code), JWT design, session vs token, RBAC/ABAC, multi-tenancy isolation, IdP choice, CORS and security headers. DO NOT USE FOR: auth threat analysis (use security-authentication), ASP.NET Core Identity code (use stack-aspnet-identity), endpoint design (use dev-backend-api-design).
---

# Authentication & Authorization Patterns

## Overview
Authentication (authn) verifies *who* a user is. Authorization (authz) determines *what* they can do. Getting these right is non-negotiable -- a flaw in either can expose user data, enable privilege escalation, or bring regulatory consequences. This skill covers the major authentication flows, token formats, authorization models, multi-tenancy patterns, and security headers needed to build secure backend systems.

## OpenID Connect (OIDC)

OIDC is an identity layer built on top of OAuth 2.0. It adds:

| Component | Purpose |
|-----------|---------|
| **ID Token** | A JWT containing user identity claims (sub, email, name) -- proves who the user is |
| **UserInfo Endpoint** | `GET /userinfo` returns additional user profile claims |
| **Discovery** | `GET /.well-known/openid-configuration` returns all endpoint URLs, supported scopes, signing algorithms |
| **Standard Scopes** | `openid` (required), `profile`, `email`, `address`, `phone` |

**Key distinction:** OAuth 2.0 alone is for *authorization* (access to resources). OIDC adds *authentication* (identity of the user).

## API Key Authentication

Appropriate for:
- Server-to-server communication where OAuth is overkill.
- Public APIs with usage-based billing (keys identify the caller for rate limiting and billing).
- Development/testing environments.

**Not appropriate for:** User-facing authentication (API keys cannot represent user identity or consent).

**Best practices:**
- Treat API keys as secrets. Hash them in storage (like passwords).
- Support key rotation: allow multiple active keys per client.
- Include the key in a header (`X-API-Key` or `Authorization: Bearer`), never in the URL.
- Scope keys to specific permissions and rate limits.

## Best Practices
- Use a managed identity provider (Auth0, Entra ID, Cognito, Keycloak) instead of building authentication from scratch. Authentication is a security-critical function where the cost of getting it wrong is severe.
- Always use PKCE with the Authorization Code flow -- even for server-side apps. It adds security with no meaningful cost.
- Keep access token lifetimes short (5-15 minutes). Use refresh tokens for longer sessions.
- Check permissions, not roles, in your authorization code. This makes RBAC more granular and decouples business logic from role definitions.
- Implement row-level security or tenant-scoped queries as a defense-in-depth measure -- never rely solely on application-level tenant filtering.
- Set all security headers from day one. Adding HSTS, CSP, and CORS retroactively often breaks existing functionality.
- Store secrets (API keys, client secrets, signing keys) in a secrets manager (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault), never in code or environment variables in plain text.
- Rotate signing keys and refresh tokens regularly. Implement token family revocation for refresh token reuse detection.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/oauth-2-0-flows.md](references/oauth-2-0-flows.md) | OAuth 2.0 Flows — Authorization Code + PKCE (Recommended for Most Apps), Client Credentials (Machine-to-Machine), Device Code (TV / IoT / CLI) |
| [references/jwt-json-web-token.md](references/jwt-json-web-token.md) | JWT (JSON Web Token) — Structure, Standard Claims, Access Tokens vs. Refresh Tokens, Token Rotation |
| [references/details.md](references/details.md) | Session-Based Authentication; RBAC (Role-Based Access Control); ABAC (Attribute-Based Access Control); Multi-Tenancy Patterns; Identity Providers; Security Headers |

## References

- [OAuth 2.0 — RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)
- [OAuth.net — OAuth 2.0](https://oauth.net/2/)
- [JSON Web Tokens — jwt.io](https://jwt.io/introduction)

See references/rules.md for the full rule catalog.
