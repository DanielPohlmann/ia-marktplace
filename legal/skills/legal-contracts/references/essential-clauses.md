<!-- Part of the legal-contracts skill. Loaded on demand from SKILL.md. -->

# Essential Clauses

## Limitation of Liability

Limitation of liability clauses are among the most heavily negotiated provisions in software contracts. They define the maximum financial exposure each party faces.

- **Cap types** — Liability is typically capped at the contract value, fees paid in the prior 12 months, or a specified insurance amount. The cap amount should reflect the risk profile of the engagement.
- **Carve-outs** — Certain obligations are commonly excluded from the liability cap, including IP infringement, data breach, willful misconduct, and confidentiality breach. These carve-outs may have their own higher cap or be uncapped.
- **Mutual vs one-sided** — Best practice is to negotiate mutual liability caps. One-sided caps that disproportionately favor one party may be unenforceable in some jurisdictions and are often a sign of an imbalanced negotiation.

## Indemnification

Indemnification provisions allocate responsibility for third-party claims between the contracting parties.

- **IP infringement** — The provider typically indemnifies the customer against claims that the software infringes third-party intellectual property rights.
- **Data breach** — The party responsible for the breach (or whose negligence caused it) typically bears the indemnification obligation for resulting third-party claims.
- **Third-party claims** — Broader indemnification may cover claims arising from a party's breach of representations, warranties, or applicable law.
- **Defense obligation vs reimbursement** — A defense obligation requires the indemnifying party to actively defend the claim (hire counsel, manage litigation). Reimbursement-only obligations are less protective, requiring the indemnified party to manage their own defense and seek repayment afterward.

## Warranties and Disclaimers

Warranties define the promises each party makes about their performance, products, or services.

- **What is typically warranted** — Conformance to published specifications or documentation, non-infringement of third-party IP, authority to enter the agreement, and compliance with applicable laws.
- **Statutory warranties that cannot be disclaimed** — Many jurisdictions impose mandatory warranties that cannot be disclaimed by contract. For example, the UK's Unfair Contract Terms Act, Australia's Australian Consumer Law (statutory guarantees), and Germany's BGB provisions on defect liability all limit the ability to exclude warranties.
- **"As-is" disclaimers** — In jurisdictions that permit it, providers often disclaim all warranties not expressly stated, including implied warranties of merchantability and fitness for a particular purpose.

## Data Protection

Data processing agreements are mandatory under GDPR and increasingly required under other privacy laws.

- **GDPR Article 28 requirements** — DPAs must specify the subject matter and duration of processing, the nature and purpose of processing, the types of personal data, categories of data subjects, and the controller's obligations and rights.
- **Sub-processor management** — The processor must obtain prior authorization (general or specific) before engaging sub-processors, maintain a list of sub-processors, and ensure sub-processors are bound by equivalent data protection obligations.
- **Data return and deletion on termination** — The DPA must specify the processor's obligations to return or delete all personal data at the end of the processing relationship, and certify deletion upon request.

## Jurisdiction and Governing Law

Choice of law and forum clauses determine which jurisdiction's laws apply and where disputes will be resolved.

- **Choice of law vs choice of forum** — These are distinct concepts. Choice of law determines which legal rules apply to interpret the contract. Choice of forum determines where disputes will be litigated or arbitrated. They need not be the same jurisdiction.
- **Mandatory consumer protection overrides** — In many jurisdictions, consumer protection laws override contractual choice of law or forum clauses when the other party is a consumer. B2B contracts have more flexibility.
- **Arbitration vs litigation** — Arbitration offers privacy, speed, and the ability to select specialized arbitrators. Litigation provides broader discovery, appeal rights, and public precedent. The right choice depends on the nature of the relationship and the value at stake.

## Force Majeure

Force majeure clauses excuse performance when extraordinary events beyond a party's control prevent fulfillment of contractual obligations.

- **Post-COVID expansion** — Many organizations have expanded their force majeure clauses following the COVID-19 pandemic to explicitly cover pandemics, epidemics, and government-mandated shutdowns.
- **What constitutes force majeure in software** — Events commonly covered include infrastructure failure (cloud provider outages), pandemic, government action (sanctions, embargoes), natural disasters, war, terrorism, and widespread cyberattacks.
- **Notice requirements** — Most force majeure clauses require the affected party to provide prompt written notice, describe the event and its expected duration, and demonstrate efforts to mitigate the impact.

## IP Ownership

Clarity on intellectual property ownership is essential, especially when custom development or data is involved.

- **Who owns customizations** — Contracts should clearly state whether customizations, configurations, or integrations developed for a customer are owned by the provider, the customer, or jointly.
- **Who owns data** — Customer data should remain the customer's property. The provider should have only a limited license to use customer data for the purpose of delivering the service.
- **Background IP vs foreground IP** — Background IP is intellectual property that existed before the contract. Foreground IP is created during the engagement. Contracts should clearly delineate ownership and licensing rights for both.

## Termination

Termination provisions define how and when each party can exit the contract.

- **For cause vs for convenience** — Termination for cause allows a party to exit when the other party materially breaches the agreement. Termination for convenience allows exit without cause, typically with a notice period.
- **Cure periods** — A cure period gives the breaching party a specified number of days (commonly 30) to remedy the breach before the other party can terminate. Critical breaches (data breach, insolvency) may have shorter or no cure periods.
- **Wind-down obligations** — The contract should specify each party's obligations during the wind-down period, including continued service delivery, transition assistance, and final invoicing.
- **Data portability on exit** — Customers should negotiate the right to export their data in a standard, machine-readable format upon termination, along with a specified period during which the provider will make the data available before deletion.
