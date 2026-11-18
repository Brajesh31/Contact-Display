# 🧩 System Design

## 1. 🧭 Entry and routing design

The browser entry is `index.html`. Vite serves the project and loads `src/main.jsx`. The entry creates a browser router and mounts it through `RouterProvider` inside React Strict Mode.

## 2. 🔀 Route/action design

```mermaid
flowchart TD
    Start[index.html] --> Main[src/main.jsx]
    Main --> Router[createBrowserRouter]
    Router --> Root[/]
    Root --> List[Index element]
    Root --> Contact[/contacts/:contactId]
    Root --> Edit[/contacts/:contactId/edit]
    Root --> Destroy[/contacts/:contactId/destroy]
    Root --> Error[ErrorPage]
```

| Route | Loader | Action | Main responsibility |
|---|---|---|---|
| `/` | `rootLoader` | `rootAction` | Load and search records; create a record. |
| `/contacts/:contactId` | `contactLoader` | `contactAction` | Read details; update favorite. |
| `/contacts/:contactId/edit` | `editLoader` | `editAction` | Read and update fields. |
| `/contacts/:contactId/destroy` | None | `destroyAction` | Delete record. |

## 3. 💾 Data design

The shared data helper is `src/contacts.js`. It reads localForage key `contacts`, treats missing storage as an empty array in `getContacts`, filters by first/last name, and sorts results. Create/update/delete functions mutate the collection and persist it through localForage.

## 4. 🧱 UI composition

The root route renders a sidebar containing search and contact navigation, plus an `Outlet` for selected route content. Detail and edit screens render inside the outlet.

## 5. 🛡️ Error design

The router configures an application-level error element and route-level error handling. The contact loader throws a 404 response for an unknown record. The destroy route includes a local error element.

## 6. 🚫 Not part of this design

There is no verified backend service, REST contract, database server, authentication provider, queue, or external API integration in the inspected root project.
