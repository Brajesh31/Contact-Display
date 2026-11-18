# 🧱 Module Responsibilities

| Module | Public exports / role | Collaborators | Notes |
|---|---|---|---|
| `src/main.jsx` | Creates browser router and React root. | React, React DOM, React Router, route modules. | Application entry point. |
| `src/contacts.js` | `getContacts`, `createContact`, `getContact`, `updateContact`, `deleteContact`. | localForage, match-sorter, sort-by. | Primary data helper imported by routes. |
| `src/routes/root.jsx` | Root component, loader, action. | Contact helpers, React Router. | Sidebar, search, create flow. |
| `src/routes/index.jsx` | Index component. | None beyond React rendering. | Root index content. |
| `src/routes/contact.jsx` | Contact component, loader, action, Favorite component. | Contact helpers, React Router. | Detail and favorite workflow. |
| `src/routes/edit.jsx` | Edit component, loader, action. | Contact helpers, React Router. | Edit submission and redirect. |
| `src/routes/destroy.jsx` | Delete action. | Contact delete helper, redirect. | Action-only route. |
| `src/error.jsx` | Error UI component. | React Router error hook. | Displays route errors. |
| `src/contacts2.js` | Additional helper file in repository. | Inspect separately if used. | Primary router imports `contacts.js`, not this file. |

This is a static module inventory; verify exports against the branch before relying on it after source changes.
