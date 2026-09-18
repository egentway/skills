# Review code quality

Use this procedure for a requested code-quality audit. Read the relevant sections
of [code-smells.md](code-smells.md) as inspection criteria, not mandatory findings.
Catalogue maintenance instead routes directly to that file through
[SKILL.md](SKILL.md); it does not start this procedure.

## Establish the boundary

Recover the requested scope, confirmed design choices, exclusions, and repository
conventions. Identify relevant entry points, owners, callers, and tests. Resolve
scope from available context first. If materially different interpretations remain,
summarize them and ask one focused question before expanding the audit.

Do not classify an explicitly selected tradeoff as an accidental defect. Do not
broaden a changed-code review into unrelated repository cleanup. Existing choices
can have risks worth naming, but distinguish those from implementation mistakes.

## Follow behavior before judging structure

Trace successful operations and important rejection, failure, and cleanup paths.
Inspect complete functions and their callers, not isolated suspicious lines.
Use the repository's symbol-navigation tools and current guidance. Check dynamic
and framework consumers before concluding a symbol is unused.

A catalogue recognition signal starts an investigation; it does not establish a
finding. Similar syntax may express different domain rules. Conversely, small
helpers may hide a large state machine or competing ownership.

## Establish the cost

For each candidate, determine:

- What behavior or invariant the code owns and why it exists.
- Which callers, configuration, data, and tests depend on it.
- Whether similar code implements the same rule at the same boundary.
- What concrete failure, reader burden, or maintenance risk exists now.
- The smallest change that removes that cost without losing required behavior.

Use size and nesting measurements as supporting evidence, never automatic
thresholds for splitting files or extracting helpers. Prefer preserving a clear
linear operation over fragmenting it to achieve a lower line count.

Check whether existing tests actually defend the claimed invariant. A passing
suite does not establish maintainability, and a test may pass because another
invalid condition masks the intended failure. Inspect fixtures and assertions,
not just test names or counts.

### Bounded coverage check

Before reporting, revisit the inspected boundaries for:

- Rules enforced by more than one owner.
- Repeated transformations or framework work.
- Remnants at former owners after an integration change.
- Tests unable to distinguish intended behavior from a plausible regression.

This checks coverage of code already in scope; it does not authorize expanding
the audit. A category may have no finding. Do not require a finding count or an
exhaustive file-by-file checklist.

## Probe consequential uncertainty

Use focused, deterministic probes when runtime evidence would materially change
a finding. Prefer isolated synthetic inputs. Do not expose private data, bypass
access restrictions, install dependencies, or exercise real external effects
merely to complete an audit. Ask when stronger evidence requires such access.

Distinguish naturally reproducible failures from fault-injection results. An
injected implementation exception can demonstrate faulty error classification;
it does not prove that defect currently occurs during normal production use.
Likewise, a simulated transport establishes local failure handling, not real
server behavior.

Keep probes disposable and outside tracked source. Do not add permanent tests or
modify production files during a read-only audit. Process-local substitutions
must be isolated and restored or discarded with the process. Clean up temporary
artifacts and resources that the audit creates.

Do not run broad validation by reflex. Run only checks that answer an audit
question, and report what was actually exercised. Retract candidates contradicted
by observed runtime behavior rather than relying on remembered library behavior.

## Report findings

Lead with the consequential findings. Separate:

- **Confirmed defects:** supported by source and, where needed, executed evidence.
- **Maintainability concerns:** concrete costs, without claiming a demonstrated bug.
- **Unresolved candidates:** the exact missing evidence and how to obtain it.

For each finding include its source location/symbol, evidence, present
consequence, recommended bounded simplification, and relevant uncertainty. Label
static inference and fault injection explicitly. Rank by consequence, not stylistic
preference, and consolidate symptoms sharing one structural cause.

Consolidate related smaller observations beneath their owning finding or in a
compact optional-simplifications section. Do not omit an evidence-backed
observation merely because it is not a standalone defect. Keep speculative
optimizations separate from recommended fixes, and state when observed repetition
does not yet justify a change.

Explain what should remain unchanged and which apparent repetition is justified.
Do not recommend a framework, new model hierarchy, or broad rewrite to eliminate
small local duplication. Describe the complete affected boundary of a proposed
cut, including callers and tests, without presenting an unapproved implementation.

End with a bounded recommended next step and an approval checkpoint before fixes.
Do not treat approval of findings as permission for unrelated changes. Reporting
no substantial findings is valid. State scope and verification limits, and confirm
whether files were changed. Do not silently maintain the catalogue from findings;
a user request to revise criteria belongs in code-smells.md.
