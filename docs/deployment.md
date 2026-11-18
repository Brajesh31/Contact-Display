# 🚀 Deployment

The configured build command is `npm run build`, using Vite. The default output is `dist/`.

```mermaid
flowchart TD
    Source[Git repository] --> Install[npm ci]
    Install --> Build[npm run build]
    Build --> Artifact[dist static artifact]
    Artifact --> Host[Static hosting]
    Host --> User[Browser]
```

## Hosting considerations
- Configure the host to serve the app entry for supported client-side routes.
- Verify browser refresh on nested contact routes.
- Use HTTPS.
- Keep a stable origin because browser storage is origin-scoped.
- Do not assume a backend/database is part of the current app.

No live provider, production URL, or deployed build verification was established during inspection.
