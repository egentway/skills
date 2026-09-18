# Code-smell catalogue

Editable inspection knowledge for [review.md](review.md). Each signal requires
investigation, not automatic condemnation. A request to add, revise, or remove a
criterion edits this file without initiating an audit. Ordinary audits do not
silently extend it. Change the procedure only when the criterion changes how an
audit must run.

## Competing rule owners

**Signals:** adapters and domain models check the same references; option queries
and mutation methods independently encode eligibility; defaults are resolved by
both caller and callee.

**Consequence:** policy changes can update one path and leave another behind;
callers receive conflicting answers or unnecessary validation work accumulates.

**Evidence:** trace the rule's consumers and trust boundaries. Distinguish wire
normalization, structural validity, and current-state eligibility. Determine
whether one check merely repeats a guarantee already established by its input.

Inspect scalar constraints as well as graph/reference rules. Follow a value from
wire extraction through normalization, model construction, event construction,
and owner admission. Identify the owner of requiredness, type validity, ranges,
references, and current-state eligibility. Strict domain models may make adapter
checks redundant, but retain checks needed before normalization: removing them
must not turn malformed input into a valid default, sentinel, or unknown case.

Include small boundary validators shared by sibling components. Compare their
actual accepted/rejected inputs before declaring them the same rule. A shared
function or type is justified only when it removes a real duplicate authority.

**Direction:** prefer one owner per invariant. Keep boundary-specific checks where
they protect genuinely different guarantees. Do not remove validation merely
because the syntax is similar, or replace small duplication with a rules engine.

## Exception misclassification

**Signals:** a broad catch spans parsing, construction, and application work;
programming failures become expected rejection; errors are logged and processing
continues without an explicit failure policy.

**Consequence:** valid work may disappear while the application appears healthy;
diagnostics identify the wrong cause or expose untrusted payloads.

**Evidence:** identify each exception's actual producers and the caller's response.
Probe classification with valid input and an isolated internal fault when useful.
Check whether an exception list redundantly names subclasses of a broad parent.
Inspect every handler branch for catch-and-reraise paths with no producer inside
the protected region and obsolete translations left after responsibility moved.
Establish producers before calling a branch redundant; distinguish unexpected
implementation failures from expected input rejection.

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

**Evidence:** trace normal exit, body failure, cleanup failure, cancellation during
cleanup, and combinations. Separate completion of cleanup from correct propagation
of its result. Compare actual resource ownership and cancellation requirements.

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

**Evidence:** identify the normal path and invariant behind each branch/flag.
Measure size or nesting only to locate hotspots. Determine which complexity is
required by the behavior and which is introduced by its representation.
Look for flags and repeated scans that indirectly express membership, coverage,
or ordering. Compare the implementation with a direct expression of that
relationship, preserving semantics, ordering, and useful short-circuiting.
A set-based rewrite is not inherently clearer or faster.

**Direction:** prefer early rejection, visible domain steps, and direct invariant
expressions. A linear field mapping or operation may be long without being hard
to understand. More functions and files can increase cognitive cost.

## Unclean integration

**Signals:** stale caller-side logic after an ownership change, redundant argument
forwarding, competing state, implicit startup order, or abstractions that hide an
incompatible lifecycle.

**Consequence:** maintainers cannot identify the authority for a decision; defaults
drift or correctness depends on incidental call order.

**Evidence:** follow real entry points through construction, dependency supply,
operation, and shutdown. Compare claimed ownership to actual callers. Check
whether explicit overrides intentionally differ from default resolution.
After moving responsibility, inspect both the new owner and former callers for
default resolution, argument transformation, validation, or lifecycle work still
active in both places.

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

**Evidence:** identify what each abstraction protects and who consumes it. Separate
external protocol representation from domain representation before declaring two
models redundant. Establish present use rather than hypothetical reuse.
Follow a representative value through the complete operation. Framework
construction can repeat validation, conversion, copying, or traversal even when
application code passes an existing immutable object. When uncertain, count
invocations or transformations before claiming overhead. Observed repetition is
not measured performance impact; do not introduce validation bypasses, caches,
or parallel representations merely to eliminate a small repeated cost.

**Direction:** retain abstractions that enforce an invariant, isolate a volatile
boundary, or name a substantial domain operation. Remove those whose cost exceeds
their present role. Do not replace removable helpers with another comprehensive
schema hierarchy merely to make the implementation look declarative.

## Misleading verification

**Signals:** fixtures violate several invariants while claiming to test one;
assertions echo mocks, pin incidental wording or wiring, or cannot expose the
claimed aliasing/ordering failure.

**Consequence:** regressions pass unnoticed and refactors pay for brittle tests
that protect no observable contract.

**Evidence:** ask what plausible bug would fail each assertion. Check whether a
preceding conversion already guarantees the result. Where useful, use an isolated
mutation probe to see whether removing the intended check still passes the case.

Ask whether another invalid condition would still reject the fixture if the
intended protection disappeared. Check whether an earlier serialization, copy,
normalization, or mock already guarantees the asserted result; such an assertion
may not exercise its claimed boundary.

For diagnostics, distinguish contractual privacy or machine-readable fields from
incidental prose. Prove sanitization and the required operational response rather
than matching an entire human-readable sentence.

**Direction:** make boundary cases otherwise valid and assert consumer-observable
behavior. Preserve meaningful integration and failure tests. Do not add permanent
tests during the audit, or confuse a process-local mutation probe with proof of a
production failure.
