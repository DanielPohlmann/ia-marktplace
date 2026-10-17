---
name: specs-diagramming-uml
description: Use when you need UML notation semantics independent of a tool. USE FOR: class, sequence, activity, state machine, use case, component, deployment, package, object diagrams, relationships, multiplicity, visibility, stereotypes, OCL notes. DO NOT USE FOR: tool syntax (use specs-diagramming-plantuml or specs-diagramming-mermaidjs), enterprise views (use specs-diagramming-archimate), data models (use specs-diagramming-erd).
---

# UML — Unified Modeling Language

## Overview

UML (Unified Modeling Language) is a standardized visual modeling language maintained by the Object Management Group (OMG). It provides a comprehensive set of diagram types for describing the structure, behavior, and interactions of software systems. UML is tool-agnostic — it defines notation and semantics, not rendering. For text-based rendering of UML diagrams, see the `mermaidjs`, `plantuml`, or `d2` skills.

## Relationships

### Relationship Types

| Relationship | Line | Arrowhead | Meaning |
|-------------|------|-----------|---------|
| Association | Solid | Open arrow or none | "Uses" or "knows about" |
| Directed Association | Solid | Open arrow (one end) | One-way navigability |
| Aggregation | Solid | Open diamond | "Has-a" (weak ownership, part can exist independently) |
| Composition | Solid | Filled diamond | "Owns-a" (strong ownership, part destroyed with whole) |
| Inheritance (Generalization) | Solid | Open triangle | "Is-a" (subclass extends superclass) |
| Realization (Implementation) | Dashed | Open triangle | Class implements an interface |
| Dependency | Dashed | Open arrow | "Uses temporarily" (parameter, local variable) |

### Visual Notation

```
Association:         A ──────────── B
Directed:            A ─────────> B
Aggregation:         A ◇────────── B    (A has B, B can exist alone)
Composition:         A ◆────────── B    (A owns B, B dies with A)
Inheritance:         A ────────▷ B      (A extends B)
Realization:         A - - - -▷ B       (A implements B)
Dependency:          A - - - -> B       (A depends on B)
```

### Multiplicity

Multiplicity indicates how many instances participate in a relationship.

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `0..1` | Zero or one (optional) |
| `*` or `0..*` | Zero or more |
| `1..*` | One or more |
| `n` | Exactly n |
| `n..m` | Between n and m |

Example:
```
Customer 1 ──────── 0..* Order
(One customer places zero or more orders)

Order 1 ──────── 1..* OrderItem
(One order contains one or more items)
```

### Association Classes

When a relationship itself has attributes:

```
Student ────────── Course
            │
     ┌──────┴──────┐
     │ Enrollment   │
     ├──────────────┤
     │ grade: Grade  │
     │ semester: Str │
     └──────────────┘
```

## Component Diagram

Shows the high-level components of a system and their interfaces.

### Notation

| Symbol | Meaning |
|--------|---------|
| Rectangle with component icon | Component |
| Circle (lollipop) | Provided interface |
| Half-circle (socket) | Required interface |
| Dashed arrow `<<use>>` | Usage dependency |

### Example

```
┌──────────────┐        ┌──────────────┐
│ <<component>> │        │ <<component>> │
│  Web UI       │──○─────┤  API Service  │
│               │  REST  │              │
└──────────────┘        └──────┬───────┘
                               │
                          ○────┘ IDataAccess
                          │
                   ┌──────┴───────┐
                   │ <<component>> │
                   │  Data Layer   │
                   └──────────────┘
```

## Package Diagram

Groups model elements into namespaces to show code organization and dependencies.

```
┌──── Domain ────────────┐
│  ┌──────┐ ┌──────────┐ │
│  │Order │ │ Customer │ │
│  └──────┘ └──────────┘ │
└────────┬───────────────┘
         │ <<import>>
┌────────▼───────────────┐
│ Infrastructure          │
│  ┌────────────────────┐ │
│  │ OrderRepository    │ │
│  └────────────────────┘ │
└─────────────────────────┘
```

## Object Diagram

A snapshot of instances and their relationships at a specific point in time. Uses the same notation as class diagrams but shows objects (instances) instead of classes.

```
┌──────────────────┐
│ order1 : Order    │
├──────────────────┤
│ id = 42           │
│ status = "ACTIVE" │
│ total = 99.50     │
└────────┬─────────┘
         │ contains
┌────────▼─────────┐
│ item1 : OrderItem │
├──────────────────┤
│ product = "Book"  │
│ quantity = 2      │
│ price = 49.75     │
└──────────────────┘
```

## Best Practices

- **Choose the right diagram for the audience.** Use case diagrams for stakeholders, class diagrams for developers, deployment diagrams for operations.
- **Do not model everything.** UML is a communication tool, not a code generation specification. Model only what adds clarity.
- **Keep diagrams focused.** One diagram, one concern. A class diagram should not try to show every class in the system.
- **Use consistent naming.** Class names in PascalCase, operations in camelCase, constants in UPPER_CASE.
- **Show multiplicity on all associations.** Omitted multiplicity is ambiguous and forces readers to guess.
- **Distinguish aggregation from composition.** Use composition (filled diamond) when the part cannot exist without the whole; use aggregation (open diamond) when it can.
- **Use stereotypes sparingly.** Only add stereotypes that convey meaning your audience needs. Do not decorate every element.
- **Combine structural and behavioral diagrams.** A class diagram shows what exists; a sequence diagram shows how it behaves. Together they tell the full story.
- **Use packages to manage complexity.** For systems with many classes, organize them into packages first, then detail individual packages.
- **Validate against code.** If your UML diverges from the actual code, the diagrams become misleading. Keep them synchronized or clearly label them as aspirational.
- **Prefer text-based tools.** Use Mermaid, PlantUML, or D2 to write UML diagrams as code so they can be version-controlled and reviewed in pull requests.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | Diagram Categories; Class Diagram; Stereotypes; Sequence Diagram; Activity Diagram; State Machine Diagram; Use Case Diagram; Deployment Diagram; Constraints and Notes |

## References

- [OMG Unified Modeling Language (UML) Specification](https://www.omg.org/spec/UML/)
- [UML — Wikipedia](https://en.wikipedia.org/wiki/Unified_Modeling_Language)

See references/rules.md for the full rule catalog.
