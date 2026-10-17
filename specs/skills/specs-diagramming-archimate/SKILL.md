---
name: specs-diagramming-archimate
description: Use when modeling enterprise architecture in ArchiMate 3.2. USE FOR: business/application/technology layers, motivation and strategy elements, relationships, viewpoints, cross-layer dependencies. DO NOT USE FOR: the ADM process (use specs-diagramming-togaf), system decomposition (use specs-diagramming-c4-diagrams), general diagrams (use specs-diagramming-mermaidjs).
---

# ArchiMate - Enterprise Architecture Modeling Language

## Overview
ArchiMate is an open and independent enterprise architecture modeling language maintained by The Open Group. It provides a uniform representation for describing, analyzing, and communicating enterprise architectures. ArchiMate is designed to be used alongside TOGAF — where TOGAF defines the process (ADM), ArchiMate provides the visual notation.

ArchiMate 3.2 organizes elements across **layers** (Business, Application, Technology) and **aspects** (Active Structure, Behavior, Passive Structure), with a Motivation extension and Strategy layer.

## Strategy Elements

| Element | Description |
|---------|-------------|
| **Resource** | An asset owned or controlled by an individual or organization |
| **Capability** | An ability that an active structure element possesses |
| **Course of Action** | An approach or plan for achieving a goal |
| **Value Stream** | A sequence of activities that creates an overall result for a customer, stakeholder, or end user |

## Relationships

ArchiMate defines a precise set of relationships between elements. Relationships are categorized into structural, dependency, dynamic, and other.

### Structural Relationships
| Relationship | Notation | Description | Example |
|-------------|----------|-------------|---------|
| **Composition** | Filled diamond ◆───► | Element is composed of one or more other elements | Application Component ◆───► Data Object |
| **Aggregation** | Open diamond ◇───► | Element groups other elements | Business Role ◇───► Business Actor |
| **Assignment** | Filled circle ●───► | Allocation of responsibility, execution, or storage | Business Role ●───► Business Process |
| **Realization** | Dashed line with open triangle ╌╌╌▷ | Element plays a critical role in the creation of a more abstract element | Application Service ╌╌╌▷ Business Service |

### Dependency Relationships
| Relationship | Notation | Description | Example |
|-------------|----------|-------------|---------|
| **Serving** | Open arrowhead ───► | Element provides functionality to another | Application Service ───► Business Process |
| **Access** | Dashed line with arrowhead ╌╌╌► | Process reads/writes data | Business Process ╌╌╌► Business Object |
| **Influence** | Dashed line with open arrowhead ╌╌╌► (with + or -) | Element affects implementation or achievement of a motivation element | Driver ╌╌╌►(+) Goal |

### Dynamic Relationships
| Relationship | Notation | Description | Example |
|-------------|----------|-------------|---------|
| **Triggering** | Filled arrowhead ──▶ | Element causes another to begin | Business Event ──▶ Business Process |
| **Flow** | Filled arrowhead with label ──▶ (label) | Transfer of content between elements | Business Process ──▶"order data"──▶ Business Process |

### Other Relationships
| Relationship | Notation | Description | Example |
|-------------|----------|-------------|---------|
| **Specialization** | Open triangle ───▷ | Element is a particular kind of another element | Online Order ───▷ Order |
| **Association** | Plain line ─── | Unspecified relationship | Element ─── Element |
| **Junction** | Filled circle (AND) or open circle (OR) | Combine relationships | Process1 ──▶ ● ──▶ Process2, Process3 |

## Mapping ArchiMate to TOGAF ADM Phases

| TOGAF ADM Phase | ArchiMate Layer / Viewpoint |
|----------------|----------------------------|
| Phase A: Architecture Vision | Motivation Viewpoint, high-level Layered Viewpoint |
| Phase B: Business Architecture | Business Layer elements, Organization Viewpoint |
| Phase C: Information Systems | Application Layer, Data Objects, Application Structure Viewpoint |
| Phase D: Technology Architecture | Technology Layer, Technology Viewpoint |
| Phase E-F: Opportunities & Migration | Layered Viewpoint with gap annotations |
| Phase G-H: Governance & Change | Implementation and Migration Viewpoint |

## Best Practices
- **Use the correct layer.** Do not model application concerns in the Business Layer or vice versa. Cross-layer connections should use serving or realization relationships.
- **Keep viewpoints focused.** Each diagram should use a single viewpoint. A Layered Viewpoint can show cross-layer dependencies, but avoid cramming all elements into one diagram.
- **Use relationships precisely.** ArchiMate relationships have specific semantics. Do not use "serving" when you mean "realization" — they convey different architectural meaning.
- **Color-code by layer.** Follow the standard color convention: yellow for Business, blue for Application, green for Technology. This provides instant visual orientation.
- **Start with the Layered Viewpoint.** When introducing an architecture to stakeholders, the Layered Viewpoint provides the best overview of how business is supported by applications and technology.
- **Model motivation first.** Before modeling structure, capture stakeholder goals, drivers, and requirements. This ensures architecture decisions are traceable to business rationale.
- **Pair with TOGAF.** ArchiMate provides the notation; TOGAF provides the process. Use ArchiMate diagrams as deliverables within TOGAF ADM phases.
- **Limit elements per diagram to 15-20.** Overcrowded diagrams lose communicative value. Split into multiple viewpoints if needed.
- **Name elements with precision.** Use clear, specific names (e.g., "Order Management Service" not "Service 1"). Element names should be self-explanatory.
- **Version your models.** Like code, ArchiMate models should be version-controlled. Use tool exports (e.g., Archi Open Exchange format) stored alongside source code.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/business-layer-elements.md](references/business-layer-elements.md) | Business Layer Elements — Active Structure Elements, Behavior Elements, Passive Structure Elements |
| [references/technology-layer-elements.md](references/technology-layer-elements.md) | Technology Layer Elements — Active Structure Elements, Behavior Elements, Passive Structure Elements |
| [references/viewpoints.md](references/viewpoints.md) | Viewpoints — Organization Viewpoint, Application Structure Viewpoint, Technology Viewpoint, Layered Viewpoint, Motivation Viewpoint |
| [references/details.md](references/details.md) | Layer and Aspect Framework; Application Layer Elements; Motivation Elements; Example: E-Commerce System in ArchiMate Notation |

## References

- [ArchiMate Specification — The Open Group](https://pubs.opengroup.org/architecture/archimate3-doc/)
- [ArchiMate — The Open Group Overview](https://www.opengroup.org/archimate-forum/archimate-overview)

See references/rules.md for the full rule catalog.
