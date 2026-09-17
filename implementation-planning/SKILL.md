---
name: implementation-planning
description: >-
  Turn a prior discussion, source study, or agreed design into a reviewable
  implementation plan. Use when the user wants explanations interleaved with
  abridged code, explicit existing/new file paths, visible connections between
  components, a final blast-radius file tree, and approval before implementation.
---

# Implementation planning

Make a plan the user can evaluate as a connected implementation, not a list of
promises. Show what each part does, where it lives, and how control and data pass
between parts. End with the planned file impact and an explicit approval question.

This is a working draft. Refine it through observed planning and implementation
feedback; do not present an untried process as validated practice.

## Working contract

- Plan first. Do not implement until the user approves the plan.
- Carry forward the user's decisions, terminology, constraints, and exclusions.
  A reference catalogue is evidence, not approval to implement every capability.
- When the work has obvious, coherent task boundaries, give each unit a separate
  reviewable plan. Keep tightly coupled changes together; do not force a split.
- Interleave explanations and abridged code. Neither a prose-only checklist nor
  a disconnected collection of snippets is sufficient.
- Label every code excerpt with its project-relative file path and whether the
  file is existing, new, moved, or removed. Separate proposed code from current code.
- Show the connections: callers, arguments, results, ownership, composition,
  lifecycle, and the important rejection/failure paths.
- End the plan with a brief blast-radius tree, then ask for approval and wait.
- A request to revise the plan, or praise for its presentation, is not approval
  to implement. Approval of scope is not approval of the finished plan either.
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

Start with a compact overview naming all units, their outcomes, and their real
dependencies or implementation order. Preserve the full agreed scope. Division
must not quietly defer a requested unit or turn it into an unspecified follow-up.

Each task plan follows the presentation contract below: its own scope and
exclusions, main path, explanation interleaved with abridged code, connections,
implementation sequence, verification, and planned file impact. A task heading
over a checklist is not a separate plan. Shared context and contracts may be
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

## 2. Present the main path first

Begin the plan with the selected scope and a short end-to-end flow. Name the real
entry point and the user-visible result. Follow that flow through the explanation
rather than touring files alphabetically.

Then show the connecting code early: for example, the application composition or
main operation that ties the components together. Introduce its collaborators in
the sections that follow. Use the same names and signatures throughout.

For each substantive section, include:

- **Responsibility:** what this part owns and why it belongs here.
- **Location:** exact existing or proposed path; include each repository root when
  the work spans projects.
- **Abridged code:** the relevant structure and interface, not all implementation
  details.
- **Connection:** what calls or constructs it, what it depends on, what it returns
  or publishes, and who uses that result.
- **Consequential choice:** any behavior or boundary the user should evaluate.

Do not create a new file or abstraction merely to give each section its own home.
Several sections may describe different parts of one existing file.

## 3. Make abridged code honest and useful

Introduce the excerpts as proposed design code, not edits already made or a
compilable implementation. Mark any current-code comparison separately.

Retain the information that makes the design reviewable:

- Public types, function signatures, significant fields, and return semantics.
- Dependency direction and resource construction/cleanup.
- The order of validation, decisions, mutation, and downstream work.
- Important accepted, rejected, pending, or failed outcomes, where applicable.
- Concrete call sites and argument flow across the proposed boundaries.

Omit routine imports, repetitive fields, boilerplate, and secondary branches.
Explain what is omitted when its absence could mislead the reader. If a condition
is essential to correctness, show it or explicitly describe where it is enforced;
never make an unsafe happy path look like the intended complete behavior.

New APIs are allowed: defining them is part of the plan. Make them intentional,
coherent proposed contracts, with named owners and consumers. Existing APIs must
be grounded in source. Do not assume a framework method exists because it would
make the sketch convenient.

Avoid empty bodies and magical helpers that conceal the central work. If a helper
is the substantive operation, show its structure in the next section or describe
its precise invariant and result. An abridged plan is not permission to ship
stubs, fake fallbacks, or unimplemented branches.

Before presenting, trace at least one successful operation and one meaningful
rejection/failure through the excerpts. Check that:

- Signatures, names, arguments, and result types agree across sections.
- Required state has a clear owner and a visible acquisition path.
- Composition actually supplies the dependencies that consumers need.
- A changed public interface includes its affected callers and tests.
- A delayed reaction cannot accidentally decide whether an earlier operation
  was valid. Where events are used, distinguish input receipt, accepted change,
  delivery, and external acknowledgement according to the project's contracts.

Use the repository's architecture, not a universal framework imposed by this
skill. Do not encode one project's module or event design as a requirement for
unrelated projects.

## 4. Connect implementation order to proof

After the walkthrough, give a compact implementation sequence. Each step names:

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

## 5. Finish with the blast-radius map

Place a brief tree of impacted files immediately before the approval checkpoint.
The tree is the compact index of the preceding plan, not an additional scope list.
For divided work, give each task plan its own map, then finish the overall
presentation with a compact combined tree before asking for approval. Annotate
shared files with the tasks that affect them so overlap remains visible.

Use a legend such as:

- `+` new file
- `~` existing file modified
- `-` file removed
- `>` file moved; show old and new paths

Illustrative format, not a claim about the user's repository:

```text
src/package/
├── application.py                 ~ Connect the capability
└── feature/
    ├── models.py                  + Public data and result contracts
    └── service.py                 + Operations and owned state

tests/package/
└── feature/test_service.py         + Behavioral regression cases

docs/
└── feature.md                     + Usage and ownership guidance
```

Map requirements:

- Cover production code, tests, documentation, configuration/build changes, and
  required package markers. Do not hide those under an unexplained directory.
- Mark new test/document filenames as proposed when their exact names are being
  selected by this plan.
- Add a short responsibility/change annotation to each file. Keep the tree
  shallow through grouped common prefixes, without losing exact locations.
- Keep it consistent with every code excerpt and interface migration above.
- Add a short **Intentionally untouched** list for adjacent areas a reader might
  reasonably expect to change. Do not list the whole repository.
- Call out the main integration risk, such as a signature change, package move,
  persistence boundary, or external contract.
- Label the map as planned impact, not completed edits. If a location cannot yet
  be resolved, expose that uncertainty rather than inventing a confident path.

## 6. Ask for approval, then respect the answer

End with a direct question, for example:

> Do you approve this plan for implementation, or would you like to change any
> of these boundaries or code shapes first?

Briefly identify consequential choices if they would otherwise be buried in the
walkthrough. Then stop. Do not edit implementation files while waiting.

For divided work, name the task plans covered by the approval question. The user
may approve the set or a named subset; approval of one does not approve the rest.
Implement only approved units whose prerequisites are already available or also
approved. Keep unapproved units visible as pending, not silently dropped.

If the user requests a change, update the relevant explanation, code connections,
verification, and blast-radius map together. Ask for approval of the revised plan.
Do not treat a presentation improvement as approval of the implementation scope.

Present the plan in the conversation unless the user requests a file or repository
rules require a planning artifact. This skill does not itself authorize creating
design documents, running a Git workflow, committing, or installing dependencies.

## 7. Implement against the plan and refine the process

After approval, follow the repository's implementation and verification rules.
Use the plan as the agreed contract, not a reason to ignore new evidence.

- Resolve routine details autonomously using local conventions.
- Surface consequential changes before they spread through callers or schemas.
  Explain the discovered seam, viable choices, recommendation, and impact on the
  plan/map. Obtain approval when the change alters the agreed behavior or boundary.
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
were missing, whether the map predicted the actual impact, and where approval
failed to settle an important choice. Add reusable lessons, not project-specific
architecture or one-off incidents. Do not claim a successful outcome before it
has been observed.

## Working with related skills

- `simple-planning`: preserves the plan-before-implementation approval gate.
- `cognitive-budget-coding`: keeps the main path, naming, and abstraction choices
  easy to evaluate. Proposed excerpts remain clearly distinguished from existing
  APIs and must form a grounded, coherent design.
- `feedback-driven-execution`: governs consequential choices discovered during
  implementation; it does not require asking about every routine detail.

Use applicable repository and workflow instructions alongside this skill. This
skill supplies the presentation and review contract, not a competing engineering
or Git policy.
