# 🧱 Technical Debt Register

| ID | Area | Debt / uncertainty | Risk | Follow-up |
|---|---|---|---|---|
| TD-01 | Initialization | Default card helper references are inconsistent. | High: potential runtime failure. | Reproduce and propose focused fix. |
| TD-02 | Delete | Delete helper assumes collection/index exists. | High: destructive path can throw. | Add edge-case tests/fix separately. |
| TD-03 | Update | Update helper assumes collection exists. | Medium. | Define missing-storage behavior. |
| TD-04 | Duplicate module | Two contact helper files exist. | Medium. | Confirm usage before cleanup. |
| TD-05 | Documentation | Former README described unverified backend. | Medium. | Corrected in README. |
| TD-06 | Testing | No test script declared in root manifest. | Medium. | Propose test-only plan separately. |

No registered item is changed by this document. Source-level work requires explicit authorization.
