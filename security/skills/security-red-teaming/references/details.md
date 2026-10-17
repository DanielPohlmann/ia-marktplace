<!-- Part of the security-red-teaming skill. Loaded on demand from SKILL.md. -->

# Red Teaming — details

## Purple Teaming

Purple teaming is the **collaborative integration** of red team (attack) and blue team (defense) to maximize learning and improve detection coverage.

| Aspect | Traditional Red Team | Purple Team |
|--------|---------------------|-------------|
| **Collaboration** | Adversarial — red hides from blue | Cooperative — red and blue work together |
| **Goal** | Find gaps in detection and response | Improve detection and response in real-time |
| **Process** | Red attacks, writes report, blue reads later | Red executes technique, blue tunes detection, iterate |
| **Speed of improvement** | Slow (report → fix cycle) | Fast (immediate feedback loop) |
| **Best for** | Mature security programs | Building and validating detection capabilities |

### Purple Team Exercise Flow

1. **Select ATT&CK technique** to test (e.g., T1059 — Command and Scripting Interpreter)
2. **Red team executes** the technique in a controlled environment
3. **Blue team observes** — did alerts fire? Were logs generated? Was the activity detected?
4. **Gap analysis** — identify what was missed and why
5. **Detection engineering** — blue team writes or tunes detection rules
6. **Re-execute** — red team runs the technique again to verify detection
7. **Document** — record the detection coverage and any remaining gaps
8. **Repeat** for the next technique

## C2 Frameworks

Command and Control (C2) frameworks provide the infrastructure for maintaining access to compromised systems during engagements. These tools must only be used in authorized engagements.

| Framework | Type | Key Features | Best For |
|-----------|------|-------------|----------|
| **Cobalt Strike** | Commercial | Beacon payload, Malleable C2 profiles, team server, industry standard | Professional red teams, APT simulation |
| **Sliver** | Open source (BishopFox) | Cross-platform implants, mutual TLS, DNS/HTTP/WireGuard C2 | Modern open-source alternative to Cobalt Strike |
| **Havoc** | Open source | Demon agent, sleep obfuscation, token manipulation | Advanced evasion techniques |
| **Mythic** | Open source | Multi-agent support, containerized, extensible | Flexible multi-platform C2 |
| **Brute Ratel** | Commercial | Badger payload, EDR evasion focused, syscall-level evasion | EDR bypass testing |
| **Caldera** | Open source (MITRE) | ATT&CK-aligned automated adversary emulation | Automated purple team exercises |

## AI / LLM Red Teaming

AI systems require specialized red teaming to test for vulnerabilities unique to language models and autonomous agents.

| Concern | Test Approach | Tools |
|---------|--------------|-------|
| **Prompt injection** | Craft adversarial inputs to override system instructions | Garak, Promptfoo |
| **Data extraction** | Attempt to extract training data or PII from model responses | Manual probing, ARTKIT |
| **System prompt leakage** | Try to reveal hidden system prompts or instructions | Manual, Promptfoo |
| **Jailbreaking** | Bypass safety guardrails to produce harmful content | Garak, DeepTeam |
| **Excessive agency** | Test whether agent takes unauthorized actions | Scenario-based testing, sandboxed execution |
| **Hallucination exploitation** | Trick model into generating convincing false information | Domain-specific fact-checking probes |
| **Multi-turn manipulation** | Gradually shift model behavior across conversation turns | ARTKIT (multi-turn framework) |

### AI Red Teaming Tools

| Tool | Maintainer | Focus |
|------|-----------|-------|
| **Garak** | OWASP | 100+ attack modules for LLM vulnerability scanning |
| **ARTKIT** | — | Multi-turn adversarial interaction framework |
| **Promptfoo** | — | Prompt testing, comparison, and red teaming |
| **DeepTeam** | — | Comprehensive LLM red team framework |
| **Counterfit** | Microsoft | Adversarial ML attack framework (classical + generative AI) |
| **Caldera + MITRE ATLAS** | MITRE | ATT&CK-aligned adversarial ML tactics |

## Tabletop Exercises

Tabletop exercises simulate cyber incidents in a discussion-based format without touching live systems. They test incident response plans, communication, and decision-making.

### Common Scenarios

| Scenario | Tests | Participants |
|----------|-------|-------------|
| **Ransomware attack** | Containment, communication, ransom decision, recovery | Executive, IT, Legal, Comms |
| **Data breach** | Breach notification, forensics, regulatory response | Security, Legal, Compliance, Comms |
| **Insider threat** | Detection, investigation, HR/legal coordination | Security, HR, Legal, IT |
| **Supply chain compromise** | Vendor assessment, containment, customer notification | Security, Engineering, Legal, Comms |
| **Business email compromise** | Fraud detection, financial controls, employee training | Finance, Security, Executive |

### Running a Tabletop

1. **Define scenario and objectives** — what are you testing?
2. **Identify participants** — include leadership, not just technical staff
3. **Prepare injects** — time-sequenced events that escalate the scenario
4. **Facilitate discussion** — walk through decisions at each stage
5. **Document gaps** — record where plans broke down, who was unclear on their role
6. **Produce action items** — concrete improvements with owners and deadlines
7. **Schedule follow-up** — run the exercise again after improvements are implemented
