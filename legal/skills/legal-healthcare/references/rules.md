# Healthcare Regulation Rules

Best practices and rules for Healthcare Regulation.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Engage healthcare regulatory counsel early and often. | MEDIUM | [`healthcare-engage-healthcare-regulatory-counsel-early-and-often.md`](healthcare-engage-healthcare-regulatory-counsel-early-and-often.md) |
| 2 | Assume you are a business associate until proven otherwise. | MEDIUM | [`healthcare-assume-you-are-a-business-associate-until-proven-otherwise.md`](healthcare-assume-you-are-a-business-associate-until-proven-otherwise.md) |
| 3 | Execute BAAs with all covered entity customers and downstream subcontractors. | HIGH | [`healthcare-execute-baas-with-all-covered-entity-customers-and.md`](healthcare-execute-baas-with-all-covered-entity-customers-and.md) |
| 4 | Implement encryption for ePHI at rest and in transit. | HIGH | [`healthcare-implement-encryption-for-ephi-at-rest-and-in-transit.md`](healthcare-implement-encryption-for-ephi-at-rest-and-in-transit.md) |
| 5 | Conduct a thorough SaMD assessment before launch. | MEDIUM | [`healthcare-conduct-a-thorough-samd-assessment-before-launch.md`](healthcare-conduct-a-thorough-samd-assessment-before-launch.md) |
| 6 | Design for the minimum necessary standard. | MEDIUM | [`healthcare-design-for-the-minimum-necessary-standard.md`](healthcare-design-for-the-minimum-necessary-standard.md) |
| 7 | Prepare a breach response plan specific to healthcare. | HIGH | [`healthcare-prepare-a-breach-response-plan-specific-to-healthcare.md`](healthcare-prepare-a-breach-response-plan-specific-to-healthcare.md) |
| 8 | Monitor the evolving digital health regulatory landscape. | MEDIUM | [`healthcare-monitor-the-evolving-digital-health-regulatory-landscape.md`](healthcare-monitor-the-evolving-digital-health-regulatory-landscape.md) |

---

---
title: "Assume you are a business associate until proven otherwise."
impact: MEDIUM
impactDescription: "general best practice"
tags: healthcare, legal, hipaa, hitech, phi
---

## Assume you are a business associate until proven otherwise.

If your software could possibly touch PHI, operate under that assumption and implement HIPAA-compliant safeguards. Getting this wrong exposes you to direct liability.

---

---
title: "Conduct a thorough SaMD assessment before launch."
impact: MEDIUM
impactDescription: "general best practice"
tags: healthcare, legal, hipaa, hitech, phi
---

## Conduct a thorough SaMD assessment before launch.

Determine early whether your software meets the FDA's definition of a medical device. Launching an uncleared or unapproved medical device carries severe consequences, including product seizure and criminal prosecution.

---

---
title: "Design for the minimum necessary standard."
impact: MEDIUM
impactDescription: "general best practice"
tags: healthcare, legal, hipaa, hitech, phi
---

## Design for the minimum necessary standard.

Build role-based access controls, audit logging, and data segmentation into your architecture from day one. Retroactively restricting PHI access is far more difficult and expensive.

---

---
title: "Engage healthcare regulatory counsel early and often."
impact: MEDIUM
impactDescription: "general best practice"
tags: healthcare, legal, hipaa, hitech, phi
---

## Engage healthcare regulatory counsel early and often.

Healthcare is one of the most heavily regulated industries, and ignorance is not a defense for HIPAA violations. The cost of a single breach can dwarf the cost of proactive legal advice.

---

---
title: "Execute BAAs with all covered entity customers and downstream subcontractors."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: healthcare, legal, hipaa, hitech, phi
---

## Execute BAAs with all covered entity customers and downstream subcontractors.

A BAA is not optional — it is a legal prerequisite to receiving PHI. Ensure your BAA template has been reviewed by healthcare counsel.

---

---
title: "Implement encryption for ePHI at rest and in transit."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: healthcare, legal, hipaa, hitech, phi
---

## Implement encryption for ePHI at rest and in transit.

While HIPAA technically treats encryption as "addressable" rather than "required," failing to encrypt ePHI is the single most common basis for enforcement actions and dramatically increases breach notification obligations.

---

---
title: "Monitor the evolving digital health regulatory landscape."
impact: MEDIUM
impactDescription: "general best practice"
tags: healthcare, legal, hipaa, hitech, phi
---

## Monitor the evolving digital health regulatory landscape.

FDA guidance on AI/ML in SaMD, state telehealth laws, and international health data frameworks are changing rapidly. What is compliant today may not be compliant next year.

---

---
title: "Prepare a breach response plan specific to healthcare."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: healthcare, legal, hipaa, hitech, phi
---

## Prepare a breach response plan specific to healthcare.

HIPAA breach notification has specific timelines (60 days to individuals, HHS, and media for breaches affecting 500+), content requirements, and documentation obligations that differ from general data breach laws.
