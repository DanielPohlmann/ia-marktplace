<!-- Part of the legal-healthcare skill. Loaded on demand from SKILL.md. -->

# Healthcare Regulation — details

## Health Data Privacy Laws

| Law | Jurisdiction | Scope | Protected Data | Penalties |
|---|---|---|---|---|
| **HIPAA Privacy Rule** | US | Covered entities + business associates | PHI (Protected Health Information) | Up to $1.5M/year per violation category |
| **HIPAA Security Rule** | US | Covered entities + business associates handling ePHI | ePHI (electronic Protected Health Information) | Up to $1.5M/year per violation category |
| **HITECH Act** | US | Expands HIPAA to business associates + breach notification | PHI | Increased penalties + state Attorney General enforcement |
| **UK GDPR + NHS Code of Practice** | UK | Health data processors | Special category data | Up to £17.5M or 4% global revenue |
| **DSGVO / German Federal Data Protection Act** | Germany | Extra protections for health data | Health data | GDPR penalties + sector-specific rules |
| **PIPEDA Health Data** | Canada | Health information custodians in some provinces | Personal health information | Provincial enforcement |
| **LGPD** | Brazil | Sensitive data category for health | Health data | 2% of revenue up to R$50M |

## EU Medical Device Regulation (MDR)

The **EU MDR (Regulation 2017/745)** significantly expanded the scope of medical device regulation for software in the European Union.

**Key aspects for software:**

- **Rule 11 classification** — Software intended to provide information used to make decisions with diagnosis or therapeutic purposes is classified based on the seriousness of the condition and the state of the patient. Software can be classified anywhere from Class I to Class III depending on its intended purpose.
- **CE marking** — Required before placing a medical device on the EU market. Involves conformity assessment, technical documentation, and (for higher-risk classes) notified body review.
- **Notified body assessment** — For Class IIa and above, an independent notified body must assess the device. There is currently a significant shortage of notified bodies, causing delays.
- **Post-market surveillance** — Ongoing obligations to monitor device performance, collect user feedback, report incidents, and update risk assessments throughout the device lifecycle.
- **EUDAMED registration** — The European Database on Medical Devices requires registration of devices, economic operators, certificates, and clinical investigations. Rollout has been phased.

## HITRUST CSF

**HITRUST CSF (Common Security Framework)** is a comprehensive security framework widely adopted in the healthcare industry as a way to demonstrate compliance with HIPAA and other regulatory requirements.

**What it is:** A certifiable framework that harmonizes requirements from HIPAA, NIST, ISO 27001, PCI DSS, and other standards into a single set of controls tailored for organizations handling health information.

**Relationship to HIPAA:** HITRUST is not required by law, but it has become a de facto standard for demonstrating HIPAA compliance. Many healthcare organizations require their vendors to have HITRUST certification.

**Certification levels:**

| Level | Name | Scope | Effort |
|---|---|---|---|
| **e1** | Essentials, 1-Year | Basic cybersecurity hygiene, 44 requirements | Lower effort, suitable for lower-risk organizations |
| **i1** | Implemented, 1-Year | Good security practices, 182 requirements | Moderate effort, demonstrates established security program |
| **r2** | Risk-Based, 2-Year | Comprehensive risk-based assessment, 200+ requirements | Highest effort, gold standard for healthcare vendors |

## Telehealth and Digital Health

Telehealth and digital health regulation adds additional layers of complexity beyond data privacy and device regulation.

**United States:**
- **State-by-state licensure** — Healthcare providers must generally be licensed in the state where the patient is located at the time of the telehealth encounter. Interstate compacts (such as the Interstate Medical Licensure Compact) simplify this for physicians, but coverage is not universal.
- **Prescribing restrictions** — Rules about prescribing medications via telehealth vary by state and drug schedule. The DEA's temporary COVID-era flexibilities for controlled substance prescribing via telehealth have been extended but remain in flux.
- **Reimbursement parity** — Many states have telehealth parity laws requiring insurers to reimburse telehealth services at the same rate as in-person services, but details vary.

**European Union:**
- Cross-border telehealth in the EU is governed by the **Cross-Border Healthcare Directive**, but practical implementation varies significantly by member state. Healthcare provider licensing remains a national competency.

**FDA and health apps:**
- The FDA distinguishes between health apps that are regulated as medical devices and those that are not. General wellness apps (exercise tracking, diet logging) that do not claim to diagnose or treat conditions are generally not regulated. Apps that claim to diagnose, treat, or prevent disease may be regulated as medical devices.
