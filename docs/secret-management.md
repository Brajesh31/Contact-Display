# 🔑 Secret and Sensitive Data Handling

## 📌 Current application context

The inspected client application does not require a project-specific secret or server API key in its root package manifest. Contact data is personal information, but it is not a credential. Browser storage is not a secure secret vault.

## ✅ Rules

1. Never commit API keys, passwords, tokens, private keys, session cookies, or production credentials.
2. Do not put secrets in Vite client-side environment variables. Client-exposed build variables must be treated as public.
3. Use GitHub Actions secrets only for workflows that genuinely need them, and grant minimum permissions.
4. Never print secrets or contact records in CI logs.
5. Rotate and revoke exposed credentials promptly, then assess repository history and affected services.
6. Keep `.env` files local and untracked; share only safe variable names and placeholders in `.env.example`.
7. Do not store passwords or highly sensitive notes in Contact Display contact records.

## 🧭 Incident response

| Step | Action |
|---|---|
| Detect | Identify secret type, location, exposure window, and impacted service. |
| Contain | Revoke/rotate credential with provider; disable compromised automation if needed. |
| Assess | Inspect logs and access history; identify data or systems affected. |
| Remediate | Remove unsafe copies and fix the source of exposure. History rewriting may require a separate coordinated operation. |
| Verify | Test replacement credential and confirm old credential fails. |
| Record | Document timeline, impact, and follow-up without reproducing the secret. |

## 🔒 Contact data handling

Use synthetic names and phone numbers in screenshots, test data, issues, and documentation examples. Redact contact exports and notes.

## 🔗 Related

[Security overview](security.md) · [Threat model](threat-model.md) · [Privacy](privacy.md)