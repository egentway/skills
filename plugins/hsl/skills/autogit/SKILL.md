---
name: autogit
description: >-
  Use when the user asks to do coding work in a Git repository. Enable directly
  when the user invokes or explicitly requests this skill; otherwise ask first.
---

# Autogit

Run coding work in a clean feature workspace, plan coherent commits, and offer a
fast-forward merge with explicit local cleanup.

Explicit invocation enables this workflow for the requested task, including a
user-invoked skill message or an explicit request to use it. Otherwise ask:

> Would you like to enable the automatic Git workflow for this task? It starts
> from a clean worktree, asks whether to use an isolated Worktrunk worktree or an
> in-place feature branch when needed, plans coherent commits with the work,
> commits verified changes, and offers a separately approved fast-forward merge
> with local cleanup.

If declined, continue the original task without loading the workflow or taking
Git actions on this skill's behalf. If enabled, read
[01-workflow-code.md](01-workflow-code.md) before repository edits and follow it
for the rest of the task.

Enabling authorizes the workflow's preparation and commit process. Workspace
choices and merging retain the gates defined there. Pushing and remote branch
deletion require separate authorization.
