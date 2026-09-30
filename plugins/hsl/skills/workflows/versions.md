# Workflow format versions

A workflow declares `format: <major>.<minor>` and carries a copy of the matching
reading instructions, so changing this skill never changes an existing workflow.

- **Major:** a change that alters how an existing workflow behaves.
- **Minor:** an addition that leaves existing workflows unchanged.

There is no patch number.

## 1.1

Adds the `file/<path>` part: read a file in the workflow's folder when the step is
reached, not earlier. Workflows at 1.0 are unaffected.

## 1.0

Steps are blocks: read all of a step's parts, then act. Parts are `skill/<name>`,
plain text, and `action/<name>` (an open set with no enforced meaning).
