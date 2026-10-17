<!-- Part of the dev-backend-authentication skill. Loaded on demand from SKILL.md. -->

# JWT (JSON Web Token)

## Structure

```
header.payload.signature

Header (base64url):
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "key-2024-01"
}

Payload (base64url):
{
  "iss": "https://auth.example.com",
  "sub": "user_42",
  "aud": "https://api.example.com",
  "exp": 1705312800,
  "iat": 1705309200,
  "scope": "read:orders write:orders",
  "roles": ["admin"],
  "tenant_id": "org_acme"
}

Signature:
  RS256(base64url(header) + "." + base64url(payload), private_key)
```

## Standard Claims

| Claim | Purpose |
|-------|---------|
| `iss` | Issuer -- who created the token |
| `sub` | Subject -- who the token represents |
| `aud` | Audience -- who the token is intended for |
| `exp` | Expiration time (Unix timestamp) |
| `iat` | Issued at time |
| `nbf` | Not before -- token is not valid before this time |
| `jti` | JWT ID -- unique identifier for the token |

## Access Tokens vs. Refresh Tokens

| Property | Access Token | Refresh Token |
|----------|-------------|---------------|
| **Purpose** | Authorize API requests | Obtain new access tokens |
| **Lifetime** | Short (5-60 minutes) | Long (hours to days) |
| **Stored** | Memory (preferred) or secure cookie | Secure, HttpOnly cookie or secure storage |
| **Sent to** | Resource server (API) | Authorization server only |
| **Revocable** | Difficult (until expiry) | Yes (server-side revocation list) |

## Token Rotation

Refresh token rotation issues a new refresh token with every access token refresh. If a refresh token is used twice, the server assumes the original was stolen and revokes the entire token family.

```
1. Client sends refresh_token_v1 → Server returns access_token + refresh_token_v2
2. Client sends refresh_token_v2 → Server returns access_token + refresh_token_v3
3. Attacker sends refresh_token_v1 → Server detects reuse → revokes ALL tokens for user
```
