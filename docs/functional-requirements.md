# 📋 Functional Requirements

| ID | Requirement | Source evidence | Verification idea |
|---|---|---|---|
| FR-01 | The application shall list stored contacts. | Root loader and contacts map. | Seed records and inspect root route. |
| FR-02 | The application shall search contacts by first and last name. | `matchSorter` keys. | Search exact and partial names. |
| FR-03 | The application shall create a contact record. | `createContact()`. | Submit the root New form. |
| FR-04 | A contact can be opened by its ID. | `contacts/:contactId` loader. | Open a valid record route. |
| FR-05 | A missing contact should produce a not-found response. | Contact loader. | Request a nonexistent ID. |
| FR-06 | A contact can be marked or unmarked as favorite. | Contact action and Favorite fetcher. | Toggle twice and reload. |
| FR-07 | Contact fields can be updated. | Edit route action. | Save updated field values. |
| FR-08 | A contact can be deleted. | Destroy route action. | Confirm deletion and verify removal. |
| FR-09 | Contact data should be persisted through the configured storage abstraction. | localForage data helper. | Reload and verify stored data. |

## 🧩 Data fields

See the observed contact field table in [product overview](product-overview.md). Additional fields may exist in locally stored records because the update helper merges arbitrary form values into the contact object.

## 🚫 Excluded requirements

The inspected source does not establish requirements for remote accounts, REST endpoints, MongoDB, payments, notifications, or cloud backups.
