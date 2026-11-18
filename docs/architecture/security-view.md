# 🛡️ Security Architecture View

```mermaid
flowchart TD
    User[User] --> Browser[Browser profile]
    Browser --> UI[React application]
    UI --> Router[React Router]
    Router --> Helpers[Client data helpers]
    Helpers --> Storage[(Browser storage)]
    UI --> External[External avatar / website URLs]
    External -. third-party request/navigation .-> Internet[External web]
```

## 🔐 Boundaries and controls

| Boundary | Security meaning |
|---|---|
| Browser profile | User/device access controls govern stored contact visibility. |
| Application UI | Client code can be inspected or modified by the user. |
| Browser storage | Not a server-side security boundary. |
| External URLs | Values are user-provided and can point outside the application. |

There is no verified backend authentication, authorization, or server firewall layer in the inspected source. See [threat model](../threat-model.md).
