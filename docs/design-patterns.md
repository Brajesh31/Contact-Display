# 🧠 Implementation Patterns Observed

| Pattern | Where observed | Why it is used |
|---|---|---|
| Route loader/action | React Router route modules. | Separate data reads and mutations from route rendering. |
| Nested layout route | Root route with nested children and outlet. | Keeps shared sidebar while rendering child views. |
| Fetcher form | Favorite control. | Submits an update without requiring full page navigation. |
| Data helper module | `src/contacts.js`. | Centralizes contact collection operations. |
| Browser-local persistence | localForage. | Persists records within the browser origin. |

## ⚠️ Notes

These are patterns visible in the implementation, not claims of strict adherence to a named architecture methodology. Avoid describing the codebase as clean architecture, hexagonal architecture, microservices, or MVC unless a fuller implementation review supports that characterization.
