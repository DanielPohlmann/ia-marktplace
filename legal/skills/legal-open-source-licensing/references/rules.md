# Open-Source Licensing Rules

Best practices and rules for Open-Source Licensing.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always consult qualified legal counsel for GPL compliance. | CRITICAL | [`open-source-licensing-always-consult-qualified-legal-counsel-for-gpl-compliance.md`](open-source-licensing-always-consult-qualified-legal-counsel-for-gpl-compliance.md) |
| 2 | Maintain a software bill of materials (SBOM). | MEDIUM | [`open-source-licensing-maintain-a-software-bill-of-materials-sbom.md`](open-source-licensing-maintain-a-software-bill-of-materials-sbom.md) |
| 3 | Integrate license scanning into your CI/CD pipeline. | CRITICAL | [`open-source-licensing-integrate-license-scanning-into-your-ci-cd-pipeline.md`](open-source-licensing-integrate-license-scanning-into-your-ci-cd-pipeline.md) |
| 4 | Establish an open-source policy for your organization. | HIGH | [`open-source-licensing-establish-an-open-source-policy-for-your-organization.md`](open-source-licensing-establish-an-open-source-policy-for-your-organization.md) |
| 5 | Review license obligations before adopting any new dependency. | MEDIUM | [`open-source-licensing-review-license-obligations-before-adopting-any-new.md`](open-source-licensing-review-license-obligations-before-adopting-any-new.md) |
| 6 | Pay special attention to AGPL in SaaS environments. | HIGH | [`open-source-licensing-pay-special-attention-to-agpl-in-saas-environments.md`](open-source-licensing-pay-special-attention-to-agpl-in-saas-environments.md) |
| 7 | Track license changes across dependency updates. | HIGH | [`open-source-licensing-track-license-changes-across-dependency-updates.md`](open-source-licensing-track-license-changes-across-dependency-updates.md) |
| 8 | Contribute back to the open-source projects you depend on. | MEDIUM | [`open-source-licensing-contribute-back-to-the-open-source-projects-you-depend-on.md`](open-source-licensing-contribute-back-to-the-open-source-projects-you-depend-on.md) |

---

---
title: "Always consult qualified legal counsel for GPL compliance."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Always consult qualified legal counsel for GPL compliance.

The boundary between a "derivative work" and an independent work is legally nuanced. A licensed attorney can evaluate your specific linking, modification, and distribution patterns.

---

---
title: "Contribute back to the open-source projects you depend on."
impact: MEDIUM
impactDescription: "general best practice"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Contribute back to the open-source projects you depend on.

Beyond legal compliance, contributing upstream strengthens the ecosystem and builds goodwill with the communities that power your product.

---

---
title: "Establish an open-source policy for your organization."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Establish an open-source policy for your organization.

Define which licenses are approved, which require legal review, and which are prohibited. Communicate this policy to all developers.

---

---
title: "Integrate license scanning into your CI/CD pipeline."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Integrate license scanning into your CI/CD pipeline.

Automated tools catch license issues before they reach production. Configure allow/deny lists to block incompatible licenses at build time.

---

---
title: "Maintain a software bill of materials (SBOM)."
impact: MEDIUM
impactDescription: "general best practice"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Maintain a software bill of materials (SBOM).

Track every open-source component, its version, and its license. An up-to-date SBOM is the foundation of license compliance.

---

---
title: "Pay special attention to AGPL in SaaS environments."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Pay special attention to AGPL in SaaS environments.

AGPL's network copyleft provision can require you to disclose the source code of your entire application if you use an AGPL component in a networked service.

---

---
title: "Review license obligations before adopting any new dependency."
impact: MEDIUM
impactDescription: "general best practice"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Review license obligations before adopting any new dependency.

A quick check before adding a library is far less costly than discovering an incompatibility after shipping.

---

---
title: "Track license changes across dependency updates."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: open-source-licensing, legal, open-source-licenses, mit, apache
---

## Track license changes across dependency updates.

Libraries can change their license between versions. Ensure your tooling alerts you when a dependency's license changes.
