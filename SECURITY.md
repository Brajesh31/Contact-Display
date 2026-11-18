# 🔐 Security Policy

## 📌 Scope

Contact Display is a browser-side React application. The inspected implementation uses localForage for browser-managed persistence and does not include an application server, remote database, or server-side authentication layer in the root project.

## ✅ Supported versions

| Version | Security support |
|---|---|
| Current default branch | Best-effort review of responsibly reported issues. |
| Older snapshots | No separate support commitment is stated. |

## 📣 Reporting a vulnerability

Please do not publish exploitable details, private contact records, browser storage exports, or credentials in a public issue.

Use GitHub's private vulnerability reporting feature if enabled for this repository. Otherwise, contact the maintainer through [GitHub](https://github.com/Brajesh31) and request a private disclosure channel.

Include:
- A concise vulnerability description.
- Affected route, component, or dependency.
- Reproduction steps or a minimal proof of concept.
- Impact and realistic attack preconditions.
- Suggested mitigation, if known.

## 🧭 Response expectations

The maintainer will assess reports, request clarification where necessary, determine affected versions, and coordinate a fix or mitigation. No fixed response-time SLA is claimed by this policy.

## 🛡️ Security considerations in the current design

| Area | Observed design / guidance |
|---|---|
| Persistence | Contact records are stored in browser-managed storage through localForage. Treat the browser profile as user-controlled. |
| Authentication | No server-side authentication mechanism was found in the inspected root application. |
| Authorization | No server-side role or permission model was found. |
| Transport | No project API transport layer was found in the inspected application modules. |
| Personal data | Names, phone numbers, websites, notes, and avatar URLs can be entered. Avoid storing highly sensitive information. |
| Dependencies | Review npm dependencies and the vendored Bootstrap distribution during maintenance. |
| Logging | Avoid adding real contact details to logs or issue reports. |

## 🔄 Maintainer checklist

1. Reproduce and classify the report.
2. Identify affected source paths and dependencies.
3. Assess whether private contact data can be exposed or altered.
4. Prepare a minimal mitigation.
5. Verify the mitigation without disclosing sensitive data.
6. Publish an advisory or release note when appropriate.

## ⚠️ Limitations

This document is not a security audit or certification. No penetration test, dependency audit, or independent review is claimed by adding this file.
