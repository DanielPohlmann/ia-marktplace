<!-- Part of the specs-diagramming-c4-diagrams skill. Loaded on demand from SKILL.md. -->

# The Four Levels

## Level 1: System Context

The highest level of abstraction. Shows the system under consideration and its relationships with users (actors) and other systems. Answers: "What is the system and who uses it?"

```
workspace {
    model {
        user = person "User" "A customer of the system."
        email = softwareSystem "Email System" "Sends transactional emails." "External"
        system = softwareSystem "My System" "Handles core business logic."

        user -> system "Uses"
        system -> email "Sends emails via"
    }
    views {
        systemContext system "SystemContext" {
            include *
            autolayout lr
        }
    }
}
```

## Level 2: Container

Zooms into a single software system to show the high-level technology choices — web apps, APIs, databases, message brokers, etc. Answers: "What are the major technology building blocks?"

```
workspace {
    model {
        user = person "User"
        system = softwareSystem "My System" {
            webapp = container "Web Application" "Serves the UI." "React"
            api = container "API Service" "Handles business logic." "Node.js"
            db = container "Database" "Stores data." "PostgreSQL" "Database"
        }

        user -> webapp "Visits"
        webapp -> api "Calls" "HTTPS/JSON"
        api -> db "Reads from and writes to" "SQL/TCP"
    }
    views {
        container system "Containers" {
            include *
            autolayout lr
        }
    }
}
```

## Level 3: Component

Zooms into a single container to show the logical components inside it and their interactions. Answers: "What are the major structural building blocks inside a container?"

```
workspace {
    model {
        system = softwareSystem "My System" {
            api = container "API Service" {
                controller = component "API Controller" "Handles HTTP requests." "Express Router"
                service = component "Business Service" "Implements domain logic." "TypeScript Class"
                repo = component "Repository" "Data access layer." "TypeORM Repository"
            }
            db = container "Database" "PostgreSQL" "Database"

            controller -> service "Delegates to"
            service -> repo "Uses"
            repo -> db "Reads/writes" "SQL"
        }
    }
    views {
        component api "Components" {
            include *
            autolayout lr
        }
    }
}
```

## Level 4: Code

The lowest level. Shows the internal structure of a single component — typically a UML class diagram or similar. This level is usually auto-generated from code and is optional in most C4 workflows.

> **Note:** Level 4 is often omitted in practice because it can be generated directly from source code by IDEs or static analysis tools. Use it only when the internal structure of a component is complex enough to warrant explicit documentation.
