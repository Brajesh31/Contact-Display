# 📚 Contact Display Documentation

Welcome to the engineering documentation for Contact Display. This documentation is based on the root application source inspected in the repository. It describes the current client-side implementation and identifies unknowns rather than assuming a server architecture.

## 🧭 Documentation map

| Area | Document | Purpose |
|---|---|---|
| Product | [Product overview](product-overview.md) | Purpose, users, scope, and behavior. |
| Features | [Features](features.md) | Verified feature inventory and requirements. |
| Architecture | [Architecture](architecture.md) | Runtime components and boundaries. |
| Design | [System design](system-design.md) | Routing, state, and persistence design. |
| Code | [Technical overview](technical-overview.md) | Source module responsibilities. |
| Lifecycle | [Application lifecycle](application-lifecycle.md) | Startup and route execution. |
| Components | [Component architecture](component-architecture.md) | UI composition. |
| Modules | [Module documentation](module-documentation.md) | Source-level module reference. |
| Dependencies | [Dependencies](dependencies.md) | Runtime and development dependencies. |
| Structure | [Project structure](project-structure.md) | Directory tree and file responsibilities. |
| Pages | [Page documentation](page-documentation.md) | Route-by-route behavior. |
| Data | [Data flow](data-flow.md) | Contact record lifecycle. |
| Development | [Developer guide](developer-guide.md) | Setup and commands. |
| Testing | [Testing](testing.md) | Existing checks and proposed test coverage. |
| Operations | [Deployment](deployment.md) | Static build and hosting guidance. |
| Security | [Security](security.md) | Threats and design limitations. |
| Accessibility | [Accessibility](accessibility.md) | Accessibility review checklist. |
| Privacy | [Privacy](privacy.md) | Browser storage and personal data. |
| Maintenance | [Maintenance](maintenance.md) | Maintenance and review process. |
| Risk | [Known issues](known-issues.md) | Verified observations and follow-up. |
| Templates | [Templates](templates/README.md) | Reusable engineering templates. |
| Architecture visuals | [Diagram catalog](architecture/README.md) | Editable diagrams and exports. |

## 🧪 Accuracy and status conventions

- **Implemented** means directly supported by inspected source.
- **Configured** means present in repository configuration, not necessarily verified in a live environment.
- **Proposed** means a suggested improvement that has not been implemented.
- **Unknown** means the available source does not establish the behavior.

## 🔒 Change boundary

Application source, package manifests, lockfiles, application styles, and build configuration are outside the scope of this documentation set. Refer to [contribution rules](../CONTRIBUTING.md) before proposing changes.
