# Issue a skill

Use these steps with [conventions.md](conventions.md). Creation from a brief and
extraction from ongoing work share this process; only their starting evidence differs.
Shape every message to the user as [presentation.md](presentation.md) describes, and
run checks as [verification.md](verification.md) describes.

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
locate the skills repository by checking `~/skills` and `~/Projects/skills`,
expanding `~` to the current user's home:

- Exactly one is an existing directory: use it.
- Both are directories: resolve their real paths. If they name the same directory,
  use it; otherwise ask which repository to use.
- Neither is a directory: ask for a destination. Do not silently create a repository
  or use the current project instead.

Skills live in bundles: `<repository>/plugins/<bundle>/skills/<skill-name>/`. Pick
the bundle from the directories under `<repository>/plugins/`:

- Exactly one bundle: use it.
- Several: recommend the best fit for the skill's purpose and ask which to use.
- None, or the skill fits no existing bundle: propose a new bundle in the proposal.
  Creating one means its manifests and a `marketplace.json` entry, so it needs the
  same approval as any other file. Do not create a bundle silently.

An explicit destination is not permission to create a missing repository. Surface
unavailable destinations before writing. No configuration file or Nix integration
is required. If an explicit destination is already a `skills/` directory, use it as
given. The output is `<bundle>/skills/<skill-name>/`; if it already exists, ask
whether to revise that skill or choose another name rather than overwriting it as
a new package.

Resolve scope and activation from the conversation and local conventions first, and
record what they settle as assumptions the user can veto. When activation is unclear,
ask whether the produced skill should be request-driven, recommending automatic
applicability. Do not skip this question just because a default exists. Separately
decide whether automatic activation needs an execution-confirmation gate; see
conventions.md.

Infer only what is obvious, and ask what materially affects the skill. Collect every
open decision into one decisions message with recommendations, as presentation.md
describes. Use reasonable local conventions for routine details; do not turn
authoring into a fixed questionnaire.

## 3. Present a reviewable proposal

Present the proposal in the conversation before creating files, in the shape
presentation.md defines: main path first, representative proposed excerpts, the
bundle and invocation metadata for each target harness, where editable knowledge
lives, and a map of affected files ending in an approval question.

Split independently selected capabilities when useful. Do not split shared stages
into separate workflows merely because intake differs. A cohesive small skill may
need only SKILL.md and a compact proposal; additional files must have a purpose.

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

Run the checks in [verification.md](verification.md): structure, discovery, and
behavior proportional to risk. They are the agent's work and are reported as results.
Ask the user only for an action that needs authorization, such as a forward-test,
using the ask format defined there. Correct gaps before delivery.

## 7. Commit and deliver

After verification, commit the completed skill change using the policy in
conventions.md. Keep separate skill changes in separate commits.

Finish with the results-list report from presentation.md: affected files, checks run
and not run, commit hash, and open items. If committing is blocked, report the
completed file changes and the remaining blocker explicitly. Do not claim the skill
is installed or reliably enforced by a harness that was not exercised.
