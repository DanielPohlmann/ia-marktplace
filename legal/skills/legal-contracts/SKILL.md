---
name: legal-contracts
description: Use when reviewing contract terms for a software business. USE FOR: SLA, DPA, MSA, SaaS agreements, licensing, liability caps, indemnification, warranties, jurisdiction, force majeure, escrow. DO NOT USE FOR: OSS license choice (use legal-open-source-licensing), consumer ToS (use legal-consumer-protection), IP disputes (use legal-intellectual-property); drafting final contracts needs counsel.
---

# Contracts

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Software companies operate through a web of contracts with customers, vendors, partners, and employees. Understanding the key contract types and essential clauses helps teams engage legal counsel more effectively and avoid common pitfalls. Whether negotiating a SaaS agreement with a new enterprise customer or reviewing a vendor DPA, familiarity with standard contract structures and jurisdiction-specific requirements is a critical competency for product, engineering, and business teams.

## Best Practices

- **Have all contracts reviewed by qualified legal counsel in the relevant jurisdiction.** Contract law is jurisdiction-specific, and terms that are enforceable in one country may be void in another. Invest in legal review before signing, not after a dispute arises.
- **Use a Master Service Agreement as the foundation.** Structure your contract relationships with an MSA that covers general terms, supplemented by SOWs, order forms, or schedules for specific engagements. This approach reduces negotiation overhead for repeat business.
- **Negotiate mutual liability caps and carve-outs.** Ensure that both parties share risk proportionally. Pay particular attention to uncapped carve-outs and ensure they are limited to areas of genuine catastrophic risk (IP infringement, data breach, willful misconduct).
- **Include clear SLAs with measurable metrics and meaningful remedies.** Vague performance commitments are unenforceable and erode trust. Define uptime targets, measurement methodology, credit structures, and termination triggers with specificity.
- **Address data ownership, portability, and deletion explicitly.** Ensure customer data remains the customer's property, that it can be exported in a standard format on termination, and that the provider is obligated to delete it after a defined retention period.
- **Build in regular contract review cycles.** Laws change, business relationships evolve, and technology advances. Schedule annual reviews of key contracts to ensure they remain current and reflect the actual state of the relationship.
- **Maintain a contract repository with key date tracking.** Use a centralized system to store all executed contracts and track renewal dates, termination notice periods, and other critical deadlines to avoid inadvertent auto-renewals or missed cure periods.
- **Negotiate data processing agreements proactively.** Do not wait for a customer to request a DPA. Prepare a GDPR-compliant DPA template that can be attached to your standard agreements, and keep your sub-processor list current and publicly accessible.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/essential-clauses.md](references/essential-clauses.md) | Essential Clauses — Limitation of Liability, Indemnification, Warranties and Disclaimers, Data Protection, Jurisdiction and Governing Law, Force Majeure, … |
| [references/sla-design.md](references/sla-design.md) | SLA Design — Availability Tiers, Credit Structures, Exclusions, Measurement Methodology |
| [references/details.md](references/details.md) | Key Contract Types for Software Companies; Jurisdiction-Specific Considerations |

## References

- [Uniform Commercial Code (UCC) — Cornell Law Institute](https://www.law.cornell.edu/ucc)
- [GDPR Data Processing Agreement Requirements (Article 28)](https://gdpr-info.eu/art-28-gdpr/)

See references/rules.md for the full rule catalog.
