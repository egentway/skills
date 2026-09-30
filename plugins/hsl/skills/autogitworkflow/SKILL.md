---
name: autogitworkflow
description: >-
  Use when the user asks to do coding work in a Git repository. Enable directly
  when the user invokes or explicitly requests this skill; otherwise ask first.
---

# Automatic Git Workflow

Treat either of these as explicit consent to enable the workflow:

- The skill arrives in a user-invoked skill message, such as from
  `/skill:autogitworkflow`.
- The user explicitly asks to use or enable the automatic Git workflow.

In either case, skip the activation prompt. Read `workflow.md` in this skill's
directory before making repository edits and follow it for the rest of the task.

When this skill matches the task automatically instead, ask:

> Would you like to enable the automatic Git workflow for this task? It starts
> from a clean worktree, asks whether to use an isolated Worktrunk worktree or an
> in-place feature branch when a feature workspace is needed, commits completed
> changes using the repository's convention, proposes task-based commits alongside
> the work plan, and offers fast-forward-only merges followed by local cleanup.

- If the user declines, perform the requested work normally. Do not load
  `workflow.md` or take Git actions on this skill's behalf.
- If the user agrees, read `workflow.md` before making repository edits and
  follow it for the rest of the task.
