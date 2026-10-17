<!-- Part of the security-api-security skill. Loaded on demand from SKILL.md. -->

# API Security — details

## Security Headers

Security headers instruct browsers and clients on how to handle responses, significantly reducing the attack surface for common web-based attacks.

| Header | Purpose | Recommended Value |
|---|---|---|
| `Strict-Transport-Security` | Forces HTTPS connections; prevents protocol downgrade attacks | `max-age=31536000; includeSubDomains; preload` |
| `X-Content-Type-Options` | Prevents MIME type sniffing; ensures browser respects declared content type | `nosniff` |
| `X-Frame-Options` | Prevents clickjacking by controlling whether the page can be framed | `DENY` (or `SAMEORIGIN` if framing is required) |
| `Content-Security-Policy` | Controls which resources the browser is allowed to load; mitigates XSS | See CSP section below for detailed directives |
| `Referrer-Policy` | Controls how much referrer information is sent with requests | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | Restricts access to browser features (camera, microphone, geolocation) | `camera=(), microphone=(), geolocation=()` |
| `Cache-Control` | Prevents caching of sensitive data by intermediaries and browsers | `no-store, no-cache, must-revalidate, private` |
| `X-Request-Id` | Provides a unique identifier for request tracing and correlation | Generate a UUID per request; echo it in the response |

For pure JSON APIs that are not serving HTML, a minimal set of headers should include `Strict-Transport-Security`, `X-Content-Type-Options`, `Cache-Control` (for sensitive responses), and `X-Request-Id`. The full set above is recommended when the API serves content rendered in a browser.

## CORS Configuration

**What CORS Is**

Cross-Origin Resource Sharing (CORS) is a browser-enforced mechanism that controls which origins are permitted to make requests to your API. When a browser makes a cross-origin request, it sends an `Origin` header; the server must respond with appropriate `Access-Control-*` headers to allow or deny the request.

**Dangerous Misconfigurations**

- **Wildcard with credentials**: Setting `Access-Control-Allow-Origin: *` together with `Access-Control-Allow-Credentials: true` is invalid per the specification, but some implementations attempt it. This would allow any website to make authenticated requests to your API.
- **Reflecting the Origin header**: Dynamically returning whatever origin the request sends without validation is equivalent to a wildcard and defeats the purpose of CORS.
- **Overly broad origin patterns**: Matching `*.example.com` without anchoring can be tricked by domains like `evil-example.com`.

**Proper Configuration Example**

```
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization, X-Request-Id
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 86400
```

Key rules:
- Explicitly list allowed origins; never use wildcard with credentials.
- Restrict allowed methods to only those the API actually supports.
- Restrict allowed headers to those your API requires.
- Set `Access-Control-Max-Age` to cache preflight responses and reduce latency.

**Preflight Requests**

Browsers send an `OPTIONS` preflight request before making "non-simple" requests (those with custom headers, methods other than GET/POST, or non-standard content types). Your API must handle `OPTIONS` requests and return the appropriate CORS headers with a `204 No Content` response. Ensure preflight handling does not require authentication.

## Content Security Policy

Content Security Policy (CSP) tells the browser which sources of content are trusted, providing a strong defense against cross-site scripting (XSS) and data injection attacks.

**Key Directives**

| Directive | Purpose | Example Value |
|---|---|---|
| `default-src` | Fallback for all resource types not explicitly configured | `'self'` |
| `script-src` | Controls which scripts can execute | `'self'` (avoid `'unsafe-inline'` and `'unsafe-eval'`) |
| `style-src` | Controls which stylesheets can be applied | `'self' 'unsafe-inline'` (inline styles often required) |
| `img-src` | Controls which image sources are allowed | `'self' data: https://cdn.example.com` |
| `connect-src` | Controls which URLs can be accessed via fetch, XHR, WebSocket | `'self' https://api.example.com` |
| `frame-ancestors` | Controls which origins can embed this page in a frame | `'none'` (replaces X-Frame-Options) |

**Example Policies**

For a JSON API (minimal CSP since no HTML rendering):
```
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
```

For a web application:
```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' https://api.example.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

**Monitoring Violations**

Use `report-uri` (deprecated but widely supported) or `report-to` to receive violation reports without blocking content. Start with `Content-Security-Policy-Report-Only` to monitor before enforcing:
```
Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report
```

## API Authentication

Different authentication mechanisms suit different contexts. Choose based on the trust level, client type, and security requirements.

| Method | Use Case | Security Level | Details |
|---|---|---|---|
| API Keys | Internal services, low-risk public APIs | Low-Medium | Simple to implement; transmitted in headers; easily leaked if not managed; rotate regularly; never embed in client-side code |
| OAuth 2.0 Bearer Tokens | User-delegated access, third-party integrations | High | Industry standard for delegated authorization; use short-lived access tokens with refresh tokens; validate scopes on every request |
| mTLS (Mutual TLS) | Service-to-service communication | Very High | Both client and server present certificates; strong identity verification; requires certificate management infrastructure (PKI) |
| HMAC Signatures | Webhook verification, request integrity | High | Request body is signed with a shared secret; prevents tampering and replay (with timestamp); no credentials transmitted |

Key considerations across all methods:
- Always transmit credentials over HTTPS.
- Implement token/key rotation and revocation mechanisms.
- Log authentication events for audit and anomaly detection.
- Use short-lived tokens and refresh mechanisms where possible.

## API Gateway Security

An API gateway acts as a centralized entry point for all API traffic, providing a single location to enforce security policies consistently across services.

**What an API Gateway Provides**

- **Authentication and authorization**: Validate tokens, API keys, and certificates at the edge before requests reach backend services.
- **Rate limiting**: Enforce per-client and per-endpoint rate limits centrally.
- **Request validation**: Validate request schemas (JSON Schema, OpenAPI spec) and reject malformed input before it reaches application logic.
- **TLS termination**: Handle HTTPS at the gateway; backend services can communicate over a trusted internal network.
- **Logging and monitoring**: Capture request/response metadata, latency metrics, and error rates in a centralized location.
- **IP allowlisting/blocklisting**: Restrict access by source IP for internal or partner APIs.
- **Request/response transformation**: Strip sensitive headers, mask fields, or add security headers uniformly.

**Common API Gateways**

| Gateway | Type | Key Features |
|---|---|---|
| Kong | Open source / Enterprise | Plugin ecosystem, declarative config, gRPC support, Kubernetes-native |
| AWS API Gateway | Managed (AWS) | Lambda integration, usage plans, WAF integration, mutual TLS |
| Azure API Management | Managed (Azure) | Policy engine, developer portal, built-in caching, multi-region |
| Envoy | Open source (proxy) | Service mesh integration (Istio), advanced load balancing, extensible via WASM |
| NGINX | Open source / Commercial | High performance, Lua scripting, broad protocol support |
