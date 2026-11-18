# 🛡️ Threat Model

## 🎯 Assets
Contact names, phone numbers, websites, avatar references, notes, and browser storage records.

## 👤 Actors
| Actor | Capability |
|---|---|
| Legitimate user | Adds, reads, edits, deletes local records. |
| Shared-profile user | May access data in the same unlocked browser profile. |
| External resource | Can receive requests when a stored URL is loaded or followed. |
| Dependency publisher/attacker | May affect the application if a dependency is compromised. |

## Threat scenarios
| ID | Scenario | Impact | Mitigation |
|---|---|---|---|
| T-01 | Shared device exposes contacts. | Privacy loss. | Use protected browser profile; avoid sensitive content. |
| T-02 | User clears origin storage. | Data loss. | Explain local-only persistence; keep an independent backup. |
| T-03 | Untrusted URL entered. | External request/navigation. | Treat URL fields as untrusted. |
| T-04 | Dependency compromise. | Client code compromise. | Review dependencies and lockfile changes. |
| T-05 | Unredacted support screenshot. | Personal data disclosure. | Redact before attaching. |

There is no server identity or authorization boundary evidenced by the inspected code. A client-only model cannot provide server-enforced confidentiality, multi-user controls, or remote backup.
