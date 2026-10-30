<!-- Part of the dev-backend-api-design skill. Loaded on demand from SKILL.md. -->

# API Design Patterns — details

## WebSocket Protocol Design

### Connection Lifecycle

```
1. Client sends HTTP Upgrade request
2. Server responds with 101 Switching Protocols
3. Full-duplex communication over persistent TCP connection
4. Either side can send frames at any time
5. Close handshake (close frame + acknowledgment)
```

### Design Patterns

| Pattern | Description |
|---------|-------------|
| **Rooms / Channels** | Group connections by topic; broadcast within a room (e.g., `chat:room-42`) |
| **Heartbeat / Ping-Pong** | Periodic ping frames detect dead connections; server or client can initiate |
| **Reconnection with backoff** | Client reconnects on disconnect with exponential backoff + jitter |
| **Message acknowledgment** | Assign IDs to messages; receiver acknowledges; sender retries unacknowledged |

### Message Format Convention

```json
{
  "type": "order.status_changed",
  "payload": {
    "order_id": "ord_123",
    "new_status": "shipped"
  },
  "id": "msg_abc",
  "timestamp": "2024-01-15T14:30:00Z"
}
```

## Cross-Cutting API Concerns

### API Gateway Patterns
- **Request routing** -- route by path, header, or method to the correct backend service.
- **Authentication offloading** -- verify tokens at the gateway; pass claims to backends.
- **Rate limiting** -- enforce quotas per client/API key at the gateway.
- **Response caching** -- cache GET responses at the edge.
- **Request/response transformation** -- reshape payloads between external and internal formats.

### Idempotency Keys

For non-idempotent operations (especially payments), clients include a unique `Idempotency-Key` header. The server stores the result keyed by this value and returns the cached result on retry.

```
POST /payments
Idempotency-Key: pay_req_abc123
Content-Type: application/json

{ "amount": "99.99", "currency": "USD" }
```

Monetary amounts travel as decimal strings (or integer minor units such as `9999`), never as JSON floats — many parsers decode JSON numbers into binary doubles, which cannot represent most decimal fractions exactly.

### OpenAPI / Swagger Documentation

For REST APIs, maintain an OpenAPI specification as the source of truth. Cross-reference **specs** for documentation standards. Generate client SDKs, server stubs, and interactive docs from the spec.
