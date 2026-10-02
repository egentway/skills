# Skill authoring conventions

These are the editable rules applied by [issue.md](issue.md). Change them when the
user requests an authoring-rule refinement; ordinary execution does not silently
accumulate new rules. Keep reusable lessons, not a diary of individual tasks.

## Discovery and scope

Use SKILL.md with YAML frontmatter containing `name` (matching the directory) and
`description`. Describe when the skill applies, not just its topic, and state the
intended outcome and boundaries in the instructions.

Recover existing user decisions before asking questions. Clearly distinguish agreed
requirements, observed techniques, and new recommendations. Do not elevate incidental
behavior or an agent's mistakes into permanent policy.

## Functional decomposition

Split functionality into separate files when users can select one capability without
needing the others. Keep SKILL.md as a discoverable router with direct relative links
and clear conditions for reading each file. Keep cohesive procedures together; a small
single-purpose skill can remain entirely in SKILL.md.

## Writing instructions

Explain why a rule matters instead of using shouting-case MUST or NEVER. State the
outcome, non-obvious context, and real constraints. Keep SKILL.md short and move
mode-specific detail into linked files. Correct an observed failure narrowly rather
than adding a universal rule.

Separate Markdown blocks of different kinds with a blank line: after every
heading, and before and after each list, code block, and table. Renderers such as
pandoc otherwise merge a list into the paragraph above it. In a numbered list
where any item wraps onto a second line, put a blank line between all its items;
keep lists of one-line items compact.

## Activation and approval

Choose activation deliberately for each produced skill:

1. Use the policy established by the user's request or clear context.

2. Otherwise ask whether the skill should be request-driven, recommending automatic
   applicability by default. The default does not replace asking when unclear.

3. State the selected policy in the proposal.

For request-driven skills, state the request-only boundary in the instructions and
set the invocation metadata for each harness the skill targets:

- Claude Code and omp: `disable-model-invocation: true` in the frontmatter. omp
  normalizes this form, and the skill stays reachable through `/skill:<name>`.
- Codex: `agents/openai.yaml` containing the following. Explicit `$<name>`
  invocation still works. Preserve other fields if the file already exists, and
  create the file only for this purpose.

  ```yaml
  policy:
    allow_implicit_invocation: false
  ```

For automatically applicable skills, omit both. Verify enforcement where the harness
is available and report anything unverified. Never invent a metadata field and claim
it provides a working gate.

Automatic applicability and execution consent are separate decisions. When a skill
requires confirmation, especially on automatic matching:

- Keep the execution procedure outside SKILL.md.
- Have SKILL.md explain the capability and ask for activation before loading or
  executing that procedure. Adapt the prompt to the situation; offer a capability
  choice when multiple functions are available.
- Explicit user invocation normally satisfies activation consent for the requested
  capability; it does not authorize unrelated capabilities or later consequential
  actions that require their own approval.
- On refusal, do not load or execute the gated procedure. Continue the original task
  without that functionality. Do not repeatedly prompt within the same scope.

Invocation of issueskill starts authoring, not writing. Its proposal-approval gate
remains in effect even though the user explicitly invoked it.

## File layout

Give every supporting file a two-digit index, even when the files do not form a
sequence: a fixed reading order tells a reader where to start and keeps the outline
stable. A file that holds a workflow, with its own `# Steps`, also takes the
`workflow-` prefix and the workflow's verb: `02-workflow-initialize.md` for
**Initialize**. SKILL.md keeps its name and comes first.

When a sequence exists, number in that order. Otherwise number in the order the
entry point lists the files: the default or most frequent workflow first, then the
others, then files that mainly serve other files. The entry point lists them in
index order. `scripts/` and `agents/` hold tooling and stay unnumbered.

Numbered files are the skill's stable part: the procedure and its rules, changed
deliberately. Collections meant to grow through frequent edits, such as a
code-smell catalogue, go in `catalogues/` with descriptive names and no index.
Entries can then be added without touching the procedure, and the procedure reads
without the entries.

## Process and editable knowledge

Separate a procedure from knowledge that benefits from independent maintenance:
for example, review steps in SKILL.md or `01-review.md`, and review criteria in
`catalogues/code-smells.md`. No universal catalogue schema is required.

Make ownership and maintenance discoverable:

- The entry point names and links the knowledge files and explains their purpose.
- The procedure identifies which knowledge it consumes and when to read it.
- A user request to add, revise, or remove knowledge routes to its owning file
  without activating the associated procedure.
- Update dependent instructions only when the knowledge change affects them.

Choose a structure suited to the contents. A code-smell entry might include its
name, recognition signals, consequences, and exceptions or counterexamples. Avoid
bare prohibitions that confuse a useful inspection signal with an automatic defect.
Do not silently add findings to a catalogue during normal execution.

## Workflow skills

A workflow skill runs named steps that draw on other skills, usually with user
gates. Its body is both the overview of the run and its instructions. Use this
layout only when sequencing steps is the skill's job; other skills keep free-form
bodies.

Lay SKILL.md out in this order:

1. An opening: one line on what the skill does; if the skill also takes requests
   that are not a run, such as maintaining its catalogue, one line routing them to
   their file; then the reading block below, copied as is with its markers.

2. `# Operations`, if any: short actions named as verbs, such as `## Approve`.
   Define one only when it recurs across steps, workflows, or skills; anything
   used once stays in its step. A step runs an operation by writing its name in
   bold where it takes effect, in a sentence that says when.

3. `# Steps`, with one `## <Verb>` per step. Open each step with a one-line
   purpose, then the fields that apply:

   - **Input:** what the step consults or receives.
   - **Output:** what it leaves behind.
   - **Gate:** where the run pauses for the user, naming the operation in bold;
     it continues from their answer.
   - **Stop if:** what the agent may find that ends the run early.

   The body follows: the procedure, as numbered actions where the work has an
   order and as prose where it does not; prefer numbered actions. A body that
   starts with a bullet list opens with a lead-in line, so renderers keep it
   apart from the fields instead of merging the two lists. Branches that
   change the work without ending the run go in the body. Move long material,
   such as a template, into a `###` part and name it from the action that uses it.

4. If supporting sections follow, a horizontal rule (`---`, with a blank line
   before it), then those sections. A section belongs outside the steps only when
   several steps read it; otherwise its content stays in its step. A collection
   that grows goes in `catalogues/` instead (see File layout).

A skill with several workflows puts `# Workflows` in SKILL.md in place of
`# Steps`: one line per workflow with its bold verb, its file, and when it
applies. Each `NN-workflow-<verb>.md` file holds a `# Steps` laid out as above,
without the reading block. It may open with a short paragraph saying when the
workflow applies and what it does not cover. Operations are defined only in
SKILL.md.
A step runs another workflow by its bold verb, as it runs an operation.

The reading block:

```markdown
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
```

- Name a section by its exact heading text, and keep every heading name unique in
  the file. Link a file relative to the skill folder.
- Name only model-invocable skills, by bare name.
- Read a skill that should shape the whole run in the first step.
- Workflow skills are usually request-only; set activation as above.
- The number in the opening marker versions the block. When you change the block,
  bump the number and replace every copy that
  `grep -rn '<!-- workflow-instructions [0-9]' plugins/` reports with an older one.

When the skill needs execution consent (see Activation and approval), SKILL.md
holds only the gate. The layout above goes in `01-workflow-<verb>.md`, operations
included, which SKILL.md reads once consent is given, so nothing of the run is read
before the user agrees.

## Reviewable proposals

How proposals and the other user-facing messages are presented lives in
[presentation.md](presentation.md). Whatever the format, show actual proposed
excerpts with their connections, identify recommendations and open choices, refine
from feedback, and obtain approval before writing. Do not mistake a scope discussion
or a presentation improvement for approval of the complete proposal.

## Portability

Keep supporting links relative to the skill root. Do not embed machine-specific
paths in portable instructions when the process can resolve them. For issueskill,
use the destination lookup in issue.md; do not add a configuration system.

Distinguish structural checks, instruction walkthroughs, model exercises, and real
harness invocation results when reporting verification; issue.md defines the levels.

Installation, pushing, and remote publication require separate authorization.
Do not add scripts, dependencies, tests, or documentation merely to make a skill
appear more substantial.

## Commit completed skill changes

After each completed and verified skill creation or modification, including changes
to procedures, conventions, or knowledge catalogues, create a commit in the skill's
Git repository. No additional commit confirmation is required.

Commit the coherent change, not every intermediate edit. Keep separate skill
changes in separate commits. Stage only changes belonging to that skill task.
Preserve unrelated working-tree and staged changes; never include them accidentally.
If pre-existing edits overlap the task, establish which changes are authorized
before including them.

Follow the repository's commit-message convention. Do not create empty commits.
If the destination is not a Git repository, changes cannot be safely isolated, or
committing fails, report the blocker rather than initializing a repository,
discarding changes, or claiming completion. Do not bypass failing hooks.

Include an equivalent, self-contained commit policy in generated skills'
maintenance instructions, in a few lines (commit verified changes, stage only that
skill's files, do not push), so later procedure or catalogue edits follow it without
requiring issueskill to be loaded. This policy concerns changes to the skill
package, not application-code changes made or inspected during ordinary skill use.

Installation, pushing, and remote publication remain separately authorized actions.
