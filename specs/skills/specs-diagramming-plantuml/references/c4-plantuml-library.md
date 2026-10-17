<!-- Part of the specs-diagramming-plantuml skill. Loaded on demand from SKILL.md. -->

# C4-PlantUML Library

The C4-PlantUML library provides macros for creating C4 model diagrams using PlantUML.

## Installation

Include the library from GitHub or a local copy:

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml
' or for container diagrams:
' !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
' or for component diagrams:
' !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml
@enduml
```

## C4 Context Diagram

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

LAYOUT_WITH_LEGEND()

title System Context Diagram

Person(customer, "Customer", "A user who shops online.")
System(ecommerce, "E-Commerce Platform", "Handles catalog, orders, and payments.")
System_Ext(payment, "Payment Provider", "Processes credit card transactions.")
System_Ext(email, "Email Service", "Sends transactional emails.")

Rel(customer, ecommerce, "Browses and purchases", "HTTPS")
Rel(ecommerce, payment, "Processes payments", "HTTPS")
Rel(ecommerce, email, "Sends notifications", "SMTP")

@enduml
```

## C4 Container Diagram

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

title Container Diagram - E-Commerce Platform

Person(customer, "Customer")

System_Boundary(ecommerce, "E-Commerce Platform") {
    Container(webapp, "Web Application", "Next.js", "Serves the storefront UI.")
    Container(api, "API Service", "Node.js / Express", "Handles business logic and API endpoints.")
    Container(worker, "Background Worker", "Node.js", "Processes async tasks.")
    ContainerDb(db, "Database", "PostgreSQL", "Stores users, orders, products.")
    ContainerQueue(queue, "Message Queue", "RabbitMQ", "Async event processing.")
    Container(cache, "Cache", "Redis", "Session and data caching.")
}

System_Ext(payment, "Stripe", "Payment processing.")

Rel(customer, webapp, "Browses", "HTTPS")
Rel(webapp, api, "API calls", "HTTPS/JSON")
Rel(api, db, "Reads/Writes", "SQL")
Rel(api, cache, "Reads/Writes", "Redis Protocol")
Rel(api, queue, "Publishes events", "AMQP")
Rel(worker, queue, "Consumes events", "AMQP")
Rel(worker, db, "Reads/Writes", "SQL")
Rel(api, payment, "Charges", "HTTPS")

@enduml
```

## C4-PlantUML Macros

| Macro | Purpose |
|-------|---------|
| `Person(alias, label, description)` | Human user |
| `Person_Ext(alias, label, description)` | External human user |
| `System(alias, label, description)` | Software system in scope |
| `System_Ext(alias, label, description)` | External software system |
| `System_Boundary(alias, label)` | System boundary for container views |
| `Container(alias, label, technology, description)` | Container (app, service) |
| `ContainerDb(alias, label, technology, description)` | Database container |
| `ContainerQueue(alias, label, technology, description)` | Message queue container |
| `Component(alias, label, technology, description)` | Component inside a container |
| `Rel(from, to, label, technology)` | Relationship |
| `Rel_D(from, to, label)` | Relationship (downward) |
| `Rel_U(from, to, label)` | Relationship (upward) |
| `Rel_L(from, to, label)` | Relationship (leftward) |
| `Rel_R(from, to, label)` | Relationship (rightward) |
| `LAYOUT_WITH_LEGEND()` | Show legend with color meanings |
| `LAYOUT_TOP_DOWN()` | Top-to-bottom layout |
| `LAYOUT_LEFT_RIGHT()` | Left-to-right layout |
