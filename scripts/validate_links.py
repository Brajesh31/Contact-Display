#!/usr/bin/env python3
"""Check repository-owned Markdown links without altering application assets.

Third-party vendored documentation inside src/ is intentionally excluded.
Only relative paths are checked; external URLs are not fetched.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "node_modules", "src", "public"}
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
REFERENCE_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
FENCED_RE = re.compile(r"(?s)^\s*(```+|~~~+).*?^\s*\1\s*$", re.MULTILINE)
INLINE_RE = re.compile(r"`[^`]*`")

def main() -> int:
    failures, checked = [], 0
    markdown_files = sorted(ROOT.rglob("*.md"))
    for markdown in markdown_files:
        relative = markdown.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        source = markdown.read_text(encoding="utf-8")
        source = FENCED_RE.sub("", source)
        source = INLINE_RE.sub("", source)
        targets = LINK_RE.findall(source) + REFERENCE_RE.findall(source)
        for raw in targets:
            target = raw.strip().split()[0].strip("<>")
            if "{{" in target or "}}" in target:
                continue
            parsed = urlparse(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            part = unquote(parsed.path)
            if not part:
                continue
            if part.startswith("/"):
                candidate = (ROOT / part.lstrip("/")).resolve()
            else:
                candidate = (markdown.parent / part).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                failures.append(f"{relative}: link escapes repository: {target}")
                continue
            checked += 1
            if not candidate.exists():
                failures.append(f"{relative}: missing target: {target}")
    if failures:
        print("\n".join(failures))
        print(f"Found {len(failures)} broken local link(s) across {checked} checked.")
        return 1
    print(f"Repository Markdown links passed ({checked} checked; vendored src/public content excluded).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
