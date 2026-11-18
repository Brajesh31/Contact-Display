# ⚠️ Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Browser storage cleared. | Medium | High | Explain local-only persistence; independent backup. |
| R-02 | Shared device exposes contacts. | Medium | High | Avoid sensitive data; protect browser profile. |
| R-03 | Initialization references inconsistent. | Unknown until runtime test | High | Reproduce and track separately. |
| R-04 | Delete helper fails on invalid/empty state. | Plausible from source | High | Add edge-case tests in approved code work. |
| R-05 | No automated test runner declared. | Confirmed in package scripts | Medium | Design test strategy separately. |
| R-06 | Vendored framework needs advisory review. | Unknown | Medium | Review upstream notices and advisories. |
| R-07 | Existing README timestamp workflow has write permission and hourly schedule. | Confirmed | Medium | Review schedule and permissions separately. |

Ratings are qualitative and should be updated when new evidence is available.
