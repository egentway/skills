---
name: mod
description: >-
  Model Oriented Development: keep a project's requirements in a project model
  built from accepted decisions, and change the codebase within it. Use for
  ordinary work in a repository that has mod installed, to propose or record a
  decision, or to initialize, migrate, or install mod's documentation. Audit it
  only on an explicit user request.
---

Decisions determine the project model, and the project model determines the
implementation. For ordinary repository work, follow
[01-consultation.md](01-consultation.md); loading this skill does not start a
workflow. Record formats live in [07-records.md](07-records.md).

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

Skill-internal links are relative to the skill root, wherever this package is
loaded or installed. Project destinations are relative to the target repository
root; do not write project documentation into the skill package.

# Operations

## Approve

Present what was produced up to this point, then stop and wait for the user. Their
response applies to this gate only.

## Check discovery

Start at the root `AGENTS.md` pointer with only a task in mind. For a real change,
find the project-model sections and the decision parts in force for it, the
implementation owner, its invariants, gaps, and focused checks, without reading
superseded decisions, pre-genesis records, or the archive. Separately, find why a
requirement exists, what is pending, and the evidence behind a decision. Record
each route and any misleading detour. Use scenarios from the actual application,
and do not invent application concepts for the exercise. Links can all work while
discovery still fails.

# Workflows

- **Decide** — [02-workflow-decide.md](02-workflow-decide.md): a change needs
  requirements the project model lacks or contradicts, or the user asks to
  propose or record a decision.
- **Initialize** — [03-workflow-initialize.md](03-workflow-initialize.md): a new
  or undocumented project, on request.
- **Migrate** — [04-workflow-migrate.md](04-workflow-migrate.md): a project
  documented in an earlier system, agent-docs included, on request.
- **Audit** — [05-workflow-audit.md](05-workflow-audit.md): only when the user
  explicitly asks for an audit.
- **Install** — [06-workflow-install.md](06-workflow-install.md): install or
  update the project-local skill. Initialize and Migrate end with it.

Decide runs whenever the Check fit section of 01-consultation.md finds that a
change needs new requirements. Do not run Initialize, Migrate, Install, or Audit merely because
the skill was loaded; ordinary code edits, stale docs, and general reviews do not
trigger them.

The other files are part of this skill, not optional dependencies. Install the
complete package in the target project and keep its root `AGENTS.md` section
pointing at the installed consultation guide.
