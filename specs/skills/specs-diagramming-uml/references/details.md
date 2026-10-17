<!-- Part of the specs-diagramming-uml skill. Loaded on demand from SKILL.md. -->

# UML — Unified Modeling Language — details

## Diagram Categories

UML defines two broad categories: **structural diagrams** (static aspects) and **behavioral diagrams** (dynamic aspects).

### Structural Diagrams

| Diagram | Purpose |
|---------|---------|
| Class | Classes, attributes, operations, and relationships |
| Object | Snapshot of instances at a point in time |
| Component | High-level components and their interfaces |
| Package | Grouping of model elements into namespaces |
| Deployment | Physical deployment of artifacts to nodes |
| Composite Structure | Internal structure of a class or component |
| Profile | Extension mechanisms for UML itself |

### Behavioral Diagrams

| Diagram | Purpose |
|---------|---------|
| Use Case | Actor-system interactions (functional requirements) |
| Sequence | Message ordering between lifelines over time |
| Activity | Workflow and process logic (flowchart-like) |
| State Machine | States and transitions for a single object |
| Communication | Object interactions emphasizing links |
| Interaction Overview | High-level flow combining interaction fragments |
| Timing | Behavior changes over time (real-time systems) |

## Class Diagram

The most widely used UML diagram. Models the static structure of a system by showing classes, their attributes, operations, and relationships.

### Notation

```
┌────────────────────────────┐
│      <<stereotype>>        │
│       ClassName             │
├────────────────────────────┤
│ - privateField: Type       │
│ # protectedField: Type     │
│ + publicField: Type        │
│ ~ packageField: Type       │
├────────────────────────────┤
│ + publicMethod(): RetType  │
│ - privateMethod(): void    │
│ # protectedMethod(): void  │
│ + staticMethod(): Type     │  (underlined = static)
│ + abstractMethod()*: void  │  (* = abstract)
└────────────────────────────┘
```

### Visibility Modifiers

| Symbol | Visibility | Meaning |
|--------|-----------|---------|
| `+` | Public | Accessible from any class |
| `-` | Private | Accessible only within the class |
| `#` | Protected | Accessible within the class and subclasses |
| `~` | Package | Accessible within the same package/namespace |

### Attribute Syntax

```
visibility name : Type [multiplicity] = defaultValue {constraint}
```

Examples:
```
- id : int
+ name : String
# items : List<Item> [0..*]
+ status : Status = ACTIVE {readOnly}
```

### Operation Syntax

```
visibility name(param: Type, ...): ReturnType {constraint}
```

Examples:
```
+ calculateTotal(): Decimal
- validate(input: String): Boolean
+ findById(id: int): Customer {query}
```

## Stereotypes

Stereotypes extend UML elements with domain-specific meaning. They are shown in guillemets (`<< >>`).

### Common Stereotypes

| Stereotype | Applied To | Meaning |
|-----------|-----------|---------|
| `<<interface>>` | Class | Defines a contract (no implementation) |
| `<<abstract>>` | Class | Cannot be instantiated directly |
| `<<enumeration>>` | Class | Fixed set of named values |
| `<<entity>>` | Class | Domain object with identity |
| `<<value>>` | Class | Immutable value object |
| `<<service>>` | Class | Stateless service |
| `<<repository>>` | Class | Data access object |
| `<<controller>>` | Class | Handles user input / HTTP requests |
| `<<factory>>` | Class | Creates instances of other classes |
| `<<singleton>>` | Class | Only one instance exists |
| `<<dataType>>` | Class | Pure data structure |
| `<<utility>>` | Class | Static methods only |

## Sequence Diagram

Models the time-ordered exchange of messages between participants.

### Notation

```
┌─────┐          ┌─────┐          ┌──────┐
│Actor│          │Obj A│          │Obj B │
└──┬──┘          └──┬──┘          └──┬───┘
   │   message()    │                │
   │───────────────>│                │
   │                │  delegate()    │
   │                │───────────────>│
   │                │   response     │
   │                │<─ ─ ─ ─ ─ ─ ─ │
   │   result       │                │
   │<─ ─ ─ ─ ─ ─ ─ │                │
```

### Message Types

| Arrow | Type | Meaning |
|-------|------|---------|
| `────>` | Synchronous | Caller waits for response |
| `- - ->` | Asynchronous / Return | Fire-and-forget or return value |
| `────>` (to self) | Self-call | Object calls its own method |

### Combined Fragments

| Fragment | Keyword | Purpose |
|----------|---------|---------|
| Alternative | `alt` / `else` | If/else branching |
| Option | `opt` | If (no else) |
| Loop | `loop` | Repetition |
| Parallel | `par` | Concurrent execution |
| Critical | `critical` | Mutual exclusion region |
| Break | `break` | Exit enclosing fragment |
| Reference | `ref` | Reference to another sequence |

## Activity Diagram

Models workflows and process logic. Similar to flowcharts but with UML semantics for concurrency (fork/join) and swimlanes.

### Notation

| Symbol | Meaning |
|--------|---------|
| Filled circle | Initial node (start) |
| Rounded rectangle | Action / Activity |
| Diamond | Decision / Merge |
| Thick horizontal bar | Fork (split) / Join (synchronize) |
| Circle with X | Flow final (terminates one path) |
| Bullseye | Activity final (ends all flows) |

### Example Structure

```
    (●)              ← Initial node
     │
  ┌──▼──┐
  │Receive│
  │Order  │
  └──┬──┘
     ◇                ← Decision
    / \
  Yes   No
  /       \
┌▼────┐  ┌▼─────┐
│Check │  │Reject │
│Stock │  │Order  │
└──┬──┘  └──┬───┘
   │        (◉)      ← Activity final
   ═══                ← Fork bar
  / \
┌▼──┐ ┌▼────────┐
│Pack│ │Process   │
│Item│ │Payment   │
└─┬─┘ └────┬────┘
   ═══                ← Join bar
    │
 ┌──▼──┐
 │ Ship │
 └──┬──┘
    (◉)
```

### Swimlanes (Partitions)

Swimlanes divide activities by responsible actor or system.

```
│  Customer   │   System    │  Warehouse  │
│             │             │             │
│  (●)        │             │             │
│   │         │             │             │
│ Place Order │             │             │
│   │─────────┼──> Validate │             │
│             │   │─────────┼──> Pick Item│
│             │             │   │         │
│             │   Invoice ◄─┼───│         │
│             │   │         │   Ship      │
│  Receive ◄──┼───│         │             │
│   (◉)       │             │             │
```

## State Machine Diagram

Models the lifecycle of a single object through its states and transitions.

### Notation

| Symbol | Meaning |
|--------|---------|
| Filled circle | Initial pseudo-state |
| Rounded rectangle | State |
| Arrow | Transition |
| Bullseye | Final state |

### Transition Syntax

```
trigger [guard] / effect
```

- **trigger**: Event that causes the transition (e.g., `submit`, `timeout`)
- **guard**: Boolean condition in brackets (e.g., `[isValid]`)
- **effect**: Action performed during transition (e.g., `/ sendEmail()`)

### Example

```
(●)
 │
 ▼
┌──────────┐    submit       ┌────────────┐
│   Draft   │───────────────>│  Submitted  │
│           │                │             │
│entry/init │                │entry/notify │
└──────────┘                └──────┬─────┘
     ▲                            │
     │ reopen                     ◇
     │                      [valid]│ [invalid]
     │                     ┌──────▼─┐  │
     │                     │Approved │  │
     │                     │         │  │
     │                     └────┬───┘  │
     │                          │      ▼
     │                          │ ┌────────┐
     │                          │ │Rejected│
     └──────────────────────────┤ └────────┘
                                │
                                ▼
                              (◉)
```

### Composite (Nested) States

States can contain substates to model complex behavior.

```
┌──────────── Active ──────────────┐
│  ┌─────────┐      ┌───────────┐ │
│  │Processing│─────>│ Validating│ │
│  └─────────┘      └───────────┘ │
└──────────────────────────────────┘
```

## Use Case Diagram

Models functional requirements by showing actors and the use cases (features) they interact with.

### Notation

| Symbol | Meaning |
|--------|---------|
| Stick figure | Actor (user or external system) |
| Oval | Use case (feature / function) |
| Rectangle | System boundary |
| Solid line | Association (actor participates in use case) |
| Dashed arrow `<<include>>` | Use case always includes another |
| Dashed arrow `<<extend>>` | Use case optionally extends another |
| Open triangle arrow | Generalization (actor or use case inheritance) |

### Example

```
                    ┌─────── Online Store ────────┐
                    │                              │
  ┌────┐           │   (Browse Catalog)            │
  │User│───────────┼──>(Place Order)               │
  └──┬─┘           │       │                       │
     │              │       │ <<include>>           │
     │              │       ▼                       │
     │              │   (Process Payment)           │
     │              │       │                       │
     │              │       │ <<extend>>            │
     │              │       ▼                       │
     │              │   (Apply Coupon)              │
     │              │                              │
  ┌──┴──┐          │   (Manage Inventory)          │
  │Admin│──────────┼──>(Generate Reports)          │
  └─────┘          │                              │
                    └──────────────────────────────┘
```

## Deployment Diagram

Maps software artifacts to hardware/infrastructure nodes.

### Notation

| Symbol | Meaning |
|--------|---------|
| 3D box | Node (server, VM, device, container) |
| Rectangle inside node | Artifact (deployed software) |
| Dashed arrow `<<deploy>>` | Deployment relationship |

### Example

```
┌──────────── <<device>> ────────────┐
│            Client Browser           │
│  ┌─────────────────────────┐       │
│  │ <<artifact>> SPA Bundle │       │
│  └─────────────────────────┘       │
└─────────────────┬──────────────────┘
                  │ HTTPS
┌─────────────────▼──────────────────┐
│     <<executionEnvironment>>        │
│            Kubernetes               │
│  ┌──────────────┐ ┌──────────────┐ │
│  │ <<artifact>> │ │ <<artifact>> │ │
│  │  API Pod     │ │  Worker Pod  │ │
│  └──────┬───────┘ └──────────────┘ │
└─────────┼──────────────────────────┘
          │ TCP/5432
┌─────────▼──────────────────────────┐
│       <<device>> DB Server          │
│  ┌─────────────────────────┐       │
│  │ <<artifact>> PostgreSQL │       │
│  └─────────────────────────┘       │
└────────────────────────────────────┘
```

## Constraints and Notes

### Constraints

Constraints are boolean expressions enclosed in curly braces `{}` that restrict model elements.

```
{ordered}          - Collection is ordered
{unique}           - No duplicates allowed
{readOnly}         - Cannot be modified after initialization
{frozen}           - Cannot be changed after creation
{xor}              - Exactly one of the associations applies
{subset}           - One collection is a subset of another
```

### Notes

Notes are attached to any UML element with a dashed line.

```
┌──────────────┐
│ Order         │ ─ ─ ─ ┐
├──────────────┤         │
│ + total: Dec │    ┌────┴──────────────┐
└──────────────┘    │ total must be >= 0 │
                    │ {total >= 0}       │
                    └───────────────────┘
```
