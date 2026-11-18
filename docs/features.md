# ✨ Feature Inventory

This document catalogs behavior observed in the root application source. It does not treat README claims about a backend, MongoDB, REST services, or Tailwind as implemented features.

| ID | Feature | Entry point | Behavior | Status |
|---|---|---|---|---|
| F-01 | Contact list | `src/routes/root.jsx` | Loads and renders records in navigation. | Implemented in source |
| F-02 | Contact search | Root search form | Submits `q`; filters first/last names with match-sorter. | Implemented in source |
| F-03 | Create contact | Root route action | Creates a record and redirects to its edit route. | Implemented in source |
| F-04 | Contact details | `src/routes/contact.jsx` | Loads and displays a contact. | Implemented in source |
| F-05 | Favorite toggle | Contact route action and Favorite component | Updates the `favorite` field using a router fetcher form. | Implemented in source |
| F-06 | Edit contact | `src/routes/edit.jsx` | Submits form values to update helper and redirects to detail. | Implemented in source |
| F-07 | Delete contact | `src/routes/destroy.jsx` | Deletes by route parameter and redirects to root. | Implemented in source |
| F-08 | Error route UI | `src/error.jsx` | Displays route error details. | Implemented in source |
| F-09 | Browser persistence | `src/contacts.js` | Reads/writes the contacts collection via localForage. | Implemented in source |
| F-10 | Sorting | `src/contacts.js` | Sorts records by last name and creation time. | Implemented in source |

## 🧭 User-visible states

| State | Current behavior |
|---|---|
| Empty list | Shows a no-contacts message. |
| Search in progress | Adds loading presentation based on router navigation. |
| Selected contact | Displays details in the detail outlet. |
| Unknown contact | Contact loader throws a 404 response. |
| Delete confirmation | Browser `confirm()` is requested before submitting deletion. |
| Favorite | Star button displays favorite state. |

## 🧪 Acceptance criteria for documented workflows

1. Contact list route resolves and renders the current saved collection.
2. Search submits a query and returns matching first/last names.
3. Create flow reaches the edit route with the created record ID.
4. Contact detail route handles a missing record with a 404 response.
5. Edit action updates the record and returns to its detail route.
6. Favorite action persists the boolean-like form value.
7. Delete action removes a record and redirects to root.

These are behavior expectations based on source structure, not a statement that every flow currently passes at runtime. See [known issues](known-issues.md).
