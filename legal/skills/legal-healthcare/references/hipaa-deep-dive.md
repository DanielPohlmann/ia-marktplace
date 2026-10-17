<!-- Part of the legal-healthcare skill. Loaded on demand from SKILL.md. -->

# HIPAA Deep Dive

## Who Is a Covered Entity?

HIPAA applies directly to three categories of **covered entities**:

1. **Health plans** — Health insurance companies, HMOs, employer-sponsored health plans, government health programs (Medicare, Medicaid).
2. **Healthcare clearinghouses** — Entities that process nonstandard health information into standard formats.
3. **Healthcare providers** — Any provider who transmits health information electronically in connection with a HIPAA-covered transaction (claims, eligibility inquiries, referral authorizations, etc.).

## Who Is a Business Associate?

A **business associate** is any person or organization that performs functions or activities on behalf of (or provides services to) a covered entity that involve access to PHI. This includes:

- Cloud service providers hosting ePHI (yes, including IaaS, PaaS, and SaaS providers)
- Software vendors whose products store, process, or transmit PHI
- IT contractors with access to systems containing PHI
- Data analytics firms processing PHI
- Billing and claims processing companies
- Shredding and document destruction companies

**Key point for software developers:** If your SaaS product is used by a healthcare organization and your systems can access PHI — even if you never intend to look at it — you are likely a business associate.

## Business Associate Agreement (BAA)

Before any PHI is shared, a **Business Associate Agreement** must be in place. A BAA is a legally binding contract that:

- Establishes the permitted uses and disclosures of PHI
- Requires the business associate to implement appropriate safeguards
- Requires reporting of breaches and security incidents
- Gives the covered entity the right to terminate the agreement if the business associate violates HIPAA
- Requires the business associate to ensure any subcontractors also agree to the same restrictions

## PHI vs. De-Identified Data

**Protected Health Information (PHI)** is individually identifiable health information that is created or received by a covered entity. Data can be **de-identified** through two methods:

- **Safe Harbor Method** — Remove 18 specified identifiers (names, geographic data smaller than state, dates except year, phone numbers, email addresses, SSNs, medical record numbers, etc.) and have no actual knowledge that the remaining information could identify an individual.
- **Expert Determination Method** — A qualified statistical expert determines that the risk of identifying an individual is very small and documents the methods and results.

De-identified data is not subject to HIPAA. However, re-identification risk must be carefully managed, and some state laws may impose additional restrictions.

## Minimum Necessary Standard

HIPAA requires that covered entities and business associates limit PHI access, use, and disclosure to the **minimum necessary** to accomplish the intended purpose. This means:

- Role-based access controls that restrict PHI access to what each role requires
- Policies defining who needs access to what categories of PHI
- Technical controls that enforce the minimum necessary standard programmatically
