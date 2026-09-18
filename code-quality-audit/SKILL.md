---
name: code-quality-audit
description: >-
  Audit code for maintainability, excessive complexity or nesting,
  unclear integration boundaries, exception-handling mistakes, and
  duplication caused by poor structure. Use when the task calls for
  a code-quality audit or a critical review of produced code.
---

# Code-quality audit

Produce evidence-backed findings and bounded simplifications. Do not refactor
while auditing or add an unsolicited audit to ordinary implementation work.

## Choose the requested capability

- Audit code: read [review.md](review.md), then consult the relevant criteria in
  [code-smells.md](code-smells.md).
- Add, revise, or remove inspection criteria: edit
  [code-smells.md](code-smells.md) without running an audit.
- Change the audit procedure: update [review.md](review.md); update this entry
  point only if scope or routing changes.

This skill is automatically applicable to tasks calling for this kind of audit;
no additional activation prompt is required. An audit authorizes inspection and
appropriate isolated probes, not production edits, permanent tests, dependency
installation, commits, or deployment. Obtain separate approval before fixes.

Do not silently add findings to the catalogue. Respect repository instructions,
access controls, private-data boundaries, and any narrower user scope.
