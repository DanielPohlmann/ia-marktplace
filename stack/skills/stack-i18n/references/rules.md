# Internationalization (i18n) Rules

Best practices and rules for Internationalization (i18n).

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Externalize every user-facing string | MEDIUM | [`i18n-externalize-every-user-facing-string.md`](i18n-externalize-every-user-facing-string.md) |
| 2 | Use the `IStringLocalizer<T>` generic pattern | MEDIUM | [`i18n-use-the-istringlocalizer-t-generic-pattern.md`](i18n-use-the-istringlocalizer-t-generic-pattern.md) |
| 3 | Create a shared resource class | HIGH | [`i18n-create-a-shared-resource-class.md`](i18n-create-a-shared-resource-class.md) |
| 4 | Always provide a neutral culture fallback | CRITICAL | [`i18n-always-provide-a-neutral-culture-fallback.md`](i18n-always-provide-a-neutral-culture-fallback.md) |
| 5 | Use parameterized localization | MEDIUM | [`i18n-use-parameterized-localization.md`](i18n-use-parameterized-localization.md) |
| 6 | Enable data annotations localization | MEDIUM | [`i18n-enable-data-annotations-localization.md`](i18n-enable-data-annotations-localization.md) |
| 7 | Test with pseudo-localization | MEDIUM | [`i18n-test-with-pseudo-localization.md`](i18n-test-with-pseudo-localization.md) |
| 8 | Handle `ResourceNotFound` gracefully | MEDIUM | [`i18n-handle-resourcenotfound-gracefully.md`](i18n-handle-resourcenotfound-gracefully.md) |
| 9 | Support RTL layouts | MEDIUM | [`i18n-support-rtl-layouts.md`](i18n-support-rtl-layouts.md) |
| 10 | Keep resource keys stable and descriptive | MEDIUM | [`i18n-keep-resource-keys-stable-and-descriptive.md`](i18n-keep-resource-keys-stable-and-descriptive.md) |

---

---
title: "Always provide a neutral culture fallback"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Always provide a neutral culture fallback

(e.g., `SharedResource.resx` without a culture suffix) so missing translations return a meaningful default rather than the resource key.

---

---
title: "Create a shared resource class"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Create a shared resource class

Create a shared resource class: for strings used across multiple components (button labels, validation messages, app name) to avoid duplication across `.resx` files.

---

---
title: "Enable data annotations localization"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Enable data annotations localization

Enable data annotations localization: with a shared resource provider so all validation messages are centralized and translatable.

---

---
title: "Externalize all user-facing strings"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization
---

## Externalize all user-facing strings

Externalize all user-facing strings

---

---
title: "Externalize every user-facing string"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Externalize every user-facing string

Externalize every user-facing string: into `.resx` files from the start; retrofitting i18n into an existing codebase is significantly more expensive than designing for it up front.

---

---
title: "Handle `ResourceNotFound` gracefully"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Handle `ResourceNotFound` gracefully

Handle `ResourceNotFound` gracefully: by checking `LocalizedString.ResourceNotFound` in development mode and logging missing keys for the translation team.

---

---
title: "Handle right-to-left languages"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization
---

## Handle right-to-left languages

Handle right-to-left languages

---

---
title: "Keep resource keys stable and descriptive"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Keep resource keys stable and descriptive

(e.g., `OrderConfirmation_Subject` rather than `String1`) because renaming keys breaks existing translations.

---

---
title: "Support culture-specific formatting"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization
---

## Support culture-specific formatting

Support culture-specific formatting

---

---
title: "Support RTL layouts"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Support RTL layouts

Support RTL layouts: by setting `dir="rtl"` conditionally in your layout based on `CultureInfo.CurrentUICulture.TextInfo.IsRightToLeft`.

---

---
title: "Test with different locales"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization
---

## Test with different locales

Test with different locales

---

---
title: "Test with pseudo-localization"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Test with pseudo-localization

(artificially lengthened strings, accented characters) to catch UI layout issues before real translations arrive.

---

---
title: "Use parameterized localization"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Use parameterized localization

(`_localizer["Hello, {0}!", name]`) instead of string concatenation to support word-order differences across languages.

---

---
title: "Use resource files ("
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization
---

## Use resource files (

Use resource files (.resx)

---

---
title: "Use the `IStringLocalizer<T>` generic pattern"
impact: MEDIUM
impactDescription: "general best practice"
tags: i18n, dotnet, localization, designing-i18n-ready-applications, externalizing-user-facing-strings, building-multi-language-aspnet-core-apps
---

## Use the `IStringLocalizer<T>` generic pattern

Use the `IStringLocalizer<T>` generic pattern: instead of `IStringLocalizerFactory` directly, so the DI container automatically resolves the correct resource file based on the type.
