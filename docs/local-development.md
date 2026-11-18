# 💻 Local Development

```mermaid
flowchart TD
    A[Clone repository] --> B[npm ci]
    B --> C[npm run dev]
    C --> D[Explore routes]
    D --> E[Review source and docs]
    E --> F[npm run lint]
    F --> G[npm run build]
```

Use [commands reference](commands-reference.md) for the package scripts. Keep development-only data private and do not commit local browser exports or credentials.

Documentation maintenance must not change application modules, package files, lockfiles, or build configuration.
