<!-- Part of the specs-diagramming-archimate skill. Loaded on demand from SKILL.md. -->

# Technology Layer Elements

The Technology Layer describes the infrastructure (hardware, networks, system software) that supports the Application Layer.

## Active Structure Elements
| Element | Notation | Description |
|---------|----------|-------------|
| **Node** | Green 3D box | A computational or physical resource that hosts artifacts |
| **Device** | Green 3D box with device icon | A physical hardware resource |
| **System Software** | Green 3D box with software icon | A software environment for specific types of components and objects (e.g., OS, JVM, DBMS) |
| **Technology Collaboration** | Green rectangle with double-head icon | An aggregate of nodes working together |
| **Technology Interface** | Green rectangle with socket icon | A point of access to technology services |
| **Path** | Green line | A link between two or more nodes through which they exchange data |
| **Communication Network** | Green line with network icon | A set of structures connecting nodes for transmission, routing, and reception |

## Behavior Elements
| Element | Notation | Description |
|---------|----------|-------------|
| **Technology Function** | Green rounded rectangle | A collection of technology behavior |
| **Technology Service** | Green rounded rectangle with horizontal line | An externally visible unit of technology functionality |
| **Technology Process** | Green rounded rectangle with arrow | A sequence of technology behaviors |
| **Technology Interaction** | Green rounded rectangle with double arrow | Technology behavior performed by a collaboration |
| **Technology Event** | Green rounded rectangle with lightning bolt | A technology-level event |

## Passive Structure Elements
| Element | Notation | Description |
|---------|----------|-------------|
| **Artifact** | Green rectangle with folded corner and binary icon | A piece of data used or produced by technology, typically a file or deployable unit |
