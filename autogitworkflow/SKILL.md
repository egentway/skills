---
name: autogitworkflow
description: >-
  Use when the user asks to do coding work in a Git repository. Ask whether
  they want the automatic Git workflow before editing.
---

# Automatic Git Workflow

When the user starts coding work in a Git repository, ask:

> Would you like to enable the automatic Git workflow for this task? It starts
> from a clean worktree, works on a feature branch, commits completed changes using
> the repository's commit convention, proposes task-based commits alongside the
> work plan, and offers fast-forward-only merges followed by local feature branch
> deletion after substantial work.

- If the user declines, perform the requested work normally. Do not load the
  workflow instructions or take Git actions on this skill's behalf.
- If the user agrees, read `workflow.md` in this skill's directory before
  making any repository edits. Follow its instructions for the rest of the
  task.
