# Verification

Verification is the agent's work, reported as results before committing.
Routine forward-tests use isolated temporary workspaces outside the working tree.

## Choose checks

| Check | When | Evidence to report |
|---|---|---|
| Structure | Every package change | Available validators; frontmatter, names, links, packaging |
| Discovery | New or changed discovery metadata | About three intended matches and three near-misses |
| Invocation policy | Request-only skill, where harness available | Actual harness visibility; otherwise mark unverified |
| Behavior | Relevant changed behavior | Normal outcome, ambiguity, refusal, or knowledge-edit route |
| Forward-test | Complex, risky, or gated skill | Fresh subagent run in an isolated workspace |

### Structure

Run available validators: `claude plugin validate <repository>`,
`claude plugin validate <repository>/plugins/<bundle>`, and Codex's
`quick_validate.py` when present. If a validator is absent or cannot run, report
that limitation and perform applicable fallback checks: frontmatter parsing,
name/directory agreement, supporting links, and bundle placement.

### Discovery and invocation

Judge the description against intended matches and near-misses; tighten it if it
misroutes. For request-only skills, check actual model-visible discovery where the
harness permits, such as `codex debug prompt-input`. Metadata presence alone does
not prove cross-harness enforcement.

### Behavior

Exercise the resulting instructions, not just the plan. Select applicable cases:
normal outcome or approval checkpoint; ambiguity producing a focused question;
consent absent or declined stopping before execution; knowledge edits reaching the
owning file without running the main task. A walkthrough suffices for simple skills.

For issueskill, cover creation and extraction, activation questions, destination
and bundle ambiguity, and proposal approval before writes.

Report structural checks, instruction walkthroughs, model exercises, and actual
harness invocation as distinct evidence levels. Correct observed gaps before delivery.

## Run an isolated forward-test

For complex, risky, or gated skills, run a fresh subagent without asking for routine
fixture testing. Give it a realistic request, the skill, and minimum raw artifacts;
do not supply the intended answer or prior conclusions.

```text
Realistic request + skill + minimum raw artifacts
                       ↓
               Fresh subagent
                       ↓
          Inspect behavior and actual writes
                       ↓
      Correct only observed gaps; compare baseline
                when value is uncertain
                       ↓
       Confirm containment → clean up → report cost
```

Keep all generated artifacts inside the temporary workspace outside the working tree.
Confirm actual writes stayed within it, remove throwaway artifacts, and report the
outcome and rough cost. A baseline without the skill is useful when its value is
in question.

## Request additional authorization

Ask before a check writes beyond the isolated workspace, uses credentials, the
network or a live system, or has unusually large cost. Routine fixture testing
needs no additional confirmation.

```text
Needs your OK: <action>.
Tests: <what it checks>.
Why: <what cheaper checks cannot show>.
Reaches beyond the temp workspace: <what, or estimated unusual cost>.
If skipped: <coverage lost>.
Recommend: <run or skip, with reason>.
```

If declined, mark the check Not run and continue. Do not ask again in the same task.
