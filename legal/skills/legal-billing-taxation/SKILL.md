---
name: legal-billing-taxation
description: Use when identifying tax, invoicing, or revenue-recognition obligations for software sold globally, including Brazil. USE FOR: VAT/GST/sales tax, nexus, NF-e/NFS-e, ISS, Simples Nacional, service classification codes, ASC 606/IFRS 15, prepaid credits, withholding, digital services tax. DO NOT USE FOR: payments and PCI DSS (use legal-financial-regulation), refunds (use legal-consumer-protection), pricing terms (use legal-contracts).
---

# Billing & Taxation

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice** and is **not tax advice**. Tax laws are complex, vary by jurisdiction, and change frequently. Always consult a qualified tax advisor and legal counsel licensed in the relevant jurisdiction before making tax or billing decisions for your organization.

## Overview

Every software company that charges customers faces a web of tax and billing obligations that vary by what you sell, how you sell it, who you sell it to, and where both parties are located. Misclassifying your service type, failing to collect applicable taxes, or improperly recognizing revenue can result in back-tax liabilities, penalties, and audit exposure. Additionally, billing models that use "credits," "tokens," or "units" instead of currency can inadvertently trigger money transmission, stored-value, or consumer protection regulations.

## Transfer Pricing

If your company has entities in multiple countries, inter-company transactions must be priced at arm's length (as if between unrelated parties). This affects:

- Licensing IP from a parent to a subsidiary
- Charging for shared services (engineering, support)
- Allocating costs of cloud infrastructure
- Cost-sharing arrangements for R&D

> **Transfer pricing audits** are a top priority for tax authorities globally. Documentation (typically a transfer pricing study) is mandatory in most jurisdictions above certain revenue thresholds.

## Best Practices

- **Always consult a qualified tax advisor** for each jurisdiction in which you sell — tax classification of software varies dramatically.
- **Unbundle invoices** by service type — separate software, professional services, training, and support to apply correct tax treatment to each.
- **Automate tax calculation and collection** using tools like Stripe Tax, Avalara, or a Merchant of Record — manual processes do not scale.
- **Classify credits carefully** — design prepaid/credit systems to minimize money transmission, stored-value, and e-money regulatory risk by making credits non-transferable, non-refundable, and denominated in abstract units rather than currency.
- **Disclose credit terms clearly** at the point of purchase — expiration dates, refund policies, and balance access are required by consumer protection laws in most jurisdictions.
- **Recognize revenue per ASC 606 / IFRS 15** — do not recognize credit purchases as revenue; recognize when credits are consumed or expire (breakage).
- **Monitor nexus and registration thresholds** — US economic nexus rules, EU VAT OSS, and expanding DST regimes create new obligations as your business grows.
- **Prepare for e-invoicing mandates** — Italy, India, Brazil, and France already require structured electronic invoices; the EU-wide ViDA mandate is coming.
- **Address withholding tax in contracts** — specify whether payments are net or gross of withholding and include tax treaty cooperation clauses.
- **Keep billing codes consistent** between your invoicing system, tax engine, and general ledger — mismatches create audit exposure.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/service-type-classification.md](references/service-type-classification.md) | Service Type Classification — Classification Categories, US State-by-State Complexity, Billing Codes and Tax Codes, Bundled vs Unbundled Invoicing |
| [references/vat-gst-sales-tax.md](references/vat-gst-sales-tax.md) | VAT / GST / Sales Tax — Global Tax Obligations, EU VAT for Digital Services (B2C), Tax Automation Tools |
| [references/invoicing-requirements.md](references/invoicing-requirements.md) | Invoicing Requirements — Mandatory Invoice Elements (Most Jurisdictions), E-Invoicing Mandates |
| [references/revenue-recognition-asc-606-ifrs-15.md](references/revenue-recognition-asc-606-ifrs-15.md) | Revenue Recognition (ASC 606 / IFRS 15) — Five-Step Model, Common Software Revenue Scenarios |
| [references/cloud-credits-and-prepaid-models.md](references/cloud-credits-and-prepaid-models.md) | Cloud Credits and Prepaid Models — Common Credit Models, Legal and Regulatory Risks, Structuring Credits to Minimize Regulatory Risk |
| [references/details.md](references/details.md) | Withholding Tax on Cross-Border Payments |

## References

- [OECD International VAT/GST Guidelines](https://www.oecd.org/tax/consumption/international-vat-gst-guidelines.htm)
- [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/)
- [FASB ASC 606 Revenue Recognition](https://asc.fasb.org/606)

See references/rules.md for the full rule catalog.
