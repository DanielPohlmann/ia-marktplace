<!-- Part of the specs-diagramming-togaf skill. Loaded on demand from SKILL.md. -->

# TOGAF - The Open Group Architecture Framework — details

## Architecture Repository

The Architecture Repository stores all architecture outputs and serves as a holding area for architecture deliverables at various levels of abstraction.

```
┌─────────────────────────────────────────────────┐
│              Architecture Repository             │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌───────────────┐   ┌────────────────────────┐ │
│  │ Architecture   │   │ Standards Information  │ │
│  │ Metamodel      │   │ Base                   │ │
│  └───────────────┘   └────────────────────────┘ │
│                                                  │
│  ┌───────────────┐   ┌────────────────────────┐ │
│  │ Architecture   │   │ Reference Library      │ │
│  │ Capability     │   │                        │ │
│  └───────────────┘   └────────────────────────┘ │
│                                                  │
│  ┌───────────────┐   ┌────────────────────────┐ │
│  │ Architecture   │   │ Governance Log         │ │
│  │ Landscape      │   │                        │ │
│  └───────────────┘   └────────────────────────┘ │
│                                                  │
└─────────────────────────────────────────────────┘
```

| Component | Contents |
|-----------|----------|
| **Architecture Metamodel** | Definitions of architecture content types and their relationships |
| **Architecture Capability** | Parameters, structures, and processes for the architecture practice |
| **Architecture Landscape** | Baseline, target, and transition architectures at Strategic, Segment, and Capability levels |
| **Standards Information Base** | Standards that the architecture must comply with (regulatory, industry, organizational) |
| **Reference Library** | Reference architectures, patterns, templates, and guidelines |
| **Governance Log** | Decision records, compliance assessments, capability assessments, change requests |

## Enterprise Continuum

The Enterprise Continuum classifies architecture and solution assets along a spectrum from generic to organization-specific.

```
Generic ◄──────────────────────────────────────► Specific

┌──────────────┬──────────────┬──────────────┬──────────────┐
│  Foundation   │  Common      │  Industry    │ Organization │
│  Architecture │  Systems     │  Architecture│ -Specific    │
│               │  Architecture│              │ Architecture │
├──────────────┼──────────────┼──────────────┼──────────────┤
│  Foundation   │  Common      │  Industry    │ Organization │
│  Solutions    │  Systems     │  Solutions   │ -Specific    │
│               │  Solutions   │              │ Solutions    │
└──────────────┴──────────────┴──────────────┴──────────────┘
  Architecture Continuum (top row)
  Solutions Continuum (bottom row)
```

- **Architecture Continuum:** Ranges from Foundation Architectures (e.g., TOGAF TRM) through Common Systems Architectures (e.g., III-RM) to Industry and Organization-Specific Architectures.
- **Solutions Continuum:** Ranges from Foundation Solutions (e.g., platforms, operating systems) through to Organization-Specific Solutions (e.g., custom applications).

## Key Deliverables Summary

| Phase | Primary Deliverables |
|-------|---------------------|
| Preliminary | Tailored Architecture Framework, Principles |
| A - Vision | Architecture Vision, Statement of Architecture Work |
| B - Business | Business Architecture document, Gap analysis |
| C - Info Systems | Data Architecture, Application Architecture, Gap analysis |
| D - Technology | Technology Architecture, Standards catalog, Gap analysis |
| E - Opportunities | Architecture Roadmap, Transition Architectures |
| F - Migration | Implementation and Migration Plan |
| G - Governance | Architecture Contract, Compliance assessments |
| H - Change Mgmt | Change requests, Updated requirements |
| Requirements Mgmt | Architecture Requirements Specification (continuous) |
