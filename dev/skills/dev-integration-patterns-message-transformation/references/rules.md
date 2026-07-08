# Message Transformation Rules

Best practices and rules for Message Transformation.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Apply Content Enricher early in the pipeline so downstream... | MEDIUM | [`message-transformation-apply-content-enricher-early-in-the-pipeline-so-downstream.md`](message-transformation-apply-content-enricher-early-in-the-pipeline-so-downstream.md) |
| 2 | Apply Content Filter at system boundaries -- especially... | MEDIUM | [`message-transformation-apply-content-filter-at-system-boundaries-especially.md`](message-transformation-apply-content-filter-at-system-boundaries-especially.md) |
| 3 | Use Claim Check proactively; do not wait until you hit... | CRITICAL | [`message-transformation-use-claim-check-proactively-do-not-wait-until-you-hit.md`](message-transformation-use-claim-check-proactively-do-not-wait-until-you-hit.md) |
| 4 | Define the Canonical Data Model collaboratively across... | MEDIUM | [`message-transformation-define-the-canonical-data-model-collaboratively-across.md`](message-transformation-define-the-canonical-data-model-collaboratively-across.md) |
| 5 | Version your Canonical Data Model and treat it as a... | MEDIUM | [`message-transformation-version-your-canonical-data-model-and-treat-it-as-a.md`](message-transformation-version-your-canonical-data-model-and-treat-it-as-a.md) |
| 6 | Keep transformations stateless and side-effect free -- they... | MEDIUM | [`message-transformation-keep-transformations-stateless-and-side-effect-free-they.md`](message-transformation-keep-transformations-stateless-and-side-effect-free-they.md) |
| 7 | Log transformation inputs and outputs (redacting sensitive... | MEDIUM | [`message-transformation-log-transformation-inputs-and-outputs-redacting-sensitive.md`](message-transformation-log-transformation-inputs-and-outputs-redacting-sensitive.md) |
| 8 | Prefer Normalizer at system entry points so the rest of the... | LOW | [`message-transformation-prefer-normalizer-at-system-entry-points-so-the-rest-of-the.md`](message-transformation-prefer-normalizer-at-system-entry-points-so-the-rest-of-the.md) |

---

---
title: "Apply Content Enricher early in the pipeline so downstream..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Apply Content Enricher early in the pipeline so downstream...

Apply Content Enricher early in the pipeline so downstream consumers have all the data they need.

---

---
title: "Apply Content Filter at system boundaries -- especially..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Apply Content Filter at system boundaries -- especially...

Apply Content Filter at system boundaries -- especially before sending data to external partners or analytics.

---

---
title: "Define the Canonical Data Model collaboratively across..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Define the Canonical Data Model collaboratively across...

Define the Canonical Data Model collaboratively across teams; a model imposed by one team rarely succeeds.

---

---
title: "Keep transformations stateless and side-effect free -- they..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Keep transformations stateless and side-effect free -- they...

Keep transformations stateless and side-effect free -- they should be pure functions on message data.

---

---
title: "Log transformation inputs and outputs (redacting sensitive..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Log transformation inputs and outputs (redacting sensitive...

Log transformation inputs and outputs (redacting sensitive fields) for debugging data mapping issues.

---

---
title: "Prefer Normalizer at system entry points so the rest of the..."
impact: LOW
impactDescription: "recommended but situational"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Prefer Normalizer at system entry points so the rest of the...

Prefer Normalizer at system entry points so the rest of the pipeline works with a single format.

---

---
title: "Use Claim Check proactively; do not wait until you hit..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Use Claim Check proactively; do not wait until you hit...

Use Claim Check proactively; do not wait until you hit channel size limits in production.

---

---
title: "Version your Canonical Data Model and treat it as a..."
impact: MEDIUM
impactDescription: "general best practice"
tags: message-transformation, dev, integration-patterns, envelope-wrapping, content-enrichment
---

## Version your Canonical Data Model and treat it as a...

Version your Canonical Data Model and treat it as a contract with the same rigour as an API contract.
