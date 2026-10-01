---
name: feature
description: >-
  Run the feature workflow. Plan, implement, and review a code change.
disable-model-invocation: true
---

Plan, implement, and review a code change. The user's request follows the command.

<!-- workflow-instructions 2 -->
This is a workflow skill. Work through the steps in order; the user may redo, skip,
or reorder them. Only the headings under `# Steps` are steps; any other section is
read when a step refers to it. Under each step, read everything listed before
acting: `skill: <name>` through the skill mechanism, and `[Name]` as the section
with that heading, or the link defined for it relative to this skill's folder. Say
what you read in each step.
<!-- workflow-instructions end -->

# Steps

## Setup
- skill: cognitive-budget-coding

## Plan
Plan the change and present it, including the file impact.
- skill: implementation-planning
- skill: present-for-review
- [Approve]

## Implement
Implement the approved plan; surface consequential choices as they appear.
- skill: feedback-driven-execution

## Audit
Audit the change and present the findings; do not fix without approval.
- skill: code-quality-audit
- [Approve]

---

# Operations

## Approve
Once the step's work is done, present what it produced, then stop and wait for the
user. Their response applies to this gate only.
