<!-- Part of the specs-diagramming-togaf skill. Loaded on demand from SKILL.md. -->

# Architecture Development Method (ADM)

The ADM is an iterative, cyclic process of continuous architecture development. Each phase produces defined deliverables, is validated against requirements, and feeds into the next phase.

```
                    ┌──────────────┐
                    │  Preliminary │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  Architecture│
                    │  Vision (A)  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼───────┐   │   ┌────────▼─────┐
       │  Business     │   │   │ Technology   │
       │  Arch (B)     │   │   │ Arch (D)     │
       └──────┬───────┘   │   └────────┬─────┘
              │     ┌──────▼───────┐   │
              │     │  Info Systems │   │
              │     │  Arch (C)    │   │
              │     └──────┬───────┘   │
              └────────────┼───────────┘
                           │
                    ┌──────▼───────┐
                    │ Opportunities│
                    │ & Solutions  │
                    │    (E)       │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  Migration   │
                    │  Planning(F) │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │ Implementation│
                    │ Governance(G)│
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  Architecture│
                    │  Change Mgmt │
                    │    (H)       │
                    └──────────────┘

      Requirements Management (center, continuous)
```

## Preliminary Phase
**Purpose:** Establish the architecture capability and tailor TOGAF for the organization.

| Activity | Output |
|----------|--------|
| Define architecture organization | Architecture team structure |
| Identify stakeholders and concerns | Stakeholder map |
| Establish architecture principles | Principles catalog |
| Tailor the ADM | Customized ADM process |
| Select architecture tools | Tooling strategy |

**Key Deliverables:**
- Organizational Model for Enterprise Architecture
- Tailored Architecture Framework
- Architecture Principles catalog
- Architecture Repository (initial structure)

## Phase A: Architecture Vision
**Purpose:** Set the scope, constraints, and expectations for the architecture engagement. Secure stakeholder buy-in.

| Activity | Output |
|----------|--------|
| Establish architecture project | Request for Architecture Work |
| Identify stakeholders and concerns | Stakeholder Map matrix |
| Confirm architecture principles | Refined Principles catalog |
| Develop Architecture Vision | Architecture Vision document |
| Obtain approval | Statement of Architecture Work |

**Key Deliverables:**
- Architecture Vision document
- Statement of Architecture Work
- Refined stakeholder map
- High-level baseline and target descriptions
- Gap analysis (high-level)

## Phase B: Business Architecture
**Purpose:** Develop the Target Business Architecture that supports the Architecture Vision.

| Activity | Output |
|----------|--------|
| Develop Baseline Business Architecture | Baseline description |
| Develop Target Business Architecture | Target description |
| Perform gap analysis | Gap analysis report |
| Define roadmap components | Business Architecture roadmap |

**Key Deliverables:**
- Business Architecture document (Baseline and Target)
- Gap analysis results
- Business Architecture components of the Architecture Roadmap

**Catalogs, Matrices, and Diagrams:**
- Organization/Actor catalog
- Business Service/Function catalog
- Business Interaction matrix
- Business Footprint diagram
- Business Service/Information diagram

## Phase C: Information Systems Architecture
**Purpose:** Develop Target Data Architecture and Target Application Architecture.

This phase has two sub-phases that can be done in either order or in parallel:

**Data Architecture:**
- Data Entity/Data Component catalog
- Data Entity/Business Function matrix
- Conceptual/Logical Data diagrams
- Data Dissemination diagram
- Data Lifecycle diagram

**Application Architecture:**
- Application Portfolio catalog
- Interface catalog
- Application/Organization matrix
- Application Communication diagram
- Application and User Location diagram

**Key Deliverables:**
- Data Architecture document (Baseline and Target)
- Application Architecture document (Baseline and Target)
- Gap analysis for data and application domains

## Phase D: Technology Architecture
**Purpose:** Develop the Target Technology Architecture that enables the data and application components.

| Activity | Output |
|----------|--------|
| Develop Baseline Technology Architecture | Current technology landscape |
| Develop Target Technology Architecture | Target technology landscape |
| Perform gap analysis | Technology gaps identified |
| Define candidate roadmap components | Technology roadmap elements |

**Key Deliverables:**
- Technology Architecture document (Baseline and Target)
- Technology Standards catalog
- Technology Portfolio catalog
- Gap analysis results
- Environments and Locations diagram
- Platform Decomposition diagram
- Network Computing/Hardware diagram

## Phase E: Opportunities and Solutions
**Purpose:** Generate the initial Architecture Roadmap based on gap analysis from Phases B, C, and D. Identify major work packages and transition architectures.

**Key Deliverables:**
- Architecture Roadmap (initial, consolidated)
- Transition Architectures (intermediate states between baseline and target)
- Implementation and Migration Strategy
- Work package descriptions

## Phase F: Migration Planning
**Purpose:** Finalize the Architecture Roadmap and the Implementation and Migration Plan. Prioritize projects and create detailed migration plans.

**Key Deliverables:**
- Implementation and Migration Plan (finalized)
- Architecture Roadmap (finalized)
- Transition Architecture descriptions (detailed)
- Architecture implementation governance model

## Phase G: Implementation Governance
**Purpose:** Provide architecture oversight for the implementation. Ensure conformance of projects to the Target Architecture.

| Activity | Output |
|----------|--------|
| Confirm scope and priorities | Implementation governance plan |
| Identify deployment resources | Resource plan |
| Guide implementation | Architecture Contract compliance |
| Perform architecture compliance reviews | Compliance assessment |

**Key Deliverables:**
- Architecture Contract
- Compliance assessments
- Change requests (for architecture updates)
- Architecture-compliant implemented solutions

## Phase H: Architecture Change Management
**Purpose:** Establish procedures for managing change to the architecture. Monitor ongoing enterprise changes and determine whether to initiate a new ADM cycle.

**Key Deliverables:**
- Architecture updates and changes
- New Request for Architecture Work (when significant change detected)
- Change management process documentation
- Updated Architecture Requirements Specification

## Requirements Management (Continuous)
**Purpose:** Operate continuously throughout the ADM cycle to manage architecture requirements as they are identified, stored, and fed into relevant phases.

**Key Activities:**
- Identify and document requirements
- Baseline requirements
- Monitor and manage requirements changes
- Assess impact of changed requirements on current and previous ADM phases
- Ensure requirements traceability
