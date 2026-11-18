#!/usr/bin/env python3
"""Validate required documentation files without modifying the repository."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md",
    "docs/README.md", "docs/architecture.md", "docs/project-structure.md",
    "docs/page-documentation.md", "docs/data-flow.md", "docs/testing.md",
    "docs/deployment.md", "docs/privacy.md", "docs/known-issues.md",
    "docs/assets/README.md", "docs/templates/README.md",
]

def main() -> int:
    missing, empty = [], []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file():
            missing.append(relative)
        elif path.stat().st_size == 0:
            empty.append(relative)
    if missing or empty:
        for label, items in (("Missing", missing), ("Empty", empty)):
            if items:
                print(f"{label} documentation files:")
                for item in items:
                    print(f"  - {item}")
        return 1
    print(f"Documentation file check passed ({len(REQUIRED)} required files).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
