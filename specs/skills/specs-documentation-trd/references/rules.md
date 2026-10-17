# TRD (Technical Requirements Document) Rules

Best practices and rules for TRD (Technical Requirements Document).

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Reference the PRD | HIGH | [`trd-reference-the-prd.md`](trd-reference-the-prd.md) |
| 2 | Include diagrams | MEDIUM | [`trd-include-diagrams.md`](trd-include-diagrams.md) |
| 3 | Specify API contracts precisely | LOW | [`trd-specify-api-contracts-precisely.md`](trd-specify-api-contracts-precisely.md) |
| 4 | Define performance targets with percentiles | MEDIUM | [`trd-define-performance-targets-with-percentiles.md`](trd-define-performance-targets-with-percentiles.md) |
| 5 | Document the security model explicitly | CRITICAL | [`trd-document-the-security-model-explicitly.md`](trd-document-the-security-model-explicitly.md) |
| 6 | Plan for failure | MEDIUM | [`trd-plan-for-failure.md`](trd-plan-for-failure.md) |
| 7 | Record decisions as ADRs | MEDIUM | [`trd-record-decisions-as-adrs.md`](trd-record-decisions-as-adrs.md) |
| 8 | Keep it current | MEDIUM | [`trd-keep-it-current.md`](trd-keep-it-current.md) |
| 9 | Review with the full engineering team | CRITICAL | [`trd-review-with-the-full-engineering-team.md`](trd-review-with-the-full-engineering-team.md) |
| 10 | Use version control | MEDIUM | [`trd-use-version-control.md`](trd-use-version-control.md) |

---

---
title: "Define performance targets with percentiles"
impact: MEDIUM
impactDescription: "general best practice"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Define performance targets with percentiles

P50, P95, and P99 targets are more useful than averages, which hide tail latency.

---

---
title: "Document the security model explicitly"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Document the security model explicitly

Document the security model explicitly: authentication, authorization, encryption, input validation, and secrets management deserve dedicated sections, not afterthoughts.

---

---
title: "Include diagrams"
impact: MEDIUM
impactDescription: "general best practice"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Include diagrams

Include diagrams: architecture diagrams (C4, sequence, ERD) communicate structure far better than prose alone. Use Mermaid for Markdown-native rendering.

---

---
title: "Keep it current"
impact: MEDIUM
impactDescription: "general best practice"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Keep it current

Keep it current: update the TRD as the system evolves. An outdated TRD is a liability, not an asset.

---

---
title: "Plan for failure"
impact: MEDIUM
impactDescription: "general best practice"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Plan for failure

Plan for failure: include rollback procedures, circuit breaker strategies, fallback behaviors, and disaster recovery in the deployment plan.

---

---
title: "Record decisions as ADRs"
impact: MEDIUM
impactDescription: "general best practice"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Record decisions as ADRs

Record decisions as ADRs: when the TRD makes a significant technical choice (database, framework, architecture style), create a linked ADR to capture the context and trade-offs.

---

---
title: "Reference the PRD"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Reference the PRD

Reference the PRD: every technical decision should trace back to a product requirement. If a TRD section cannot be justified by the PRD, question whether it belongs.

---

---
title: "Review with the full engineering team"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Review with the full engineering team

Review with the full engineering team: the TRD should be reviewed by backend, frontend, infrastructure, security, and QA engineers before implementation begins.

---

---
title: "Specify API contracts precisely"
impact: LOW
impactDescription: "recommended but situational"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Specify API contracts precisely

Specify API contracts precisely: include request/response schemas, error codes, authentication, pagination, and rate limiting. Consider providing an OpenAPI spec as an appendix.

---

---
title: "Use version control"
impact: MEDIUM
impactDescription: "general best practice"
tags: trd, specs, documentation, technical-design-specifications, api-contracts, data-model-documentation
---

## Use version control

Use version control: store the TRD in the repository alongside the code it describes so it evolves with the system.
