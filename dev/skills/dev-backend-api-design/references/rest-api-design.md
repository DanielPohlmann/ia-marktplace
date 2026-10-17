<!-- Part of the dev-backend-api-design skill. Loaded on demand from SKILL.md. -->

# REST API Design

## Resource Naming Conventions

```
GET    /users              → List users
POST   /users              → Create a user
GET    /users/{id}         → Get a specific user
PUT    /users/{id}         → Replace a user
PATCH  /users/{id}         → Partially update a user
DELETE /users/{id}         → Delete a user

GET    /users/{id}/orders  → List orders for a user (sub-resource)
```

**Rules:**
- Use **nouns** (not verbs) for resource names: `/users` not `/getUsers`.
- Use **plural** nouns: `/users` not `/user`.
- Use **kebab-case** for multi-word resources: `/order-items` not `/orderItems`.
- Nest sub-resources only one level deep. Beyond that, promote to a top-level resource.

## HTTP Methods & Status Codes

| Method | Semantics | Idempotent | Safe |
|--------|-----------|------------|------|
| GET | Read a resource | Yes | Yes |
| POST | Create a resource / trigger action | No | No |
| PUT | Replace a resource entirely | Yes | No |
| PATCH | Partially update a resource | No* | No |
| DELETE | Remove a resource | Yes | No |

*PATCH can be made idempotent with careful design (e.g., JSON Merge Patch).

| Status Code | When to Use |
|-------------|-------------|
| 200 OK | Successful GET, PUT, PATCH |
| 201 Created | Successful POST (include `Location` header) |
| 204 No Content | Successful DELETE |
| 400 Bad Request | Malformed request body or parameters |
| 401 Unauthorized | Missing or invalid authentication |
| 403 Forbidden | Authenticated but insufficient permissions |
| 404 Not Found | Resource does not exist |
| 409 Conflict | State conflict (e.g., duplicate, version mismatch) |
| 422 Unprocessable Entity | Validation errors on well-formed request |
| 429 Too Many Requests | Rate limit exceeded (include `Retry-After`) |
| 500 Internal Server Error | Unhandled server error |

## HATEOAS (Hypermedia As The Engine Of Application State)

Include links in responses so clients can discover available actions:

```json
{
  "id": "usr_42",
  "name": "Alice",
  "_links": {
    "self": { "href": "/users/usr_42" },
    "orders": { "href": "/users/usr_42/orders" },
    "deactivate": { "href": "/users/usr_42/deactivate", "method": "POST" }
  }
}
```

## Pagination

| Strategy | Pros | Cons |
|----------|------|------|
| **Offset-based** (`?offset=20&limit=10`) | Simple, supports jumping to page N | Inconsistent with concurrent writes; slow at large offsets |
| **Cursor-based** (`?cursor=abc123&limit=10`) | Consistent during writes; performant at any depth | Cannot jump to arbitrary page; cursor is opaque |

**Recommendation:** Use cursor-based pagination for any dataset that changes frequently or grows large. Use offset-based only for small, static datasets or when page-jumping is a hard requirement.

```json
{
  "data": [...],
  "pagination": {
    "next_cursor": "eyJpZCI6MTAwfQ==",
    "has_more": true
  }
}
```

## Filtering & Sorting

```
GET /orders?status=shipped&created_after=2024-01-01&sort=-created_at&limit=20
```

- Use query parameters for filtering. Prefix sort fields with `-` for descending.
- For complex filtering, consider a structured query parameter: `?filter[status]=shipped&filter[total_gte]=100`.

## Versioning Strategies

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| **URL path** | `/v1/users` | Explicit, easy to route | URL pollution, hard to sunset |
| **Header** | `Accept: application/vnd.api+json;version=2` | Clean URLs | Hidden, harder to test in browser |
| **Content negotiation** | `Accept: application/vnd.myapp.v2+json` | RESTful, media-type driven | Complex, less discoverable |

**Recommendation:** URL-path versioning (`/v1/`, `/v2/`) is the most practical for most teams. Use it unless you have strong reasons for header-based versioning.

## Richardson Maturity Model

| Level | Description | Example |
|-------|-------------|---------|
| **0 — The Swamp of POX** | Single URI, single HTTP method (usually POST) | `POST /api` with action in body |
| **1 — Resources** | Multiple URIs, but only POST/GET | `GET /users`, `POST /users` |
| **2 — HTTP Verbs** | Proper use of GET, POST, PUT, DELETE, status codes | `PUT /users/42` returns 200 |
| **3 — Hypermedia Controls** | HATEOAS: responses include links to related actions | Links in response body |

Most production APIs target Level 2. Level 3 (HATEOAS) adds discoverability but increases response size and complexity.
