<!-- Part of the specs-diagramming-archimate skill. Loaded on demand from SKILL.md. -->

# Viewpoints

ArchiMate viewpoints define a selection of elements, relationships, and their presentation. Use the right viewpoint for the right audience.

## Organization Viewpoint
**Purpose:** Show the structure of the organization in terms of business actors, roles, and their relationships.

**Typical Elements:** Business Actor, Business Role, Business Collaboration, Business Interface, Location

```
┌──────────────────────────────────────────┐
│ Organization Viewpoint                    │
│                                           │
│  ┌──────────┐  assigned  ┌────────────┐  │
│  │ Business  │──────────►│ Business   │  │
│  │ Actor:    │           │ Role:      │  │
│  │ Customer  │           │ Buyer      │  │
│  │ Service   │           │            │  │
│  │ Dept      │           └────────────┘  │
│  └──────────┘                            │
│       │ composition                      │
│       ▼                                  │
│  ┌──────────┐                            │
│  │ Business  │                           │
│  │ Actor:    │                           │
│  │ Support   │                           │
│  │ Agent     │                           │
│  └──────────┘                            │
└──────────────────────────────────────────┘
```

## Application Structure Viewpoint
**Purpose:** Show the structure of applications, their components, data objects, and interfaces.

**Typical Elements:** Application Component, Application Interface, Data Object, Application Collaboration

## Technology Viewpoint
**Purpose:** Show the technology infrastructure: nodes, devices, networks, and system software.

**Typical Elements:** Node, Device, System Software, Communication Network, Path, Technology Interface, Artifact

## Layered Viewpoint
**Purpose:** Provide a cross-layer overview showing how business services are supported by application services, which in turn are supported by technology services.

```
┌──────────────────────────────────────────────────────────┐
│ Business Layer                                            │
│  ┌────────────────┐       ┌─────────────────────────┐    │
│  │ Business Role:  │──────►│ Business Process:       │    │
│  │ Account Manager │ assgn │ Handle Customer Order   │    │
│  └────────────────┘       └───────────┬─────────────┘    │
│                                        │ serving          │
├────────────────────────────────────────┼─────────────────┤
│ Application Layer                      ▼                  │
│                           ┌─────────────────────────┐    │
│                           │ Application Service:     │    │
│                           │ Order Processing Service │    │
│                           └───────────┬─────────────┘    │
│                                        │ realization      │
│                           ┌───────────▼─────────────┐    │
│                           │ Application Component:   │    │
│                           │ Order Management System  │    │
│                           └───────────┬─────────────┘    │
│                                        │ serving          │
├────────────────────────────────────────┼─────────────────┤
│ Technology Layer                       ▼                  │
│                           ┌─────────────────────────┐    │
│                           │ Technology Service:      │    │
│                           │ Application Hosting      │    │
│                           └───────────┬─────────────┘    │
│                                        │ realization      │
│                           ┌───────────▼─────────────┐    │
│                           │ Node:                    │    │
│                           │ Application Server       │    │
│                           └─────────────────────────┘    │
└──────────────────────────────────────────────────────────┘
```

## Motivation Viewpoint
**Purpose:** Show stakeholders, their drivers, assessments, goals, principles, requirements, and constraints.

**Typical Elements:** Stakeholder, Driver, Assessment, Goal, Principle, Requirement, Constraint

```
┌──────────────────────────────────────────────────────────┐
│ Motivation Viewpoint                                      │
│                                                           │
│  ┌─────────────┐  has  ┌───────────┐  leads  ┌────────┐ │
│  │ Stakeholder: │──────►│ Driver:   │────────►│ Goal:  │ │
│  │ CTO          │       │ Need for  │         │ Reduce │ │
│  └─────────────┘       │ agility   │         │ TTM by │ │
│                         └───────────┘         │ 30%    │ │
│                                                └───┬────┘ │
│                                                    │      │
│                               realizes             ▼      │
│                         ┌────────────────────────────────┐│
│                         │ Requirement:                    ││
│                         │ Implement microservice arch     ││
│                         └────────────────────────────────┘│
└──────────────────────────────────────────────────────────┘
```
