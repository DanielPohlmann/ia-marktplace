# LinkDaily — Feature Discovery Context

Concrete mapping for generating **customer-facing** docs from the LinkDaily codebase.
LinkDaily is a scheduling SaaS for independent professionals: a .NET modular monolith
with a distributed deployment.

## Where to look

| Layer | Path | What it tells you |
|---|---|---|
| **E2E tests** | `tests/E2E/LinkDaily.E2E.Tests` | **Verified user journeys** — start here; the strongest signal for what customers actually do |
| API surface | `src/Services/LinkDaily.Api` | HTTP endpoints → actions a customer can trigger |
| Business operations | `src/Modules/LinkDaily.<Module>` | Command/query handlers → the verbs behind each capability |
| Background behavior | `src/Services/LinkDaily.Worker` | What happens *after* an action (emails, reminders, async processing) |
| Admin UI | `frontend/admin-spa` | The professional's dashboard — most customer-facing screens live here |
| Public site | `frontend/public-nuxt` | The end-client booking experience (the professional's *clients*) |
| Product intent | `specs/` PRDs, root `README.md`, `CLAUDE.md` | Feature names, personas, intended value |

### E2E tests — read these first

LinkDaily's E2E suite is a **.NET xUnit + Playwright** project that drives the Aspire
AppHost and the real frontends (it navigates `public-nuxt` and `admin-spa` via
`AppHostFixture.GetEndpointUrl(...)`). This is the closest thing to a verified,
executable list of customer journeys.

- **Test classes** (`tests/E2E/.../Browser/*.cs`) group flows by screen/area — e.g.
  `HomePageTests` covers the public landing page.
- **Test method names** encode the scenario in `Subject_WhenCondition_ShouldOutcome`
  form — read them as Given/When/Then. `HomePage_WhenLoaded_ShouldDisplayTitle` →
  "the booking home page loads and shows the professional's page".
- **The endpoint each test targets** (`GetEndpointUrl("public-nuxt", ...)` vs
  `"admin-spa"`) tells you *which customer* the flow belongs to.
- Ignore `Infrastructure/*` fixtures (`AppHostFixture`, `PlaywrightFixture`) and
  everything under `bin/`/`obj/` — plumbing, not journeys.

Translate the *journey*, not the assertion: a test asserting `title.Should().NotBeNullOrEmpty()`
becomes "when a client opens your booking link, your page loads with your name and
services" — never "the page title is non-empty". As the suite grows (booking, payments,
auth flows), each new test class is a candidate section in the matching guide page.

> Two customer types exist. Be explicit about which one a page addresses:
> - **The professional** (the paying user) — uses the admin SPA to manage their business.
> - **Their client** (the end booker) — uses the public Nuxt site to book.

## Module → customer feature mapping

The customer never sees "modules". Translate:

| Module | Internal role | Customer-facing feature area | Audience |
|---|---|---|---|
| `Identity` | Auth, users, roles, invites | **Your account & team** — sign in, invite team members, set permissions | Professional |
| `Scheduling` | Appointments, availability, calendar | **Booking & calendar** — set your availability, take appointments, online booking page | Both |
| `Payments` | Charges, invoices, receipts | **Payments & invoices** — get paid, send receipts, plan billing | Professional |
| `Notifications` | Email/messaging, reminders | **Reminders & confirmations** — automatic confirmations and reminders | Both |
| `Logistics` | Location/routing (Valhalla) | **Locations & travel** — service areas, travel between appointments | Professional |

A single customer feature often spans modules. Example: "Online booking" =
`Scheduling` (availability + appointment) + `Notifications` (confirmation email) +
`Payments` (deposit, if enabled). Document it as **one** page, not three.

## Suggested customer-facing page set

```
docs/user-guide/
├── index.md
├── getting-started.md                # Sign up, set up your profile, first availability
├── booking-and-calendar.md           # Availability, appointments, the calendar
├── your-online-booking-page.md       # The public page clients use to book (public-nuxt)
├── payments-and-invoices.md          # Getting paid, receipts, plan billing
├── reminders-and-confirmations.md    # Automatic emails/reminders
├── your-clients.md                   # Managing client records
├── team-and-permissions.md           # Inviting team members, roles
└── your-account.md                   # Profile, security, plan
```

Confirm the set against what's actually shipped before writing — some areas may be
partial or admin-only.

## Before / after (voice)

**Endpoint found:** `POST /appointments` in `LinkDaily.Api`, handled by a
`CreateAppointmentHandler` in `Scheduling`, which publishes an event consumed by
`Notifications`.

- ❌ *Leaked:* "Calling `POST /appointments` triggers `CreateAppointmentHandler`, which emits `AppointmentCreated`; the `Notifications` module then sends the email."
- ✅ *Customer voice:* "When you book an appointment, your client automatically receives a confirmation email with the date, time, and location."

**Route found:** a public Nuxt page rendering a professional's availability with a booking form.

- ❌ *Leaked:* "The `public-nuxt` app renders availability from the `Scheduling` module's query endpoint."
- ✅ *Customer voice:* "Share your booking link and clients pick an open time slot themselves — no back-and-forth."

## Gating signals

Check `aspire.config.json`, feature flags, and plan/tier logic (often in `Payments` or
`Identity`) to mark capabilities as plan-specific ("Available on the Pro plan"). Don't
guess — if gating isn't clear in code, list it as an open question in the report.

## Things to exclude from customer docs

- Infra and ops (Aspire, Docker, Postgres, Redis, RabbitMQ, Elasticsearch, Valhalla).
- The migrator, worker internals, health checks, observability/OTLP.
- Admin/internal-only endpoints not exposed to the paying customer.
- Anything behind a disabled feature flag or not yet shipped — list it in the report
  instead of documenting it.
