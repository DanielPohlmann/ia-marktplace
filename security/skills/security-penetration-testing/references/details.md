<!-- Part of the security-penetration-testing skill. Loaded on demand from SKILL.md. -->

# Penetration Testing — details

## Methodologies

| Methodology | Scope | Phases | Best For |
|-------------|-------|--------|----------|
| **OWASP Testing Guide** | Web applications | Information gathering, configuration testing, identity management, authentication, authorization, session management, input validation, error handling, cryptography, business logic, client-side | Web app and API pen tests |
| **PTES** | General | Pre-engagement, intelligence gathering, threat modeling, vulnerability analysis, exploitation, post-exploitation, reporting | Full-scope engagements |
| **OSSTMM** | Networks and systems | Scope, channel, index, vectors, verification, resolution | Network and infrastructure testing |
| **NIST SP 800-115** | Technical security | Planning, discovery, attack, reporting | Government and regulatory compliance |
| **CREST** | General (UK-focused) | Certified methodology for regulated industries | UK/EU regulated environments |

## Pen Test Types

| Type | Target | Techniques | Common Findings |
|------|--------|------------|-----------------|
| **Web Application** | HTTP endpoints, UI, business logic | Authentication bypass, injection, XSS, IDOR, privilege escalation, SSRF | OWASP Top 10 vulnerabilities |
| **API** | REST/GraphQL/gRPC endpoints | BOLA, broken auth, excessive data exposure, mass assignment, rate limit bypass | OWASP API Top 10 vulnerabilities |
| **Network / Infrastructure** | Hosts, services, protocols | Port scanning, service enumeration, exploit known CVEs, lateral movement, privilege escalation | Unpatched services, weak configs, default credentials |
| **Mobile** | iOS/Android apps | Binary analysis, certificate pinning bypass, local storage review, API interception, reverse engineering | Insecure storage, hardcoded secrets, weak transport |
| **Cloud** | AWS/Azure/GCP resources | Misconfiguration audits, IAM review, storage bucket enumeration, metadata service abuse | Over-permissioned roles, public resources, SSRF to metadata |
| **Wireless** | Wi-Fi, Bluetooth | Rogue AP, WPA cracking, evil twin, Bluetooth sniffing | Weak encryption, rogue access points |
| **Social Engineering** | People and processes | Phishing campaigns, pretexting, physical access testing | Credential harvesting, policy violations |

## Severity Rating

| Severity | CVSS Range | Description | Example |
|----------|-----------|-------------|---------|
| **Critical** | 9.0 - 10.0 | Immediate exploitation possible with severe impact | Unauthenticated RCE, SQL injection to database dump |
| **High** | 7.0 - 8.9 | Exploitation likely with significant impact | Authentication bypass, privilege escalation to admin |
| **Medium** | 4.0 - 6.9 | Exploitation possible with moderate impact | Stored XSS, IDOR with limited data exposure |
| **Low** | 0.1 - 3.9 | Exploitation difficult or limited impact | Information disclosure, verbose error messages |
| **Informational** | 0.0 | No direct security impact but worth noting | Missing security headers, outdated software versions |

## Bug Bounty and Responsible Disclosure

| Program Type | Description | Reward | Best For |
|-------------|-------------|--------|----------|
| **Bug Bounty (managed)** | Ongoing program via HackerOne/Bugcrowd/Intigriti | Monetary bounties | Continuous external testing at scale |
| **Bug Bounty (self-hosted)** | Company-run program with security@ email | Monetary or swag | Companies wanting control over process |
| **VDP (Vulnerability Disclosure Policy)** | Published policy inviting responsible reports | Recognition (no monetary) | Minimum baseline for any company |

### Responsible Disclosure Process

1. Researcher discovers vulnerability
2. Researcher reports via designated channel
3. Company acknowledges receipt (target: 1 business day)
4. Company triages and validates (target: 5 business days)
5. Company remediates (target: 90 days for standard, 7 days for actively exploited)
6. Coordinated public disclosure after fix
