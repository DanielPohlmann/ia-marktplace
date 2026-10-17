<!-- Part of the dev-backend-api-design skill. Loaded on demand from SKILL.md. -->

# GraphQL Schema Design

## Schema Example (Schema-First / SDL)

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders(first: Int, after: String): OrderConnection!
}

type Order {
  id: ID!
  total: Float!
  status: OrderStatus!
  items: [OrderItem!]!
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
