---
name: create-frontend
description: >-
  Create or refine frontend interfaces with cohesive reusable components,
  clear information architecture, restrained copy, and verified interaction.
  Use for new screens, application shells, UI previews, and substantial
  frontend changes.
---

# Create frontend

Build interfaces whose structure, components, content, and behavior serve the
user's task. Follow existing project conventions before introducing new ones.

## Choose the requested capability

- Creating or refining a frontend: read [implementation.md](implementation.md),
  then consult applicable entries in [common-problems.md](common-problems.md).
- Adding, revising, or removing a recurring problem: edit
  [common-problems.md](common-problems.md) without starting application work.
- Changing the implementation workflow: update
  [implementation.md](implementation.md). Change this entry point only when scope
  or routing changes.

This skill is automatically applicable to frontend creation/refinement tasks;
no additional activation prompt is required. Applicability does not authorize
unrelated work. A request to improve an interface is not permission to migrate its
stack, redesign unrelated screens, or implement deferred backend functionality.
Respect the user's scope and the project's planning and approval boundaries.

## Maintain this package

The catalogue is editable knowledge, not an automatic defect detector. Do not
silently add findings during ordinary frontend work. Update dependent instructions
only when a requested knowledge change affects the workflow or routing.

After completing and verifying a change to this skill's procedure or catalogue,
commit the coherent change in the skill's Git repository without another commit
confirmation. Follow that repository's commit convention. Stage only this task's
changes and preserve unrelated working-tree and staged changes. Resolve overlapping
pre-existing edits before including them. Do not create empty commits. If the
repository is absent, changes cannot be isolated, or committing fails, report the
blocker; do not initialize a repository, discard work, or bypass hooks.

This commit policy concerns the skill package, not application code created during
ordinary use. Installation, pushing, and remote publication require separate
authorization. Keep package links relative and include all supporting files when
installation is separately requested.
