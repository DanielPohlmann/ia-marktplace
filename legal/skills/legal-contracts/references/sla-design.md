<!-- Part of the legal-contracts skill. Loaded on demand from SKILL.md. -->

# SLA Design

Service Level Agreements define measurable performance commitments and the remedies available when those commitments are not met.

## Availability Tiers

| Tier | Uptime | Downtime per Year | Typical Use |
|---|---|---|---|
| **99.9%** | Three nines | 8.76 hours | Standard SaaS applications |
| **99.95%** | Three nines five | 4.38 hours | Business-critical applications |
| **99.99%** | Four nines | 52.6 minutes | Mission-critical applications |

## Credit Structures

SLA breaches are typically remedied through one or more of the following mechanisms:

- **Service credits** — A percentage of the monthly fee is credited to the customer's account for each period of downtime exceeding the SLA. Credits commonly range from 10% to 30% of the monthly fee.
- **Refunds** — In more severe cases, the customer may be entitled to a pro-rata refund for the affected period.
- **Termination rights** — Persistent or severe SLA breaches may trigger the customer's right to terminate the agreement without penalty.

## Exclusions

SLA commitments typically exclude downtime caused by:

- **Scheduled maintenance** — Planned maintenance windows that are communicated in advance (commonly with 48-72 hours notice).
- **Customer-caused issues** — Downtime resulting from the customer's own actions, such as misconfiguration, exceeding usage limits, or unauthorized modifications.
- **Force majeure** — Events beyond the provider's reasonable control, as defined in the force majeure clause.

## Measurement Methodology

The SLA should clearly define how availability is measured, including the monitoring tools used, the measurement interval, and whether the calculation excludes scheduled maintenance windows. Ambiguity in measurement methodology is a common source of disputes.
