# 🌳 Component Hierarchy

```mermaid
flowchart TD
    Mount[ReactDOM.createRoot] --> Strict[React.StrictMode]
    Strict --> Provider[RouterProvider]
    Provider --> Root[Root]
    Root --> Sidebar[Sidebar and search]
    Root --> Outlet[Outlet]
    Outlet --> Index[Index]
    Outlet --> Contact[Contact]
    Contact --> Favorite[Favorite]
    Outlet --> Edit[EditContact]
    Provider --> Error[ErrorPage]
```

| Component | Responsibility |
|---|---|
| Root | Shared app shell and contact navigation. |
| Index | Initial route content. |
| Contact | Contact detail and actions. |
| Favorite | Favorite state submission UI. |
| EditContact | Contact edit fields and save/cancel. |
| ErrorPage | Router error presentation. |

See [component architecture](../component-architecture.md) for the detailed inventory.
