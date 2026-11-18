# 🧰 Technology Stack and Responsibilities

| Layer | Technology | Role | Evidence |
|---|---|---|---|
| UI | React 18 | Component-based rendering. | Root package manifest. |
| Routing | React Router DOM 6 | Browser routes, loaders/actions, forms. | `src/main.jsx`, route modules. |
| Build | Vite 5 | Development and production build. | `vite.config.js`, package manifest. |
| Persistence | localForage 1.10 | Browser-managed contact storage. | `src/contacts.js`. |
| Search | match-sorter | Match first/last contact names. | `src/contacts.js`. |
| Sorting | sort-by | Sort contact records. | `src/contacts.js`. |
| Styles | CSS and vendored Bootstrap assets | Application styling resources. | `src/index.css`, source tree. |
| Linting | ESLint 8 | Static code analysis. | Package scripts and config. |

## 🚫 Not established by inspected implementation

No Express application server, MongoDB instance, remote REST API, cloud database, server-side authentication, or cross-device sync was found in the inspected source overview. Do not add these technologies to project diagrams or claims without new evidence.
