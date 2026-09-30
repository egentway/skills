# Authoring a workflow

A workflow is a skill whose body holds a YAML step list and which carries its own
reading instructions. The YAML fields are `format`, `name`, `description`, and
`steps`. Each step is a block of parts: `skill/<name>`, `file/<path>`, plain text,
and `action/<name>`.

- Write skills by bare name.
- Quote any instruction that contains a colon followed by a space; otherwise YAML
  reads it as a mapping.
- Use only actions whose meaning is clear from their name. Actions are an open set
  with no enforced meaning.
- `file/<path>` needs format 1.1. The file lives in the workflow's own folder and is
  read when its step is reached.
- A skill that should shape the whole run is read in the first step.

## Packaging

Create `<bundle>/skills/<workflow>/` with:

- `SKILL.md`, request-only (`disable-model-invocation: true` in the frontmatter). The
  first line of the body tells the agent to read `reading.md` first, with the format
  version, then follow the workflow. Use that imperative wording: a soft reference
  such as "as reading.md describes" was skipped in trials. The YAML step list follows,
  including `format: <major>.<minor>`;
- `reading.md`, an unchanged copy of this skill's [reading.md](reading.md), whose
  title gives the format version;
- `agents/openai.yaml` containing `allow_implicit_invocation: false` for Codex;
- any files that `file/` parts name.

Check that every named skill and file exists. Creating the skill package follows the
usual skill-authoring approval.

## Upgrading a workflow

Read [versions.md](versions.md) for what changed between the workflow's format and
the target. Replace its `reading.md` with the current copy, adjust any part the
changes affect, and set `format`. A minor upgrade needs nothing else.
