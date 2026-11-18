# 🧭 Navigation Structure

```mermaid
flowchart TD
    Home["/"] --> Detail["/contacts/:contactId"]
    Detail --> Edit["/contacts/:contactId/edit"]
    Detail --> Delete["/contacts/:contactId/destroy (action)"]
    Edit --> Detail
    Delete --> Home
```

The sidebar title returns to root, contact links open detail routes, Edit opens the edit route, Save redirects to detail, Delete redirects to root, and Cancel uses browser history.
