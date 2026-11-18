# 🔌 API Boundary

The inspected app uses React Router's client-side loaders and actions. These are not a public HTTP API.

```mermaid
flowchart LR
    Component[React component] --> Router[React Router action/loader]
    Router --> Helper[contacts.js]
    Helper --> Storage[localForage]
    Storage --> Browser[(Browser storage)]
```

No server route, controller, REST endpoint, API authentication middleware, or remote API service was identified in the root application files.
