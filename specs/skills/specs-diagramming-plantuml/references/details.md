<!-- Part of the specs-diagramming-plantuml skill. Loaded on demand from SKILL.md. -->

# PlantUML — details

## Activity Diagram

PlantUML supports both legacy and modern (beta) activity diagram syntax. The modern syntax is recommended.

```plantuml
@startuml
title Order Fulfillment Process

start

:Receive Order;

if (Payment Valid?) then (yes)
    :Reserve Inventory;

    fork
        :Pack Items;
    fork again
        :Generate Invoice;
    fork again
        :Send Confirmation Email;
    end fork

    :Ship Order;

    if (Domestic?) then (yes)
        :Standard Shipping;
    else (no)
        :International Shipping;
        :Customs Declaration;
    endif

    :Update Tracking;
    :Mark as Shipped;
else (no)
    :Reject Order;
    :Notify Customer;
    :Refund if Charged;
endif

stop

@enduml
```

### Activity Diagram Elements

| Syntax | Meaning |
|--------|---------|
| `start` | Start node |
| `stop` | Stop node (success) |
| `end` | End node (termination) |
| `:Action;` | Action / activity step |
| `if (cond) then (yes) ... else (no) ... endif` | Decision |
| `fork ... fork again ... end fork` | Parallel execution |
| `while (cond?) is (yes) ... endwhile (no)` | Loop |
| `repeat ... repeat while (cond?)` | Do-while loop |
| `\|swimlane\|` | Swimlane / partition |
| `#color:Action;` | Colored action |

### Swimlanes

```plantuml
@startuml

|Customer|
start
:Place Order;

|System|
:Validate Order;
:Process Payment;

|Warehouse|
:Pick Items;
:Pack Shipment;

|Shipping|
:Ship Package;
:Update Tracking;

|Customer|
:Receive Package;
stop

@enduml
```

## Component Diagram

```plantuml
@startuml
title System Components

package "Frontend" {
    [Web App] as webapp
    [Mobile App] as mobile
}

package "Backend" {
    [API Gateway] as gateway
    [Auth Service] as auth
    [Order Service] as orders
    [Catalog Service] as catalog
}

package "Data" {
    database "PostgreSQL" as db
    database "Redis" as cache
    queue "RabbitMQ" as queue
}

cloud "External" {
    [Stripe] as stripe
    [SendGrid] as email
}

webapp --> gateway : REST
mobile --> gateway : REST
gateway --> auth : gRPC
gateway --> orders : gRPC
gateway --> catalog : gRPC
catalog --> db
catalog --> cache
orders --> db
orders --> queue
orders --> stripe : HTTPS
queue --> email : AMQP

@enduml
```

## Use Case Diagram

```plantuml
@startuml
title E-Commerce Use Cases

left to right direction

actor Customer as C
actor Admin as A
actor "Payment System" as PS <<external>>

rectangle "E-Commerce Platform" {
    usecase "Browse Catalog" as UC1
    usecase "Search Products" as UC2
    usecase "Place Order" as UC3
    usecase "Process Payment" as UC4
    usecase "Track Order" as UC5
    usecase "Manage Inventory" as UC6
    usecase "Generate Reports" as UC7
    usecase "Authenticate" as UC8
}

C --> UC1
C --> UC2
C --> UC3
C --> UC5
C --> UC8

A --> UC6
A --> UC7
A --> UC8

UC3 ..> UC4 : <<include>>
UC3 ..> UC8 : <<include>>
UC4 --> PS

@enduml
```

## Object Diagram

```plantuml
@startuml
title Order Instance Snapshot

object "order42 : Order" as o {
    id = 42
    status = CONFIRMED
    total = 149.97
    createdAt = "2025-03-15T10:30:00Z"
}

object "item1 : OrderItem" as i1 {
    productId = 101
    name = "Mechanical Keyboard"
    quantity = 1
    unitPrice = 99.99
}

object "item2 : OrderItem" as i2 {
    productId = 205
    name = "USB-C Cable"
    quantity = 2
    unitPrice = 24.99
}

object "customer7 : User" as u {
    id = 7
    name = "Alice Smith"
    email = "alice@example.com"
}

u --> o : places
o *-- i1 : contains
o *-- i2 : contains

@enduml
```

## Deployment Diagram

```plantuml
@startuml
title Production Deployment

node "CDN (CloudFront)" as cdn {
    artifact "Static Assets" as static
}

node "Kubernetes Cluster" as k8s {
    node "API Pod (x3)" as api_pod {
        artifact "API Service" as api
    }
    node "Worker Pod (x2)" as worker_pod {
        artifact "Background Worker" as worker
    }
}

node "AWS RDS" as rds {
    database "PostgreSQL Primary" as db_primary
    database "PostgreSQL Replica" as db_replica
}

node "AWS ElastiCache" as ec {
    database "Redis Cluster" as redis
}

node "AWS SQS" as sqs {
    queue "Order Queue" as queue
}

cdn --> api : HTTPS
api --> db_primary : SQL (write)
api --> db_replica : SQL (read)
api --> redis : Cache
api --> queue : Enqueue
worker --> queue : Dequeue
worker --> db_primary : SQL

db_primary --> db_replica : Replication

@enduml
```

## Skinparam and Theming

### Skinparam

`skinparam` controls the visual appearance of all diagram elements.

```plantuml
@startuml

skinparam backgroundColor #2E3440
skinparam defaultFontColor #ECEFF4
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 12

skinparam class {
    BackgroundColor #4C566A
    BorderColor #D8DEE9
    FontColor #ECEFF4
    ArrowColor #88C0D0
    StereotypeFontColor #81A1C1
}

skinparam note {
    BackgroundColor #3B4252
    BorderColor #4C566A
    FontColor #ECEFF4
}

skinparam package {
    BackgroundColor #3B4252
    BorderColor #4C566A
    FontColor #D8DEE9
}

class User {
    + name: String
    + email: String
}

class Order {
    + total: Decimal
    + status: Status
}

User --> Order

@enduml
```

### Common Skinparam Properties

| Property | Description |
|----------|-------------|
| `BackgroundColor` | Shape fill color |
| `BorderColor` | Shape border color |
| `FontColor` | Text color |
| `FontSize` | Text size |
| `FontName` | Font family |
| `ArrowColor` | Connection line color |
| `ArrowThickness` | Connection line width |
| `Shadowing` | true/false for drop shadows |
| `RoundCorner` | Border radius in pixels |
| `Padding` | Internal padding |
| `Margin` | External margin |

### Built-in Themes

PlantUML includes built-in themes that can be applied with a single directive.

```plantuml
@startuml
!theme cerulean
' Other themes: amiga, blueprint, cerulean, crt-amber, crt-green,
' cyborg, hacker, lightgray, mars, materia, metal, minty, plain,
' reddress, sandstone, silver, sketchy-outline, spacelab, superhero,
' toy, united, vibrant

class Example {
    + field: Type
}

@enduml
```

## Preprocessing Directives

PlantUML includes a preprocessor with variables, conditionals, loops, and functions.

### Variables

```plantuml
@startuml
!$primary_color = "#5E81AC"
!$font_color = "#ECEFF4"
!$bg_color = "#2E3440"

skinparam backgroundColor $bg_color
skinparam class {
    BackgroundColor $primary_color
    FontColor $font_color
}

class Example {
    + field: Type
}

@enduml
```

### Conditionals

```plantuml
@startuml
!$env = "production"

!if ($env == "production")
    skinparam backgroundColor #2E3440
    skinparam defaultFontColor #ECEFF4
!else
    skinparam backgroundColor White
    skinparam defaultFontColor Black
!endif

class Config {
    + env: String
}

@enduml
```

### Procedures (Macros)

```plantuml
@startuml
!procedure $service($name, $tech)
    rectangle "$name\n<size:10>[$tech]</size>" as $name
!endprocedure

!procedure $database($name, $tech)
    database "$name\n<size:10>[$tech]</size>" as $name
!endprocedure

$service(API, "Node.js")
$service(Auth, "Go")
$database(DB, "PostgreSQL")
$database(Cache, "Redis")

API --> Auth
API --> DB
API --> Cache

@enduml
```

### Loops

```plantuml
@startuml
!$i = 0
!while $i < 3
    class "Service_$i" {
        + process(): void
    }
    !$i = $i + 1
!endwhile

Service_0 --> Service_1
Service_1 --> Service_2

@enduml
```

## Running PlantUML

### Command Line

```bash
# Generate PNG from a .puml file
java -jar plantuml.jar diagram.puml

# Generate SVG
java -jar plantuml.jar -tsvg diagram.puml

# Generate all diagrams in a directory
java -jar plantuml.jar -tsvg -o output/ src/diagrams/

# Generate from stdin
echo "@startuml\nA -> B\n@enduml" | java -jar plantuml.jar -pipe > diagram.png

# Use a config file for shared skinparam settings
java -jar plantuml.jar -config style.puml diagram.puml
```

### Docker

```bash
# Run PlantUML server
docker run -d -p 8080:8080 plantuml/plantuml-server:tomcat

# Generate via Docker (no local Java needed)
docker run --rm -v $(pwd):/data plantuml/plantuml -tsvg /data/diagram.puml
```

### IDE Integration

- **VS Code:** "PlantUML" extension by jebbs — provides syntax highlighting, live preview, and export.
- **IntelliJ IDEA:** Built-in PlantUML support via the PlantUML Integration plugin.
- **Confluence:** PlantUML plugin renders diagrams inline.
