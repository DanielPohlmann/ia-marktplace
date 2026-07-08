# Data Protection Rules

Best practices and rules for Data Protection.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Maintain a comprehensive data inventory | CRITICAL | [`data-protection-maintain-a-comprehensive-data-inventory.md`](data-protection-maintain-a-comprehensive-data-inventory.md) |
| 2 | Apply privacy by design from the start | HIGH | [`data-protection-apply-privacy-by-design-from-the-start.md`](data-protection-apply-privacy-by-design-from-the-start.md) |
| 3 | Encrypt by default | MEDIUM | [`data-protection-encrypt-by-default.md`](data-protection-encrypt-by-default.md) |
| 4 | Implement least-privilege access to sensitive data | MEDIUM | [`data-protection-implement-least-privilege-access-to-sensitive-data.md`](data-protection-implement-least-privilege-access-to-sensitive-data.md) |
| 5 | Automate compliance processes | CRITICAL | [`data-protection-automate-compliance-processes.md`](data-protection-automate-compliance-processes.md) |
| 6 | Test your data deletion capabilities | MEDIUM | [`data-protection-test-your-data-deletion-capabilities.md`](data-protection-test-your-data-deletion-capabilities.md) |
| 7 | Monitor for data exfiltration | HIGH | [`data-protection-monitor-for-data-exfiltration.md`](data-protection-monitor-for-data-exfiltration.md) |
| 8 | Train all employees on data handling | CRITICAL | [`data-protection-train-all-employees-on-data-handling.md`](data-protection-train-all-employees-on-data-handling.md) |

---

---
title: "Apply privacy by design from the start"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Apply privacy by design from the start

Apply privacy by design from the start: embed data protection into architecture decisions, not as a retrofit; conduct Data Protection Impact Assessments (DPIAs) for new systems that process personal data.

---

---
title: "Automate compliance processes"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Automate compliance processes

Automate compliance processes: manual compliance processes do not scale; automate DSAR fulfillment, retention enforcement, consent management, and breach detection to reduce human error and response times.

---

---
title: "Encrypt by default"
impact: MEDIUM
impactDescription: "general best practice"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Encrypt by default

Encrypt by default: enable encryption at rest and in transit for all data stores and communication channels; treat encryption as baseline, not an add-on for sensitive data only.

---

---
title: "Implement least-privilege access to sensitive data"
impact: MEDIUM
impactDescription: "general best practice"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Implement least-privilege access to sensitive data

Implement least-privilege access to sensitive data: restrict access to personal and confidential data based on role and business need; review access permissions regularly and revoke unnecessary grants.

---

---
title: "Maintain a comprehensive data inventory"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Maintain a comprehensive data inventory

Maintain a comprehensive data inventory: you cannot protect data you do not know about; catalog all personal and sensitive data, where it is stored, how it flows, and who has access.

---

---
title: "Monitor for data exfiltration"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Monitor for data exfiltration

Monitor for data exfiltration: deploy Data Loss Prevention (DLP) tools to detect unauthorized data transfers via email, cloud storage, USB, and API calls; alert on anomalous data access patterns.

---

---
title: "Test your data deletion capabilities"
impact: MEDIUM
impactDescription: "general best practice"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Test your data deletion capabilities

Test your data deletion capabilities: regularly verify that erasure requests result in actual deletion across all systems, including backups, caches, logs, and third-party processors.

---

---
title: "Train all employees on data handling"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: data-protection, security, data-encryption, pii-handling, gdpr
---

## Train all employees on data handling

Train all employees on data handling: security and privacy training should cover data classification, acceptable use, incident reporting, and regulatory obligations; tailor training to roles (developers, support, executives).
