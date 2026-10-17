<!-- Part of the security-ai-security skill. Loaded on demand from SKILL.md. -->

# Model & Data Poisoning

Model and data poisoning attacks target the training and fine-tuning pipeline to corrupt the model's behavior in subtle, hard-to-detect ways.

## Attack Types

- **Backdoor creation** — Inject training examples that cause the model to behave maliciously when a specific trigger pattern is present in the input (e.g., a specific phrase causes the model to output attacker-controlled content).
- **Behavioral manipulation** — Shift the model's general behavior by biasing the training data (e.g., making the model consistently recommend a specific product or downplay certain risks).
- **Code injection** — For code-generating models, poison training data with examples that introduce vulnerabilities (e.g., code that includes backdoors or uses insecure patterns).
- **Capability degradation** — Degrade the model's performance on specific tasks or for specific user groups through targeted data poisoning.

## Attack Vectors

- **Pretraining data** — Poisoning large-scale web scrapes or public datasets used for pretraining. Difficult to detect at scale.
- **Fine-tuning data** — Compromising the curated datasets used for task-specific fine-tuning. More targeted and potentially more impactful.
- **Infrastructure** — Compromising the training pipeline itself (compute infrastructure, data storage, model registries) to inject poisoned data or modify model weights directly.

## Defenses

- **Data validation and provenance** — Verify the source and integrity of all training data. Use data lineage tracking to trace each training example to its origin.
- **Access controls** — Restrict access to training pipelines, datasets, and model registries. Apply the principle of least privilege to ML infrastructure.
- **Model attestation** — Sign models and track their provenance through the entire lifecycle (training, fine-tuning, deployment). Verify model integrity before deployment.
- **Anomaly detection** — Monitor model behavior for unexpected changes in performance, output distribution, or behavior on specific inputs. Automated regression testing against benchmark datasets can detect poisoning.
- **Red teaming** — Regularly test models for backdoor behaviors using adversarial inputs and trigger pattern detection techniques.
