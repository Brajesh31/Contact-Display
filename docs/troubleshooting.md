# 🧯 Troubleshooting

| Problem | Likely area | Safe next step |
|---|---|---|
| Contacts seem missing | Browser profile/origin or cleared site data | Check origin and browser storage before clearing anything. |
| Detail route returns not found | Contact ID absent | Return to list and open an existing record. |
| Search is unexpected | Search matches first/last names | Inspect record fields and query text. |
| Create flow fails | Root loader/action/initializer | Review browser console and [known issues](known-issues.md). |
| Delete flow errors | Delete helper assumptions | Preserve data and capture a sanitized reproduction. |
| npm command unavailable | Package scripts | Use commands listed in root package manifest. |

Do not clear browser storage as an initial troubleshooting step. It may contain the only copy of the contacts.
