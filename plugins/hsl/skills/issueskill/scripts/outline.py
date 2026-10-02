#!/usr/bin/env python3
"""Print a skill's outline: files in reading order, their headings, and the
first sentence of each step and supporting section.

Usage: python3 scripts/outline.py <skill-dir>
"""

import re
import sys
from pathlib import Path

FENCE = re.compile(r"^(```|~~~)")
HEADING = re.compile(r"^(#{1,3}) (.+)$")
BOLD = re.compile(r"\*\*([^*]+)\*\*")


def body_lines(text):
    """Lines outside frontmatter, code blocks, and HTML comment blocks."""
    lines = text.splitlines()
    if lines and lines[0] == "---":
        lines = lines[lines.index("---", 1) + 1 :]
    fenced = comment = False
    for line in lines:
        if FENCE.match(line):
            fenced = not fenced
            continue
        if line.startswith("<!--"):
            comment = "-->" not in line
            continue
        if comment:
            comment = "-->" not in line
            continue
        if not fenced:
            yield line


def sections(text):
    """(level, title, paragraph lines, after_rule) per heading."""
    out, after_rule = [], False
    for line in body_lines(text):
        if line.strip() == "---":
            after_rule = True
        elif m := HEADING.match(line):
            out.append([len(m[1]), m[2], [], after_rule])
        elif out:
            out[-1][2].append(line)
    return out


def first_sentence(lines, width=90):
    para = []
    for line in lines:
        if not line.strip():
            if para:
                break
            continue
        para.append(line.strip())
    text = " ".join(para)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text).replace("**", "")
    text = re.split(r"(?<=[.:])\s", text, maxsplit=1)[0]
    return text if len(text) <= width else text[: width - 1] + "…"


def names(text, group):
    """Names defined under a top-level group: ## headings or bold list items."""
    found, inside = set(), False
    for level, title, lines, _ in sections(text):
        if level == 1:
            inside = title == group
        elif inside and level == 2:
            found.add(title)
        if inside and level == 1:
            found |= {m[1] for l in lines if l.startswith("- ") for m in [BOLD.search(l)] if m}
    return found


def outline(path, known):
    group = None
    for level, title, lines, after_rule in sections(path.read_text()):
        indent = "  " * level
        if level == 1:
            group = title
            print(f"{indent}{'--- ' if after_rule else ''}# {title}")
            continue
        line = f"{indent}{'#' * level} {title}"
        if level == 2 and (group == "Steps" or after_rule):
            line = f"{line:<34} {first_sentence(lines)}"
            used = sorted({m for l in lines for m in BOLD.findall(l)} & known)
            if used:
                line += "  → " + ", ".join(used)
        print(line)


def main(skill):
    skill = Path(skill)
    entry = skill / "SKILL.md"
    known = names(entry.read_text(), "Operations") | names(entry.read_text(), "Workflows")
    files = [entry] + sorted(p for p in skill.glob("*.md") if p != entry)
    catalogues = sorted((skill / "catalogues").glob("*.md"))
    for path in files + catalogues:
        rel = path.relative_to(skill)
        tag = "  [workflow]" if rel.name[3:].startswith("workflow-") else ""
        tag = "  [catalogue]" if path in catalogues else tag
        print(f"{rel}{tag}")
        outline(path, known)
        print()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
