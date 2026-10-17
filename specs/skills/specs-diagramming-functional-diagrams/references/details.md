<!-- Part of the specs-diagramming-functional-diagrams skill. Loaded on demand from SKILL.md. -->

# Functional Diagrams — details

## Combining Functional Diagram Types

These diagram types are complementary:

```
Functional Decomposition Tree
    │
    │ identifies functions to model
    ▼
IDEF0 Diagrams
    │
    │ identifies data transformations
    ▼
Data Flow Diagrams
    │
    │ identifies processes to orchestrate
    ▼
BPMN Process Models
```

1. **Start with Functional Decomposition** to identify the major functions of the system.
2. **Use IDEF0** to understand the inputs, outputs, controls, and mechanisms of critical functions.
3. **Create DFDs** to trace how data moves through and between the functions.
4. **Model in BPMN** when the focus shifts to implementing business processes with specific roles and decision logic.
