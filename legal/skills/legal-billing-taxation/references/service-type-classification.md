<!-- Part of the legal-billing-taxation skill. Loaded on demand from SKILL.md. -->

# Service Type Classification

How your product is classified determines which tax rates, billing codes, and regulations apply. The same software can be classified differently depending on the jurisdiction and delivery method.

## Classification Categories

| Classification | Description | Tax Treatment (General) | Examples |
|---------------|-------------|------------------------|----------|
| **SaaS** | Software accessed via internet, no download | Taxable in many US states + most countries (digital service) | Salesforce, Slack, GitHub |
| **Licensed software (download)** | Software delivered electronically for local installation | Taxable as tangible personal property in some states; digital good in others | Adobe Creative Suite (perpetual), desktop apps |
| **Professional services** | Consulting, implementation, custom development | Often exempt or lower rate than software | Integration services, custom dev, training |
| **Information services** | Data feeds, research, analytics | Varies widely — exempt in some states, taxable in others | Bloomberg terminal, market data feeds |
| **Infrastructure / IaaS** | Compute, storage, networking resources | Emerging rules — taxable as digital service in many jurisdictions | AWS EC2, Azure VMs, GCP Compute |
| **Platform / PaaS** | Development platforms and tools | Similar to IaaS — taxable as digital service | Heroku, Vercel, Azure App Service |
| **Digital goods** | E-books, media, downloadable content | Taxable in most jurisdictions | App Store purchases, digital media |
| **Telecommunications** | Voice, messaging, video conferencing | Heavily taxed with industry-specific surcharges | Twilio, Zoom (voice/telephony components) |

## US State-by-State Complexity

US sales tax on software varies dramatically by state:

| State Approach | Example States | SaaS Taxable? | Custom Software? |
|---------------|---------------|---------------|-----------------|
| **SaaS is taxable** | TX, NY, PA, CT, OH, WA | Yes | Often yes |
| **SaaS is not taxable** | CA, CO, FL, IL, MO, VA | No (currently) | Varies |
| **SaaS taxability depends on factors** | GA, IN, UT | Depends on customization, access method | Varies |

> **This landscape changes annually.** States are increasingly moving to tax SaaS. Always verify current rules with a tax advisor.

## Billing Codes and Tax Codes

Proper billing line items are critical for tax compliance and audit defense. Each line item should map to a tax classification:

| Line Item Category | Common Tax Code/Category | Why It Matters |
|-------------------|------------------------|----------------|
| **Software subscription** | SaaS / Electronic services / Digital service | Determines VAT/sales tax rate |
| **Implementation / setup** | Professional services / Consulting | Often a different (or zero) tax rate |
| **Support / maintenance** | Maintenance agreement / Service | May be taxed differently than the subscription |
| **Training** | Educational services | Exempt in many jurisdictions |
| **Data storage** | IaaS / Cloud computing | Emerging tax classification |
| **API usage / compute** | IaaS or Telecommunications | May trigger telecom-specific taxes |
| **Hardware** | Tangible personal property | Standard sales tax applies |
| **Managed services** | Professional services or SaaS | Classification depends on what predominates |

## Bundled vs Unbundled Invoicing

| Approach | Description | Tax Impact |
|----------|-------------|-----------|
| **Bundled** | Single line item "Platform Fee: $10,000" | Taxed at the rate of the predominant component (or the highest applicable rate in some jurisdictions) |
| **Unbundled** | Separate lines: "Subscription: $7,000" + "Implementation: $2,000" + "Training: $1,000" | Each line taxed at its own rate — can reduce total tax |

> **Best practice**: Unbundle invoices wherever possible. Bundling can cause the entire invoice to be taxed at the highest applicable rate. Work with your tax advisor to determine the correct unbundling for each jurisdiction.
