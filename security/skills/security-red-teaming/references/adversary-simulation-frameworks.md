<!-- Part of the security-red-teaming skill. Loaded on demand from SKILL.md. -->

# Adversary Simulation Frameworks

## MITRE ATT&CK

The industry-standard knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world observations.

| Tactic | Description | Example Techniques |
|--------|-------------|-------------------|
| **Reconnaissance** | Gathering information about the target | Active scanning, search open websites, gather victim identity info |
| **Resource Development** | Establishing infrastructure for the attack | Acquire infrastructure, develop capabilities, establish accounts |
| **Initial Access** | Getting into the target environment | Phishing, exploit public-facing application, supply chain compromise |
| **Execution** | Running adversary-controlled code | Command/scripting interpreter, exploitation for client execution |
| **Persistence** | Maintaining access across restarts | Boot/logon autostart, scheduled tasks, account manipulation |
| **Privilege Escalation** | Gaining higher-level permissions | Exploitation for privilege escalation, access token manipulation |
| **Defense Evasion** | Avoiding detection | Obfuscated files, indicator removal, masquerading |
| **Credential Access** | Stealing credentials | OS credential dumping, brute force, credentials from password stores |
| **Discovery** | Understanding the environment | Network service scanning, system information discovery |
| **Lateral Movement** | Moving through the environment | Remote services, exploitation of remote services, lateral tool transfer |
| **Collection** | Gathering data of interest | Data from local system, email collection, screen capture |
| **Command and Control** | Communicating with compromised systems | Application layer protocol, encrypted channel, proxy |
| **Exfiltration** | Stealing data | Exfiltration over C2 channel, exfiltration over web service |
| **Impact** | Disrupting, destroying, or manipulating systems | Data encrypted for impact (ransomware), defacement, data destruction |

## Cyber Kill Chain (Lockheed Martin)

A linear model of cyberattack progression:

```
1. Reconnaissance ──► 2. Weaponization ──► 3. Delivery ──► 4. Exploitation
         │                                                         │
         │              7. Actions on ◄── 6. Command ◄── 5. Installation
         │                 Objectives       & Control
         └──────────────────────────────────────────────────────────┘
                          Defender can break the chain at any stage
```

| Stage | Attacker Activity | Defender Response |
|-------|------------------|-------------------|
| **Reconnaissance** | Research targets, scan for vulnerabilities | Monitor for scanning, minimize public exposure |
| **Weaponization** | Create exploit payload, craft phishing lure | Threat intelligence, signature updates |
| **Delivery** | Send phishing email, exploit web app | Email filtering, web application firewall, user training |
| **Exploitation** | Execute exploit, trigger vulnerability | Patching, endpoint detection, application hardening |
| **Installation** | Install backdoor, establish persistence | EDR, application allowlisting, integrity monitoring |
| **Command & Control** | Establish C2 channel, beacon | Network monitoring, DNS filtering, egress controls |
| **Actions on Objectives** | Exfiltrate data, deploy ransomware, pivot | DLP, segmentation, incident response, backups |
