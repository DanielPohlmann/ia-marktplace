<!-- Part of the dev-backend-authentication skill. Loaded on demand from SKILL.md. -->

# Authentication & Authorization Patterns — details

## Session-Based Authentication

### Server-Side Sessions

```
1. User submits credentials
2. Server validates, creates session record (in DB or Redis)
3. Server sends session ID in a cookie
4. Client sends cookie with every request
5. Server looks up session by ID, retrieves user context
```

### Cookie Security

| Attribute | Purpose | Recommendation |
|-----------|---------|----------------|
| `HttpOnly` | Prevents JavaScript access (XSS mitigation) | Always set |
| `Secure` | Cookie sent only over HTTPS | Always set in production |
| `SameSite=Lax` | Mitigates CSRF for top-level navigations | Default for most apps |
| `SameSite=Strict` | Cookie never sent cross-site | For sensitive operations |
| `Path=/` | Scope the cookie to a path | Set appropriately |
| `Max-Age` / `Expires` | Session duration | Match your session TTL |

### CSRF Protection

- **SameSite cookies** (Lax or Strict) -- primary defense in modern browsers.
- **Synchronizer Token Pattern** -- server generates a random token, embeds in forms, validates on POST.
- **Double Submit Cookie** -- CSRF token in both a cookie and a request header; server verifies they match.

## RBAC (Role-Based Access Control)

Users are assigned **roles**; roles are granted **permissions**. Users inherit the permissions of their assigned roles.

```
Role Hierarchy Example:

  admin
    ├── manage_users
    ├── manage_orders
    └── viewer (inherits)
          ├── read_orders
          └── read_products

User "Alice" → roles: [admin]
  → effective permissions: [manage_users, manage_orders, read_orders, read_products]

User "Bob" → roles: [viewer]
  → effective permissions: [read_orders, read_products]
```

### Implementation Pattern

```python
# Check permission, not role (more granular and maintainable)
# Bad:  if user.role == "admin"
# Good: if user.has_permission("manage_orders")

def require_permission(permission):
    def decorator(handler):
        def wrapper(request):
            if not request.user.has_permission(permission):
                raise ForbiddenError()
            return handler(request)
        return wrapper
    return decorator

@require_permission("manage_orders")
def cancel_order(request, order_id):
    ...
```

**Best for:** Most applications. Simple to understand, implement, and audit.

## ABAC (Attribute-Based Access Control)

Access decisions based on **attributes** of the subject, resource, action, and environment -- evaluated by a **policy engine**.

| Attribute Source | Examples |
|-----------------|----------|
| **Subject** | user.role, user.department, user.clearance_level |
| **Resource** | document.classification, order.owner_id, record.tenant_id |
| **Action** | read, write, delete, approve |
| **Environment** | current_time, ip_address, request.is_internal |

### Policy Example (Pseudocode)

```
PERMIT action=read ON resource=document
  WHERE subject.clearance_level >= resource.classification
    AND subject.department == resource.department
    AND environment.time BETWEEN 08:00 AND 18:00
```

**Best for:** Complex authorization requirements where RBAC role explosion becomes unmanageable (e.g., healthcare, government, multi-tenant SaaS with granular permissions).

## Multi-Tenancy Patterns

| Pattern | Isolation Level | Complexity | Cost |
|---------|----------------|------------|------|
| **Shared database, shared schema** | Row-level (tenant_id column) | Low | Lowest |
| **Shared database, schema-per-tenant** | Schema-level | Medium | Medium |
| **Database-per-tenant** | Full database isolation | High | Highest |

### Row-Level Security (Shared Schema)

```sql
-- PostgreSQL Row-Level Security
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_setting('app.current_tenant')::uuid);

-- Set tenant context per request
SET app.current_tenant = 'org_acme';
SELECT * FROM orders;  -- only returns org_acme's orders
```

**Decision heuristic:**
- **Shared schema + RLS** for most SaaS applications (simplest, cost-effective, sufficient isolation).
- **Schema-per-tenant** when tenants need custom schema extensions or stronger isolation without separate databases.
- **Database-per-tenant** when regulatory, compliance, or contractual requirements mandate full data isolation (e.g., healthcare, finance, government).

## Identity Providers

| Provider | Type | Best For |
|----------|------|----------|
| **Auth0** | Managed (Okta) | SaaS apps, rapid development, extensive social login support |
| **Microsoft Entra ID** (Azure AD) | Managed (Microsoft) | Enterprise apps, Microsoft ecosystem, B2B federation |
| **Amazon Cognito** | Managed (AWS) | AWS-native apps, user pools + federated identity |
| **Keycloak** | Open-source (self-hosted) | Full control, on-premises, custom requirements |
| **Firebase Auth** | Managed (Google) | Mobile-first apps, Google ecosystem, quick prototyping |

**Recommendation:** Use a managed identity provider unless you have strong requirements for self-hosting. Building authentication from scratch is a security liability.

## Security Headers

| Header | Purpose | Recommended Value |
|--------|---------|-------------------|
| **CORS** (`Access-Control-Allow-Origin`) | Controls which origins can call your API | Explicit allowlist (never `*` with credentials) |
| **Content-Security-Policy (CSP)** | Controls what content the browser can load/execute | `default-src 'self'; script-src 'self'` (customize per app) |
| **Strict-Transport-Security (HSTS)** | Forces HTTPS for all future requests | `max-age=31536000; includeSubDomains; preload` |
| **Referrer-Policy** | Controls how much referrer info is sent | `strict-origin-when-cross-origin` |
| **X-Content-Type-Options** | Prevents MIME type sniffing | `nosniff` |
| **X-Frame-Options** | Prevents clickjacking via iframes | `DENY` or `SAMEORIGIN` |
| **Permissions-Policy** | Controls browser features (camera, mic, geolocation) | Restrict to only what your app needs |

### CORS Configuration

```
# Preflight request
OPTIONS /api/orders
Origin: https://app.example.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization, Content-Type

# Preflight response
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 86400
Access-Control-Allow-Credentials: true
```

**Rules:**
- Never use `Access-Control-Allow-Origin: *` when `Access-Control-Allow-Credentials: true`.
- Maintain an explicit allowlist of trusted origins.
- Set `Access-Control-Max-Age` to reduce preflight request overhead.
