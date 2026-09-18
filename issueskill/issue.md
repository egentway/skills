# Issue a skill

Use these steps with [conventions.md](conventions.md). Creation from a brief and
extraction from ongoing work share this process; only their starting evidence differs.

## 1. Recover the intended capability

For a new brief, identify the desired outcome, inputs, constraints, and exclusions.
For extraction, recover the relevant request, actions, results, and user corrections
from the conversation. Do not ask the user to repeat available context.

Extract the intended activity, not automatically the whole conversation. After an
implementation followed by a review, an invocation referring to that review should
produce a review workflow, not an implementation-and-review workflow. If multiple
activities are plausible, summarize the alternatives and ask which to systematize.

Distinguish:

- User requirements and confirmed decisions: preserve these.
- Observed techniques: evaluate their usefulness before making them rules.
- Agent recommendations: identify these as proposals, not prior agreements.
- Incidental commands, project details, and particular findings: omit unless they
  serve a reusable purpose or the skill is intentionally project-specific.

Do not canonize mistakes or claim an observed procedure is validated merely because
an agent performed it. Preserve relevant corrections and known limitations.

## 2. Resolve the destination and consequential questions

Use an explicit destination supplied by the user for this invocation. Otherwise,
check `~/skills` and `~/Projects/skills`, expanding `~` to the current user's home:

- Exactly one is an existing directory: use it.
- Both are directories: resolve their real paths. If they name the same directory,
  use it; otherwise ask which repository to use.
- Neither is a directory: ask for a destination. Do not silently create a repository
  or use the current project instead.

An explicit destination is not permission to create a missing repository. Surface
unavailable destinations before writing. No configuration file or Nix integration
is required. The output is `<repository>/<skill-name>/`; if it already exists,
ask whether to revise that skill or choose another name rather than overwriting it
as a new package.

Resolve scope and activation from the conversation and local conventions first.
When activation is unclear, ask whether the produced skill should be request-driven,
with automatic applicability as the default recommendation. Do not skip this question
just because a default exists. Separately decide whether automatic activation needs
an execution-confirmation gate; see conventions.md.

Ask only questions that materially affect the skill. Use reasonable local conventions
for routine details; do not turn authoring into a fixed questionnaire.

## 3. Present a reviewable proposal

Present the proposal in the conversation before creating files. Include:

- The capability, outcome, inputs, exclusions, and extraction boundary.
- The selected activation policy and any later approval gates.
- A short end-to-end invocation example.
- The resolved destination and a tree of every proposed file.
- Each file's responsibility and abridged contents, including its important headings,
  instructions, routing links, and connections to other files.
- Where editable knowledge lives and how a user requests changes to it.
- Consequential recommendations, unresolved choices, and planned verification.

Show actual proposed instruction excerpts, not only descriptions of what files will
contain. Label them as proposed and make omissions clear. Keep the proposal small
enough to evaluate, but do not hide important gates or maintenance behavior.

Split independently selected capabilities when useful. Do not split shared stages
into separate workflows merely because intake differs. A cohesive small skill may
need only SKILL.md; additional files must have a purpose.

## 4. Refine and obtain approval

Invite focused feedback on the proposed boundaries and instruction shapes. Revise
the affected excerpts and file tree together. Incorporate feedback visibly rather
than restarting the discussion or repeatedly asking settled questions.

Ask for approval of the resulting proposal and wait. Praise, a clarification, or
approval of the general idea does not authorize writing. Approval of a subset
covers only that subset. If implementation reveals a consequential change to the
approved behavior or structure, surface it before proceeding with that change.

## 5. Write the approved package

Create the agreed files at the resolved destination, following local conventions.
Keep the description, frontmatter, entry-point routing, procedures, and knowledge
files consistent. Use relative links within the package and ensure every required
supporting file is included.

Do not install the skill, modify unrelated skills, or publish remotely merely
because skill creation was approved. Commit completed changes after verification
using the policy in conventions.md.

## 6. Verify

Check frontmatter parsing, the name/directory relationship, and supporting-file links.
Where the target harness is available, check that it recognizes the intended invocation
metadata. Do not claim cross-harness enforcement from a field's presence alone.

Exercise representative scenarios using the resulting instructions, not just the plan:

- A normal invocation reaches the intended outcome or approval checkpoint.
- An ambiguous input produces a focused question rather than a silent scope choice.
- A gated workflow stops before execution when consent is absent or declined.
- A request to update knowledge reaches its owning file without running the main task.

Select scenarios applicable to the produced skill. For issueskill itself, cover both
fresh creation and extraction, the activation question, destination ambiguity, and
proposal approval before writes. Walkthroughs or isolated model exercises can expose
instruction gaps; distinguish them from actual harness invocation tests.

Correct gaps before delivery and remove any throwaway verification artifacts.

## 7. Commit and deliver

After verification, commit the completed skill change using the policy in
conventions.md. Keep separate skill changes in separate commits.

Report the affected files, verification performed, and commit hash. If committing
is blocked, report the completed file changes and the remaining blocker explicitly.
Do not claim the skill is installed or reliably enforced by a harness that was not
exercised.
