<!-- Part of the dev-architecture-domain-driven-design skill. Loaded on demand from SKILL.md. -->

# Strategic DDD

Strategic DDD deals with the big picture: how to decompose a large system into manageable parts, how those parts relate to each other, and how teams communicate across boundaries.

## Ubiquitous Language

A shared, precise language between developers and domain experts for each bounded context. The same term means the same thing everywhere within a context -- in conversations, documentation, code, and tests.

**Rules:**
- One bounded context, one ubiquitous language.
- If a term means different things to different people, you likely have multiple bounded contexts.
- The language should appear literally in the code: class names, method names, variable names.
- Refine the language continuously as understanding deepens.

**Example:** In an e-commerce system, "Order" means different things in different contexts:
- **Sales context:** An Order is a customer's purchase intent with line items and pricing.
- **Fulfillment context:** An Order is a set of items to pick, pack, and ship.
- **Billing context:** An Order is an invoice with payment terms.

Each context has its own Order model with its own ubiquitous language.

## Bounded Contexts

A bounded context is an explicit boundary within which a domain model is defined and applicable. Inside a bounded context, the ubiquitous language is consistent. Across bounded contexts, the same word may mean different things.

```
┌─────────────────────────────────────────────────────┐
│                    E-Commerce System                  │
│                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │    Sales     │  │ Fulfillment │  │   Billing   │  │
│  │   Context    │  │   Context   │  │   Context   │  │
│  │             │  │             │  │             │  │
│  │ Order =     │  │ Order =     │  │ Order =     │  │
│  │ purchase    │  │ shipment    │  │ invoice     │  │
│  │ intent      │  │ items       │  │             │  │
│  │             │  │             │  │ Customer =  │  │
│  │ Customer =  │  │ Customer =  │  │ billing     │  │
│  │ buyer with  │  │ shipping    │  │ account     │  │
│  │ preferences │  │ address     │  │             │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│                                                       │
│  Each context has its own model, language, and data   │
└─────────────────────────────────────────────────────┘
```

## Subdomains

Subdomains represent areas of the business. They exist independently of software -- they are about the business problem space, not the solution.

| Type | Description | Investment Strategy | Example |
|------|-------------|-------------------|---------|
| **Core** | Your competitive advantage; what differentiates the business | Build custom; invest the best talent | Pricing engine for an insurance company |
| **Supporting** | Necessary for the business but not differentiating | Build simpler custom solutions or customize off-the-shelf | Customer onboarding |
| **Generic** | Common to many businesses; commodity | Buy or use open-source | Authentication, email, payment processing |

**Key insight:** Align bounded contexts with subdomains where possible. Invest the most effort in core subdomains.

## Context Maps

A context map is a visualization of the relationships between bounded contexts. It shows how contexts integrate and what the power dynamics are.

```
┌──────────────┐          ┌──────────────┐
│    Sales     │          │  Fulfillment │
│   (Core)     │─────────▶│ (Supporting) │
│              │  Customer │              │
│              │  -Supplier│              │
└──────┬───────┘          └──────────────┘
       │
       │ Published
       │ Language
       │
┌──────▼───────┐          ┌──────────────┐
│   Billing    │          │  Shipping    │
│   (Core)     │◀─────────│  (Generic)   │
│              │   ACL     │  (3rd party) │
└──────────────┘          └──────────────┘
```

## Context Mapping Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Shared Kernel** | Two contexts share a subset of the model (code, schema). Changes require coordination. | Closely collaborating teams; small shared concepts |
| **Customer-Supplier** | Upstream (supplier) provides what downstream (customer) needs. Customer can influence the API. | Teams with a cooperative relationship; downstream has negotiation power |
| **Conformist** | Downstream conforms to upstream's model without negotiation. | Upstream won't change for you (e.g., large legacy system, external API) |
| **Anti-Corruption Layer (ACL)** | Downstream translates the upstream model into its own model via a translation layer. | Protecting your domain model from a foreign or legacy model |
| **Open Host Service** | Upstream provides a well-defined, versioned API (protocol) for many consumers. | Serving multiple downstream contexts; public APIs |
| **Published Language** | A shared, documented data format (e.g., JSON schema, Protobuf, XML schema) used for integration. | Standardized exchange format; often combined with Open Host Service |
| **Separate Ways** | Contexts have no integration; they solve their own problems independently. | When integration cost exceeds benefit |
| **Partnership** | Two contexts evolve together with mutual coordination. Neither is upstream or downstream. | Co-developing teams with aligned release cadences |
