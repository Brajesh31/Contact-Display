# 🧭 User Journeys

## 1. ➕ Create and save a contact

```mermaid
flowchart TD
    A[Open contact list] --> B[Select New]
    B --> C[Create empty record]
    C --> D[Redirect to edit route]
    D --> E[Enter contact details]
    E --> F[Submit Save]
    F --> G[Update localForage record]
    G --> H[Redirect to contact detail]
```

## 2. 🔎 Find a contact

```mermaid
flowchart TD
    A[Open root route] --> B[Enter search text]
    B --> C[React Router submits search form]
    C --> D[Root loader reads q]
    D --> E[match-sorter checks first and last]
    E --> F[Render filtered contact list]
```

## 3. ⭐ Mark a contact as favorite

```mermaid
sequenceDiagram
    actor User
    participant UI as Favorite button
    participant Router as React Router fetcher
    participant Data as contacts.js
    participant Store as localForage
    User->>UI: Toggle star
    UI->>Router: Submit favorite value
    Router->>Data: updateContact(id, updates)
    Data->>Store: Persist updated contacts
    Store-->>UI: Updated contact state
```

## 4. 🗑️ Delete a contact

```mermaid
flowchart TD
    A[Open contact details] --> B[Select Delete]
    B --> C{Browser confirmation}
    C -->|Cancel| D[Keep current record]
    C -->|Confirm| E[Submit destroy action]
    E --> F[deleteContact]
    F --> G[Redirect to root]
```

## 🧪 Journey review

The diagrams represent the intended route/action sequence visible in the source. Run each journey in a browser before treating it as a verified end-to-end test. Known source inconsistencies are listed in [known issues](known-issues.md).
