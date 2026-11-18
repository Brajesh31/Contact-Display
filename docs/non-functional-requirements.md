# ⚙️ Non-functional Requirements

The following are quality requirements and verification targets, not claims that the application has been certified against them.

| Area | Requirement / target | Verification |
|---|---|---|
| Usability | Main contact actions should be understandable and discoverable. | Task-based review. |
| Responsiveness | List and detail UI should remain usable at common viewport widths. | Manual viewport checks. |
| Accessibility | Target WCAG 2.2 AA where applicable. | Keyboard, screen reader, and contrast audit. |
| Privacy | Contact data should not be unnecessarily sent to external services. | Network inspection and source review. |
| Data durability | Explain browser storage scope and user-controlled clearing. | Reload and browser storage tests. |
| Performance | Search and list rendering should remain responsive for expected local datasets. | Browser profiling with representative datasets. |
| Maintainability | Route modules and data helpers should have documented responsibilities. | Code review. |
| Compatibility | Support should be stated only after testing specific browsers. | Browser matrix. |
| Security | Avoid displaying or logging sensitive contact values unnecessarily. | Static review and privacy testing. |

## 📏 Measurement policy

Do not publish numerical performance thresholds, availability targets, test coverage, or WCAG conformance results until they have been measured and recorded with evidence.
