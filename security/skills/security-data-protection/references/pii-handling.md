<!-- Part of the security-data-protection skill. Loaded on demand from SKILL.md. -->

# PII Handling

Personally Identifiable Information (PII) requires specific technical and procedural controls throughout its lifecycle.

**Data Minimization**

Collect only the personal data that is strictly necessary for the stated purpose. Review data collection forms, API request schemas, and database schemas to identify and eliminate unnecessary fields. Ask: "Do we need this data to provide the service?" If not, do not collect it.

**Purpose Limitation**

Use personal data only for the purpose for which it was collected. If a new use case arises, assess whether it is compatible with the original purpose or whether new consent is required. Document the purpose for each data element in a data inventory.

**Tokenization and Pseudonymization**

- **Tokenization**: Replace sensitive data with non-sensitive tokens that map back to the original data via a secure token vault. Tokens have no mathematical relationship to the original data.
- **Pseudonymization**: Replace identifying fields with pseudonyms; the data can be re-identified with a separate key. GDPR recognizes pseudonymization as a risk-reduction measure but still treats pseudonymized data as personal data.

**Right to Erasure (Right to be Forgotten)**

Implement a process to delete or anonymize all personal data associated with a data subject upon verified request. This must cover primary databases, backups, caches, logs, analytics systems, and third-party processors. Key considerations:
- Define what "erasure" means for each data store (hard delete vs. cryptographic erasure vs. anonymization).
- Propagate deletion requests to all downstream systems and third-party processors.
- Maintain a record of the deletion request and its execution (without retaining the deleted data itself).
- Handle exceptions for legal holds and regulatory retention requirements.

**Data Subject Access Requests (DSAR)**

Build automated or semi-automated workflows to respond to DSARs within regulatory timelines (30 days under GDPR). The system must be able to locate, extract, and export all personal data associated with a given identity across all data stores.
