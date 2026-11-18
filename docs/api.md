# 🔌 API Documentation

## Current status
The inspected root project does not define an HTTP API server or route handlers. React Router loaders/actions are in-process application data operations, not public REST endpoints.

| Interface | Type | Purpose |
|---|---|---|
| Root loader/action | React Router APIs | Read/search and create contacts. |
| Contact loader/action | React Router APIs | Read contact and update favorite. |
| Edit loader/action | React Router APIs | Read and update contact. |
| Destroy action | React Router API | Delete contact. |
| localForage | Browser storage library | Persist local contact records. |

No verified HTTP methods, API URLs, auth headers, or JSON response contracts are present to document.
