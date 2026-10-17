---
name: security-red-teaming
description: Use when planning an authorized red team engagement that tests detection and response beyond vuln discovery. USE FOR: adversary simulation, MITRE ATT&CK, kill chain, purple teaming, C2 frameworks, assumed breach, attack paths, AI/LLM red teaming, tabletops. DO NOT USE FOR: CI scanning (use security-security-testing), scoped vuln discovery (use security-penetration-testing), threat modeling (use security-threat-modeling).
---

# Red Teaming

## Overview

Red teaming is an adversarial assessment that goes beyond penetration testing to evaluate an organization's **detection, response, and resilience** capabilities against realistic attack scenarios. While pen testing asks "can we get in?", red teaming asks "can you detect us, stop us, and recover?"

Red teams operate with stealth, simulate real-world threat actors (APTs, insider threats, ransomware groups), and test the full kill chain — from initial access through lateral movement to objective completion. The goal is not just to find vulnerabilities, but to expose gaps in people, processes, and technology.

> **Important**: Red team engagements require explicit written authorization from organizational leadership. Only a small group (the "white team" or "trusted agents") should know the engagement is occurring. Unauthorized adversarial activity is illegal.

### Key References

| Title | Author(s) | Focus |
|-------|-----------|-------|
| *Red Team Development and Operations* | Joe Vest & James Tubberville | Planning and executing red team engagements |
| *The Hacker Playbook 3* | Peter Kim | Red team field manual with practical TTPs |
| *Adversarial Tradecraft in Cybersecurity* | Dan Borges | Offensive and defensive techniques for red/blue teams |
| *MITRE ATT&CK Framework* | MITRE Corporation | Comprehensive knowledge base of adversary tactics and techniques |
| *Cyber Kill Chain* | Lockheed Martin | Seven-stage model of cyberattack progression |

## Red Team vs Pen Test vs Vulnerability Assessment

| Dimension | Vulnerability Assessment | Penetration Test | Red Team |
|-----------|------------------------|------------------|----------|
| **Goal** | Find known vulnerabilities | Exploit vulnerabilities to prove impact | Test detection and response against realistic attacks |
| **Scope** | Broad, automated scanning | Defined targets and systems | Objective-based (e.g., "exfiltrate customer database") |
| **Stealth** | None | Minimal | High — evade detection, mimic real threat actors |
| **Duration** | Hours to days | Days to weeks | Weeks to months |
| **Blue team awareness** | Yes | Usually yes | No (except white team) |
| **Tests people/process** | No | Limited | Yes — primary focus |
| **Methodology** | Scan and report | OWASP/PTES/OSSTMM | MITRE ATT&CK, Cyber Kill Chain |
| **Output** | Vulnerability list with severities | Exploit proof with business impact | Detection gaps, response failures, attack narratives |

## Attack Path Mapping

| Tool | Purpose | Type |
|------|---------|------|
| **BloodHound** | Active Directory attack path visualization | Open source |
| **PlumHound** | BloodHound report automation | Open source |
| **PingCastle** | AD security assessment and risk scoring | Free (community) |
| **ADExplorer** | AD snapshot and analysis | Free (Sysinternals) |

## Best Practices

- **Distinguish red teaming from pen testing** — pen tests find vulnerabilities; red teams test your ability to detect and respond to real attacks.
- **Start with purple teaming** if your security program is still maturing — get collaborative value before going adversarial.
- **Map engagements to MITRE ATT&CK** to measure detection coverage systematically against known adversary techniques.
- **Use assumed breach as a starting point** for red team engagements — skip initial access and focus on lateral movement and detection gaps.
- **Conduct tabletop exercises** quarterly to test incident response without the cost and risk of live red team engagements.
- **Rotate between internal and external red teams** — external teams bring fresh TTPs; internal teams bring organizational knowledge.
- **Debrief collaboratively** — red team findings should lead to blue team improvements, not blame.
- **Invest in detection engineering** based on red team results — every missed detection is an opportunity to build a new rule.
- **Test AI systems with specialized AI red teaming** — traditional pen testing tools do not cover prompt injection, jailbreaking, or excessive agency.
- **Treat red team reports as highly confidential** — they contain detailed attack playbooks specific to your organization.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/adversary-simulation-frameworks.md](references/adversary-simulation-frameworks.md) | Adversary Simulation Frameworks — MITRE ATT&CK, Cyber Kill Chain (Lockheed Martin) |
| [references/details.md](references/details.md) | Purple Teaming; C2 Frameworks; AI / LLM Red Teaming; Tabletop Exercises |

## References

- [MITRE ATT&CK Framework](https://attack.mitre.org)
- [Lockheed Martin Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [NIST SP 800-53 Security and Privacy Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

See references/rules.md for the full rule catalog.
