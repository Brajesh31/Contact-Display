# 🕊️ Privacy and Data Handling

## 📌 Data the application can store
Names, phone numbers, websites, avatar URLs, and free-form notes.

## 💾 Storage
The inspected data helper uses localForage and the `contacts` key. This is browser-managed storage associated with the current browser profile and origin.

## Practical implications
- Other people with access to the same browser profile may see records.
- Clearing site data may remove contacts.
- Different profiles or origins do not automatically share records.
- No cloud backup or cross-device synchronization was found.
- External avatar/website values may cause external requests or navigation.

Avoid highly sensitive information. Redact data from screenshots, logs, and support tickets. This is a technical privacy note, not a legal policy or compliance certification.
