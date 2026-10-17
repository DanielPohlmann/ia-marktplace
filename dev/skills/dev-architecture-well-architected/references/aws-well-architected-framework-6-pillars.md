<!-- Part of the dev-architecture-well-architected skill. Loaded on demand from SKILL.md. -->

# AWS Well-Architected Framework (6 Pillars)

## 1. Operational Excellence
Design, run, and monitor systems to deliver business value and continually improve processes and procedures.

**Key principles:**
- Perform operations as code (Infrastructure as Code)
- Make frequent, small, reversible changes
- Refine operations procedures frequently
- Anticipate failure; learn from all operational events
- Use managed services to reduce operational burden

## 2. Security
Protect data, systems, and assets through risk assessments, security controls, and automated security best practices.

**Key principles:**
- Implement a strong identity foundation (least privilege, IAM)
- Enable traceability (logging, auditing, monitoring)
- Apply security at all layers (edge, VPC, subnet, instance, OS, application)
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data (reduce direct access)
- Prepare for security events (incident response runbooks)

## 3. Reliability
Ensure a workload can recover from failures and meet demand through proper planning and design.

**Key principles:**
- Automatically recover from failure
- Test recovery procedures
- Scale horizontally to increase aggregate availability
- Stop guessing capacity (use auto-scaling)
- Manage change through automation

## 4. Performance Efficiency
Use computing resources efficiently and maintain that efficiency as demand changes and technologies evolve.

**Key principles:**
- Democratize advanced technologies (use managed services)
- Go global in minutes (multi-region)
- Use serverless architectures where possible
- Experiment more often
- Consider mechanical sympathy (understand how services are consumed)

## 5. Cost Optimization
Avoid unnecessary costs and understand where money is being spent.

**Key principles:**
- Implement cloud financial management
- Adopt a consumption model (pay for what you use)
- Measure overall efficiency
- Stop spending money on undifferentiated heavy lifting
- Analyze and attribute expenditure

## 6. Sustainability
Minimize environmental impact of cloud workloads.

**Key principles:**
- Understand your impact
- Establish sustainability goals
- Maximize utilization
- Anticipate and adopt new, more efficient offerings
- Use managed services (shared infrastructure is more efficient)
- Reduce downstream impact of your cloud workloads

---
