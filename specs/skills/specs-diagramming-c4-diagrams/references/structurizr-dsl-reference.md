<!-- Part of the specs-diagramming-c4-diagrams skill. Loaded on demand from SKILL.md. -->

# Structurizr DSL Reference

## Workspace Definition

Every Structurizr DSL file starts with a `workspace` block that contains a `model` and `views`.

```
workspace "Name" "Description" {
    !identifiers hierarchical

    model {
        // Define people, software systems, containers, components
    }

    views {
        // Define diagrams (views) of the model
    }
}
```

## Model Elements

| Element | Syntax | Description |
|---------|--------|-------------|
| Person | `person "Name" "Description" "Tag"` | A human user of the system |
| Software System | `softwareSystem "Name" "Description" "Tag"` | A top-level system |
| Container | `container "Name" "Description" "Technology" "Tag"` | A deployable unit inside a system |
| Component | `component "Name" "Description" "Technology" "Tag"` | A logical grouping inside a container |

## Relationships

```
source -> destination "Description" "Technology" "Tag"
```

Examples:
```
user -> system "Uses"
webapp -> api "Makes API calls to" "HTTPS/JSON"
api -> db "Reads from and writes to" "JDBC"
```

## Views

| View | Syntax | Shows |
|------|--------|-------|
| System Context | `systemContext <system> "key" { ... }` | Level 1 |
| Container | `container <system> "key" { ... }` | Level 2 |
| Component | `component <container> "key" { ... }` | Level 3 |
| Dynamic | `dynamic <scope> "key" { ... }` | Interaction sequences |
| Deployment | `deployment <system> <environment> "key" { ... }` | Infrastructure mapping |

## Styles

```
views {
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
        element "Database" {
            shape Cylinder
        }
        element "External" {
            background #999999
        }
        relationship "Relationship" {
            thickness 2
            color #707070
            style dashed
        }
    }
}
```

## Available Shapes

`Box` (default), `RoundedBox`, `Circle`, `Ellipse`, `Hexagon`, `Cylinder`, `Pipe`, `Person`, `Robot`, `Folder`, `WebBrowser`, `MobileDevicePortrait`, `MobileDeviceLandscape`, `Component`
