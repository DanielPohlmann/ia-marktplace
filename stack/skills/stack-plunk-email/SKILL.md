---
name: stack-plunk-email
description: Plunk transactional and marketing email integration for .NET. Use when the Notifications bounded context needs to send transactional emails (booking confirmations, reminders, receipts) via the Plunk REST API or Node SDK. USE FOR: Plunk API email send, contact creation, event tracking, automated workflows, audience segmentation, HTML template variables, PLUNK_SECRET_KEY / PLUNK_PUBLIC_KEY configuration. DO NOT USE FOR: bulk email without personalisation (use an ESP like SendGrid), push notifications (use FCM/APNs), SMS/WhatsApp (use stack-masstransit + Twilio consumer), generic .NET email abstractions (use stack-serilog for log delivery, not email).
---

# Plunk Email

## Overview
Plunk é uma plataforma open-source de email para desenvolvedores, suportando emails transacionais e de marketing com escalabilidade para milhões de contatos. Oferece API REST, SDK Node.js/TypeScript, gerenciamento de contatos, workflows automatizados e segmentação dinâmica de audiência.

## Variáveis de Ambiente

```bash
PLUNK_SECRET_KEY=sk_...   # Nunca expor no frontend
PLUNK_PUBLIC_KEY=pk_...   # Seguro para uso client-side
```

## SDK Node.js/TypeScript

```bash
npm install @plunk/node
```

```typescript
import Plunk from "@plunk/node";

const plunk = new Plunk(process.env.PLUNK_SECRET_KEY!);
```

## Envio de Email Transacional

```typescript
// Simples
await plunk.emails.send({
  to: "destinatario@exemplo.com",
  subject: "Assunto do email",
  body: "<p>Corpo do email em HTML</p>",
});

// Com variáveis de template
await plunk.emails.send({
  to: "destinatario@exemplo.com",
  subject: "Bem-vindo, {{name}}!",
  body: "<p>Olá {{name}}, sua conta foi criada com o plano {{plan}}.</p>",
  data: {
    name: "Daniel",
    plan: "Pro",
  },
});
```

### Via API REST

```http
POST https://api.useplunk.com/v1/send
Authorization: Bearer <PLUNK_SECRET_KEY>
Content-Type: application/json

{
  "to": "destinatario@exemplo.com",
  "subject": "Assunto do email",
  "body": "<p>Corpo do email em HTML</p>"
}
```

## Rastreamento de Eventos (Contatos)

Eventos criam ou atualizam contatos automaticamente e disparam workflows.

```typescript
// Rastrear evento (cria contato se não existir)
await plunk.events.track({
  event: "user-signup",
  email: "contato@exemplo.com",
  data: {
    name: "Daniel",
    plan: "pro",
  },
});
```

### Via API REST

```http
POST https://api.useplunk.com/v1/track
Authorization: Bearer <PLUNK_SECRET_KEY>
Content-Type: application/json

{
  "event": "user-signup",
  "email": "contato@exemplo.com",
  "data": {
    "name": "Daniel",
    "plan": "pro"
  }
}
```

## Gerenciamento de Contatos

```http
# Listar contatos
GET https://api.useplunk.com/v1/contacts
Authorization: Bearer <PLUNK_SECRET_KEY>

# Buscar contato por email
GET https://api.useplunk.com/v1/contacts/{email}
Authorization: Bearer <PLUNK_SECRET_KEY>
```

## Conceitos Principais

| Conceito | Descrição |
|---|---|
| **Transactional Emails** | Emails individuais disparados por API com suporte a templates e variáveis |
| **Campaigns** | Broadcasts únicos enviados para uma lista de contatos com agendamento |
| **Workflows** | Sequências automáticas de emails com lógica condicional |
| **Contacts** | Gerenciamento de contatos com campos customizados e importação CSV |
| **Segments** | Segmentação dinâmica de audiência por dados e comportamento |
| **Templates** | Templates reutilizáveis para emails transacionais e de marketing |
| **Events** | Rastreamento de eventos para disparar workflows e segmentar audiências |

## Boas Práticas

- Armazene `PLUNK_SECRET_KEY` apenas em variáveis de ambiente server-side; nunca exponha no frontend.
- Use `plunk.events.track()` para criar/atualizar contatos e disparar workflows ao invés de gerenciá-los manualmente.
- Utilize `{{variavel}}` nos campos `subject` e `body` com o objeto `data` para personalização dinâmica.
- Verifique o domínio remetente nas configurações do Plunk para melhorar a entregabilidade.
- Use a `PLUNK_PUBLIC_KEY` para operações client-side (ex: formulários de inscrição no browser).

## References

- [Plunk API Reference](https://docs.useplunk.com/api-reference/overview)
- [Plunk GitHub Repository](https://github.com/useplunk/plunk)
- [Plunk NPM Package](https://www.npmjs.com/package/@plunk/node)
