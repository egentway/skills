# Review code quality

Audit within the requested boundary. Consult relevant catalogue criteria as
inspection signals, not mandatory findings.

# Steps

## Scope

Establish the requested boundary and confirmed design constraints.

- **Input:** Audit request, available context, and repository conventions.
- **Output:** Inspection scope, exclusions, entry points, owners, and tests.

1. Recover the requested scope, confirmed design choices, exclusions, and repository
   conventions. Identify relevant entry points, owners, callers, and tests.

2. Resolve scope from available context first. If materially different interpretations
   remain, summarize them and ask one focused question before expanding the audit.

3. Read cognitive-budget-coding to assess reader cost throughout the audit. Consult
   relevant criteria in [catalogues/code-smells.md](catalogues/code-smells.md).

Do not classify an explicitly selected tradeoff as an accidental defect. Its risks
can be worth naming, but distinguish them from implementation mistakes. Do not
broaden changed-code review into unrelated repository cleanup.

## Trace

Follow behavior before judging structure.

- **Input:** Inspection scope and relevant criteria.
- **Output:** Successful, rejection, failure, and cleanup paths.

1. Trace successful operations and important rejection, failure, and cleanup paths.
   Inspect complete functions and callers, not isolated suspicious lines.

2. Use repository symbol-navigation tools and current guidance. Check dynamic and
   framework consumers before concluding a symbol is unused.

3. Treat catalogue signals as investigation leads, not findings. Similar syntax may
   express different domain rules; small helpers may hide a large state machine or
   competing ownership.

## Evaluate

Establish the present cost and smallest useful simplification.

- **Input:** Traced behavior and candidate concerns.
- **Output:** Supported candidates, justified structure, and open uncertainty.

For each candidate:

1. Identify its behavior or invariant, why it exists, and the callers, configuration,
   data, and tests that depend on it.

2. Determine whether similar code implements the same rule at the same boundary.

3. Establish a concrete failure, reader burden, or maintenance risk that exists now.

4. Identify the smallest change removing that cost without losing required behavior.

5. Inspect whether tests defend the claimed invariant. A passing suite does not prove
   maintainability. Check fixtures and assertions, not just names or counts; another
   invalid condition may mask the intended failure.

6. Run Bounded coverage check before reporting.

Use size and nesting to locate hotspots, never as automatic extraction thresholds.
Preserve a clear linear operation rather than fragmenting it to reduce line count.

### Bounded coverage check

Revisit only the boundaries already inspected:

| Area | Question |
|---|---|
| Rule ownership | Is the same invariant enforced by competing owners? |
| Transformations | Does the operation repeat meaningful conversion or framework work? |
| Integration cutover | Is superseded logic active at former owners? |
| Verification | Could a plausible regression pass the claimed test? |

This does not expand scope or require a finding count or exhaustive file checklist.
Any category may have no finding.

## Probe

Resolve uncertainty when runtime evidence would change the finding.

- **Input:** Consequential uncertainty from Evaluate.
- **Output:** Executed evidence, retracted candidates, or explicit limitations.

1. Use focused deterministic probes, preferably with isolated synthetic inputs.
   Skip execution when it adds no useful evidence; do not run broad validation by
   reflex. Exercise only checks answering an audit question.

2. Keep probes disposable and outside tracked source. Isolate process-local
   substitutions and restore them or discard the process. Clean up temporary
   artifacts and resources created by the audit.

3. Ask before stronger evidence needs access or external effects beyond audit
   authorization. Do not expose private data, bypass access restrictions, install
   dependencies, or exercise real external effects merely to finish an audit.

4. Distinguish natural reproduction, fault injection, and simulated transport.
   An injected internal exception can establish faulty classification, not that
   the fault occurs naturally in production. A simulated transport establishes
   local handling, not real server behavior.

5. Retract candidates contradicted by observed runtime behavior rather than relying
   on remembered library behavior. Record exactly what was exercised and what
   remains unresolved.

## Report

Present findings and a bounded recommended next step.

- **Input:** Supported findings, probe results, and coverage limits.
- **Output:** Completed audit report; no fixes performed.

1. Read present-for-review for message structure. Lead with consequential findings,
   using Finding format. Rank by consequence rather than stylistic preference.

2. Consolidate symptoms sharing one structural cause. Put related smaller supported
   observations under their owning finding or in optional simplifications; do not
   omit them just because they are not standalone defects. Keep speculative
   optimizations separate and state when repetition does not justify a change.

3. Explain justified repetition and constraints a proposed simplification must
   preserve. Describe the complete affected boundary, including callers and tests.
   Do not recommend a framework, model hierarchy, or broad rewrite for small local
   duplication, or present an unapproved implementation as completed work.

4. State scope, evidence limits, and whether files changed. No substantial findings
   is a valid outcome. Recommend bounded remediation where warranted.

The audit ends here. Approval of findings alone does not authorize fixes. A
remediation proposal identifies its scope and obtains separate approval; a calling
workflow may own that gate.

### Finding format

| Category | Required support |
|---|---|
| Confirmed defect | Source evidence and executed evidence where needed |
| Maintainability concern | Concrete present cost without an unsupported bug claim |
| Unresolved candidate | Exact missing evidence and how to obtain it |

For each finding:

```text
Finding: <consequence-oriented description>
Location: <file and symbol>
Evidence: <source / natural reproduction / fault injection / static inference>
Present consequence:
Bounded recommendation:
Uncertainty:
```

Label static inference and fault injection explicitly.
