# ⚠️ Known Issues and Source Review Notes

These items were found by static source inspection. They are not claims that a live runtime test reproduced each issue. Application code remains untouched.

| ID | Location | Observation | Potential impact | Next step |
|---|---|---|---|---|
| K-01 | `src/routes/root.jsx` | Calls `createhussainCard()`, while visible helper is named `createBrajeshCard()` and is not exported. | Root loader/effect may fail with unresolved reference. | Reproduce separately; authorize code fix if required. |
| K-02 | `src/routes/root.jsx` | Helper references `BrajeshContactCard.id`, which is not declared in the visible helper. | Initialization path may fail. | Confirm intended seed-card logic. |
| K-03 | `src/routes/root.jsx` | Hussain/Brajesh storage key and variable names are inconsistent. | Seed-card identity may not be stable. | Establish intended behavior. |
| K-04 | `src/contacts.js` | Delete helper dereferences `contacts[index]` before verifying index. | Empty collection or unknown ID may throw. | Add edge-case tests in separate approved fix. |
| K-05 | `src/contacts.js` | Update helper assumes stored collection exists before `find`. | Missing storage may throw. | Define missing-storage behavior. |
| K-06 | `src/contacts2.js` | Duplicates data helper logic but application entry imports `contacts.js`. | Source-of-truth ambiguity. | Confirm whether intentionally retained. |
| K-07 | Former README | MERN, MongoDB, REST APIs and client/server setup were not found in inspected root tree. | Misleading installation/architecture. | Corrected in README. |
| K-08 | Existing update-readme workflow | Hourly scheduled write-enabled workflow updates README. | Automatic commit churn. | Preserved; review separately if desired. |

Do not mark any source concern resolved until a separate authorized change is implemented and verified.
