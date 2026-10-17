<!-- Part of the specs-diagramming-plantuml skill. Loaded on demand from SKILL.md. -->

# Sequence Diagram

The most commonly used PlantUML diagram type. Models the time-ordered exchange of messages between participants.

```plantuml
@startuml
title Order Processing Sequence

actor Customer
participant "Web App" as UI
participant "API Server" as API
database "PostgreSQL" as DB
queue "RabbitMQ" as Queue

Customer -> UI: Place Order
activate UI

UI -> API: POST /api/orders
activate API

API -> DB: BEGIN TRANSACTION
API -> DB: INSERT INTO orders
DB --> API: order_id = 42

API -> DB: UPDATE inventory
DB --> API: OK

API -> DB: COMMIT
DB --> API: OK

API -> Queue: Publish OrderCreated event
Queue --> API: ACK

API --> UI: 201 Created {order_id: 42}
deactivate API

UI --> Customer: Order Confirmation
deactivate UI

Queue -> API: Process OrderCreated
activate API
API -> API: Send confirmation email
deactivate API

@enduml
```

## Participant Types

| Keyword | Shape |
|---------|-------|
| `participant` | Rectangle (default) |
| `actor` | Stick figure |
| `boundary` | Boundary symbol |
| `control` | Control symbol |
| `entity` | Entity symbol |
| `database` | Cylinder |
| `collections` | Stacked rectangles |
| `queue` | Queue symbol |

## Arrow Types

| Syntax | Description |
|--------|-------------|
| `->` | Solid line, solid arrowhead |
| `-->` | Dashed line, solid arrowhead |
| `->>` | Solid line, thin arrowhead |
| `-->>` | Dashed line, thin arrowhead |
| `-\` | Solid line, upper half arrowhead |
| `-/` | Solid line, lower half arrowhead |
| `->x` | Solid line with lost message |
| `-[#red]>` | Colored arrow |

## Grouping and Fragments

```plantuml
@startuml

alt Successful
    A -> B: Request
    B --> A: Response
else Failure
    A -> B: Request
    B --> A: Error
end

loop Every 5 seconds
    A -> B: Heartbeat
    B --> A: ACK
end

par Parallel
    A -> B: Task 1
also
    A -> C: Task 2
end

opt Optional Step
    A -> B: Notify
end

critical Mutex Section
    A -> B: Lock
    B --> A: Acquired
end

@enduml
```
