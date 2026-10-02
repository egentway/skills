---
name: issueskill
description: >-
  Create a skill from a user brief or systematize a process from the current
  conversation into a reusable skill. Use only when the user requests skill
  creation or invokes issueskill.
disable-model-invocation: true
---

# Issueskill

Produce a reusable skill from a user brief or the relevant activity in the conversation.
Use only when requested or explicitly invoked. Invocation authorizes discussion and
a proposal; writing requires approval of the resulting proposal.
For authoring-rule edits, use the direct routes under Maintain authoring rules.

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

- **Issue a skill** — read [01-workflow-issue.md](01-workflow-issue.md) to create
  from a brief or extract from the relevant conversation activity.

---

# Maintain authoring rules

For authoring-rule changes, read and update [02-conventions.md](02-conventions.md).
For presentation or verification changes, use [03-presentation.md](03-presentation.md)
or [04-verification.md](04-verification.md), respectively. These requests do not
start the authoring workflow. Update dependent instructions only when affected.
Verify the affected instructions and commit using the policy in 02-conventions.md.
