<!-- Part of the specs-documentation-userguide skill. Loaded on demand from SKILL.md. -->

# Feature Discovery — mapping code to customer capabilities

The customer never sees your architecture. Translate these signals into features:

| Code signal | What to read | Yields |
|---|---|---|
| **E2E tests** | End-to-end/browser test files, scenario/test names, the flows they drive | Verified user journeys — the strongest signal for "what a customer actually does" |
| **BDD `.feature` files** | Gherkin scenarios (Given/When/Then), if present | Behavior already phrased in near-customer language — reuse the wording |
| **API endpoints** | Controllers / minimal-API routes, their HTTP verbs and route names | Actions the customer can trigger |
| **Module handlers** | Command/query handlers per module (the business operations) | The verbs behind each capability |
| **Frontend routes/pages** | SPA routes, Nuxt pages, page titles and forms | The screens the customer actually navigates |
| **Public UI copy / i18n** | Translation files, labels, button text | The product's own vocabulary — reuse it |
| **PRDs & READMEs** | `specs/` PRDs, project README | Intended value, feature names, personas |
| **Config/feature flags** | Flags, plans/tiers | Which capabilities are gated / plan-specific |

**Prefer the frontend and UI copy as your naming source** — it's the closest thing to
what the customer sees. Fall back to endpoints/handlers to confirm a capability exists
and to find ones the UI doesn't obviously expose.

**E2E tests and `.feature` files are the highest-value discovery signal.** They encode
complete, *verified* user journeys — a test named `Booking_WhenSlotSelected_SendsConfirmation`
maps almost one-to-one to a "How to use it" section. The page/route each test drives
confirms the flow is customer-facing and actually works. Read the scenario/test names
first, then the steps. But keep the audience rule: a test asserts on selectors and
status codes — translate the *journey* it proves, never its assertions. If the repo has
a QA/browser-automation skill (e.g. `playwright-cli`, `bdd-gherkin`), those tests are
where its scenarios live.

**Group by customer mental model.** "Booking", "Payments & invoices", "Your clients",
"Notifications & reminders", "Team & permissions", "Your account" — these are feature
areas a customer recognizes, and each may be assembled from several modules.
