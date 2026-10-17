---
name: specs-diagramming-d2
description: Use when writing diagrams in the D2 language. USE FOR: D2 syntax, shapes, nested containers, SQL tables, styles and classes, grids, layers, scenarios, sequence diagrams, layout engines, D2 CLI. DO NOT USE FOR: GitHub-native rendering (use specs-diagramming-mermaidjs), C4 (use specs-diagramming-c4-diagrams), strict UML (use specs-diagramming-plantuml).
---

# D2 — Declarative Diagramming

## Overview

D2 is a modern, declarative diagramming language created by Terrastruct. It compiles text into diagrams with support for multiple layout engines, nested containers, scenarios, layers, SQL table shapes, and advanced styling. D2 emphasizes readability, composability, and high-quality rendered output (SVG, PNG, PDF).

## Containers and Nesting

D2 supports arbitrarily nested containers to represent hierarchical structure.

```d2
aws: AWS Cloud {
  vpc: VPC {
    subnet_a: Subnet A {
      api: API Server {
        shape: rectangle
      }
      worker: Background Worker {
        shape: rectangle
      }
    }
    subnet_b: Subnet B {
      db: PostgreSQL {
        shape: cylinder
      }
      cache: Redis {
        shape: cylinder
      }
    }
  }
  cdn: CloudFront {
    shape: cloud
  }
}

user: User {
  shape: person
}

user -> aws.cdn: HTTPS
aws.cdn -> aws.vpc.subnet_a.api: Forward
aws.vpc.subnet_a.api -> aws.vpc.subnet_b.db: SQL
aws.vpc.subnet_a.api -> aws.vpc.subnet_b.cache: Redis Protocol
aws.vpc.subnet_a.worker -> aws.vpc.subnet_b.db: SQL
```

## SQL Tables

D2 has first-class support for SQL table shapes with columns, types, and constraints.

```d2
users: Users {
  shape: sql_table
  id: int {constraint: primary_key}
  email: varchar(255) {constraint: unique}
  name: varchar(100)
  created_at: timestamp
  org_id: int {constraint: foreign_key}
}

organizations: Organizations {
  shape: sql_table
  id: int {constraint: primary_key}
  name: varchar(100)
  plan: varchar(50)
}

orders: Orders {
  shape: sql_table
  id: int {constraint: primary_key}
  user_id: int {constraint: foreign_key}
  total: decimal(10,2)
  status: varchar(20)
  created_at: timestamp
}

users.org_id -> organizations.id
orders.user_id -> users.id
```

## UML Class Shapes

```d2
UserService: UserService {
  shape: class
  -connection: DBConnection
  -cache: RedisClient
  +getUser(id int): User
  +createUser(data UserDTO): User
  +deleteUser(id int): bool
  -validateEmail(email string): bool
}

UserRepository: UserRepository {
  shape: class
  -db: DBConnection
  +findById(id int): User
  +save(user User): User
  +delete(id int): void
}

UserService -> UserRepository: uses
```

## Classes (Reusable Styles)

Define reusable style classes and apply them to multiple elements.

```d2
classes: {
  primary: {
    style: {
      fill: "#5E81AC"
      font-color: "#ECEFF4"
      border-radius: 8
    }
  }
  database: {
    shape: cylinder
    style: {
      fill: "#A3BE8C"
      font-color: "#2E3440"
    }
  }
  external: {
    style: {
      fill: "#BF616A"
      font-color: "#ECEFF4"
      stroke-dash: 5
    }
  }
}

api: API Server {
  class: primary
}
db: PostgreSQL {
  class: database
}
stripe: Stripe API {
  class: external
}

api -> db
api -> stripe
```

## Icons

D2 supports icons from URLs. Commonly used with icon sets hosted online.

```d2
aws: AWS {
  icon: https://icons.terrastruct.com/aws%2F_Group%20Icons%2FAWS-Cloud-alt_light-bg.svg
}

postgres: PostgreSQL {
  icon: https://icons.terrastruct.com/dev%2Fpostgresql.svg
  shape: image
}

github: GitHub Actions {
  icon: https://icons.terrastruct.com/dev%2Fgithub.svg
}
```

## Grid Layouts

Grid layouts arrange child elements in a grid pattern.

```d2
services: Microservices {
  grid-rows: 2
  grid-columns: 3
  grid-gap: 16

  auth: Auth Service
  users: User Service
  orders: Order Service
  payments: Payment Service
  notifications: Notification Service
  analytics: Analytics Service
}
```

## Layers

Layers let you define multiple views within a single D2 file. Each layer produces a separate diagram.

```d2
# Base diagram (always rendered)
client -> server
server -> db

layers: {
  detailed: {
    client: Web Browser {
      shape: rectangle
    }
    server: API Server {
      auth: Auth Module
      handler: Request Handler
      auth -> handler
    }
    db: PostgreSQL {
      shape: cylinder
    }
    client -> server.auth: "Authenticate"
    server.handler -> db: "Query"
  }
}
```

## Scenarios

Scenarios show the same diagram in different states — useful for illustrating state changes or progressive disclosure.

```d2
server: Server {
  style.fill: "#A3BE8C"
}
db: Database {
  shape: cylinder
}
server -> db

scenarios: {
  failure: {
    server: Server {
      style.fill: "#BF616A"
    }
    server -> db: "Connection Lost" {
      style.stroke: red
      style.stroke-dash: 5
    }
  }
  recovery: {
    server: Server {
      style.fill: "#EBCB8B"
    }
    server -> db: "Reconnecting..." {
      style.stroke: orange
      style.animated: true
    }
  }
}
```

## Sequence Diagrams

D2 supports sequence diagrams with its own syntax inside a `shape: sequence_diagram` container.

```d2
interaction: {
  shape: sequence_diagram

  user: User
  api: API Server
  db: Database
  cache: Redis

  user -> api: "POST /orders"
  api -> cache: "Check inventory"
  cache -> api: "In stock"
  api -> db: "INSERT order"
  db -> api: "order_id: 42"
  api -> user: "201 Created"
}
```

## VS Code Extension

The official D2 extension for Visual Studio Code provides:

- Syntax highlighting for `.d2` files
- Live preview panel (renders the diagram as you type)
- Error diagnostics
- Autocompletion for shape types, styles, and keywords

Install from the VS Code marketplace: search for "D2" by Terrastruct.

## Best Practices

- **Use containers to represent system boundaries.** Nesting shapes inside containers clearly communicates which components belong to which subsystem.
- **Define style classes** for consistent visual language across the diagram. Create classes for services, datastores, external systems, etc.
- **Use the `direction` keyword** to control the overall layout orientation. `direction: right` works well for data flow; `direction: down` works well for hierarchies.
- **Leverage layers for progressive detail.** Use a base layer for the high-level overview and named layers for zoomed-in views.
- **Use scenarios to show state changes.** Scenarios are ideal for showing normal operation vs. failure modes, or before/after states.
- **Choose the right layout engine.** Start with `dagre` for simplicity. Switch to `ELK` for complex diagrams. Use `TALA` for presentation-quality output.
- **Use `--watch` during development.** The watch mode auto-recompiles on save, giving you a live preview workflow.
- **Use `--sketch` for informal communication.** The hand-drawn style signals that diagrams are conceptual, not final.
- **Keep `.d2` files in version control.** Like all diagrams-as-code, D2 files should live in the repository alongside the systems they describe.
- **Use SQL table shapes for data modeling.** D2's `sql_table` shape with constraints is a concise way to document database schemas.
- **Reference icons from the Terrastruct icon set** or use custom icon URLs for visual clarity in architecture diagrams.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | Basic Syntax; Shape Types; Styles; Layout Engines; CLI Commands; Complete Example |

## References

- [D2 Language Documentation](https://d2lang.com/)
- [D2 — GitHub Repository (Terrastruct)](https://github.com/terrastruct/d2)

See references/rules.md for the full rule catalog.
