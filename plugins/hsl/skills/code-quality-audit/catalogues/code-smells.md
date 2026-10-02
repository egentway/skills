# Code-smell catalogue

Inspection knowledge for [the audit workflow](../01-workflow-audit.md).
Signals require investigation, not automatic condemnation. Each entry provides
signals, consequences, evidence checks, and a bounded direction with exceptions.

## Competing rule owners

**Signals:** adapters and domain models check the same references; option queries
and mutation methods independently encode eligibility; defaults are resolved by
both caller and callee.

**Consequence:** policy changes can update one path and leave another behind;
callers receive conflicting answers or unnecessary validation work accumulates.

**Evidence:**

- Trace consumers and trust boundaries. Distinguish wire normalization, structural
  validity, and current-state eligibility; determine whether a check repeats an input
  guarantee.
- Follow scalar values and graph/reference rules from wire extraction through
  normalization, model and event construction, and owner admission. Identify owners of
  requiredness, type validity, ranges, references, and eligibility.
- Retain checks required before normalization: removing them must not turn malformed
  input into a valid default, sentinel, or unknown case, even with strict domain models.
- Compare accepted and rejected inputs of sibling boundary validators before declaring a
  shared rule. A shared function or type should remove real duplicate authority.
- For remnants after ownership moves, also consult Unclean integration.

**Direction:** prefer one owner per invariant. Keep boundary-specific checks where
they protect genuinely different guarantees. Do not remove validation merely
because the syntax is similar, or replace small duplication with a rules engine.

## Exception misclassification

**Signals:** a broad catch spans parsing, construction, and application work;
programming failures become expected rejection; errors are logged and processing
continues without an explicit failure policy.

**Consequence:** valid work may disappear while the application appears healthy;
diagnostics identify the wrong cause or expose untrusted payloads.

**Evidence:**

- Identify actual exception producers and caller responses. Establish producers before
  calling a handler redundant.
- When useful, probe classification with valid input and an isolated internal fault;
  distinguish implementation failures from input rejection.
- Check exception lists for subclasses already covered by a parent, catch-and-reraise
  branches with no producer in the protected region, and obsolete translations after
  responsibility moved.

**Direction:** translate expected input errors at narrow boundaries; let unexpected
failures reach their supervisor. Broad catches can be justified at resource owners
that must settle work and re-raise; inspect whether they preserve failures rather
than banning them categorically. Safe diagnostics need not mean erased causality.

## Cleanup machinery

**Signals:** repeated cancellation/shield loops, copied failure aggregation,
stored exceptions with implicit precedence, cleanup errors retrieved but ignored,
or resource owners attempting each other's recovery.

**Consequence:** independent failures can be lost; shutdown becomes hard to reason
about; fixing one copy leaves another inconsistent.

**Evidence:**

- Trace normal exit, body failure, cleanup failure, cancellation during cleanup, and
  combinations.
- Separate cleanup completion from propagation of its result. Compare resource ownership
  and cancellation requirements.

**Direction:** state precedence explicitly. Consolidate a truly shared settlement
invariant in a small primitive when duplication earns it. Do not build a lifecycle
framework or remove required settlement just to shorten code. Similar cleanup is
not necessarily equivalent for resources with different guarantees.

## Reader-hostile control flow

**Signals:** deeply nested branches, nested conditional expressions, overlapping
flags, long methods mixing decisions with effects, or helpers that move rather
than explain complexity.

**Consequence:** readers must simulate execution to discover the main operation or
remember distant conditions to judge correctness.

**Evidence:**

- Identify the normal path and invariant behind branches and flags. Use size or nesting
  to locate hotspots, separating required behavior from representation complexity.
- Look for flags and repeated scans indirectly expressing membership, coverage, or
  ordering. Compare with a direct expression while preserving semantics, ordering, and
  useful short-circuiting.
- A set-based rewrite is not inherently clearer or faster.

**Direction:** prefer early rejection, visible domain steps, and direct invariant
expressions. A linear field mapping or operation may be long without being hard
to understand. More functions and files can increase cognitive cost.

## Unclean integration

**Signals:** stale caller-side logic after an ownership change, redundant argument
forwarding, competing state, implicit startup order, or abstractions that hide an
incompatible lifecycle.

**Consequence:** maintainers cannot identify the authority for a decision; defaults
drift or correctness depends on incidental call order.

**Evidence:**

- Follow entry points through construction, dependency supply, operation, and shutdown.
  Compare claimed ownership with actual callers.
- Check whether explicit overrides intentionally differ from default resolution.
- After responsibility moves, inspect new owners and former callers for still-active
  default resolution, argument transformations, validation, or lifecycle work.
- For duplicated invariant authority, also consult Competing rule owners.

**Direction:** complete the ownership cutover and remove superseded paths. Keep
necessary lifecycle ordering explicit rather than inventing automatic wiring.
Do not remove meaningful overrides or reduce every integration to one universal
interface.

## Abstraction and representation overhead

**Signals:** pass-through wrapper chains, parallel models for the same purpose,
repeated encode/decode or copy operations, one-call helpers naming syntax rather
than invariants, and generic registries without current variation.

**Consequence:** extra concepts and file jumps obscure the behavior; duplicated
representations require synchronization and can diverge.

**Evidence:**

- Identify what abstractions protect and who consumes them. Distinguish protocol and
  domain representations; establish present use rather than hypothetical reuse.
- Follow a representative value through the operation. Framework construction can repeat
  validation, conversion, copying, or traversal even for an existing immutable object.
- Count invocations or transformations when uncertain. Observed repetition is not
  measured performance impact; it does not justify validation bypasses, caches, or
  parallel representations for small repeated costs.

**Direction:** retain abstractions that enforce an invariant, isolate a volatile
boundary, or name a substantial domain operation. Remove those whose cost exceeds
their present role. Do not replace removable helpers with another comprehensive
schema hierarchy merely to make the implementation look declarative.

### Duplicated class hierarchies

**Signals:** a second family of classes mirrors an existing model tree, with
corresponding nested entities, repeated fields and constraints, and field-by-field
conversion methods. A request for a typed boundary grows into a parallel hierarchy;
objects retain both representations or privately cache their converted counterpart.
This applies to composition trees as well as inheritance hierarchies.

**Consequence:** each domain change requires synchronized edits across model
families and translators. Validation ownership becomes unclear, objects undergo
repeated construction, and readers must reconstruct which representation is
authoritative and why both survive.

**Evidence:**

- Trace a complete payload from ingress to consumers. Identify independent operations,
  lifetimes, contracts, or serialization needs for each representation.
- Different field names or wire formats alone do not justify a complete second
  hierarchy. Compare narrow boundary normalization into existing models, retaining small
  request-specific payloads with additional meaning.
- Inspect validation and error classification during conversion, not just public
  declarations.
- Public projections, separately evolving external schemas, security boundaries, and
  persistence models can justify distinct types. Establish present need rather than
  inferring it from layer names or hypothetical reuse.

**Direction:** remove mirrored model families when narrow boundary translation and
existing domain models suffice. Preserve required external validation and any
genuinely independent contract. Update consumers, serializers, tests, and documented
payload shapes together; do not replace the hierarchy with another generic mapper,
force shared inheritance, or leak external naming into domain models just to
reduce the class count.

## Misleading verification

**Signals:** fixtures violate several invariants while claiming to test one;
assertions echo mocks, pin incidental wording or wiring, or cannot expose the
claimed aliasing/ordering failure.

**Consequence:** regressions pass unnoticed and refactors pay for brittle tests
that protect no observable contract.

**Evidence:**

- Name a plausible bug that should fail each assertion. Where useful, use an isolated
  mutation probe to see whether removing the intended protection still passes.
- Check whether another invalid condition still rejects the fixture when the intended
  protection disappears.
- Check whether serialization, copying, normalization, or mocking already guarantees the
  asserted result, bypassing its claimed boundary.
- For diagnostics, distinguish privacy and machine-readable contracts from incidental
  prose. Prove sanitization and the required operational response rather than matching
  whole human-readable sentences.

**Direction:** make boundary cases otherwise valid and assert consumer-observable
behavior. Preserve meaningful integration and failure tests.
