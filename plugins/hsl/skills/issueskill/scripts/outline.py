#!/usr/bin/env python3
"""Print a skill's outline: files in reading order, each file's opening, its
headings, and for each step its first sentence, its Gate and Stop if fields, and
the operations or workflows it runs.

Usage: python3 scripts/outline.py <skill-dir>
"""

import re
import sys
from pathlib import Path

FENCE = re.compile(r"^(```|~~~)")
HEADING = re.compile(r"^(#{1,3}) (.+)$")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
FIELD = re.compile(r"^- \*\*(Gate|Stop if):\*\*\s*(.*)$")
SHOWN = 90


def body_lines(text):
    """Lines outside frontmatter, code blocks, and HTML comments."""
    lines = text.splitlines()
    if lines and lines[0] == "---":
        lines = lines[lines.index("---", 1) + 1 :]
    fenced = comment = False
    for line in lines:
        if FENCE.match(line):
            fenced = not fenced
        elif line.startswith("<!--"):
            comment = "-->" not in line
        elif comment:
            comment = "-->" not in line
        elif not fenced:
            yield line


def sections(text):
    """The opening lines, then [level, title, lines, after_rule] per heading."""
    opening, out, after_rule = [], [], False
    for line in body_lines(text):
        if line.strip() == "---":
            after_rule = True
        elif m := HEADING.match(line):
            out.append([len(m[1]), m[2], [], after_rule])
        else:
            (out[-1][2] if out else opening).append(line)
    return opening, out


def plain(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text).replace("**", "")
    return text if len(text) <= SHOWN else text[: SHOWN - 1] + "…"


def first_sentence(lines):
    para = []
    for line in lines:
        if not line.strip():
            if para:
                break
            continue
        para.append(line.strip())
    return plain(re.split(r"(?<=\.)\s", " ".join(para), maxsplit=1)[0])


def fields(lines):
    """Gate and Stop if fields, joined with their continuation lines."""
    found, current = [], None
    for line in lines:
        if m := FIELD.match(line):
            current = [m[1], m[2]]
            found.append(current)
        elif current and line.startswith("  ") and line.strip():
            current[1] += " " + line.strip()
        else:
            current = None
    return found


def names(text, group):
    """Names defined under a top-level group: ## headings or bold list items."""
    found, inside = set(), False
    for level, title, lines, _ in sections(text)[1]:
        if level == 1:
            inside = title == group
            if inside:
                found |= {m[1] for l in lines if l.startswith("- ") for m in [BOLD.search(l)] if m}
        elif inside and level == 2:
            found.add(title)
    return found


def outline(path, known):
    opening, heads = sections(path.read_text())
    if any(l.strip() for l in opening):
        print(f"  ({first_sentence(opening)})")
    group = None
    for level, title, lines, after_rule in heads:
        indent = "  " * level
        if level == 1:
            group = title
            listed = [m[1] for l in lines if l.startswith("- ") for m in [BOLD.search(l)] if m]
            tail = "  " + " · ".join(listed) if title == "Workflows" else ""
            print(f"{indent}{'--- ' if after_rule else ''}# {title}{tail}")
            continue
        line = f"{indent}{'#' * level} {title}"
        if level != 2 or not (group == "Steps" or after_rule):
            print(line)
            continue
        step_fields = fields(lines)
        gated = {m for _, text in step_fields for m in BOLD.findall(text)}
        runs = sorted({m for l in lines for m in BOLD.findall(l)} & known - gated)
        line = f"{line:<30} {first_sentence(lines)}"
        print(line + ("  → " + ", ".join(runs) if runs else ""))
        for name, text in step_fields:
            print(f"{'':<31}{name}: {first_sentence([text])}")


def main(skill):
    skill = Path(skill)
    entry = (skill / "SKILL.md").read_text()
    known = names(entry, "Operations") | names(entry, "Workflows")
    files = [skill / "SKILL.md"] + sorted(p for p in skill.glob("*.md") if p.name != "SKILL.md")
    catalogues = sorted((skill / "catalogues").glob("*.md"))
    for path in files + catalogues:
        rel = path.relative_to(skill)
        tag = "  [workflow]" if rel.name[3:].startswith("workflow-") else ""
        print(f"{rel}{'  [catalogue]' if path in catalogues else tag}")
        outline(path, known)
        print()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
