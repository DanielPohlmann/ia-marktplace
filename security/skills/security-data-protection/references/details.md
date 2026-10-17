<!-- Part of the security-data-protection skill. Loaded on demand from SKILL.md. -->

# Data Protection — details

## Data Classification

Data classification assigns sensitivity levels to information assets, enabling organizations to apply proportionate security controls. Every piece of data should be classified, and the classification should drive technical and procedural safeguards.

| Level | Description | Examples | Controls |
|---|---|---|---|
| **Public** | Information intended for public disclosure; no adverse impact if exposed | Marketing materials, public documentation, open-source code, press releases | No special controls required; integrity protections recommended |
| **Internal** | Information for internal use only; minor impact if disclosed | Internal policies, meeting notes, project plans, org charts | Access restricted to employees; basic access controls; no public sharing |
| **Confidential** | Sensitive business information; significant impact if disclosed | Customer lists, financial reports, contracts, source code, employee records | Encryption at rest and in transit; role-based access control; audit logging; NDA required for third-party access |
| **Restricted** | Highly sensitive data; severe regulatory, legal, or business impact if disclosed | PII, PHI, payment card data (PCI), trade secrets, cryptographic keys | Strong encryption (AES-256); strict need-to-know access; MFA required; full audit trail; data loss prevention (DLP); breach notification obligations |

## Privacy Regulations

The following table compares the major privacy regulations that most organizations must consider. This is a summary — consult legal counsel for jurisdiction-specific compliance requirements.

| Regulation | Jurisdiction | Key Requirements | Penalties |
|---|---|---|---|
| **GDPR** | European Union (and EEA) | Lawful basis for processing (consent, contract, legitimate interest); data subject rights (access, rectification, erasure, portability); Data Protection Officer (DPO) required for large-scale processing; breach notification to supervisory authority within 72 hours; Data Protection Impact Assessments (DPIA) for high-risk processing; privacy by design and by default | Up to 4% of global annual revenue or 20 million EUR, whichever is higher |
| **CCPA/CPRA** | California, USA | Right to know what data is collected; right to delete personal information; right to opt-out of sale/sharing of personal information; right to non-discrimination for exercising rights; data minimization and purpose limitation (CPRA); risk assessments for high-risk processing (CPRA) | Up to $7,500 per intentional violation; $2,500 per unintentional violation; private right of action for data breaches ($100-$750 per consumer per incident) |
| **HIPAA** | United States (healthcare) | Administrative, physical, and technical safeguards for Protected Health Information (PHI); Business Associate Agreements (BAA) required for third-party processors; access logs and audit controls; minimum necessary standard for PHI access; breach notification to individuals and HHS | Up to $1.5 million per year per violation category; criminal penalties for willful neglect (up to $250,000 and imprisonment) |

## Data Masking and Tokenization

| Technique | When to Use | Details |
|---|---|---|
| **Tokenization** | When the original data must be retrievable by authorized systems (e.g., payment processing) | Non-reversible without access to the token vault; tokens can preserve format (e.g., same length as a credit card number); ideal for PCI DSS scope reduction |
| **Format-Preserving Encryption (FPE)** | When encrypted data must retain the same format as the original (e.g., SSN, phone number) | Encrypts data while preserving length and character set; useful for legacy systems that validate field formats; uses FF1 or FF3-1 algorithms |
| **Dynamic Masking** | When data must be masked in real-time based on the requesting user's role or context | Applied at query time; the underlying data is not modified; useful for analytics and support access where full data is not needed |
| **Static Masking** | When creating non-production copies of data (e.g., for testing or development environments) | Applied once to create a masked copy; original data structure is preserved; irreversible; ensures test environments contain no real PII |

Key decisions:
- Use tokenization when you need to reverse the process for legitimate business operations.
- Use static masking for non-production environments — never use real PII in development or testing.
- Use dynamic masking for production access control scenarios where different users need different levels of data visibility.
