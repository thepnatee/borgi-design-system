# Localization Standards

Borgi supports Thai and English as first-class locales.

## Rules

- Store timestamps in UTC and render in the business or customer timezone as explicitly selected.
- Use locale-aware date, time, number, currency and plural formatting.
- Never concatenate translated fragments.
- Allow at least 35% text expansion in layouts.
- Keep customer names, service names and addresses in their entered script.
- Define fallback order per tenant and preserve the original template locale in delivery records.
- Thai UI should avoid unnecessary English abbreviations; English UI should use sentence case.

## Required test cases

Thai Buddhist-era display policy, Gregorian storage, midnight boundaries, daylight-saving zones, long service names, missing translations, mixed Thai/English names and right-to-left readiness even when not yet enabled.
