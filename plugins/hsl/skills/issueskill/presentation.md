# Presentation

How issueskill's messages are shaped. The goal is that the user keeps control of the
decisions that matter, spends little effort on them, and always knows what is
happening and what is being asked.

Present the proposal, and the decisions message below, using the `present-for-review`
skill. If it is unavailable, present with the main path first, labeled excerpts, a
file map, and an approval question. What a skill proposal must contain is listed in
[issue.md](issue.md) step 3; how a skill is shown, the decisions message, and the
final report have their own formats here.

## Presenting a skill

Show a skill, existing or proposed, through its structure, then open only what is
under review.

1. **Entry.** The description and the opening line, abridged.
2. **Outline.** Every file in reading order: SKILL.md, then the numbered files,
   then `catalogues/`. Under each, its headings in file order. A step carries its
   first sentence and the operations or workflows it runs; a section after `---`
   carries its first sentence; other headings appear bare. For an existing skill,
   generate it with `python3 scripts/outline.py <skill-dir>`, resolving the script
   relative to this skill's folder; for a proposed one, write it in the same form.
3. **Opened sections.** Expand the sections that changed or that the user asked
   about, as abridged excerpts labeled proposed or current. Everything else stays
   in the outline.

The proposal and the report use this view, and so does any request to show or
compare a skill.

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
