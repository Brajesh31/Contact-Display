#!/usr/bin/env python3
"""Parse documentation SVG files and check basic accessibility metadata."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "docs" / "assets"

def main() -> int:
    failures = []
    files = sorted(SVG_DIR.rglob("*.svg"))
    for path in files:
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            names = {element.tag.split("}")[-1] for element in root.iter()}
            if root.tag.split("}")[-1] != "svg":
                failures.append(f"{path.relative_to(ROOT)}: root is not svg")
            if "title" not in names or "desc" not in names:
                failures.append(f"{path.relative_to(ROOT)}: missing title or desc")
        except ET.ParseError as exc:
            failures.append(f"{path.relative_to(ROOT)}: invalid XML: {exc}")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"SVG validation passed ({len(files)} files).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
