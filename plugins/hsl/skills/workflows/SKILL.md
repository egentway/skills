---
name: workflows
description: >-
  Use to write, upgrade, or explain an hsl workflow definition (a YAML list of steps
  that read skills), such as feature. A workflow carries its own reading
  instructions and is run by invoking it.
---

# Workflows

A workflow strings skills into an ordered series of steps. Skills stay unaware of
workflows; the workflow says which skills are read at which step. Each workflow
carries its own copy of the reading instructions for its format version, so it is
run by invoking it, not through this skill.

- Writing or changing a workflow: read [authoring.md](authoring.md).
- What changed between format versions: read [versions.md](versions.md).
- The current reading instructions, copied into every new workflow:
  [reading.md](reading.md).
