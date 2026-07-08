# Export Controls Rules

Best practices and rules for Export Controls.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Always consult qualified trade compliance counsel. | CRITICAL | [`export-controls-always-consult-qualified-trade-compliance-counsel.md`](export-controls-always-consult-qualified-trade-compliance-counsel.md) |
| 2 | Classify your products early in the development cycle. | MEDIUM | [`export-controls-classify-your-products-early-in-the-development-cycle.md`](export-controls-classify-your-products-early-in-the-development-cycle.md) |
| 3 | Automate restricted party screening. | MEDIUM | [`export-controls-automate-restricted-party-screening.md`](export-controls-automate-restricted-party-screening.md) |
| 4 | Implement geo-blocking for embargoed jurisdictions. | MEDIUM | [`export-controls-implement-geo-blocking-for-embargoed-jurisdictions.md`](export-controls-implement-geo-blocking-for-embargoed-jurisdictions.md) |
| 5 | Track open-source encryption notifications. | MEDIUM | [`export-controls-track-open-source-encryption-notifications.md`](export-controls-track-open-source-encryption-notifications.md) |
| 6 | Monitor regulatory changes continuously. | MEDIUM | [`export-controls-monitor-regulatory-changes-continuously.md`](export-controls-monitor-regulatory-changes-continuously.md) |
| 7 | Include export compliance terms in contracts. | HIGH | [`export-controls-include-export-compliance-terms-in-contracts.md`](export-controls-include-export-compliance-terms-in-contracts.md) |
| 8 | Treat deemed exports seriously. | HIGH | [`export-controls-treat-deemed-exports-seriously.md`](export-controls-treat-deemed-exports-seriously.md) |

---

---
title: "Always consult qualified trade compliance counsel."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: export-controls, legal, ear, itar
---

## Always consult qualified trade compliance counsel.

Export control violations carry severe criminal penalties, including imprisonment up to 20 years and fines up to $1 million per violation under ITAR, and up to $300,000 per violation or twice the transaction value under EAR. Do not attempt to self-assess complex export control questions.

---

---
title: "Automate restricted party screening."
impact: MEDIUM
impactDescription: "general best practice"
tags: export-controls, legal, ear, itar
---

## Automate restricted party screening.

Manual screening is error-prone. Use commercial screening tools (e.g., Visual Compliance, Descartes, SAP GTS) to screen customers and end-users against all applicable lists in real time.

---

---
title: "Classify your products early in the development cycle."
impact: MEDIUM
impactDescription: "general best practice"
tags: export-controls, legal, ear, itar
---

## Classify your products early in the development cycle.

Determine the ECCN or other applicable classification before your product ships — not after a customer in a restricted jurisdiction places an order.

---

---
title: "Implement geo-blocking for embargoed jurisdictions."
impact: MEDIUM
impactDescription: "general best practice"
tags: export-controls, legal, ear, itar
---

## Implement geo-blocking for embargoed jurisdictions.

If you distribute software via download, implement technical controls to block access from comprehensively embargoed countries and IP addresses associated with those jurisdictions.

---

---
title: "Include export compliance terms in contracts."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: export-controls, legal, ear, itar
---

## Include export compliance terms in contracts.

Require customers and distributors to certify that they will comply with applicable export control laws and will not divert products to prohibited end-users or destinations.

---

---
title: "Monitor regulatory changes continuously."
impact: MEDIUM
impactDescription: "general best practice"
tags: export-controls, legal, ear, itar
---

## Monitor regulatory changes continuously.

Sanctions lists, embargoed jurisdictions, and export control classifications change frequently. Subscribe to BIS and OFAC alerts and review updates promptly.

---

---
title: "Track open-source encryption notifications."
impact: MEDIUM
impactDescription: "general best practice"
tags: export-controls, legal, ear, itar
---

## Track open-source encryption notifications.

If you publish open-source software with encryption, maintain records of your BIS/NSA email notifications and annual self-classification reports.

---

---
title: "Treat deemed exports seriously."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: export-controls, legal, ear, itar
---

## Treat deemed exports seriously.

Implement technology control plans in offices with foreign national employees and ensure that access to controlled technology is limited based on export classification and employee nationality.
