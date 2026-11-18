# 🧑‍💻 Use Cases

| ID | Actor | Use case | Preconditions | Main outcome |
|---|---|---|---|---|
| UC-01 | User | Browse contacts | App opened in the same browser origin/profile. | Contact list rendered. |
| UC-02 | User | Search contacts | Contacts exist in browser storage. | Filtered list rendered. |
| UC-03 | User | Create contact | Root route available. | Empty record created and edit form opened. |
| UC-04 | User | View contact | Contact ID exists. | Contact detail shown. |
| UC-05 | User | Edit contact | Contact ID exists. | Updated record saved. |
| UC-06 | User | Toggle favorite | Contact ID exists. | Favorite flag changed. |
| UC-07 | User | Delete contact | Contact ID exists. | Record removed after confirmation. |
| UC-08 | User | Recover from missing record | Requested contact ID is invalid or absent. | Contact loader returns not-found response. |

## 🔍 UC-05: Edit contact

1. User selects a contact.
2. User opens its edit route.
3. Loader retrieves the contact.
4. Form displays current values.
5. User submits changes.
6. Action converts form entries to an object.
7. Data helper updates the stored record.
8. Router redirects to the contact detail route.

**Alternate path:** A missing or stale contact ID may cause the loader or data helper to fail. Error handling should be verified in the application.
