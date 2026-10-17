<!-- Part of the legal-billing-taxation skill. Loaded on demand from SKILL.md. -->

# Cloud Credits and Prepaid Models

Cloud credits, tokens, units, and prepaid balances are common in compute, hosting, and API billing. These models create several legal and regulatory risks that traditional subscription billing does not.

## Common Credit Models

| Model | How It Works | Examples |
|-------|-------------|----------|
| **Prepaid usage credits** | Customer buys credits; credits consumed by resource usage | AWS credits, Azure credits, GCP credits, Vercel credits |
| **Token-based API billing** | Customer buys tokens; each API call consumes tokens | OpenAI tokens, Anthropic tokens |
| **Unit-based billing** | Customer buys units (abstraction over compute) | Salesforce compute credits, Snowflake credits |
| **Platform credits (non-monetary)** | Credits earned through promotions, loyalty, or incentives | Startup program credits, promotional credits |
| **Gift cards / vouchers** | Redeemable for services at face value | Digital gift cards for platform services |

## Legal and Regulatory Risks

### Money Transmission

| Risk | Description | Trigger |
|------|-------------|---------|
| **Stored value** | If credits can be purchased, held, and redeemed for services, they may be classified as "stored value" under state money transmitter laws | Credits purchasable with money and redeemable for services |
| **Money transmission** | If credits can be transferred between users or redeemed for cash, you may be operating as a money transmitter | Transferability or cash-out capability |
| **E-money** | Under EU PSD2/EMD2, if credits function like electronic money, you may need an e-money license | Credits redeemable at par value for services or cash |

**Key question**: Can a customer transfer credits to another party, or convert credits back to cash? If yes, money transmission/e-money analysis is required.

| Feature | Low Risk | High Risk |
|---------|----------|-----------|
| Purchased with currency | Moderate | — |
| Non-transferable between users | Low | — |
| Non-refundable / no cash-out | Low | — |
| Transferable between users | — | Money transmission risk |
| Redeemable for cash | — | Strong money transmission indicator |
| Expire after a period | Reduces risk | — |
| Earn interest | — | May trigger banking/investment regulation |

### Consumer Protection

| Concern | Requirement | Jurisdictions |
|---------|-------------|---------------|
| **Expiration disclosure** | Must clearly disclose if/when credits expire at time of purchase | US (state gift card laws), EU (Unfair Terms Directive), UK, Australia |
| **Gift card laws (if applicable)** | Many US states prohibit expiration of gift cards or require minimum 5-year validity; residual value laws may apply | US (CARD Act for gift cards, state laws vary), EU, Australia |
| **Refund rights** | Some jurisdictions require refund of unused prepaid balances on account termination | EU (Consumer Rights Directive), California, Australia |
| **Balance disclosure** | Customer must be able to check credit balance | US (state laws), EU, Australia |
| **Dormancy fees** | Restrictions on charging fees on dormant/unused credits | US (many states prohibit), EU |
| **Currency vs credit value** | If credits are denominated in currency equivalents, stronger consumer protections apply | Most jurisdictions |

### Revenue Recognition

| Credit Scenario | Revenue Treatment | Breakage |
|----------------|-------------------|----------|
| **Credits consumed** | Recognize as credits are used (ASC 606 step 5) | N/A |
| **Credits expire unused** | Recognize breakage revenue proportionally or at expiration | Must estimate expected breakage based on historical data |
| **Unused credits, no expiration** | May need to estimate breakage; cannot recognize until consumed or forfeited | Analyze historical consumption patterns |
| **Promotional/free credits** | Generally no revenue (contra-revenue or marketing expense) | No breakage revenue |
| **Refundable credits** | Defer until consumed; refund liability until then | Refund liability reduces recognized revenue |

### Tax Treatment

| Scenario | Tax Implications |
|----------|-----------------|
| **Credit purchase** | Generally NOT a taxable event (no service yet delivered). Tax due when credits are consumed. |
| **Credit consumption** | Taxable event — the service is being delivered. Apply tax based on service classification and customer location. |
| **Cross-border credits** | Customer buys credits in one jurisdiction, consumes in another — tax may apply where consumption occurs |
| **Expiration / breakage** | Some jurisdictions tax breakage as income; consumer protection laws may limit breakage |
| **Promotional credits** | Generally not taxable (no consideration received) |

## Structuring Credits to Minimize Regulatory Risk

| Design Decision | Lower Risk Choice | Why |
|----------------|-------------------|-----|
| **Transferability** | Non-transferable (tied to purchasing account) | Avoids money transmission classification |
| **Refundability** | Non-refundable (with clear disclosure) | Avoids stored-value / e-money classification; but check consumer protection law by jurisdiction |
| **Expiration** | Include reasonable expiration (12+ months with disclosure) | Reduces balance sheet liability; enables breakage recognition |
| **Denomination** | Denominate in abstract units, not currency | Reduces argument that credits are "money equivalents" |
| **Cash-out** | No cash-out option | Critical for avoiding money transmission |
| **Interest** | Credits do not earn interest | Avoids banking/investment regulation |
| **Promotional credits** | Separate bucket from purchased credits | Different revenue and tax treatment |
| **Minimum purchase** | No minimum (or low minimum) | Avoids appearance of investment product |
