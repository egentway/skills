---
name: implementation-planning
description: >-
  Map an agreed plan onto the repository: where each part lives, how the parts
  connect, in what order the work lands, and how each step is proven. Use once
  the idea is settled, before implementation; the user approves the result.
---

Map an agreed plan onto this repository as a connected implementation the user
approves before any code is written. Deciding what to build happens before this
skill; this skill settles how it fits.

<!-- workflow-instructions 5 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`.

When starting a workflow, record its steps by name in your task-list tool before
the first step; load or enable the tool if needed. Reuse this run's entries when
resuming, and update them as the run progresses. If the harness provides no
task-list tool, continue without one.

Track the outermost workflow. A called workflow keeps the caller's step in
progress; show its current inner step in that entry's description, or its label
if descriptions are unavailable. Do not add a second list of inner steps. Keep
a step in progress while its Gate awaits the user; complete it only after its
output and gate are settled.
<!-- workflow-instructions end -->

# Operations

## Approve

Present what was produced up to this point, then stop and wait for the user. Their
response applies to this gate only.

# Steps

## Ground

Recover what was agreed and inspect the code it lands in.

- **Input:** the prior discussion, source study, or agreed design; the repository.
- **Output:** the observable outcome, its exclusions, and the parts of the
  repository the change touches.

1. Recover the relevant discussion. Distinguish agreed requirements,
   recommendations, unresolved choices, and superseded designs. Carry forward the
   user's decisions, terminology, constraints, and exclusions; a reference
   catalogue is evidence, not approval to implement every capability.

2. Inspect the current entry points, public interfaces, composition, ownership,
   configuration, tests, and documentation the change needs. Follow the
   repository's source-navigation rules. Do not assume earlier prose or
   remembered APIs still describe the checkout.

3. State the observable outcome and the explicit exclusions. Name meaningful
   limits such as volatile state, offline-only operation, unsupported inputs,
   missing integrations, or lack of hardware verification.

4. Resolve choices through established conventions. If materially different
   scopes remain plausible, ask one focused scope question with a recommendation
   before designing their interfaces. Do not turn routine naming into a
   questionnaire, and do not silently narrow the request to the easiest slice.

5. Name unavailable contracts or evidence. Do not hide missing protocol,
   hardware, or product requirements behind invented adapters or placeholder APIs.

## Divide

Split the work into units the user can evaluate separately, when such units are
obvious.

- **Input:** the outcome and touched parts from Ground.
- **Output:** one or more units, each with its outcome, exclusions, and
  dependencies on the others.

Look for distinct outcomes, not different files, layers, or implementation
steps. If the change is one cohesive unit, keep one. Division must not quietly
defer a requested unit or turn it into an unspecified follow-up.

- Keep a behavior change with the callers, tests, and documentation that make it
  complete.
- Units may depend on one another; name the prerequisite and the interface or
  result it supplies.
- For a shared interface or file, name which unit introduces the contract, which
  units consume or change it, and where their integration is verified.
- If a split needs temporary shims, broken intermediate states, or repeated
  explanations of inseparable behavior, keep that work in one unit.

## Design

Work out how each unit fits the existing code.

- **Input:** the units from Divide.
- **Output:** for each unit, its parts, where they live, and how control and data
  pass between them.

1. Start from the real entry point and the user-visible result, then the code
   that connects the parts, then its collaborators. Several parts may live in one
   existing file; do not create a file or abstraction only to give a part a home.

2. Define new APIs as intentional contracts with named owners and consumers.
   Ground existing APIs in source; do not assume a framework method exists
   because it would make the sketch convenient.

3. Follow the repository's architecture, not a structure imposed by this skill.

4. Trace one successful operation and one meaningful rejection or failure
   through the design, and check that:

   - required state has a clear owner and a visible acquisition path;
   - composition actually supplies the dependencies consumers need;
   - a changed public interface includes its affected callers and tests;
   - a delayed reaction cannot decide whether an earlier operation was valid.
     Where events are used, distinguish input receipt, accepted change,
     delivery, and external acknowledgement.

## Sequence

Order each unit's work so every step can be proven.

- **Input:** the designs from Design; the repository's verification rules.
- **Output:** a compact implementation sequence for each unit.

Each step names the behavior it delivers, any real dependency on earlier steps,
and the command, scenario, or focused test that will demonstrate it.

Distinguish planned verification from checks already run during investigation,
and name the hardware, services, credentials, or input contracts that stronger
claims would need. Include affected existing tests and worthwhile regression
cases; do not add tests that only assert the sketch's wiring. Include the
documentation, configuration, and packaging changes the work actually requires;
do not invent migrations, compatibility layers, or version bumps.

## Present

Show the plan and settle what is approved.

- **Input:** the units, designs, and sequences.
- **Output:** the plan in the conversation, and the units the user approved.
- **Gate:** **Approve** before any implementation.

1. Present the plan as present-for-review describes. For divided work, name the
   units the approval question covers.

2. A request to revise is not approval: revise the affected parts and present
   them again.

3. Approval of some units covers only those. Implement an approved unit only
   when its prerequisites are available or also approved, and keep the others
   visible as pending.

Keep the plan in the conversation unless the user asks for a file or the
repository requires one. This skill does not authorize design documents, a Git
workflow, commits, or installing dependencies.
