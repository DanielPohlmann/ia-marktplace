---
name: stack-plunk-email
description: Plunk transactional and marketing email integration for .NET. Use when the Notifications bounded context needs to send transactional emails (booking confirmations, reminders, receipts) via the Plunk REST API or Node SDK. USE FOR: Plunk API email send, contact creation, event tracking, automated workflows, audience segmentation, HTML template variables, PLUNK_SECRET_KEY / PLUNK_PUBLIC_KEY configuration. DO NOT USE FOR: bulk email without personalisation (use an ESP like SendGrid), push notifications (use FCM/APNs), SMS/WhatsApp (use stack-masstransit + Twilio consumer), generic .NET email abstractions (use stack-serilog for log delivery, not email).
---

# Plunk Email

## Overview
Plunk is an open-source email platform for developers, supporting transactional and marketing emails with scalability to millions of contacts. It offers a REST API, a Node.js/TypeScript SDK, contact management, automated workflows, and dynamic audience segmentation.

## Environment Variables

```bash
PLUNK_SECRET_KEY=sk_...   # Never expose on frontend
PLUNK_PUBLIC_KEY=pk_...   # Safe for client-side use
```

## Node.js/TypeScript SDK

```bash
npm install @plunk/node
```

```typescript
import Plunk from "@plunk/node";

const plunk = new Plunk(process.env.PLUNK_SECRET_KEY!);
```

## Transactional Email Sending

```typescript
// Simple
await plunk.emails.send({
  to: "recipient@example.com",
  subject: "Email subject",
  body: "<p>Email body in HTML</p>",
});

// With template variables
await plunk.emails.send({
  to: "recipient@example.com",
  subject: "Welcome, {{name}}!",
  body: "<p>Hi {{name}}, your account was created on the {{plan}} plan.</p>",
  data: {
    name: "Daniel",
    plan: "Pro",
  },
});
```

### Via REST API

```http
POST https://api.useplunk.com/v1/send
Authorization: Bearer <PLUNK_SECRET_KEY>
Content-Type: application/json

{
  "to": "recipient@example.com",
  "subject": "Email subject",
  "body": "<p>Email body in HTML</p>"
}
```

## Event Tracking (Contacts)

Events automatically create or update contacts and trigger workflows.

```typescript
// Track event (creates the contact if it does not exist)
await plunk.events.track({
  event: "user-signup",
  email: "contact@example.com",
  data: {
    name: "Daniel",
    plan: "pro",
  },
});
```

### Via REST API

```http
POST https://api.useplunk.com/v1/track
Authorization: Bearer <PLUNK_SECRET_KEY>
Content-Type: application/json

{
  "event": "user-signup",
  "email": "contact@example.com",
  "data": {
    "name": "Daniel",
    "plan": "pro"
  }
}
```

## Contact Management

```http
# List contacts
GET https://api.useplunk.com/v1/contacts
Authorization: Bearer <PLUNK_SECRET_KEY>

# Get contact by email
GET https://api.useplunk.com/v1/contacts/{email}
Authorization: Bearer <PLUNK_SECRET_KEY>
```

## Key Concepts

| Concept | Description |
|---|---|
| **Transactional Emails** | Individual emails triggered via API with support for templates and variables |
| **Campaigns** | One-off broadcasts sent to a list of contacts with scheduling |
| **Workflows** | Automated email sequences with conditional logic |
| **Contacts** | Contact management with custom fields and CSV import |
| **Segments** | Dynamic audience segmentation by data and behavior |
| **Templates** | Reusable templates for transactional and marketing emails |
| **Events** | Event tracking to trigger workflows and segment audiences |

## Best Practices

- Store `PLUNK_SECRET_KEY` only in server-side environment variables; never expose it on the frontend.
- Use `plunk.events.track()` to create/update contacts and trigger workflows instead of managing them manually.
- Use `{{variable}}` in the `subject` and `body` fields together with the `data` object for dynamic personalization.
- Verify the sender domain in the Plunk settings to improve deliverability.
- Use the `PLUNK_PUBLIC_KEY` for client-side operations (e.g., signup forms in the browser).

## References

- [Plunk API Reference](https://docs.useplunk.com/api-reference/overview)
- [Plunk GitHub Repository](https://github.com/useplunk/plunk)
- [Plunk NPM Package](https://www.npmjs.com/package/@plunk/node)
