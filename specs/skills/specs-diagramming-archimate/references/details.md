<!-- Part of the specs-diagramming-archimate skill. Loaded on demand from SKILL.md. -->

# ArchiMate - Enterprise Architecture Modeling Language — details

## Layer and Aspect Framework

ArchiMate's core framework is a grid of layers and aspects:

```
              Active Structure    Behavior           Passive Structure
             (Who/What)          (How)               (On What)
           ┌──────────────────┬──────────────────┬──────────────────┐
Business   │ Business Actor   │ Business Process  │ Business Object  │
           │ Business Role    │ Business Function │ Contract         │
           │ Business         │ Business Service  │ Representation   │
           │   Collaboration  │ Business Event    │ Product          │
           │ Business         │ Business          │                  │
           │   Interface      │   Interaction     │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
Application│ Application      │ Application       │ Data Object      │
           │   Component      │   Function        │                  │
           │ Application      │ Application       │                  │
           │   Collaboration  │   Service         │                  │
           │ Application      │ Application       │                  │
           │   Interface      │   Interaction     │                  │
           │                  │ Application Event │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
Technology │ Node             │ Technology        │ Artifact         │
           │ Device           │   Function        │                  │
           │ System Software  │ Technology        │                  │
           │ Technology       │   Service         │                  │
           │   Collaboration  │ Technology        │                  │
           │ Technology       │   Process         │                  │
           │   Interface      │ Technology Event  │                  │
           │ Path             │ Technology        │                  │
           │ Communication    │   Interaction     │                  │
           │   Network        │                   │                  │
           └──────────────────┴──────────────────┴──────────────────┘
```

## Application Layer Elements

The Application Layer describes application components, their services, and the data they manage.

### Active Structure Elements
| Element | Notation | Description |
|---------|----------|-------------|
| **Application Component** | Blue rectangle with component icon | A modular, deployable, and replaceable part of a software system |
| **Application Collaboration** | Blue rectangle with double-head icon | An aggregate of application components working together |
| **Application Interface** | Blue rectangle with socket icon | A point of access where an application service is made available |

### Behavior Elements
| Element | Notation | Description |
|---------|----------|-------------|
| **Application Function** | Blue rounded rectangle | Automated behavior performed by an application component |
| **Application Service** | Blue rounded rectangle with horizontal line | An externally visible unit of application functionality |
| **Application Interaction** | Blue rounded rectangle with double arrow | A unit of behavior performed by an application collaboration |
| **Application Process** | Blue rounded rectangle with arrow | A sequence of application behaviors |
| **Application Event** | Blue rounded rectangle with lightning bolt | An application-level event |

### Passive Structure Elements
| Element | Notation | Description |
|---------|----------|-------------|
| **Data Object** | Blue rectangle with folded corner | Data structured for automated processing |

## Motivation Elements

Motivation elements model the reasons behind architecture decisions, capturing stakeholder concerns, goals, and requirements.

| Element | Description |
|---------|-------------|
| **Stakeholder** | An individual, team, or organization with interests in the architecture |
| **Driver** | An external or internal condition that motivates an organization to define its goals |
| **Assessment** | The result of analysis of a driver |
| **Goal** | A desired end state |
| **Outcome** | An end result that is achieved or intended |
| **Principle** | A qualitative statement of intent that should be met by the architecture |
| **Requirement** | A statement of need that must be met by the architecture |
| **Constraint** | A restriction on the design or implementation |
| **Meaning** | The knowledge or expertise present in a business object or representation |
| **Value** | The relative worth, utility, or importance of a concept |

## Example: E-Commerce System in ArchiMate Notation

Below is a simplified layered ArchiMate model for an e-commerce system:

```
BUSINESS LAYER
  [Business Actor: Customer]
      │ assigned
      ▼
  [Business Role: Online Buyer]
      │ assigned
      ▼
  [Business Process: Purchase Products]
      │ realizes
      ▼
  [Business Service: Product Ordering Service]

─────────────────────────────────────────────

APPLICATION LAYER
  [Application Service: Order Management Service]
      │ realization of Business Service above
      │ realized by
      ▼
  [Application Component: E-Commerce Platform]
      │ composition
      ├──► [Application Component: Shopping Cart Module]
      ├──► [Application Component: Payment Gateway Adapter]
      └──► [Application Component: Inventory Checker]
      │
      │ accesses
      ▼
  [Data Object: Order]
  [Data Object: Product Catalog]
  [Data Object: Customer Profile]

─────────────────────────────────────────────

TECHNOLOGY LAYER
  [Node: AWS Cloud]
      │ composition
      ├──► [Device: EC2 Instance]
      │        │ assignment
      │        ▼
      │    [System Software: Docker Runtime]
      │        │ assignment
      │        ▼
      │    [Artifact: ecommerce-app.jar]
      │
      ├──► [Device: RDS Instance]
      │        │ assignment
      │        ▼
      │    [System Software: PostgreSQL 15]
      │
      └──► [Communication Network: VPC]
               │ realizes
               ▼
           [Technology Service: Secure Hosting]
```
