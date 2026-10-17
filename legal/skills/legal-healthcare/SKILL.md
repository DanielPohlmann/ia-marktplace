---
name: legal-healthcare
description: Use when software handles health data or may be a medical device. USE FOR: HIPAA/HITECH, PHI/ePHI, BAAs, FDA SaMD, EU MDR, HITRUST, telehealth rules, clinical decision support. DO NOT USE FOR: general privacy law (use legal-privacy-data-protection), security controls (use security-secure-sdlc), certifications (use legal-cybersecurity-compliance).
---

# Healthcare Regulation

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

> **Additional Warning**: Healthcare regulatory violations carry **severe penalties including criminal prosecution**. HIPAA criminal penalties can include fines up to $250,000 and imprisonment up to 10 years for offenses committed with intent to sell or use PHI for personal gain. FDA enforcement for unauthorized medical devices can include injunctions, seizures, and criminal prosecution. Do not rely on this skill as a substitute for qualified healthcare regulatory counsel.

## Overview

Healthcare software faces a dual regulatory burden — **health data privacy laws** AND **medical device regulations** if the software provides clinical decision support or diagnosis. The penalty landscape is severe, with regulators empowered to impose criminal sanctions, civil monetary penalties, and injunctive relief. Even unintentional violations can result in multi-million-dollar settlements, mandatory corrective action plans, and years of monitoring. Understanding both dimensions of healthcare regulation is essential before building any software that touches health data or clinical workflows.

## Best Practices

- **Engage healthcare regulatory counsel early and often.** Healthcare is one of the most heavily regulated industries, and ignorance is not a defense for HIPAA violations. The cost of a single breach can dwarf the cost of proactive legal advice.
- **Assume you are a business associate until proven otherwise.** If your software could possibly touch PHI, operate under that assumption and implement HIPAA-compliant safeguards. Getting this wrong exposes you to direct liability.
- **Execute BAAs with all covered entity customers and downstream subcontractors.** A BAA is not optional — it is a legal prerequisite to receiving PHI. Ensure your BAA template has been reviewed by healthcare counsel.
- **Implement encryption for ePHI at rest and in transit.** While HIPAA technically treats encryption as "addressable" rather than "required," failing to encrypt ePHI is the single most common basis for enforcement actions and dramatically increases breach notification obligations.
- **Conduct a thorough SaMD assessment before launch.** Determine early whether your software meets the FDA's definition of a medical device. Launching an uncleared or unapproved medical device carries severe consequences, including product seizure and criminal prosecution.
- **Design for the minimum necessary standard.** Build role-based access controls, audit logging, and data segmentation into your architecture from day one. Retroactively restricting PHI access is far more difficult and expensive.
- **Prepare a breach response plan specific to healthcare.** HIPAA breach notification has specific timelines (60 days to individuals, HHS, and media for breaches affecting 500+), content requirements, and documentation obligations that differ from general data breach laws.
- **Monitor the evolving digital health regulatory landscape.** FDA guidance on AI/ML in SaMD, state telehealth laws, and international health data frameworks are changing rapidly. What is compliant today may not be compliant next year.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/hipaa-deep-dive.md](references/hipaa-deep-dive.md) | HIPAA Deep Dive — Who Is a Covered Entity?, Who Is a Business Associate?, Business Associate Agreement (BAA), PHI vs. De-Identified Data, Minimum Necessary Standard |
| [references/software-as-a-medical-device-samd.md](references/software-as-a-medical-device-samd.md) | Software as a Medical Device (SaMD) — FDA Classification, Clinical Decision Support (CDS) Exclusion |
| [references/details.md](references/details.md) | Health Data Privacy Laws; EU Medical Device Regulation (MDR); HITRUST CSF; Telehealth and Digital Health |

## References

- [U.S. Department of Health & Human Services — HIPAA](https://www.hhs.gov/hipaa/index.html)
- [FDA Digital Health Center of Excellence](https://www.fda.gov/medical-devices/digital-health-center-excellence)
- [EU Medical Devices Regulation (MDR) (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2017/745/oj)

See references/rules.md for the full rule catalog.
