# Verification

Verification is the agent's work, reported as results, not put to the user for
approval. That includes forward-tests, which run in a throwaway workspace outside the
working tree and touch nothing else. Only an action that reaches beyond such a
workspace, or has unusually large cost, is put to the user.

## Checks the agent runs

Run these after writing and before committing. Report each in the results list; see
[presentation.md](presentation.md).

**Structure.** Run the validators that exist: `claude plugin validate <repository>`
and `claude plugin validate <repository>/plugins/<bundle>`, and Codex's
`quick_validate.py` if present. Otherwise check frontmatter parsing, the
name/directory relationship, supporting-file links, and that the skill sits under a
bundle's `skills/` directory.

**Discovery.** Write about six prompts: three that should trigger the skill and
three near-misses that should not. Judge the description against them and tighten it
if it would misroute. For a request-driven skill, confirm where the harness allows
that the skill is absent from the model-visible list (for Codex,
`codex debug prompt-input`). Do not claim cross-harness enforcement from a field's
presence alone.

**Behavior, proportional to risk.** Exercise representative scenarios using the
resulting instructions, not just the plan:

- A normal invocation reaches the intended outcome or approval checkpoint.
- An ambiguous input produces a focused question rather than a silent scope choice.
- A gated workflow stops before execution when consent is absent or declined.
- A request to update knowledge reaches its owning file without running the main task.

Select the scenarios that apply. For issueskill itself, cover fresh creation and
extraction, the activation question, destination and bundle ambiguity, and proposal
approval before writes. For simple skills, a walkthrough of these is enough.

Correct gaps before delivery, remove any throwaway artifacts, and report which
levels were performed. Distinguish structural checks, instruction walkthroughs,
model exercises, and real harness invocation results.

## Forward-testing

For complex, risky, or gated skills, run a forward-test without asking: a fresh
subagent gets a realistic request, the skill, and the minimum artifacts, never the
intended answer, in a throwaway workspace outside the working tree. Compare with a
run without the skill when its value is in question. Fix only what the observed
behavior supports. Afterwards confirm the workspace held all its writes, then remove
it, and report the result and rough cost in the results list.

## Actions that need the user's authorization

Ask first only when a check would reach beyond a throwaway workspace: writing outside
it, using credentials, the network, or a live system, or costing unusually much.
Ask in this form:

```markdown
Needs your OK: <the action>.
Tests: <what it checks>.
Why: <what the cheaper checks can't show>.
Reaches beyond the temp workspace: <what, or "no, but cost is about X">.
If skipped: <what coverage is lost>.
Recommend: <run or skip, and why>.
```

If the user declines, report it as "Not run" and continue. Do not ask again in the
same task.
