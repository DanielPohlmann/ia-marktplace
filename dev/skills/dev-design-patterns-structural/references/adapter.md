<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 1. Adapter

## Intent
Convert the interface of a class into another interface that clients expect. Adapter lets classes work together that could not otherwise because of incompatible interfaces.

## Structure

```
┌──────────────┐        ┌──────────────────┐
│    Client     │───────▶│  Target           │
└──────────────┘        │  (interface)      │
                         ├──────────────────┤
                         │ + request()       │
                         └──────┬───────────┘
                                │ implements
                                ▼
┌──────────────┐        ┌──────────────────┐
│   Adaptee     │◀───────│    Adapter        │
├──────────────┤ wraps  ├──────────────────┤
│ + specificReq()│       │ + request()       │
└──────────────┘        └──────────────────┘
```

## Participants
- **Target** — defines the domain-specific interface that Client uses
- **Client** — collaborates with objects conforming to the Target interface
- **Adaptee** — defines an existing interface that needs adapting
- **Adapter** — adapts the interface of Adaptee to the Target interface

## When to Use
- You want to use an existing class, but its interface does not match the one you need
- You want to create a reusable class that cooperates with unrelated or unforeseen classes
- You need to integrate a third-party library without coupling your code to its API

## TypeScript Example

```typescript
// Adaptee — third-party XML analytics service
class LegacyAnalytics {
  sendXML(xml: string): void {
    console.log(`[Legacy] Sending XML: ${xml}`);
  }
}

// Target interface — what our app expects
interface Analytics {
  track(event: string, data: Record<string, unknown>): void;
}

// Adapter
class AnalyticsAdapter implements Analytics {
  constructor(private legacy: LegacyAnalytics) {}

  track(event: string, data: Record<string, unknown>): void {
    const xml = `<event name="${event}">${
      Object.entries(data)
        .map(([k, v]) => `<${k}>${v}</${k}>`)
        .join("")
    }</event>`;
    this.legacy.sendXML(xml);
  }
}

// Usage
const analytics: Analytics = new AnalyticsAdapter(new LegacyAnalytics());
analytics.track("page_view", { url: "/home", userId: 42 });
// [Legacy] Sending XML: <event name="page_view"><url>/home</url><userId>42</userId></event>
```

---
