# Presentation

How issueskill's messages are shaped. The goal is that the user keeps control of the
decisions that matter, spends little effort on them, and always knows what is
happening and what is being asked.

Present the proposal, and the decisions message below, using the `present-for-review`
skill. If it is unavailable, present with the main path first, labeled excerpts, a
file map, and an approval question. What a skill proposal must contain is listed in
[issue.md](issue.md) step 3; the decisions message and the final report have their
own formats here.

## Decisions message

Gather every open decision into one message, not a drip of questions. Open it with
an orienting status block: where we are, what is settled, what is needed from the
user, and what happens next.

- **Assumed.** List what the brief, the conversation, or local conventions settle,
  as one line the user can veto. Infer only what is obvious; when in doubt, ask.
- **Questions.** Number what materially affects the skill. Give each a recommendation
  and a one-clause reason. Activation policy, the bundle when several exist,
  destination ambiguity, and the extraction boundary are always questions when
  unsettled, never assumptions.
- **Shortcut.** Tell the user they can reply "accept" to take every recommendation
  in this message, or amend by number. "Accept" covers only this message's numbered
  questions. Assumed items stand unless the user vetoes them; accepting does not
  confirm them separately.

```markdown
Assumed (tell me if wrong): read-only, no commit; targets Claude Code, omp, Codex.
1. Bundle: `workflow` or `quality`? Recommend `workflow` (fits a release step).
2. Activation: automatic or request-only? Recommend automatic (low-risk, read-only).
Reply "accept" to take both recommendations, or change any number.
```

## Report

After writing, verifying, and committing, finish with a results list rather than
prose:

```markdown
Files: `plugins/hsl/skills/<skill>/` (+3). Commit: 1a2b3c4.
Checks run: validate repo ✔, validate bundle ✔, links ✔, discovery prompts 6/6 ✔
Not run: forward-test (declined).
Open items: none.
```

Distinguish what was run from what was only reasoned through. See
[verification.md](verification.md) for what the checks are and when to ask.
