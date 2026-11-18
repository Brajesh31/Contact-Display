# 🧪 Test Strategy

| Layer | Current status | Suggested scope |
|---|---|---|
| Unit | No test runner found in package manifest. | Test contact helper edge cases in an authorized test-only change. |
| Integration | Not configured in inspected manifest. | Test route actions with controlled storage. |
| End-to-end | Not configured in inspected manifest. | Test create/search/view/edit/favorite/delete flows. |
| Accessibility | Not verified. | Keyboard and assistive-tech review. |
| Performance | Not measured. | Profile list/search with representative local data. |
| Security | No audit evidence supplied. | Threat-focused manual checks and dependency review. |

Prioritize persistence operations, route boundaries, and destructive actions. Use synthetic data only.
