# Verification

Verification has two parts that must not be confused. Checks the agent runs on its
own are reported as results, not asked about. Only an action that needs the user's
authorization, or has meaningful cost or side effects, is put to the user.

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

## Actions that need the user's authorization

For complex, risky, or gated skills, a forward-test is worth recommending: a fresh
subagent gets a realistic request, the skill, and the minimum artifacts, never the
intended answer, in a throwaway workspace outside the working tree. Compare with a
run without the skill when its value is in question. Fix only what the observed
behavior supports.

Because it spawns an agent and costs tokens, ask first, in this form:

```markdown
Needs your OK: forward-test with a fresh subagent.
Tests: whether the skill works from a bare request with no hints.
Why: walkthroughs can't show what a cold reader would misunderstand.
Cost: about 40k tokens and one agent. If skipped: only walkthroughs cover it.
Recommend: run it, because this skill has an approval gate.
```

If the user declines, report it as "Not run" and continue. Do not ask about the
checks in the previous section, and do not ask again in the same task.
