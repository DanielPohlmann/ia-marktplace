<!-- Part of the security-data-protection skill. Loaded on demand from SKILL.md. -->

# Encryption Requirements

## At Rest

Data at rest — stored in databases, file systems, object storage, or backups — must be encrypted to protect against unauthorized access in the event of physical theft, unauthorized backup access, or misconfigured storage permissions.

| Requirement | Details |
|---|---|
| Algorithm | AES-256 (AES-256-GCM preferred for authenticated encryption) |
| Transparent encryption | Use platform-native encryption (AWS KMS + S3 SSE, Azure Storage Service Encryption, GCP CMEK) for minimal application changes |
| Key storage | Keys must be stored separately from encrypted data; use dedicated key management services (AWS KMS, Azure Key Vault, HashiCorp Vault, GCP Cloud KMS) |
| Key rotation | Rotate encryption keys at least annually; automate rotation where possible; retain old keys for decrypting historical data |
| Database encryption | Enable Transparent Data Encryption (TDE) for relational databases; use field-level encryption for highly sensitive columns |
| Backup encryption | All backups must be encrypted with the same rigor as primary data; test restoration from encrypted backups regularly |

## In Transit

Data in transit — moving between clients and servers, between services, or between data centers — must be protected from eavesdropping and tampering.

| Requirement | Details |
|---|---|
| Protocol | TLS 1.2 as minimum; TLS 1.3 preferred; disable TLS 1.0/1.1 and SSL entirely |
| HTTPS everywhere | All API endpoints, web interfaces, and webhooks must use HTTPS; redirect HTTP to HTTPS; set HSTS headers |
| Certificate validation | Validate server certificates in all clients; do not disable certificate verification in production; pin certificates for mobile apps and critical service-to-service calls where appropriate |
| Internal traffic | Encrypt service-to-service communication within the network using mTLS or a service mesh (Istio, Linkerd); do not assume internal networks are trusted |
| Certificate management | Use automated certificate management (Let's Encrypt, AWS ACM) to prevent expiration-related outages; monitor certificate expiry |
