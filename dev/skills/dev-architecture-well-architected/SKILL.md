---
name: dev-architecture-well-architected
description: Use when reviewing a cloud workload against AWS, Azure, or GCP well-architected frameworks. USE FOR: reliability, security, cost, performance, operational-excellence pillars, review process, cross-cloud comparison. DO NOT USE FOR: microservice patterns (use dev-architecture-microservices), threat modeling (use security-threat-modeling), API design (use dev-backend-api-design).
---

# Cloud Well-Architected Frameworks

## Overview
The major cloud providers each publish a Well-Architected Framework -- a set of pillars, design principles, and best practices for building reliable, secure, performant, and cost-effective workloads in the cloud. While the terminology and organization differ, the core concerns are remarkably consistent across all three.

This skill covers all three frameworks in a unified view, enabling cross-cloud comparison and provider-agnostic architecture reasoning.

## Cross-Cloud Pillar Comparison

| Concern | AWS (6 Pillars) | Azure (5 Pillars) | GCP (6 Pillars) |
|---------|-----------------|-------------------|-----------------|
| **Operations** | Operational Excellence | Operational Excellence | Operational Excellence |
| **Security** | Security | Security | Security, Privacy & Compliance |
| **Reliability** | Reliability | Reliability | Reliability |
| **Performance** | Performance Efficiency | Performance Efficiency | Performance Optimization |
| **Cost** | Cost Optimization | Cost Optimization | Cost Optimization |
| **Sustainability** | Sustainability | -- | -- |
| **System Design** | -- | -- | System Design |

**Key observation:** All three frameworks agree on the five core concerns (operations, security, reliability, performance, cost). AWS adds Sustainability; GCP adds System Design as an explicit pillar; Azure covers both implicitly within its five pillars.

---

## Pillar Tensions and Tradeoffs

The pillars are inherently in tension. Optimizing one often increases costs or complexity in another:

| Tradeoff | Example |
|----------|---------|
| Reliability vs. Cost | Multi-region deployment increases availability but doubles infrastructure cost |
| Security vs. Performance | Encryption at rest and in transit adds latency |
| Performance vs. Cost | Over-provisioning ensures headroom but wastes money |
| Operational Excellence vs. Speed | Comprehensive CI/CD and observability take time to set up but pay off long-term |
| Sustainability vs. Performance | Right-sizing reduces waste but may reduce performance headroom |

**Key principle:** Make tradeoffs explicitly. Document which pillars are prioritized and why (use Architecture Decision Records -- see `specs/documentation/adr`).

## Best Practices
- Use the well-architected framework as a common language between architects, developers, and stakeholders -- not as a compliance checklist.
- Conduct well-architected reviews early and often, not just before launch.
- Prioritize the pillars that matter most for your workload (e.g., a financial system prioritizes Security and Reliability; a data pipeline prioritizes Performance and Cost).
- Leverage the cloud provider's native review tooling to structure the assessment.
- Document all tradeoff decisions in Architecture Decision Records.
- Remember that well-architected is aspirational -- no workload scores perfectly on every pillar. The goal is continuous improvement.
- When working across clouds (multi-cloud or migration), use this cross-cloud comparison to map equivalent concerns and avoid gaps.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/aws-well-architected-framework-6-pillars.md](references/aws-well-architected-framework-6-pillars.md) | AWS Well-Architected Framework (6 Pillars) — 1. Operational Excellence, 2. Security, 3. Reliability, 4. Performance Efficiency, 5. Cost Optimization, 6. Sustainability |
| [references/azure-well-architected-framework-5-pillars.md](references/azure-well-architected-framework-5-pillars.md) | Azure Well-Architected Framework (5 Pillars) — 1. Reliability, 2. Security, 3. Cost Optimization, 4. Operational Excellence, 5. Performance Efficiency |
| [references/gcp-architecture-framework-6-pillars.md](references/gcp-architecture-framework-6-pillars.md) | GCP Architecture Framework (6 Pillars) — 1. System Design, 2. Operational Excellence, 3. Security, Privacy & Compliance, 4. Reliability, 5. Cost Optimization, 6. Performance Optimization |
| [references/details.md](references/details.md) | Well-Architected Review Process |

## References

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)

See references/rules.md for the full rule catalog.
