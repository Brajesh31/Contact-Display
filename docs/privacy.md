# 🔐 Privacy and Contact Data Handling

## 📌 Scope

Contact Display stores contact records in browser-managed storage through localForage. The inspected implementation uses the `contacts` key. This is practical product guidance, not a legal privacy notice or compliance certification.

## 🗃️ Data inventory

| Field | Observed use | Privacy consideration |
|---|---|---|
| `first`, `last` | Contact name. | Personal information. |
| `number` | Phone number. | Personal information; do not publish. |
| `website` | Website string. | May identify a person or organization. |
| `avatar` | Avatar URL. | May trigger third-party image requests. |
| `notes` | Free-form notes. | May contain sensitive details; minimize. |
| `favorite` | Favorite marker. | User preference data. |
| `id`, `createdAt` | Record identity and timestamp. | Associated metadata. |

## 🧭 Storage and data boundaries

- Records are read and written through localForage.
- The inspected implementation does not establish remote synchronization, user accounts, a centralized server database, or cloud backup.
- Browser storage is scoped to site origin and browser profile.
- Clearing browser/site data may remove locally stored records.
- Another person with access to the same unlocked browser profile may access records.
- External avatar URLs may trigger requests to third-party hosts.

## ✅ User guidance

1. Store only information needed for the contact-management task.
2. Do not put passwords, payment details, government identifiers, or highly sensitive records in notes.
3. Protect the device and browser profile.
4. Avoid shared/public computers for personal contact records.
5. Replace real records with synthetic examples before sharing screenshots, logs, or issue reports.
6. Understand that clearing browser data may remove locally stored records.

## 🧹 Retention and deletion

The application exposes per-contact deletion. The inspected implementation does not establish automated retention, bulk export, secure-erasure guarantees, or backup. Do not rely on browser storage as the only copy of important contacts.

## 🛡️ Privacy-by-design checklist

- [ ] Minimize stored information.
- [ ] Avoid sensitive free-form notes.
- [ ] Use synthetic records in tests and screenshots.
- [ ] Review external avatar requests and website navigation.
- [ ] Explain browser-local storage limitations.
- [ ] Test deletion for valid, missing, and empty datasets.
- [ ] Avoid logging contact values or storage contents.

## ⚖️ Compliance note

No privacy certification or legal compliance status is asserted. A formal notice requires review of deployment, data flows, jurisdiction, and applicable legal obligations.
