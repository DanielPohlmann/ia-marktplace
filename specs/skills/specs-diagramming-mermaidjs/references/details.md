<!-- Part of the specs-diagramming-mermaidjs skill. Loaded on demand from SKILL.md. -->

# Mermaid.js — details

## Supported Diagram Types

| Diagram | Keyword | Purpose |
|---------|---------|---------|
| Flowchart | `flowchart` or `graph` | Process flows, decision trees, workflows |
| Sequence | `sequenceDiagram` | Interaction order between participants |
| Class | `classDiagram` | Object-oriented structure and relationships |
| State | `stateDiagram-v2` | State machine transitions |
| Entity Relationship | `erDiagram` | Data model relationships |
| Gantt | `gantt` | Project scheduling and timelines |
| Pie | `pie` | Proportional data |
| Mindmap | `mindmap` | Hierarchical idea mapping |
| Timeline | `timeline` | Chronological events |
| Quadrant | `quadrantChart` | 2x2 categorization matrix |
| C4 Context | `C4Context` | C4 Level 1 diagrams |
| C4 Container | `C4Container` | C4 Level 2 diagrams |
| Git Graph | `gitGraph` | Branch and commit visualization |

## Flowchart

The most commonly used diagram type. Supports directional layouts, shape types, subgraphs, and link styles.

### Directions

| Direction | Meaning |
|-----------|---------|
| `TB` or `TD` | Top to Bottom |
| `BT` | Bottom to Top |
| `LR` | Left to Right |
| `RL` | Right to Left |

### Node Shapes

| Syntax | Shape |
|--------|-------|
| `A[Text]` | Rectangle |
| `A(Text)` | Rounded rectangle |
| `A([Text])` | Stadium / pill |
| `A{Text}` | Diamond (decision) |
| `A{{Text}}` | Hexagon |
| `A[[Text]]` | Subroutine |
| `A[(Text)]` | Cylinder (database) |
| `A((Text))` | Circle |
| `A>Text]` | Asymmetric / flag |

### Full Example

````markdown
```mermaid
flowchart LR
    A[User Request] --> B{Authenticated?}
    B -->|Yes| C[Load Dashboard]
    B -->|No| D[Login Page]
    D --> E[Enter Credentials]
    E --> F{Valid?}
    F -->|Yes| C
    F -->|No| G[Show Error]
    G --> D

    subgraph Backend
        C --> H[(Database)]
        C --> I[Cache]
    end
```
````

### Link Types

| Syntax | Type |
|--------|------|
| `-->` | Arrow |
| `---` | Line (no arrow) |
| `-.->` | Dotted arrow |
| `==>` | Thick arrow |
| `--text-->` | Arrow with label |
| `-.text.->` | Dotted arrow with label |

## Sequence Diagram

Shows the order of interactions between participants over time.

````markdown
```mermaid
sequenceDiagram
    actor User
    participant UI as Web App
    participant API as API Server
    participant DB as Database

    User->>UI: Click "Place Order"
    UI->>API: POST /orders
    activate API
    API->>DB: INSERT order
    DB-->>API: order_id
    API->>API: Validate inventory
    alt In Stock
        API-->>UI: 201 Created
        UI-->>User: Order Confirmation
    else Out of Stock
        API-->>UI: 409 Conflict
        UI-->>User: "Item unavailable"
    end
    deactivate API

    Note over API,DB: Async inventory sync runs nightly
```
````

### Arrow Types

| Syntax | Meaning |
|--------|---------|
| `->>` | Solid arrow (synchronous) |
| `-->>` | Dashed arrow (response / async) |
| `-x` | Solid with cross (lost message) |
| `--x` | Dashed with cross |
| `-)` | Solid open arrow (async fire-and-forget) |
| `--)` | Dashed open arrow |

### Features

- `activate` / `deactivate` for activation bars
- `alt` / `else` / `end` for conditional logic
- `loop` / `end` for repetition
- `par` / `and` / `end` for parallel processing
- `critical` / `option` / `end` for critical regions
- `Note over A,B: text` for annotations
- `rect rgb(...)` for background highlighting

## Class Diagram

Models object-oriented structure with classes, interfaces, relationships, and visibility.

````markdown
```mermaid
classDiagram
    class Animal {
        <<abstract>>
        +String name
        +int age
        +makeSound()* void
        +move() void
    }

    class Dog {
        +String breed
        +makeSound() void
        +fetch() void
    }

    class Cat {
        +bool isIndoor
        +makeSound() void
        +purr() void
    }

    class IFeedable {
        <<interface>>
        +feed(Food food) void
    }

    Animal <|-- Dog : extends
    Animal <|-- Cat : extends
    IFeedable <|.. Dog : implements
    IFeedable <|.. Cat : implements
    Dog "1" --> "*" Toy : plays with
```
````

### Visibility Modifiers

| Symbol | Meaning |
|--------|---------|
| `+` | Public |
| `-` | Private |
| `#` | Protected |
| `~` | Package/Internal |

### Relationship Types

| Syntax | Meaning |
|--------|---------|
| `<\|--` | Inheritance |
| `<\|..` | Implementation (interface) |
| `*--` | Composition |
| `o--` | Aggregation |
| `-->` | Association |
| `..>` | Dependency |
| `--` | Link (solid) |
| `..` | Link (dashed) |

## Directives and Themes

### Directives

Directives configure diagram behavior inline. Place them at the top of the diagram block.

````markdown
```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#BB2528'}}}%%
flowchart LR
    A --> B --> C
```
````

### Built-in Themes

| Theme | Description |
|-------|-------------|
| `default` | Standard light theme |
| `dark` | Dark background |
| `forest` | Green-toned |
| `neutral` | Grayscale |
| `base` | Minimal starting point for customization |

### Custom Theme Variables

```
%%{init: {'theme': 'base', 'themeVariables': {
    'primaryColor': '#4C566A',
    'primaryTextColor': '#ECEFF4',
    'primaryBorderColor': '#D8DEE9',
    'lineColor': '#88C0D0',
    'secondaryColor': '#5E81AC',
    'tertiaryColor': '#2E3440'
}}}%%
```
