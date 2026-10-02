# Vice catalogue

Signals the Investigate step looks for. Each one is a reason to recover a part's
purpose, not proof that it is cruft. Add, revise, or remove entries on request; do
not add findings to this file during a run.

## Remnants and migrations

Look for unreachable or unreferenced code, duplicate old and new
implementations, settled feature flags and version gates, compatibility shims,
aliases, migration bridges, commented-out code, stale TODOs, and tests or docs
for retired behavior.

## Convention drift

Look for competing ways to handle validation, errors, logging, async work,
state, configuration, serialization, identifiers, time, and null/default
semantics. Check naming, file layout, API shapes, copied boilerplate, mixed
library generations, and local utilities that duplicate the established
project path. A difference qualifies only when the alternatives solve the same
problem under the same constraints.

## Abstraction bloat

Look for pass-through wrappers, interfaces with one implementation, factories
or registries with one entry, one-call helpers that obscure rather than name
behavior, hypothetical plugin or DI machinery, checks for impossible states,
fallbacks that conceal stable invariants, conversion chains, and caching or
concurrency with no current consumer or requirement.

## Data and dependency residue

Look for fields that are written but never read or always carry one default,
old-pipeline fields in DTOs, domain models, or storage, redundant mapping and
encode/decode round trips, legacy endpoints and parameters, obsolete service
clients, unused packages and scripts, stale environment variables and
permissions, and mocks, fixtures, snapshots, type escapes, or lint suppressions
that exist only for removed behavior.

## Behavioral and operational cruft

Look for broad catches, swallowed errors, log-and-continue branches, fallbacks
that mask invalid configuration, duplicated sources of truth, competing entry
points, order-dependent initialization, mutable sentinels, global escape
hatches, legacy retries or polling, and orphaned jobs, queues, topics, telemetry
hooks, or vendor-specific paths.
