# 🔐 Application Security Guide

## 🧭 Security posture
This is a browser-side contact application in the inspected source. Browser storage is controlled by the user and is not a secure vault or authoritative database.

| Threat | Context | Guidance |
|---|---|---|
| Shared-device exposure | Browser profile may be shared. | Avoid sensitive records; protect the profile. |
| Site-data deletion | Browser storage can be cleared. | Maintain independent backups if needed. |
| Malicious avatar URL | Contact record may store remote image URL. | Use trusted URLs and review requests. |
| Malicious website URL | Stored URL is rendered as a link. | Treat values as untrusted. |
| Dependency compromise | npm and vendor assets are supply-chain inputs. | Review advisories and notices. |
| Sensitive issue attachments | Logs/screenshots may contain contacts. | Redact before publishing. |

No application-server authentication, authorization, or server-side validation layer was found in the inspected project. This guide is not a security audit or certification.
