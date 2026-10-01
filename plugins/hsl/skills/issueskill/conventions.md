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

## Process and editable knowledge

Separate a procedure from knowledge that benefits from independent maintenance:
for example, `review.md` for review steps and `code-smells.md` for review criteria.
Use descriptive Markdown filenames; no universal catalogue schema is required.

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

Lay the body out in this order:

1. An opening: one line on what the skill does, then the reading paragraph below,
   copied as is.
2. `# Steps`, with one `## <Verb>` per step: a line of instruction, then a list of
   what the step reads and ends with.
3. `# Operations`, if any: reusable actions named as verbs, such as `## Approve`.
   Each one says when it takes effect.
4. Free-form sections for supporting material the steps refer to.

The reading paragraph:

> This is a workflow skill. Work through the steps in order; the user may redo,
> skip, or reorder them. Under each step, read everything listed before acting:
> `skill: <name>` through the skill mechanism, and `[Name]` as the section with
> that heading, or the link defined for it relative to this skill's folder. Say
> what you read in each step.

- Refer to a section by its exact heading text: `[Approve]`. Every heading name
  must be unique in the file, including the group headings.
- Refer to another file with a shortcut reference link and its definition:
  `[what to flag]` with `[what to flag]: criteria.md#what-to-flag`.
- Name only model-invocable skills, by bare name.
- Read a skill that should shape the whole run in the first step.
- Workflow skills are usually request-only; set activation as above.
- There is no format version. Each workflow skill carries its own reading
  paragraph, so changing this convention means updating those skills by hand.

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
