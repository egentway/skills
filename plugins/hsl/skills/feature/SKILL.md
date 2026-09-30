---
name: feature
description: >-
  Run the feature workflow. Plan, implement, and review a code change.
disable-model-invocation: true
---

Read the `workflows` skill and its running instructions, then follow this workflow.
The user's request follows the command.

```yaml
name: feature
description: Plan, implement, and review a code change.
steps:
  - setup:
      - skill/cognitive-budget-coding
  - plan:
      - Plan the change and present it, including the file impact.
      - skill/implementation-planning
      - skill/present-for-review
      - action/approval
  - implement:
      - Implement the approved plan; surface consequential choices as they appear.
      - skill/feedback-driven-execution
  - review:
      - Audit the change and present the findings; do not fix without approval.
      - skill/code-quality-audit
      - action/approval
```
