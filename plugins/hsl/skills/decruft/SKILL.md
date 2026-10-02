---
name: decruft
description: >-
  Decruft code by finding implementation remnants, convention drift, needless
  abstractions, stale data or dependencies, and legacy runtime paths. Use when
  the user asks to decruft, remove stale or legacy code, investigate
  suspiciously useless code, or reconcile competing old and new patterns.
---

Decruft code: find parts whose present reason is missing or obsolete, confirm
them with the user, and remove whole obsolete paths. Suspicion starts an
investigation; it is not permission to delete. To add, revise, or remove a vice,
edit [catalogues/vice-catalogue.md](catalogues/vice-catalogue.md) without starting
a run.

<!-- workflow-instructions 3 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`.
<!-- workflow-instructions end -->

# Operations

## Approve
Present what was produced up to this point, then stop and wait for the user. Their
response applies to this gate only.

# Steps

## Bound
Settle where to look.
Use the boundary named by the user. Otherwise, treat the repository as the
boundary and follow its entry points into concrete subsystems rather than
sampling files at random.

## Investigate
Recover why each suspicious part exists, looking for the signals in
[catalogues/vice-catalogue.md](catalogues/vice-catalogue.md).

### Current reasons
Recover each suspicious part's current reason from the current tree: callers and
references, runtime entry points, tests, configuration, schemas, docs,
generated-code boundaries, and nearby implementations of the same job. Determine
whether an outlier is chronological drift or an intentional bounded-context
difference.

### Archaeology
Use targeted archaeology when the current tree suggests a replacement, migration,
rollout, or unexplained compatibility path. Inspect the history that introduced
the candidate, the likely replacement, and the surrounding convention. History
explains intent; current callers and contracts decide whether that intent is
still live.

## Cluster
Group candidates by theme, or stop if there are none.
Build evidence-backed candidate clusters. Group items that appear to belong to
the same old implementation, service, migration, or competing convention. If the
survey finds no evidence-backed candidates, say so, name the areas and evidence
checked, and skip the remaining steps. Do not manufacture cleanup to justify the
run.

### Candidate evidence
For every candidate, establish:

- **Location:** exact paths and symbols in the cluster.
- **Present cost:** duplicated behavior, maintenance burden, dependency,
  ambiguity, runtime branch, or cognitive load it creates now.
- **Current reach:** callers, dynamic/framework reachability, tests, contracts,
  configuration, stored data, and possible out-of-repository consumers.
- **Likely origin:** the old implementation, migration, service, or convention,
  with history evidence when available.
- **Uncertainty:** the specific fact that repository evidence cannot establish.
- **Proposed cut:** the complete deletion or convergence boundary if the user
  confirms the candidate is obsolete.

Label facts, inferences, and unknowns distinctly. A zero-reference symbol may be
reached by reflection, framework registration, generated code, external clients,
or persisted data. A referenced symbol may sit inside an entirely dead chain.
Newer code is not automatically the convention; prefer explicit project rules
and repeated comparable implementations over chronology alone.

## Review
Present one theme at a time and **Approve** each; make no edits before its answer.
Ask only what the tree and targeted history cannot settle.

### Checkpoint format
Present related candidates together:

```markdown
### <old path, migration, service, or convention>
- **Found:** <exact symbols and present cost>
- **Current reach:** <callers, contracts, and external-use risk>
- **Likely history:** <replacement or migration evidence>
- **Unresolved:** <what the repository cannot prove>
- **Proposed cut:** <everything removed or migrated if obsolete>
```

### Questions
Use the structured question tool for focused questions such as:

- What present constraint still requires `<candidate>`? Was it retained for
  that constraint, or left by `<previous implementation>`?
- Does `<legacy service or API>` still have consumers outside this repository?
- Is `<outlier pattern>` intentionally different for this domain, or an
  incomplete migration to `<established pattern>`?
- Must `<field, endpoint, or adapter>` remain compatible with stored data or
  older clients?

Recommend a disposition when the evidence supports one. Offer **remove**,
**retain with its recovered reason**, or **investigate a named unknown** as
concrete outcomes; do not turn the checkpoint into an open-ended code tour.

## Cut
Apply only the approved cleanup.
Remove the whole obsolete path: callers, adapters, flags, configuration, tests,
fixtures, docs, dependencies, and exports that exist solely for it. Migrate live
callers to the surviving convention and leave one path, without compatibility
shims or aliases unless the user explicitly preserves them.

## Verify
Show the cut works and report what remains.
Exercise the affected behavior and run the narrow project checks that cover the
cut. Report approved removals, verification evidence, and untouched candidates
whose purpose remains unresolved.
