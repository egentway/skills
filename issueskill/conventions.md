# Skill authoring conventions

These are the editable rules applied by [issue.md](issue.md). Change them when the
user requests an authoring-rule refinement; ordinary execution does not silently
accumulate new rules. Keep reusable lessons, not a diary of individual tasks.

## Discovery and scope

Use SKILL.md with YAML frontmatter containing `name` and `description`. Match the
name to the skill directory. Describe when the skill applies, not just its topic.
State the intended outcome and boundaries in the instructions.

Recover existing user decisions before asking questions. Clearly distinguish agreed
requirements, observed techniques, and new recommendations. Do not elevate incidental
behavior or an agent's mistakes into permanent policy.

## Functional decomposition

Split functionality into separate files when users can select one capability without
needing the others. Keep SKILL.md as a discoverable router to those capabilities,
with direct relative links and clear conditions for reading each file.

Keep cohesive procedures together. Do not create files solely for every section,
duplicate shared instructions, or make an agent load unrelated capabilities. A small
single-purpose skill can remain entirely in SKILL.md.

## Activation and approval

Choose activation deliberately for each produced skill:

1. Use the policy established by the user's request or clear context.
2. Otherwise ask whether the skill should be request-driven, recommending automatic
   applicability by default. The default does not replace asking when unclear.
3. State the selected policy in the proposal.

For request-driven skills, add this YAML field and state the request-only boundary
in the instructions:

```yaml
disable-model-invocation: true
```

For automatically applicable skills, omit the field. This metadata is supported by
some harnesses, including Claude Code; do not assume every loader enforces it.
Verify support where possible and report any unverified enforcement. Never invent
an alternative metadata field and claim it provides a working gate.

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

## Reviewable proposals

Show every proposed file, its responsibility, and abridged instruction content.
Preserve important sections, links, gates, and maintenance paths in the excerpts.
Show how the files work together, not a disconnected set of outlines.

Identify recommendations and open choices. Refine from feedback and obtain approval
before writing. Do not mistake a scope discussion or a presentation improvement for
approval of the complete proposal.

## Verification and portability

Check package structure and exercise relevant behavior, including scope ambiguity,
consent boundaries, and direct knowledge maintenance. Distinguish structural checks,
instruction walkthroughs, model exercises, and real harness invocation results.

Keep supporting links relative to the skill root. Do not embed machine-specific
paths in portable instructions when the process can resolve them. For issueskill,
use the destination lookup in issue.md; do not add a configuration system.

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
maintenance instructions so later procedure or catalogue edits follow it without
requiring issueskill to be loaded. This policy concerns changes to the skill
package, not application-code changes made or inspected during ordinary skill use.

Installation, pushing, and remote publication remain separately authorized actions.
