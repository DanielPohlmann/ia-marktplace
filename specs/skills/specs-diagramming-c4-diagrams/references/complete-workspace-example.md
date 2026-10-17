<!-- Part of the specs-diagramming-c4-diagrams skill. Loaded on demand from SKILL.md. -->

# Complete Workspace Example

```
workspace "Online Bookstore" "Architecture of the online bookstore system." {
    !identifiers hierarchical

    model {
        customer = person "Customer" "A person who buys books online."
        admin = person "Admin" "Internal staff managing the catalog."

        bookstore = softwareSystem "Online Bookstore" "Allows customers to browse and purchase books." {
            webapp = container "Web Application" "Delivers the storefront to customers." "Next.js" "WebBrowser"
            api = container "API Gateway" "Routes requests to microservices." "Kong"
            catalogService = container "Catalog Service" "Manages the book catalog." "Go" {
                catalogController = component "Catalog Controller" "Handles catalog HTTP endpoints." "net/http"
                catalogLogic = component "Catalog Logic" "Business rules for catalog management." "Go package"
                catalogRepo = component "Catalog Repository" "Reads/writes catalog data." "GORM"
            }
            orderService = container "Order Service" "Processes customer orders." "Java/Spring Boot"
            catalogDb = container "Catalog Database" "Stores book catalog data." "PostgreSQL" "Database"
            orderDb = container "Order Database" "Stores order data." "PostgreSQL" "Database"
            queue = container "Message Queue" "Asynchronous event processing." "RabbitMQ"
        }

        payments = softwareSystem "Payment Gateway" "Processes credit card payments." "External"

        # Relationships
        customer -> webapp "Browses and purchases books via"
        admin -> webapp "Manages catalog via"
        webapp -> api "Sends requests to" "HTTPS/JSON"
        api -> catalogService "Routes catalog requests to" "gRPC"
        api -> orderService "Routes order requests to" "gRPC"
        catalogService -> catalogDb "Reads from and writes to" "SQL/TCP"
        orderService -> orderDb "Reads from and writes to" "SQL/TCP"
        orderService -> queue "Publishes order events to" "AMQP"
        orderService -> payments "Processes payments via" "HTTPS"

        # Component-level relationships
        catalogController -> catalogLogic "Delegates to"
        catalogLogic -> catalogRepo "Uses"
        catalogRepo -> catalogDb "Queries" "SQL"
    }

    views {
        systemContext bookstore "Context" {
            include *
            autolayout lr
        }

        container bookstore "Containers" {
            include *
            autolayout lr
        }

        component catalogService "CatalogComponents" {
            include *
            autolayout lr
        }

        styles {
            element "Person" {
                shape Person
                background #08427B
                color #ffffff
            }
            element "Software System" {
                background #1168BD
                color #ffffff
            }
            element "Container" {
                background #438DD5
                color #ffffff
            }
            element "Component" {
                background #85BBF0
                color #000000
            }
            element "Database" {
                shape Cylinder
            }
            element "WebBrowser" {
                shape WebBrowser
            }
            element "External" {
                background #999999
                color #ffffff
            }
        }
    }
}
```
