<!-- Part of the dev-backend-api-design skill. Loaded on demand from SKILL.md. -->

# gRPC Service Design

## Protobuf Service Definition

```protobuf
syntax = "proto3";

package orders.v1;

service OrderService {
  // Unary RPC
  rpc GetOrder(GetOrderRequest) returns (Order);

  // Server streaming
  rpc WatchOrderStatus(WatchOrderRequest) returns (stream OrderStatusEvent);

  // Client streaming
  rpc UploadOrderItems(stream OrderItem) returns (UploadSummary);

  // Bidirectional streaming
  rpc Chat(stream ChatMessage) returns (stream ChatMessage);
}

message GetOrderRequest {
  string order_id = 1;
}

message Order {
  string id = 1;
  string user_id = 2;
  repeated OrderItem items = 3;
  OrderStatus status = 4;
  double total = 5;
}

enum OrderStatus {
  ORDER_STATUS_UNSPECIFIED = 0;
  ORDER_STATUS_PENDING = 1;
  ORDER_STATUS_SHIPPED = 2;
  ORDER_STATUS_DELIVERED = 3;
}

message OrderItem {
  string product_id = 1;
  int32 quantity = 2;
  double unit_price = 3;
}
```

## Communication Patterns

| Pattern | Use Case | Flow |
|---------|----------|------|
| **Unary** | Standard request-response | Client sends one message, server replies with one message |
| **Server streaming** | Live updates, large result sets | Client sends one message, server streams multiple responses |
| **Client streaming** | File upload, batch ingestion | Client streams multiple messages, server replies once |
| **Bidirectional streaming** | Chat, real-time collaboration | Both sides stream messages independently |

## gRPC Best Practices
- **Deadlines:** Always set deadlines on client calls. Propagate deadlines across service boundaries.
- **Interceptors:** Use interceptors (middleware) for logging, authentication, and metrics.
- **Error codes:** Use standard gRPC status codes (NOT_FOUND, INVALID_ARGUMENT, DEADLINE_EXCEEDED, etc.).
- **gRPC-Web:** For browser clients, use Envoy or grpc-web proxy since browsers do not support HTTP/2 trailers natively.
