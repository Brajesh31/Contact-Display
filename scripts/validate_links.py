#!/usr/bin/env python3
"""Validate relative Markdown links and local image targets.

This read-only check skips fenced code blocks and inline code so examples do
not create false positives. It does not make network requests.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
REFERENCE_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
FENCED_RE = re.compile(r"(?s)^\s*(```+|~~~+).*?^\s*\1\s*$", re.MULTILINE)
INLINE_RE = re.compile(r"`[^`]*`")

def main() -> int:
    failures, checked = [], 0
    for markdown in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in markdown.parts):
            continue
        source = markdown.read_text(encoding="utf-8")
        source = FENCED_RE.sub("", source)
        source = INLINE_RE.sub("", source)
        targets = LINK_RE.findall(source) + REFERENCE_RE.findall(source)
        for raw in targets:
            target = raw.strip().split()[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            part = unquote(parsed.path)
            if not part:
                continue
            candidate = (markdown.parent / part).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                failures.append(f"{markdown.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            checked += 1
            if not candidate.exists():
                failures.append(f"{markdown.relative_to(ROOT)}: missing target: {target}")
    if failures:
        print("\n".join(failures))
        print(f"Found {len(failures)} broken local link(s) across {checked} checked.")
        return 1
    print(f"Local Markdown links passed ({checked} checked).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
