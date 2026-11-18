# 🧰 Technical Overview

## 🏛️ Runtime model

The repository contains a client-side React application built by Vite. `src/main.jsx` creates a React Router browser router, registers the root/index/contact/edit/destroy routes, and mounts the router into the HTML root element.

## 🧩 Main layers

| Layer | Technology/module | Responsibility |
|---|---|---|
| Entry | `index.html`, `src/main.jsx` | Load and mount the app. |
| UI/routing | React 18, React Router DOM 6 | Render nested routes and manage loaders/actions/navigation. |
| Route modules | `src/routes/*.jsx` | List/search, detail, edit, and delete interactions. |
| Data helpers | `src/contacts.js` | Contact CRUD, matching, sorting, and storage calls. |
| Persistence | localForage | Browser-managed contact collection. |
| Build/dev | Vite 5 | Local development and production bundle. |

## 🔄 Main request lifecycle

1. Browser loads the Vite HTML entry.
2. React mounts the router.
3. React Router matches the current URL and runs a loader if configured.
4. Route code calls a contact helper.
5. The helper reads or updates localForage.
6. Router renders the route or follows a returned redirect/error.

## 🔒 Architecture boundaries

No server process, remote API, database server, user identity provider, or cloud synchronization service is established by the inspected source. See [architecture](architecture.md), [data architecture](architecture/data-architecture.md), and [project structure](project-structure.md).
