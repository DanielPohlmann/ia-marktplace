---
name: specs-diagramming-c4-diagrams
description: Use when modeling software architecture with the C4 model. USE FOR: system context, container, component, and code diagrams, Structurizr DSL workspaces, views and styles, Mermaid C4. DO NOT USE FOR: flowcharts (use specs-diagramming-mermaidjs), enterprise architecture (use specs-diagramming-archimate), data models (use specs-diagramming-erd).
---

# C4 Model Diagrams

## Overview

The C4 model, created by Simon Brown, is a hierarchical approach to software architecture diagramming. It uses four levels of abstraction — Context, Container, Component, and Code — to describe a software system at different zoom levels. The primary tooling for C4 is the **Structurizr DSL**, a text-based domain-specific language purpose-built for C4 modeling.

## Structurizr CLI Commands

```bash
# Validate a workspace DSL file
structurizr-cli validate -workspace workspace.dsl

# Push a workspace to Structurizr (cloud or on-premises)
structurizr-cli push -id <workspace-id> -key <api-key> -secret <api-secret> -workspace workspace.dsl

# Pull a workspace from Structurizr
structurizr-cli pull -id <workspace-id> -key <api-key> -secret <api-secret>

# Export diagrams to various formats
structurizr-cli export -workspace workspace.dsl -format plantuml
structurizr-cli export -workspace workspace.dsl -format mermaid
structurizr-cli export -workspace workspace.dsl -format json
structurizr-cli export -workspace workspace.dsl -format png

# Run Structurizr Lite locally (Docker)
docker run -it --rm -p 8080:8080 -v $(pwd):/usr/local/structurizr structurizr/lite
```

## Best Practices

- **Start at Level 1.** Always begin with a System Context diagram to define boundaries and external dependencies before zooming in.
- **Use hierarchical decomposition.** Each level should tell a coherent story at its abstraction level. Do not mix abstractions (e.g., do not show database tables in a Container diagram).
- **Name elements consistently.** Use the same name for an element across all levels so readers can trace from Context down to Component.
- **Limit detail per diagram.** Keep each diagram to 5-20 elements. If a diagram is too crowded, it means the container or component needs further decomposition.
- **Tag elements for styling.** Use tags like `"Database"`, `"External"`, `"WebBrowser"` to apply consistent visual styles.
- **Skip Level 4 unless necessary.** Code-level diagrams are better generated from source code. Reserve manual Level 4 diagrams for algorithmically complex components.
- **Version your DSL.** Store `workspace.dsl` in Git alongside the source code it describes. Treat it as a first-class artifact.
- **Use `autolayout`** to get consistent, automated positioning. Override with explicit positioning only when automatic layout produces poor results.
- **Add deployment views** for infrastructure mapping — they show how containers map to cloud services, VMs, or Kubernetes clusters.
- **Export to Mermaid** for embedding in Markdown documentation. Use the Structurizr CLI `export -format mermaid` command.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/the-four-levels.md](references/the-four-levels.md) | The Four Levels — Level 1: System Context, Level 2: Container, Level 3: Component, Level 4: Code |
| [references/structurizr-dsl-reference.md](references/structurizr-dsl-reference.md) | Structurizr DSL Reference — Workspace Definition, Model Elements, Relationships, Views, Styles, Available Shapes |
| [references/complete-workspace-example.md](references/complete-workspace-example.md) | Complete Workspace Example |
| [references/details.md](references/details.md) | Mermaid C4 Support |

## References

- [C4 Model — Simon Brown](https://c4model.com/)
- [Structurizr DSL Documentation](https://docs.structurizr.com/dsl)

See references/rules.md for the full rule catalog.
