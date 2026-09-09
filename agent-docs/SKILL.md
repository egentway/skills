---
name: agent-docs
description: >-
  Organize agent-facing documentation by purpose for progressive discovery.
  Use to initialize greenfield documentation, migrate an existing documentation
  tree, install or update this project-local skill, or consult and maintain its
  current/design/reference conventions.
---

# Agent documentation

Keep current application editing guidance separate from design progress and
historical evidence. A fresh agent should find the owner of a change without
reading a proposal or mistaking old behavior for today's implementation.

## Read only the guide for the task

Skill-internal guide links are relative to the skill root, wherever this package
is loaded or installed. Project destinations mentioned by the guides are relative
to the target project root; do not write application docs into the source package.

| Task | Read |
| --- | --- |
| Find application context or maintain docs while changing code | [Consultation](consultation.md) |
| Install/update the project-local skill and root pointer | [Installation](installation.md) |
| Establish docs for a new or genuinely undocumented project | [Initialization](initialization.md), then its installation step |
| Reorganize existing guidance, proposals, and research | [Migration](migration.md), then its installation step |

Consultation is the routine path. Do not run initialization or migration merely
because the skill was loaded. Installation supplies instructions; it does not by
itself create an application guide or complete a migration.

The other files are part of this skill, not optional external dependencies.
Install the complete package in the target project. Keep the root `AGENTS.md`
section small and route it directly to the installed consultation guide, not back
to setup instructions. Repository-wide engineering policy remains outside that
managed section.
