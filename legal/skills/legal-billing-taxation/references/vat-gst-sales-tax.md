<!-- Part of the legal-billing-taxation skill. Loaded on demand from SKILL.md. -->

# VAT / GST / Sales Tax

## Global Tax Obligations

| Tax Type | Jurisdictions | Registration Trigger | Rate Range | Key Requirements |
|----------|--------------|---------------------|------------|-----------------|
| **VAT** | EU (27 countries), UK, Norway, Switzerland | Selling to customers in the jurisdiction (no minimum threshold for B2C digital in EU) | 17-27% (varies by country) | VAT registration, periodic returns, reverse charge for B2B |
| **GST** | Australia, New Zealand, Canada, India, Singapore, Malaysia | Revenue thresholds vary by country | 5-18% (varies) | GST registration, BAS/returns, input tax credits |
| **Sales tax** | US (45 states + DC + territories) | Economic nexus thresholds (typically $100K revenue or 200 transactions) | 0-10.25% (state + local) | Nexus analysis, registration, collection, remittance, returns |
| **Digital services tax (DST)** | France, UK, Italy, Spain, Turkey, India, others | Revenue thresholds (typically €750M global + local threshold) | 1.5-7.5% | Separate from VAT; applies to large digital companies |
| **Withholding tax** | Many countries (India, Brazil, etc.) | Cross-border service payments | 10-30% | Deducted at source by customer; may be reduced by tax treaty |

## EU VAT for Digital Services (B2C)

The EU One-Stop Shop (OSS) simplifies VAT for digital services sold to EU consumers:

| Element | Requirement |
|---------|-------------|
| **Registration** | Register in one EU member state via OSS; covers all 27 countries |
| **Rate** | Apply the VAT rate of the customer's country (not seller's) |
| **Evidence of location** | Two pieces of non-contradictory evidence (IP address, billing address, bank country, SIM country) |
| **Returns** | Quarterly OSS return covering all EU sales |
| **B2B reverse charge** | If customer provides valid VAT ID, no VAT charged (customer self-assesses) |
| **Threshold** | No minimum — applies from the first euro of B2C digital sales |

## Tax Automation Tools

| Tool | Capability | Best For |
|------|-----------|----------|
| **Stripe Tax** | Automated tax calculation, collection, and reporting | Companies already using Stripe |
| **Avalara** | Multi-jurisdiction tax compliance (sales tax, VAT, GST) | Enterprise, complex nexus |
| **TaxJar** | US sales tax automation (now part of Stripe) | US-focused SaaS companies |
| **Vertex** | Enterprise tax technology (direct + indirect) | Large enterprise, ERP integration |
| **Paddle / FastSpring** | Merchant of Record (handles all tax obligations for you) | Smaller companies wanting to offload tax entirely |
| **Chargebee** | Subscription billing with tax integration | Subscription-first businesses |
