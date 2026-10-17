---
name: security-data-protection
description: Use when implementing technical controls for PII, PHI, or payment data. USE FOR: classification tiers, field encryption, masking, tokenization, minimization, retention, privacy-by-design, GDPR/HIPAA technical controls. DO NOT USE FOR: algorithm choice (use security-cryptography), access control (use security-authentication), legal obligations (use legal-privacy-data-protection).
---

# Data Protection

## Overview

Data protection spans both compliance requirements and technical controls. Organizations must protect data not only to meet regulatory obligations but also to maintain customer trust and limit business risk. Privacy by design — the principle of embedding privacy considerations into every stage of system development — is mandatory under GDPR and is increasingly becoming the expectation under other frameworks. Effective data protection requires understanding what data you have, where it lives, how it flows, who can access it, and how long it must be retained.

## Best Practices

- **Maintain a comprehensive data inventory** — you cannot protect data you do not know about; catalog all personal and sensitive data, where it is stored, how it flows, and who has access.
- **Apply privacy by design from the start** — embed data protection into architecture decisions, not as a retrofit; conduct Data Protection Impact Assessments (DPIAs) for new systems that process personal data.
- **Encrypt by default** — enable encryption at rest and in transit for all data stores and communication channels; treat encryption as baseline, not an add-on for sensitive data only.
- **Implement least-privilege access to sensitive data** — restrict access to personal and confidential data based on role and business need; review access permissions regularly and revoke unnecessary grants.
- **Automate compliance processes** — manual compliance processes do not scale; automate DSAR fulfillment, retention enforcement, consent management, and breach detection to reduce human error and response times.
- **Test your data deletion capabilities** — regularly verify that erasure requests result in actual deletion across all systems, including backups, caches, logs, and third-party processors.
- **Monitor for data exfiltration** — deploy Data Loss Prevention (DLP) tools to detect unauthorized data transfers via email, cloud storage, USB, and API calls; alert on anomalous data access patterns.
- **Train all employees on data handling** — security and privacy training should cover data classification, acceptable use, incident reporting, and regulatory obligations; tailor training to roles (developers, support, executives).

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/encryption-requirements.md](references/encryption-requirements.md) | Encryption Requirements — At Rest, In Transit |
| [references/pii-handling.md](references/pii-handling.md) | PII Handling |
| [references/data-retention.md](references/data-retention.md) | Data Retention |
| [references/details.md](references/details.md) | Data Classification; Privacy Regulations; Data Masking and Tokenization |

## References

- [GDPR Official Text](https://gdpr-info.eu)
- [NIST SP 800-122 Guide to Protecting PII](https://csrc.nist.gov/publications/detail/sp/800-122/final)
- [OWASP Data Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)

See references/rules.md for the full rule catalog.
