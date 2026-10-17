<!-- Part of the specs-diagramming-togaf skill. Loaded on demand from SKILL.md. -->

# TOGAF Content Metamodel

The Content Metamodel defines a formal structure for architectural artifacts. It specifies the types of entities that make up an architecture and how they relate.

## Core Content Metamodel Entities

| Entity | Domain | Description |
|--------|--------|-------------|
| **Actor** | Business | A person, organization, or system that performs behavior |
| **Role** | Business | Responsibility or part played by an actor |
| **Business Service** | Business | Supports business capabilities, exposed via interfaces |
| **Business Process** | Business | Ordered set of activities producing a defined outcome |
| **Data Entity** | Data | An encapsulation of data recognized by a business domain expert |
| **Logical Data Component** | Data | A boundary grouping of related data entities |
| **Application Component** | Application | An encapsulation of application functionality |
| **Logical Application Component** | Application | A conceptual grouping of application functionality |
| **Technology Component** | Technology | A technology building block (hardware, infrastructure, middleware) |
| **Platform Service** | Technology | A technical capability required to support application components |

## Key Metamodel Relationships

```
Actor ──performs──► Role
Role ──participates-in──► Business Process
Business Process ──produces──► Business Service
Business Service ──is-realized-by──► Logical Application Component
Logical Application Component ──is-implemented-by──► Application Component
Application Component ──is-hosted-on──► Technology Component
Data Entity ──is-accessed-by──► Logical Application Component
```

## Extensions to the Core Metamodel
TOGAF defines optional extensions:
- **Governance Extensions:** Architecture Contract, Standard, Principle
- **Services Extensions:** Information System Service, Platform Service
- **Process/Event Extensions:** Event, Control, Product
- **Data Extensions:** Physical Data Component, Data Entity relationships
- **Infrastructure Consolidation Extensions:** Physical Technology Component, Location
