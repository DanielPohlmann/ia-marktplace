<!-- Part of the dev-backend-api-design skill. Loaded on demand from SKILL.md. -->

# GraphQL Schema Design

## Schema Example (Schema-First / SDL)

```graphql
scalar Decimal  # serialized as a string, e.g. "1234.50"

type User {
  id: ID!
  name: String!
  email: String!
  orders(first: Int, after: String): OrderConnection!
}

type Order {
  id: ID!
  total: Money!
  status: OrderStatus!
  items: [OrderItem!]!
}

type Money {
  amount: Decimal!
  currency: String!  # ISO 4217 code, e.g. "USD"
}

enum OrderStatus {
  PENDING
  SHIPPED
  DELIVERED
  CANCELLED
}

type OrderConnection {
  edges: [OrderEdge!]!
  pageInfo: PageInfo!
}

type OrderEdge {
  node: Order!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  endCursor: String
}

type Query {
  user(id: ID!): User
  users(first: Int, after: String): UserConnection!
}

type Mutation {
  createOrder(input: CreateOrderInput!): Order!
  cancelOrder(id: ID!): Order!
}

type Subscription {
  orderStatusChanged(userId: ID!): Order!
}

input CreateOrderInput {
  userId: ID!
  items: [OrderItemInput!]!
}
```

**Money is never `Float`.** GraphQL `Float` is a binary double, which cannot represent most decimal fractions exactly (0.1 + 0.2 is not 0.3), so totals drift through rounding. Use a custom decimal scalar serialized as a string, or an `Int` amount in minor units (cents) plus a currency code — and note that GraphQL `Int` is 32-bit, so large minor-unit amounts also need a string-backed scalar.

## The N+1 Problem & DataLoader

```
Query: { users { orders { items } } }

Without DataLoader:
  1 query for users
  N queries for orders (one per user)     ← N+1 problem
  M queries for items (one per order)

With DataLoader:
  1 query for users
  1 batched query for all orders          ← solved
  1 batched query for all items
```

**DataLoader** batches and caches database lookups within a single request. It collects all keys requested during a single tick of the event loop, then issues a single batched query.

## Schema-First vs. Code-First

| Approach | Tools | Pros | Cons |
|----------|-------|------|------|
| **Schema-first** | Apollo, graphql-tools | Schema is the contract; language-agnostic | Schema and resolvers can drift |
| **Code-first** | Nexus, TypeGraphQL, Strawberry | Type safety, co-located logic | Schema is derived, less portable |

## Federation

For microservices, **Apollo Federation** (or similar) lets each service own part of the graph:

```
Service A owns: User { id, name, email }
Service B owns: User { orders: [Order] }   ← extends User
Gateway composes both into a single graph
```
