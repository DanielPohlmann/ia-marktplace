<!-- Part of the dev-architecture-well-architected skill. Loaded on demand from SKILL.md. -->

# Cloud Well-Architected Frameworks — details

## Well-Architected Review Process

A Well-Architected Review (WAR) is a structured assessment of a workload against the framework's pillars. All three clouds provide review tooling:

| Cloud | Tool | How It Works |
|-------|------|-------------|
| **AWS** | AWS Well-Architected Tool | Answer questions per pillar; generates findings and improvement plan |
| **Azure** | Azure Well-Architected Review (online assessment) | Self-service questionnaire; generates recommendations |
| **GCP** | Architecture Framework checklists + Cloud Architecture Center | Checklist-driven review; reference architectures |

### Review Steps

1. **Scope the workload** -- Define the boundary of what is being reviewed (a single application, a platform, a service).
2. **Assemble the team** -- Include architects, developers, operations, security, and finance.
3. **Walk through each pillar** -- Answer the framework's questions honestly. Identify gaps.
4. **Prioritize findings** -- Rank by business impact and effort. Focus on high-risk, high-impact items first.
5. **Create an improvement plan** -- Assign owners, set deadlines, track progress.
6. **Schedule regular reviews** -- Architecture is not a one-time activity. Review quarterly or after major changes.

### Review Frequency

| Trigger | Action |
|---------|--------|
| New workload launch | Full review before production |
| Major architecture change | Review affected pillars |
| Quarterly cadence | Lightweight review of all pillars |
| Incident or outage | Review Reliability and Operational Excellence pillars |
| Cost spike | Review Cost Optimization pillar |
