# Reading a workflow (format 1.0)

A workflow is a YAML list of steps. Treat it as the user's starting shape: they may
ask you to redo, skip, or reorder steps at any time.

For each step, read all of its parts first, then act:

- `skill/<name>`: read that skill through the harness's skill mechanism, not from
  memory. The name may be bare (`x`) or namespaced (`hsl:x`).
- plain text: instructions for the step.
- `action/<name>`: after the step's work, do what the name says. `approval` means
  present what the step produced and wait for the user. A response applies to that
  action only.

Say which skills you read in each step.
