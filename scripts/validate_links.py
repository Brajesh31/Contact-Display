#!/usr/bin/env python3
"""Check relative Markdown links and local image targets."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?[[^]]*](([^)]+))")
FENCED_RE = re.compile(r"(?s)```.*?```")
INLINE_RE = re.compile(r"`[^`]*`")

def main() -> int:
    failures, checked = [], 0
    for markdown in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in markdown.parts):
            continue
        source = markdown.read_text(encoding="utf-8")
        source = INLINE_RE.sub("", FENCED_RE.sub("", source))
        for raw in LINK_RE.findall(source):
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
