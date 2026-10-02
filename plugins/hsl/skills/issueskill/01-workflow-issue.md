# Issue a skill

Create from a brief or extract from ongoing work through the same authoring process.
Read [02-conventions.md](02-conventions.md) for package-design rules.
Skill authoring does not authorize installation, unrelated skill changes, pushing,
or remote publication; those require separate authorization.

# Steps

## Recover

Identify the intended capability and preserve relevant user decisions.

- **Input:** User brief or relevant conversation activity.
- **Output:** Capability, inputs, constraints, exclusions, and known limitations.

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

## Resolve

Settle the destination and consequential authoring choices.

- **Input:** Recovered capability and existing decisions.
- **Output:** Destination, bundle, scope, activation policy, and execution gates.
- **Stop if:** The destination is unavailable. Resolve required choices before proceeding.

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
given. An explicit destination that is a repository root goes through the same
bundle lookup. The output is `<bundle>/skills/<skill-name>/`; if it already exists, ask
whether to revise that skill or choose another name rather than overwriting it as
a new package.

Resolve scope and activation from the conversation and local conventions first, and
record what they settle as assumptions the user can veto. When activation is unclear,
ask whether the produced skill should be request-driven, recommending automatic
applicability. Do not skip this question just because a default exists. Separately
decide whether automatic activation needs an execution-confirmation gate; see
02-conventions.md.

Infer only what is obvious, and ask what materially affects the skill. Collect every
open decision into one decisions message with recommendations, as 03-presentation.md
describes. Use reasonable local conventions for routine details; do not turn
authoring into a fixed questionnaire.

## Propose

Show a connected, reviewable package before creating files.

- **Input:** Resolved capability and authoring choices.
- **Output:** Proposed package, representative instructions, and invocation example.

Read [03-presentation.md](03-presentation.md). Show the capability, inputs,
exclusions, activation policy and gates, and a short end-to-end invocation example.
Use the skill review view: entry, complete outline, and opened frontmatter, routing,
gates, and one procedure step. Identify each file's responsibility and connections,
the chosen bundle, metadata for each target harness, and where editable knowledge
lives and how the user requests changes to it.

A cohesive small skill gets a compact proposal. Split independently selected
capabilities when useful; do not split shared stages merely because intake differs.

## Refine

Incorporate feedback and settle the proposal.

- **Input:** Proposed package and user feedback.
- **Output:** Explicitly approved scope.
- **Gate:** Explicit approval of the resulting proposal before writing.

Incorporate feedback by revising affected excerpts and the file map together.
Preserve settled decisions rather than restarting the discussion.

Ask for explicit approval of the resulting proposal and wait. Praise, a clarification,
or approval of the general idea does not authorize writing. Approval of a subset
covers only that subset. If declined, revise with the user's feedback or stop without
writing. If later work reveals a consequential departure from the approved behavior
or structure, surface it and obtain approval before implementing that departure.

## Write

Produce the approved package at the resolved destination.

- **Input:** Approved proposal.
- **Output:** Complete package consistent with the agreed scope.

Create only the agreed files at the resolved destination, following
02-conventions.md. Keep discovery metadata, routing, procedures, and knowledge
consistent. Use relative links and include every required supporting file.

## Verify

Check that the package works as intended.

- **Input:** Written package and approved behavior.
- **Output:** Verified package and recorded limitations.

Read [04-verification.md](04-verification.md). Run structural, discovery, and
behavioral checks proportional to the change, including isolated forward-tests when
required. Correct observed gaps before delivery. Report checks as results; request
additional authorization only at the boundary defined there.

## Deliver

Commit the verified change and report the result.

- **Input:** Verified package and check results.
- **Output:** Commit and delivery report, or an explicit remaining blocker.

Commit the verified, coherent change using the policy in 02-conventions.md.
Keep separate skill changes in separate commits.

Deliver the results report from 03-presentation.md. If committing is blocked, report
the completed file changes and remaining blocker. Do not claim installation or
harness enforcement that was not exercised.
