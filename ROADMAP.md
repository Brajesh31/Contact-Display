# 🛣️ Roadmap

This roadmap separates current implementation from possible future work. Entries below are proposals, not claims that the features already exist.

## ✅ Current documented baseline

- React 18 interface with Vite.
- React Router data-router route definitions.
- Contact list, search, detail, create, edit, favorite, and delete flows in the inspected source.
- Browser-side persistence through localForage.

## 🔭 Potential improvements

| Priority | Proposal | Rationale | Status |
|---|---|---|---|
| High | Repair and verify the default contact initialization path | The inspected root route references a helper name that is not defined in the same module. | Proposed, not implemented |
| High | Review contact delete edge cases | The existing delete helper should be checked for empty/missing records before use. | Proposed, not implemented |
| Medium | Add automated route and data-helper tests | Improve regression confidence. | Proposed, not implemented |
| Medium | Add documented export/import workflow | Give users a portable backup path if implemented. | Proposed, not implemented |
| Medium | Perform a keyboard and screen-reader audit | Establish accessibility baseline. | Proposed, not implemented |
| Low | Capture genuine desktop and mobile screenshots | Improve visual documentation. | Awaiting real application capture |
| Low | Add a privacy-focused data lifecycle guide | Explain local storage retention and clearing behavior. | Documentation in progress |

## 🚫 Out of scope for this documentation update

- Rewriting the application.
- Introducing a backend or database.
- Replacing the current router or storage layer.
- Changing dependencies or build behavior.

## 🧭 Prioritization

Priorities are indicative. Product-code work requires a separate explicit authorization and should be implemented in a focused change with tests.
