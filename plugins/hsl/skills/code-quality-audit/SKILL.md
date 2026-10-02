---
name: code-quality-audit
description: >-
  Audit code for maintainability, excessive complexity or nesting,
  unclear integration boundaries, exception-handling mistakes, and
  duplication caused by poor structure. Use when the task calls for
  a code-quality audit or a critical review of produced code.
---

# Code-quality audit

Produce evidence-backed findings and bounded simplifications. Apply to requested
audits or critical reviews; do not add unsolicited audits to ordinary implementation.
An audit authorizes inspection and appropriate isolated probes, not production edits,
permanent tests, dependency installation, commits, or deployment. Fixes require
separate approval. Respect repository instructions, access controls, private-data
boundaries, and any narrower user scope. No additional activation prompt is required.
For criteria edits, use the direct route under Edit inspection criteria.

<!-- workflow-instructions 5 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`.

When starting a workflow, record its steps by name in your task-list tool before
the first step; load or enable the tool if needed. Reuse this run's entries when
resuming, and update them as the run progresses. If the harness provides no
task-list tool, continue without one.

Track the outermost workflow. A called workflow keeps the caller's step in
progress; show its current inner step in that entry's description, or its label
if descriptions are unavailable. Do not add a second list of inner steps. Keep
a step in progress while its Gate awaits the user; complete it only after its
output and gate are settled.
<!-- workflow-instructions end -->

# Workflows

- **Audit** — read [01-workflow-audit.md](01-workflow-audit.md) for a requested
  code-quality review.

---

# Edit inspection criteria

Add, revise, or remove criteria in [catalogues/code-smells.md](catalogues/code-smells.md)
without running an audit. Do not silently add ordinary findings.
For procedure changes, edit 01-workflow-audit.md; update this entry point when scope
or routing changes.
