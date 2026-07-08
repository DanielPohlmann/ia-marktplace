# ASP.NET Core Identity Rules

Best practices and rules for ASP.NET Core Identity.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Set password requirements to NIST guidelines | HIGH | [`aspnet-identity-set-password-requirements-to-nist-guidelines.md`](aspnet-identity-set-password-requirements-to-nist-guidelines.md) |
| 2 | Always enable account lockout | CRITICAL | [`aspnet-identity-always-enable-account-lockout.md`](aspnet-identity-always-enable-account-lockout.md) |
| 3 | Require email confirmation before login | HIGH | [`aspnet-identity-require-email-confirmation-before-login.md`](aspnet-identity-require-email-confirmation-before-login.md) |
| 4 | Use the built-in token providers | CRITICAL | [`aspnet-identity-use-the-built-in-token-providers.md`](aspnet-identity-use-the-built-in-token-providers.md) |
| 5 | Scope DbContext per request | CRITICAL | [`aspnet-identity-scope-dbcontext-per-request.md`](aspnet-identity-scope-dbcontext-per-request.md) |
| 6 | Prefer `AddIdentityCore<T>` over `AddIdentity<T>` | CRITICAL | [`aspnet-identity-prefer-addidentitycore-t-over-addidentity-t.md`](aspnet-identity-prefer-addidentitycore-t-over-addidentity-t.md) |
| 7 | Use `MapIdentityApi<T>()` for SPA and mobile backends | MEDIUM | [`aspnet-identity-use-mapidentityapi-t-for-spa-and-mobile-backends.md`](aspnet-identity-use-mapidentityapi-t-for-spa-and-mobile-backends.md) |
| 8 | Store sensitive Identity configuration in user secrets or a vault | CRITICAL | [`aspnet-identity-store-sensitive-identity-configuration-in-user-secrets-or-a.md`](aspnet-identity-store-sensitive-identity-configuration-in-user-secrets-or-a.md) |
| 9 | Enable two-factor authentication for elevated roles | HIGH | [`aspnet-identity-enable-two-factor-authentication-for-elevated-roles.md`](aspnet-identity-enable-two-factor-authentication-for-elevated-roles.md) |
| 10 | Audit authentication events | CRITICAL | [`aspnet-identity-audit-authentication-events.md`](aspnet-identity-audit-authentication-events.md) |

---

---
title: "Always enable account lockout"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Always enable account lockout

Always enable account lockout: configure `MaxFailedAccessAttempts` (5) and `DefaultLockoutTimeSpan` (15 minutes) to mitigate brute-force attacks while avoiding permanent lockout.

---

---
title: "Audit authentication events"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Audit authentication events

Audit authentication events: subscribe to `SecurityStampChanged` and log all sign-in attempts (success, failure, lockout) for compliance and incident response.

---

---
title: "Enable two-factor authentication for elevated roles"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Enable two-factor authentication for elevated roles

Enable two-factor authentication for elevated roles: require 2FA for admin accounts by combining `RequiresTwoFactor` checks with role-based policies.

---

---
title: "Prefer `AddIdentityCore<T>` over `AddIdentity<T>`"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Prefer `AddIdentityCore<T>` over `AddIdentity<T>`

Prefer `AddIdentityCore<T>` over `AddIdentity<T>`: in API projects to avoid pulling in cookie-based UI dependencies you do not need.

---

---
title: "Require email confirmation before login"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Require email confirmation before login

Require email confirmation before login: set `SignIn.RequireConfirmedEmail = true` and send confirmation tokens via `GenerateEmailConfirmationTokenAsync` to verify account ownership.

---

---
title: "Scope DbContext per request"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Scope DbContext per request

Scope DbContext per request: register `AppDbContext` as scoped to prevent concurrency issues; never share a single DbContext across multiple requests.

---

---
title: "Set password requirements to NIST guidelines"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Set password requirements to NIST guidelines

Set password requirements to NIST guidelines: require minimum 12 characters, check against breached password lists using `IPasswordValidator<TUser>`, and avoid arbitrary complexity rules that frustrate users.

---

---
title: "Store sensitive Identity configuration in user secrets or a vault"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Store sensitive Identity configuration in user secrets or a vault

Store sensitive Identity configuration in user secrets or a vault: never hardcode connection strings, token signing keys, or external provider credentials in `appsettings.json`.

---

---
title: "Use `MapIdentityApi<T>()` for SPA and mobile backends"
impact: MEDIUM
impactDescription: "general best practice"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Use `MapIdentityApi<T>()` for SPA and mobile backends

Use `MapIdentityApi<T>()` for SPA and mobile backends: the built-in Identity API endpoints (available in .NET 8+) provide standardized token flows without manual controller code.

---

---
title: "Use the built-in token providers"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: aspnet-identity, dotnet, security, user-registration, loginlogout-flows, password-management
---

## Use the built-in token providers

Use the built-in token providers: never implement custom password reset or confirmation token generation; use `GeneratePasswordResetTokenAsync` and `GenerateEmailConfirmationTokenAsync`.
