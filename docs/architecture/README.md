# 🏛️ Architecture Diagram Catalog

This directory contains editable, project-specific diagrams. Mermaid source is embedded in Markdown documents; SVG illustrations are maintained alongside the guides.

| Diagram | Source / asset | Explains |
|---|---|---|
| System context | [Architecture guide](../architecture.md) | Browser, React app, router, data module, browser storage. |
| Runtime route map | [System design](../system-design.md) | Route registration and child route actions. |
| Component hierarchy | [Component architecture](../component-architecture.md) | Root shell and child screens. |
| Data architecture | [Data architecture](data-architecture.md) and SVG | localForage-based data boundary. |
| Data flow | [Data flow](../data-flow.md) and SVG | Contact read/write operations. |
| Sequence flow | [Sequence flows](sequence-flows.md) and SVG | Browser-to-storage interaction. |
| Deployment view | [Deployment view](deployment-view.md) and SVG | Static Vite build path. |
| Security view | [Security view](security-view.md) and SVG | Client trust boundaries. |

## 🧰 Editing rules

1. Keep diagrams aligned with source behavior.
2. Prefer readable labels and directionally clear flows.
3. Do not add unimplemented databases, APIs, services, or authentication providers.
4. Validate SVG XML after edits.
5. Update this catalog when a diagram is added or removed.
