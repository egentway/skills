# Authoring a workflow

A workflow is a skill whose body holds a YAML step list. The fields are `name`,
`description`, and `steps`. Each step is a block of parts: `skill/<name>`, plain
text, and `action/<name>`.

- Write skills by bare name.
- Quote any instruction that contains a colon followed by a space; otherwise YAML
  reads it as a mapping.
- Use only actions whose meaning is clear from their name. Actions are an open set
  with no enforced meaning.
- A skill that should shape the whole run is read in the first step.

## Packaging

Create `<bundle>/skills/<workflow>/SKILL.md`:

- request-only: `disable-model-invocation: true` in the frontmatter, plus
  `agents/openai.yaml` containing `allow_implicit_invocation: false` for Codex;
- the first line of the body: read the `workflows` skill and its running
  instructions, then follow this workflow;
- the YAML step list below it.

Check that every named skill exists in the bundle. Creating the skill package follows
the usual skill-authoring approval.
