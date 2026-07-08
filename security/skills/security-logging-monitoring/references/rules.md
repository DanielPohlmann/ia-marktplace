# Security Logging & Monitoring Rules

Best practices and rules for Security Logging & Monitoring.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Log all security-relevant events | CRITICAL | [`logging-monitoring-log-all-security-relevant-events.md`](logging-monitoring-log-all-security-relevant-events.md) |
| 2 | Use structured logging formats | MEDIUM | [`logging-monitoring-use-structured-logging-formats.md`](logging-monitoring-use-structured-logging-formats.md) |
| 3 | Include correlation identifiers | MEDIUM | [`logging-monitoring-include-correlation-identifiers.md`](logging-monitoring-include-correlation-identifiers.md) |
| 4 | Never log sensitive data | CRITICAL | [`logging-monitoring-never-log-sensitive-data.md`](logging-monitoring-never-log-sensitive-data.md) |
| 5 | Set up real-time alerting | CRITICAL | [`logging-monitoring-set-up-real-time-alerting.md`](logging-monitoring-set-up-real-time-alerting.md) |
| 6 | Regularly test your detection capabilities | HIGH | [`logging-monitoring-regularly-test-your-detection-capabilities.md`](logging-monitoring-regularly-test-your-detection-capabilities.md) |
| 7 | Monitor the monitoring | HIGH | [`logging-monitoring-monitor-the-monitoring.md`](logging-monitoring-monitor-the-monitoring.md) |
| 8 | Review and tune detection rules quarterly | MEDIUM | [`logging-monitoring-review-and-tune-detection-rules-quarterly.md`](logging-monitoring-review-and-tune-detection-rules-quarterly.md) |

---

---
title: "Include correlation identifiers"
impact: MEDIUM
impactDescription: "general best practice"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Include correlation identifiers

(request ID, trace ID, session ID) in every log entry to enable end-to-end tracing of a single request or user session across distributed services.

---

---
title: "Log all security-relevant events"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Log all security-relevant events

Log all security-relevant events: at the application layer, not just at the infrastructure layer; application context (user identity, business action, data sensitivity) is essential for meaningful detection.

---

---
title: "Monitor the monitoring"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Monitor the monitoring

Monitor the monitoring: alert on gaps in log ingestion (silent sources), SIEM processing delays, and storage capacity thresholds to ensure your logging pipeline remains healthy.

---

---
title: "Never log sensitive data"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Never log sensitive data

Never log sensitive data: such as passwords, tokens, credit card numbers, or PII in cleartext; mask or redact sensitive fields before writing to the log.

---

---
title: "Regularly test your detection capabilities"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Regularly test your detection capabilities

Regularly test your detection capabilities: by running tabletop exercises, purple team engagements, and SIEM detection rule testing to ensure alerts fire correctly and are actionable.

---

---
title: "Review and tune detection rules quarterly"
impact: MEDIUM
impactDescription: "general best practice"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Review and tune detection rules quarterly

Review and tune detection rules quarterly: to reduce false positives, adapt to evolving threats, and incorporate lessons learned from incidents and near-misses.

---

---
title: "Set up real-time alerting"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Set up real-time alerting

Set up real-time alerting: for critical security events (authentication failures exceeding a threshold, privilege escalation, data exfiltration patterns) with clearly defined escalation paths.

---

---
title: "Use structured logging formats"
impact: MEDIUM
impactDescription: "general best practice"
tags: logging-monitoring, security, siem, security-logging, audit-trails
---

## Use structured logging formats

(JSON, key-value pairs) with a consistent schema across all services to enable reliable parsing, searching, and correlation in your SIEM.
