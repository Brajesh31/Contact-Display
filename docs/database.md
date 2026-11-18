# 💾 Database and Persistence

No server database was found in the inspected root application. The contact helper uses localForage to read and write the `contacts` key in browser-managed storage.

| Characteristic | Current model |
|---|---|
| Location | Browser-managed storage for current origin/profile. |
| Access | localForage API. |
| Collection key | `contacts`. |
| Record identity | Generated `id` property. |
| Synchronization | No remote sync found. |
| Backup | No automated backup found. |
| Access control | No server authorization found. |

Do not describe this as MongoDB, SQL, or a shared cloud database.
