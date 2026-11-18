# 🛠️ Documentation Validation Scripts

These scripts validate repository documentation and visual assets. They do not modify application source, dependencies, build configuration, or project behavior.

| Script | Purpose | Exit behavior |
|---|---|---|
| `validate_docs.py` | Check required documentation files exist and are non-empty. | Non-zero when required files are missing or empty. |
| `validate_links.py` | Check relative Markdown links and local image references. | Non-zero when broken local targets are found. |
| `validate_svg.py` | Parse SVG files as XML and check accessible title/description metadata. | Non-zero on malformed SVG. |

## ▶️ Run locally
```bash
python scripts/validate_docs.py
python scripts/validate_links.py
python scripts/validate_svg.py
```

Python 3 standard library is sufficient. Scripts do not fetch external URLs or send repository data over the network.

## ⚠️ Limitations
- Markdown parsing is intentionally lightweight.
- Mermaid syntax is not compiled by these scripts.
- External link availability is not tested.
- Screenshot authenticity requires human review.
