<!-- Part of the dev-backend-authentication skill. Loaded on demand from SKILL.md. -->

# OAuth 2.0 Flows

## Authorization Code + PKCE (Recommended for Most Apps)

The most secure flow for user-facing applications (SPAs, mobile apps, server-rendered apps). PKCE (Proof Key for Code Exchange) prevents authorization code interception attacks.

```
┌──────────┐                              ┌──────────────┐
│  Client   │──1. Auth request + ─────────>│ Authorization│
│  (Browser/│    code_challenge            │   Server     │
│   Mobile) │<──2. Redirect with ─────────│              │
│           │    authorization code        │              │
│           │──3. Exchange code + ─────────>│              │
│           │    code_verifier             │              │
│           │<──4. Access token + ─────────│              │
│           │    refresh token             │              │
└──────────┘                              └──────────────┘
       │                                         │
       │──5. API request with ──────────>┌──────────────┐
       │    Bearer access_token          │  Resource     │
       │<──6. Protected resource ────────│  Server       │
       │                                 └──────────────┘
```

**Steps:**
1. Client generates a random `code_verifier` and derives `code_challenge = SHA256(code_verifier)`.
2. Client redirects user to authorization server with `code_challenge`.
3. User authenticates and consents. Authorization server redirects back with an authorization code.
4. Client exchanges the code + `code_verifier` for tokens. Server verifies `SHA256(code_verifier) == code_challenge`.
5. Client uses the access token to call APIs.

## Client Credentials (Machine-to-Machine)

For service-to-service communication where no user is involved.

```
Service A ──POST /token──> Authorization Server
            client_id +
            client_secret
            grant_type=client_credentials

Service A <──access_token── Authorization Server

Service A ──Bearer token──> Service B
```

**Use when:** Backend services authenticate to each other. No user context needed.

## Device Code (TV / IoT / CLI)

For devices with limited input capability.

```
1. Device requests a device code and user code from auth server
2. Device displays: "Go to https://auth.example.com/device and enter code: ABCD-1234"
3. User visits URL on their phone/laptop, enters code, authenticates
4. Device polls auth server until user completes authentication
5. Auth server returns access token to device
```
