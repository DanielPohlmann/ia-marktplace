# OpenAPI Rules

Best practices and rules for OpenAPI.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Enable XML documentation generation in ` | MEDIUM | [`openapi-enable-xml-documentation-generation-in.md`](openapi-enable-xml-documentation-generation-in.md) |
| 2 | Use `[ProducesResponseType]` attributes on every action to... | MEDIUM | [`openapi-use-producesresponsetype-attributes-on-every-action-to.md`](openapi-use-producesresponsetype-attributes-on-every-action-to.md) |
| 3 | Add `WithName`, `WithDescription`, and `WithTags` to... | MEDIUM | [`openapi-add-withname-withdescription-and-withtags-to.md`](openapi-add-withname-withdescription-and-withtags-to.md) |
| 4 | Configure security definitions (`AddSecurityDefinition` +... | CRITICAL | [`openapi-configure-security-definitions-addsecuritydefinition.md`](openapi-configure-security-definitions-addsecuritydefinition.md) |
| 5 | Version your APIs and generate separate OpenAPI documents... | MEDIUM | [`openapi-version-your-apis-and-generate-separate-openapi-documents.md`](openapi-version-your-apis-and-generate-separate-openapi-documents.md) |
| 6 | Only expose Swagger UI in development or staging... | CRITICAL | [`openapi-only-expose-swagger-ui-in-development-or-staging.md`](openapi-only-expose-swagger-ui-in-development-or-staging.md) |
| 7 | Use `[Description]` attributes on parameters and `///... | MEDIUM | [`openapi-use-description-attributes-on-parameters-and.md`](openapi-use-description-attributes-on-parameters-and.md) |
| 8 | Generate typed API clients using NSwag or Kiota from the... | MEDIUM | [`openapi-generate-typed-api-clients-using-nswag-or-kiota-from-the.md`](openapi-generate-typed-api-clients-using-nswag-or-kiota-from-the.md) |
| 9 | Customize enum serialization in OpenAPI schemas (string vs... | MEDIUM | [`openapi-customize-enum-serialization-in-openapi-schemas-string-vs.md`](openapi-customize-enum-serialization-in-openapi-schemas-string-vs.md) |
| 10 | Validate your generated OpenAPI spec in CI using tools like... | HIGH | [`openapi-validate-your-generated-openapi-spec-in-ci-using-tools-like.md`](openapi-validate-your-generated-openapi-spec-in-ci-using-tools-like.md) |

---

---
title: "Add `WithName`, `WithDescription`, and `WithTags` to..."
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Add `WithName`, `WithDescription`, and `WithTags` to...

Add `WithName`, `WithDescription`, and `WithTags` to minimal API endpoints so the generated OpenAPI spec has meaningful operation IDs and grouping.

---

---
title: "Configure security definitions (`AddSecurityDefinition` +..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Configure security definitions (`AddSecurityDefinition` +...

Configure security definitions (`AddSecurityDefinition` + `AddSecurityRequirement`) so consumers know how to authenticate when using Swagger UI or generated clients.

---

---
title: "Customize enum serialization in OpenAPI schemas (string vs..."
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Customize enum serialization in OpenAPI schemas (string vs...

Customize enum serialization in OpenAPI schemas (string vs integer) to match your API's JSON serialization settings using schema filters.

---

---
title: "Document security requirements"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: openapi, dotnet, documentation
---

## Document security requirements

Document security requirements

---

---
title: "Enable XML documentation generation in `"
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Enable XML documentation generation in `

Enable XML documentation generation in `.csproj` (`<GenerateDocumentationFile>true</GenerateDocumentationFile>`) and include XML comments via `IncludeXmlComments` so API descriptions come from code comments.

---

---
title: "Generate typed API clients using NSwag or Kiota from the..."
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Generate typed API clients using NSwag or Kiota from the...

Generate typed API clients using NSwag or Kiota from the OpenAPI spec to keep client code in sync with the API contract automatically.

---

---
title: "Include XML comments"
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation
---

## Include XML comments

Include XML comments

---

---
title: "Only expose Swagger UI in development or staging..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Only expose Swagger UI in development or staging...

Only expose Swagger UI in development or staging environments; disable it in production by guarding with `app.Environment.IsDevelopment()`.

---

---
title: "Use `[Description]` attributes on parameters and `///..."
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Use `[Description]` attributes on parameters and `///...

Use `[Description]` attributes on parameters and `/// <summary>` XML comments on models so auto-generated schemas include human-readable descriptions.

---

---
title: "Use `[ProducesResponseType]` attributes on every action to..."
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Use `[ProducesResponseType]` attributes on every action to...

Use `[ProducesResponseType]` attributes on every action to document all possible HTTP status codes and response types explicitly.

---

---
title: "Use ProducesResponseType attributes"
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation
---

## Use ProducesResponseType attributes

Use ProducesResponseType attributes

---

---
title: "Validate your generated OpenAPI spec in CI using tools like..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Validate your generated OpenAPI spec in CI using tools like...

Validate your generated OpenAPI spec in CI using tools like `swagger-cli validate` or `spectral lint` to catch documentation drift before deployment.

---

---
title: "Version your API"
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation
---

## Version your API

Version your API

---

---
title: "Version your APIs and generate separate OpenAPI documents..."
impact: MEDIUM
impactDescription: "general best practice"
tags: openapi, dotnet, documentation, api-documentation-with-openapiswagger, swashbuckle-configuration, nswag-client-generation
---

## Version your APIs and generate separate OpenAPI documents...

Version your APIs and generate separate OpenAPI documents per version using `SwaggerDoc("v1", ...)` and `SwaggerDoc("v2", ...)`.
