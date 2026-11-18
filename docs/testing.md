# 🧪 Testing and Quality

## Existing package scripts
| Check | Command | Configuration |
|---|---|---|
| Lint | `npm run lint` | ESLint script declared. |
| Build | `npm run build` | Vite build declared. |
| Preview | `npm run preview` | Vite preview declared. |

No test runner or test script was found in the inspected root manifest.

## Suggested manual cases
| ID | Scenario | Expected result |
|---|---|---|
| T-01 | Open root with empty storage. | Empty state, assuming loader succeeds. |
| T-02 | Create a contact. | Record created and edit route opened. |
| T-03 | Save edit. | Record updated and detail opened. |
| T-04 | Search first/last name. | Matching contacts displayed. |
| T-05 | Toggle favorite and reload. | Favorite persists. |
| T-06 | Open unknown ID. | 404 route error. |
| T-07 | Cancel delete confirmation. | Record remains. |
| T-08 | Confirm deletion. | Record removed; root opens. |
| T-09 | Reload after save. | Record remains in same browser origin/profile. |

Record commit, browser, OS, command, exit code, and sanitized evidence.
