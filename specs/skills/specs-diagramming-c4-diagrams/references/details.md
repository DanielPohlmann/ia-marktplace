<!-- Part of the specs-diagramming-c4-diagrams skill. Loaded on demand from SKILL.md. -->

# C4 Model Diagrams — details

## Mermaid C4 Support

Mermaid supports C4 diagrams natively, making it possible to embed C4 models directly in Markdown rendered by GitHub, GitLab, and other platforms.

```mermaid
C4Context
    title System Context Diagram for Online Bookstore

    Person(customer, "Customer", "A person who buys books online.")
    System(bookstore, "Online Bookstore", "Allows customers to browse and purchase books.")
    System_Ext(payments, "Payment Gateway", "Processes credit card payments.")

    Rel(customer, bookstore, "Browses and purchases books via")
    Rel(bookstore, payments, "Processes payments via", "HTTPS")
```

```mermaid
C4Container
    title Container Diagram for Online Bookstore

    Person(customer, "Customer")
    System_Boundary(bookstore, "Online Bookstore") {
        Container(webapp, "Web Application", "Next.js", "Delivers the storefront.")
        Container(api, "API Gateway", "Kong", "Routes requests.")
        ContainerDb(db, "Database", "PostgreSQL", "Stores data.")
    }

    Rel(customer, webapp, "Uses", "HTTPS")
    Rel(webapp, api, "Calls", "HTTPS/JSON")
    Rel(api, db, "Reads/writes", "SQL")
```
