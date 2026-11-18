# 🧩 Component Architecture

## 🏛️ Route/component structure

```mermaid
flowchart TD
  Main["src/main.jsx"] --> Router["createBrowserRouter"]
  Router --> Root["Root layout"]
  Root --> Index["Index route"]
  Root --> Contact["Contact route"]
  Root --> Edit["Edit contact route"]
  Root --> Destroy["Destroy action route"]
  Contact --> Favorite["Favorite component"]
  Root --> Sidebar["Sidebar, search, contact links"]
  Root --> Outlet["Nested route outlet"]
```

## 📚 Responsibilities

| Component/module | Responsibility |
|---|---|
| `Root` | Shared sidebar and nested content layout. |
| `Index` | Root selection/welcome state. |
| `Contact` | Contact details and action controls. |
| `Favorite` | Fetcher-driven favorite toggle control. |
| `EditContact` | Contact edit form. |
| `ErrorPage` | Router error display. |
| `destroyAction` | Delete mutation route action. |

## 🔒 Component boundaries

The router uses route modules as UI/data boundaries. Contact persistence logic lives in `src/contacts.js` rather than being implemented independently in each route. This page documents the current arrangement; it does not propose a component refactor.
