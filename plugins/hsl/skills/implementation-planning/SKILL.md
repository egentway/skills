---
name: implementation-planning
description: >-
  Turn a prior discussion, source study, or agreed design into an implementation
  plan the user reviews and approves before any implementation begins.
---

# Implementation planning

Make a plan the user can evaluate as a connected implementation, not a list of
promises. Show what each part does, where it lives, and how control and data pass
between parts.

This is a working draft. Refine it through observed planning and implementation
feedback; do not present an untried process as validated practice.

## Working contract

- Plan first. Do not implement until the user approves the plan.
- Carry forward the user's decisions, terminology, constraints, and exclusions.
  A reference catalogue is evidence, not approval to implement every capability.
- When the work has obvious, coherent task boundaries, give each unit a separate
  reviewable plan. Keep tightly coupled changes together; do not force a split.
- The plan is design content: its code excerpts are proposed, not edits already
  made. Present the finished plan using the `present-for-review` skill. If it is
  unavailable, present the plan with the main path first, labeled excerpts, a file
  map, and an approval question. A request to revise the plan is not approval to
  implement.
- Treat implementation complexity as review feedback, not merely an internal
  concern. Surface meaningful growth while the user can still influence it, and
  carry unresolved concerns into the final handoff.

## 1. Ground the scope and repository boundaries

Before drafting:

1. Recover the relevant discussion and distinguish agreed requirements,
   recommendations, unresolved choices, and historical or superseded designs.
2. Inspect the current entry points, public interfaces, composition, ownership,
   configuration, tests, and documentation needed for this change. Follow the
   repository's source-navigation and reference-checking rules. Do not assume
   previous prose or remembered APIs still describe the checkout.
3. State the observable outcome and the explicit exclusions. Name meaningful
   limits such as volatile state, offline-only operation, unsupported inputs,
   missing integrations, or lack of hardware verification.
4. Resolve choices through established conventions when possible. If materially
   different scopes remain plausible, ask a focused scope question before
   designing their interfaces. Recommend an option and explain its tradeoff.
5. Identify unavailable contracts or evidence. Do not hide missing protocol,
   hardware, or product requirements behind invented adapters or placeholder APIs.

Do not turn routine naming and local implementation choices into a questionnaire.
Conversely, do not silently narrow the user's request to the easiest slice.

### Divide obvious units of work before drafting

Look for distinct outcomes the user can evaluate separately, not merely different
files, layers, or implementation steps. When those units are obvious, present
separately titled task plans rather than one undifferentiated walkthrough. If the
change is one cohesive unit, keep one plan.

Preserve the full agreed scope. Division must not quietly defer a requested unit
or turn it into an unspecified follow-up.

Each task plan is a complete plan: its own scope and exclusions, main path,
connections, implementation sequence, verification, and planned file impact. A task
heading over a checklist is not a separate plan. Shared context and contracts may be
explained once and referenced explicitly rather than copied into every plan.

Keep the boundaries honest:

- Keep a behavior change with the callers, tests, and documentation needed to
  make it complete. Do not split those into separate tasks merely by file type.
- Units may depend on one another; separate review does not imply independent
  execution. Name the prerequisite and the interface or result it supplies.
- For shared interfaces or files, identify which unit introduces the contract,
  which units consume or change it, and where their integration is verified.
- If a proposed split requires temporary shims, broken intermediate states, or
  repeated explanations of inseparable behavior, keep that work in one plan.

Present all task plans for review unless the user asks for a staged discussion.
Do not stop after outlining the first unit. Separate plans do not themselves
require separate documents, branches, commits, or agents; follow any enabled
workflow for those decisions.

For small-to-medium tasks, generally plan to do the work directly rather than
delegate it to a subagent. Task division is for reviewability, not an automatic
agent assignment. Delegate only when there is a concrete benefit, such as
substantial independent work that can genuinely run in parallel, and that benefit
outweighs the handoff, coordination, and integration overhead. Do not delegate a
bounded task merely because a subagent is available. Respect explicit user
requests and applicable repository rules about delegation.

## 2. Design content a code plan must contain

Name the real entry point and the user-visible result. Show the connecting code
early, for example the application composition or main operation that ties the
components together, then its collaborators. Several parts may live in one existing
file; do not create a file or abstraction merely to give each part a home. Include
each repository root when the work spans projects.

Retain the information that makes the design reviewable:

- Public types, function signatures, significant fields, and return semantics.
- Dependency direction and resource construction/cleanup.
- The order of validation, decisions, mutation, and downstream work.
- Important accepted, rejected, pending, or failed outcomes, where applicable.
- Concrete call sites and argument flow across the proposed boundaries.

New APIs are allowed: defining them is part of the plan. Make them intentional,
coherent proposed contracts, with named owners and consumers. Existing APIs must
be grounded in source. Do not assume a framework method exists because it would
make the sketch convenient.

Avoid empty bodies and magical helpers that conceal the central work. If a helper
is the substantive operation, show its structure or describe its precise invariant
and result. An abridged plan is not permission to ship stubs, fake fallbacks, or
unimplemented branches.

Before finishing the draft, trace at least one successful operation and one
meaningful rejection/failure through the design. Check that:

- Signatures, names, arguments, and result types agree across the plan.
- Required state has a clear owner and a visible acquisition path.
- Composition actually supplies the dependencies that consumers need.
- A changed public interface includes its affected callers and tests.
- A delayed reaction cannot accidentally decide whether an earlier operation
  was valid. Where events are used, distinguish input receipt, accepted change,
  delivery, and external acknowledgement according to the project's contracts.

Use the repository's architecture, not a universal framework imposed by this
skill. Do not encode one project's module or event design as a requirement for
unrelated projects.

## 3. Connect implementation order to proof

Give a compact implementation sequence. Each step names:

- The behavior it delivers.
- Any real dependency on earlier steps.
- The command, scenario, or focused test that will demonstrate it.

Verification must match the changed surface and repository rules. Distinguish
planned verification from checks actually executed during investigation. Name
hardware, services, credentials, or input contracts required for stronger claims.

Include affected existing tests and worthwhile new regression cases. Do not add
tests merely to assert the sketch's wiring or source text. Include documentation,
configuration, and packaging consequences where the change actually requires them.
Do not invent migrations, compatibility layers, version bumps, or extra machinery.

## 4. Cover the planned impact

The plan's file impact covers production code, tests, documentation,
configuration/build changes, and required package markers; do not hide those under
an unexplained directory. Mark new test and document filenames as proposed when the
plan is still selecting them. Call out the main integration risk, such as a
signature change, package move, persistence boundary, or external contract. For
divided work, annotate shared files with the task plans that affect them.

## 5. Approval

For divided work, name the task plans covered by the approval question. The user
may approve the set or a named subset; approval of one does not approve the rest.
Implement only approved units whose prerequisites are already available or also
approved. Keep unapproved units visible as pending, not silently dropped.

Present the plan in the conversation unless the user requests a file or repository
rules require a planning artifact. This skill does not itself authorize creating
design documents, running a Git workflow, committing, or installing dependencies.

## 6. Implement against the plan and refine the process

After approval, follow the repository's implementation and verification rules.
Use the plan as the agreed contract, not a reason to ignore new evidence.

- Resolve routine details autonomously using local conventions.
- Carry the direct-execution default above into implementation. Separate approved
  task plans do not by themselves justify handing each task to a subagent.
- Surface consequential changes before they spread through callers or schemas.
  Explain the discovered seam, viable choices, recommendation, and impact on the
  plan. Obtain approval when the change alters the agreed behavior or boundary.
- Do not conceal a broken integration behind wrappers, duplicated state, implicit
  ordering, or special-case fallbacks.
- At delivery, distinguish actual changes and exercised behavior from the plan.
  Explain meaningful deviations and remaining verification limits.

### Check complexity as the implementation takes shape

An approved sketch may turn into code that is harder to understand than the plan
suggested. Watch for long classes or methods, deep nesting, proliferating state
flags, duplicated ownership, wrapper chains, and custom machinery that overlaps
with a framework's responsibilities. These are inspection signals, not automatic
defects or fixed line-count limits.

Evaluate the implementation, not just its public interface. A two-method helper
can hide a substantial state machine. Explain which requirements create the
complexity and whether the abstraction removes work or merely moves it out of
sight. Do not call complexity necessary or minimal without evaluating plausible
alternatives.

**During implementation:**

- Report a meaningful complexity hotspot when it becomes concrete, especially
  when a user-approved change to a requirement, boundary, dependency, or code
  shape could simplify it.
- Name the file/symbol, the mechanism that grew, and its maintenance or
  correctness cost. Distinguish complexity required by the contract from
  complexity introduced by the chosen implementation.
- Keep the checkpoint small: show the relevant structure or ownership split,
  state what is still working, and recommend whether to continue provisionally,
  simplify locally, or reconsider the boundary.
- Ask before a consequential change spreads. A bounded, understood concern need
  not stop implementation; a correctness problem or unresolved integration hack
  must not be deferred merely to preserve momentum.
- Do not add abstractions, split files, or compress code solely to improve a size
  metric. Judge whether the reader has less to reconstruct afterward.

**At delivery:**

- Report material concerns that remain, including those not worth interrupting
  implementation for. Lack of a mid-task checkpoint is not a reason to omit them.
- State the hotspot, why it exists, what was verified, and what remains a design
  judgment. Identify the next useful review boundary rather than offering a vague
  warning that the code is "complex."
- Carry forward any provisional acceptance explicitly. Approval to try an
  implementation does not establish that its resulting design is satisfactory.
- Keep behavioral proof separate from design confidence: passing checks do not
  establish maintainability, and a small API does not establish simple internals.

Do not manufacture a complexity concern or a mandatory status paragraph when
nothing meaningful emerged. The purpose is timely, concrete feedback, not
ceremony or a claim that the implementation is the simplest possible.

### Refine the process from observed feedback

When the user wants this process refined, use concrete feedback and observed
implementation outcomes. Ask which excerpts made review easier, which connections
were missing, whether the impact predicted the actual result, and where approval
failed to settle an important choice. Add reusable lessons, not project-specific
architecture or one-off incidents. Do not claim a successful outcome before it
has been observed.

Use applicable repository and workflow instructions alongside this skill. This
skill supplies what a code plan must contain, not a competing engineering or Git
policy.
