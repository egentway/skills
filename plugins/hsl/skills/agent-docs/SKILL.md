---
name: agent-docs
description: >-
  Organize agent-facing documentation by purpose for progressive discovery.
  Use to initialize greenfield documentation, migrate an existing documentation
  tree, install or update this project-local skill, or consult and maintain its
  current/design/reference conventions. Audit documentation only on an explicit
  user request, presenting evidence before edits and refining incrementally
  through user feedback.
---

Keep current application editing guidance separate from design progress and
historical evidence, so a fresh agent finds the owner of a change without reading
a proposal or mistaking old behavior for today's implementation. For ordinary
repository work, consult and maintain the docs as
[01-consultation.md](01-consultation.md) describes. That is the routine path:
loading this skill does not start a workflow.

<!-- workflow-instructions 3 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`.
<!-- workflow-instructions end -->

Skill-internal links are relative to the skill root, wherever this package is
loaded or installed. Project destinations mentioned by the guides are relative to
the target project root; do not write application docs into the source package.

# Operations

## Approve

Present what was produced up to this point, then stop and wait for the user. Their
response applies to this gate only.

## Check discovery

Start at the root `AGENTS.md` pointer with only a task in mind. Find the owner of
a real change, its invariants, and its focused checks without entering design or
history; separately find a governing decision, outstanding design scope, and
reference evidence. Record each route and any misleading detour. Use scenarios
from the actual application, and do not invent application concepts for the
exercise. Links can all work while purpose discovery still fails.

# Workflows

- **Initialize** — [02-workflow-initialize.md](02-workflow-initialize.md): a new
  or genuinely undocumented project.
- **Migrate** — [03-workflow-migrate.md](03-workflow-migrate.md): reorganize
  existing guidance, proposals, and research.
- **Audit** — [04-workflow-audit.md](04-workflow-audit.md): only when the user
  explicitly asks for a documentation audit.
- **Install** — [05-workflow-install.md](05-workflow-install.md): install or update
  the project-local skill. Initialize and Migrate end with it.

Do not run Initialize, Migrate, or Audit merely because the skill was loaded.
Audit is exclusively user-invoked: ordinary code edits, stale docs, and general
repository reviews do not trigger it. Install supplies instructions; it does not
by itself create an application guide or complete a migration.

The other files are part of this skill, not optional external dependencies.
Install the complete package in the target project. Keep the root `AGENTS.md`
section small and route it directly to the installed consultation guide, not back
to setup instructions. Repository-wide engineering policy remains outside that
managed section.
