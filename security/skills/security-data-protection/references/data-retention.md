<!-- Part of the security-data-protection skill. Loaded on demand from SKILL.md. -->

# Data Retention

Data retention policies define how long data is kept and what happens when the retention period expires. Retaining data longer than necessary increases risk, storage costs, and regulatory exposure.

**Define Retention Policies**

- Establish retention periods based on regulatory requirements, business needs, and contractual obligations.
- Document retention policies in a data retention schedule that covers every data category.
- Ensure retention periods are specific (e.g., "3 years after account closure") rather than vague (e.g., "as long as needed").

**Automated Deletion**

- Implement automated processes to delete or anonymize data when the retention period expires.
- Use database-level TTL (Time-to-Live) features, scheduled jobs, or lifecycle policies (e.g., S3 lifecycle rules) to enforce retention.
- Verify automated deletion is working through regular audits.

**Legal Hold**

- Implement a legal hold process that can suspend automated deletion for data relevant to litigation, regulatory investigations, or audits.
- Legal holds must be granular — hold only the specific data relevant to the matter, not all data for a given user or category.
- Track all active legal holds and release them promptly when they are no longer needed.

**Backup Considerations**

- Retention policies must account for backup cycles. Data deleted from primary storage may still exist in backups.
- Define how long backups are retained and how deletion requests are handled for data in backups (e.g., delete upon next backup rotation vs. cryptographic erasure of the backup encryption key).
- Regularly test the ability to restore from backups and verify that retained data is still usable.
