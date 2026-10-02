---
name: feature
description: >-
  Run the feature workflow. Plan, implement, and review a code change.
disable-model-invocation: true
---

Plan, implement, and review a code change. The user's request follows the command.

<!-- workflow-instructions 4 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`. If you have a
task-list tool, including one you must load or enable first, add the steps to
it by name and keep it current.
<!-- workflow-instructions end -->

# Operations

## Approve

Present what was produced up to this point, then stop and wait for the user. Their
response applies to this gate only.

# Steps

## Setup

Set how code is written for the whole run.

- **Output:** cognitive-budget-coding loaded for every later step.

Read cognitive-budget-coding.

## Plan

Map the request onto the repository.

- **Input:** the user's request and the discussion that led to it.
- **Output:** an approved implementation plan.
- **Gate:** **Approve**, held by implementation-planning's Present step; one
  approval covers both.

Run implementation-planning.

## Implement

Build the approved plan.

- **Input:** the approved plan.
- **Output:** the change, with the plan's checks run.

Read feedback-driven-execution, then implement. Surface consequential choices
and growing complexity as they appear rather than at the end.

## Audit

Review the change and present the findings.

- **Input:** the change from Implement.
- **Output:** findings, with nothing fixed.
- **Gate:** **Approve** before any fix.

Run code-quality-audit on the changed code.
