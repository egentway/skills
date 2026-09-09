---
name: decruft
description: >-
  Decruft code by finding implementation remnants, convention drift, needless
  abstractions, stale data or dependencies, and legacy runtime paths. Use when
  the user asks to decruft, remove stale or legacy code, investigate
  suspiciously useless code, or reconcile competing old and new patterns.
---

# Decruft

Cruft is code whose present reason is missing or obsolete. Suspicion starts an
investigation; it is not permission to delete.

## Workflow

1. Use the boundary named by the user. Otherwise, treat the repository as the
   boundary and follow its entry points into concrete subsystems rather than
   sampling files at random.
2. Recover each suspicious part's current reason from the current tree:
   callers and references, runtime entry points, tests, configuration, schemas,
   docs, generated-code boundaries, and nearby implementations of the same job.
   Determine whether an outlier is chronological drift or an intentional
   bounded-context difference.
3. Use targeted archaeology when the current tree suggests a replacement,
   migration, rollout, or unexplained compatibility path. Inspect the history
   that introduced the candidate, the likely replacement, and the surrounding
   convention. History explains intent; current callers and contracts decide
   whether that intent is still live.
4. Build evidence-backed candidate clusters from the vice catalog. Group items
   that appear to belong to the same old implementation, service, migration, or
   competing convention.
5. Present one compact approval checkpoint per theme. Ask only what the tree and
   targeted history cannot settle. Wait for the user's answer before editing
   that cluster.
6. Apply only the approved cleanup. Remove the whole obsolete path: callers,
   adapters, flags, configuration, tests, fixtures, docs, dependencies, and
   exports that exist solely for it. Migrate live callers to the surviving
   convention and leave one path, without compatibility shims or aliases unless
   the user explicitly preserves them.
7. Exercise the affected behavior and run the narrow project checks that cover
   the cut. Report approved removals, verification evidence, and untouched
   candidates whose purpose remains unresolved.

If the survey finds no evidence-backed candidates, say so and name the areas
and evidence checked. Do not manufacture cleanup to justify the run.

## Vice catalog

### Remnants and migrations

Look for unreachable or unreferenced code, duplicate old and new
implementations, settled feature flags and version gates, compatibility shims,
aliases, migration bridges, commented-out code, stale TODOs, and tests or docs
for retired behavior.

### Convention drift

Look for competing ways to handle validation, errors, logging, async work,
state, configuration, serialization, identifiers, time, and null/default
semantics. Check naming, file layout, API shapes, copied boilerplate, mixed
library generations, and local utilities that duplicate the established
project path. A difference qualifies only when the alternatives solve the same
problem under the same constraints.

### Abstraction bloat

Look for pass-through wrappers, interfaces with one implementation, factories
or registries with one entry, one-call helpers that obscure rather than name
behavior, hypothetical plugin or DI machinery, checks for impossible states,
fallbacks that conceal stable invariants, conversion chains, and caching or
concurrency with no current consumer or requirement.

### Data and dependency residue

Look for fields that are written but never read or always carry one default,
old-pipeline fields in DTOs, domain models, or storage, redundant mapping and
encode/decode round trips, legacy endpoints and parameters, obsolete service
clients, unused packages and scripts, stale environment variables and
permissions, and mocks, fixtures, snapshots, type escapes, or lint suppressions
that exist only for removed behavior.

### Behavioral and operational cruft

Look for broad catches, swallowed errors, log-and-continue branches, fallbacks
that mask invalid configuration, duplicated sources of truth, competing entry
points, order-dependent initialization, mutable sentinels, global escape
hatches, legacy retries or polling, and orphaned jobs, queues, topics, telemetry
hooks, or vendor-specific paths.

## Candidate evidence

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

## Approval checkpoint

Present related candidates together:

```markdown
### <old path, migration, service, or convention>
- **Found:** <exact symbols and present cost>
- **Current reach:** <callers, contracts, and external-use risk>
- **Likely history:** <replacement or migration evidence>
- **Unresolved:** <what the repository cannot prove>
- **Proposed cut:** <everything removed or migrated if obsolete>
```

Then use the structured question tool for focused questions such as:

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
