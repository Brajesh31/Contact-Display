# 🔐 Security Policy

## 📌 Scope
Contact Display is a browser-side React application. The inspected implementation uses localForage for browser-managed persistence and does not include an application server, remote database, or server-side authentication layer in the root project.

## ✅ Supported versions
| Version | Security support |
|---|---|
| Current default branch | Best-effort review of responsibly reported issues. |
| Older snapshots | No separate support commitment is stated. |

## 📣 Reporting
Do not publish exploitable details, private contact records, browser-storage exports, or credentials in a public issue.

Use GitHub private vulnerability reporting if enabled. Otherwise, contact the maintainer through [GitHub](https://github.com/Brajesh31) and request a private disclosure channel.

Include a concise description, affected route/dependency, reproduction steps, realistic impact, and suggested mitigation. Redact all personal information.

## 🧭 Response process
The maintainer will assess the report, request clarification if required, identify affected versions, and coordinate a mitigation or fix. No fixed response-time SLA is claimed.

## 🛡️ Security considerations
| Area | Observed design / guidance |
|---|---|
| Persistence | Contact records are browser-managed. Treat the profile as user-controlled. |
| Authentication | No server-side authentication found in inspected root app. |
| Authorization | No server-side role/permission model found. |
| Personal data | Names, phone numbers, notes, avatar URLs may be entered. Avoid highly sensitive data. |
| Dependencies | Review npm packages and vendored Bootstrap notices/advisories. |
| Logging | Do not log credentials or private contact values. |

## 🔄 Maintainer checklist
1. Reproduce and classify.
2. Identify affected code/dependencies.
3. Assess confidentiality/integrity impact.
4. Prepare minimal mitigation.
5. Verify without exposing personal data.
6. Publish an advisory or release note when appropriate.

This policy is not a security audit or certification.
