# 🧭 Route and UI State Model

## 📌 Purpose

Describe the client-side route graph and interaction states configured in `src/main.jsx` and implemented by route modules.

## 🗺️ Route hierarchy

```mermaid
flowchart TD
  R["Browser router"] --> Root["/ · Root layout"]
  Root --> Index["Index route · /"]
  Root --> Contact["contacts/:contactId"]
  Contact --> Edit["contacts/:contactId/edit"]
  Contact --> Destroy["contacts/:contactId/destroy · action route"]
```

## 🔁 Route loader sequence

```mermaid
sequenceDiagram
  participant B as Browser
  participant R as React Router
  participant M as Route module
  participant D as contacts.js
  participant S as localForage
  B->>R: Navigate to route
  R->>M: Run matching loader
  M->>D: Request contact data
  D->>S: Read contacts collection
  S-->>D: Stored records
  D-->>M: Contact result
  M-->>R: Loader data or route error
  R-->>B: Render matching route
```

## 📊 State catalog

| State | Trigger | Expected UI | Source |
|---|---|---|---|
| Populated contact list | Collection contains records. | Sidebar lists records. | `root.jsx` |
| Empty contact list | No saved records. | “No contacts” message. | `root.jsx` |
| Search pending | Router navigates with `q`. | Loading class/spinner state. | `root.jsx` |
| Contact selected | Contact URL resolves. | Details panel renders. | `contact.jsx` |
| Contact missing | Loader cannot find ID. | 404 route error. | `contact.jsx` |
| Edit form | Edit URL resolves. | Form fields use stored values. | `edit.jsx` |
| Favorite pending | Fetcher has submitted form data. | Button reflects pending favorite value. | `contact.jsx` |
| Delete confirmation | User submits delete form. | Browser confirmation dialog. | `contact.jsx` |
| Delete complete | Destroy action redirects. | Navigate to root. | `destroy.jsx` |

## 🔒 State ownership

- React Router manages navigation and loader/action state.
- React renders components.
- localForage stores contact records under the `contacts` key.
- No server session, remote synchronization, or centralized state service is established by inspected implementation.

## ⚠️ Source finding

The root route has seed-card initialization calls and identifiers that are inconsistent in the currently inspected source. See [known issues](../known-issues.md). This document does not modify or claim to repair that behavior.
