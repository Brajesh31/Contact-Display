# 🚀 Deployment View

## Current build path
```mermaid
flowchart TD
    Repo[Git repository] --> Install[npm ci]
    Install --> Build[npm run build]
    Build --> Dist[dist static output]
    Dist --> Host[Static web hosting]
    Host --> Browser[User browser]
```

| Deployment unit | Current evidence |
|---|---|
| Static client bundle | Vite build script. |
| Server API | Not found in inspected root project. |
| Database server | Not found in inspected root project. |
| Hosting provider / CDN | Not established. |
| Secrets service | Not established. |

Static hosting must serve the app entry for supported client routes. Browser persistence is origin-scoped. No live hosting provider is claimed.
