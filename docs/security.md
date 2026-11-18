# 🛡️ Security Overview and Engineering Guidance

## 📌 Current security boundary

The inspected application is a client-side React application. Contact records are stored through localForage in browser-managed storage. The repository does not establish an application server, server-side authentication, remote database, API authorization, or centralized secrets service.

Browser-local data is not protected by server-side access controls. Anyone using the same unlocked browser profile may be able to access records.

## 🧭 Assets and trust boundaries

| Asset | Boundary | Security consideration |
|---|---|---|
| Contact names and phone numbers | Browser profile | Personal data stored locally. |
| Contact notes | Browser profile | Free-form text may contain sensitive details. |
| Avatar URLs | Third-party network boundary | May trigger requests to external hosts. |
| Website values | Navigation boundary | Destination and URL handling should be reviewed. |
| Source repository | GitHub | Protect branch, review, and dependency integrity. |

## ⚠️ Threat scenarios

| Threat | Potential impact | Practical mitigation/review |
|---|---|---|
| Shared-device access | Exposure of stored contacts. | Use trusted devices and lock profiles. |
| Malformed field input | Unexpected rendering or navigation. | Review rendering and URL handling. |
| Sensitive issue screenshots | Public disclosure. | Use synthetic data and redact evidence. |
| Compromised dependency | Malicious code in browser context. | Review alerts through separate authorized dependency work. |
| External avatar tracking | Third-party visibility of requests. | Prefer trusted image sources. |
| Accidental repository secret | Credential exposure. | Keep secrets out of Git and enable appropriate scanning. |

## 🔐 Security practices

1. Do not commit credentials, access tokens, or personal contact exports.
2. Do not put real contact data in demos, screenshots, bug reports, or fixtures.
3. Preserve the npm lockfile during documentation work; dependency changes need separate authorization.
4. Review user-controlled URL values and external navigation destinations.
5. Avoid logging contact values, notes, or browser storage contents.
6. Apply least-privilege permissions to GitHub Actions.
7. Pin workflow actions to reviewed immutable versions where practical.
8. Treat client-side validation as usability support, not a security boundary.

## 🚨 Vulnerability reporting

Use GitHub's private **Report a vulnerability** option when enabled. Include affected commit, impact, reproducible steps, and sanitized evidence. Do not publish exploit details or personal contact records in public issues.

## 🧪 Verification checklist

- [ ] No credentials or personal data committed.
- [ ] Dependency alerts reviewed.
- [ ] External-link and URL input behavior reviewed.
- [ ] Contact data omitted from logs/screenshots.
- [ ] Workflow permissions are minimal.
- [ ] Findings have owners and remediation status.

## 📚 Related documents

- [Threat model](threat-model.md)
- [Privacy](privacy.md)
- [Secret management](secret-management.md)
- [Dependency security](dependency-security.md)
- [Security reporting policy](../SECURITY.md)

> Static source review is not a security audit. No certification or scan result is claimed.
