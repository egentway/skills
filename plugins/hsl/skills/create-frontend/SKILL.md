---
name: create-frontend
description: >-
  Create or refine frontend interfaces with cohesive reusable components,
  clear information architecture, restrained copy, and verified interaction.
  Use for new screens, application shells, UI previews, and substantial
  frontend changes.
---

Build interfaces whose structure, components, content, and behavior serve the
user's task. Follow existing project conventions before introducing new ones.
To change the catalogue or this procedure, see [Maintaining this skill] instead
of running the steps.

<!-- workflow-instructions 2 -->
This is a workflow skill. Work through the steps in order; the user may redo, skip,
or reorder them. Only the headings under `# Steps` are steps; any other section is
read when a step refers to it. Under each step, read everything listed before
acting: `skill: <name>` through the skill mechanism, and `[Name]` as the section
with that heading, or the link defined for it relative to this skill's folder. Say
what you read in each step.
<!-- workflow-instructions end -->

[understanding]: implementation.md#understand-the-interface
[reuse]: implementation.md#reuse-before-inventing
[first slice]: implementation.md#build-a-useful-first-slice
[content review]: implementation.md#review-content-and-layout
[verification]: implementation.md#verify-the-rendered-result
[common problems]: common-problems.md

# Steps

## Understand
- [understanding]
- [Scope]

## Reuse
- [reuse]

## Build
Build the smallest slice the user can evaluate.
- [first slice]

## Review
Check content and layout against the catalogue.
- [content review]
- [common problems]

## Verify
- [verification]

---

# Scope

This skill is automatically applicable to frontend creation/refinement tasks;
no additional activation prompt is required. Applicability does not authorize
unrelated work. A request to improve an interface is not permission to migrate its
stack, redesign unrelated screens, or implement deferred backend functionality.
Respect the user's scope and the project's planning and approval boundaries.

# Maintaining this skill

- Adding, revising, or removing a recurring problem: edit
  [common-problems.md](common-problems.md) without starting application work.
- Changing the procedure: update the steps here or the sections of
  [implementation.md](implementation.md).

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
