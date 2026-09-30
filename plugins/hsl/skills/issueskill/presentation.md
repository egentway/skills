# Presentation

How issueskill talks to the user. The goal is that the user keeps control of the
decisions that matter, spends little effort on them, and always knows what is
happening and what is being asked. The proposal shape is adapted from a
plan-review process: main path first, representative abridged excerpts, visible
connections, a map of affected files, and an explicit approval question.

## Status block

Open every message that needs the user's input with these four lines:

```markdown
**Where we are:** Step 2 of 7, choosing where the skill goes and how it activates.
**Settled:** a changelog-from-diff skill; destination is the skills repository.
**Need from you:** the two decisions below.
**Next:** once you answer, I show the full proposal. Nothing is written yet.
```

Keep each line to one sentence. Progress-only messages may use just the first two.

## Decisions message

Gather every open decision into one message, not a drip of questions.

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

## Proposal

Present it in the conversation before creating files. Start with the main path: the
capability, its inputs and exclusions, the activation policy and gates, and a short
end-to-end invocation example. Then, per file:

- **Responsibility:** what the file owns and why it is a separate file.
- **Location:** the exact path, marked `+` new or `~` modified.
- **Abridged excerpt:** proposed text, labeled as proposed, with omissions stated.
  Show the parts that carry behavior: the description and frontmatter, routing
  links, gates, and one representative procedure step. Not every line.
- **Connection:** which file links to it, and when it is read.
- **Consequential choice:** anything the user should evaluate.

Also state the chosen bundle, the invocation metadata for each target harness, and
where editable knowledge lives and how the user requests changes to it.

A cohesive small skill gets a compact proposal: its frontmatter, the key
instructions, the activation policy, and the verification plan. Skip the tree and
connection notes when there is one file.

End larger proposals with a brief tree of affected files:

- `+` new file, `~` modified, `-` removed, `>` moved (show old and new paths)
- a short **Intentionally untouched** list when revising an existing skill
- the main risk, if there is one

Then ask directly for approval, for example "Do you approve this, or would you like
to change any of these boundaries or excerpts first?", and stop. When the user
requests a change, update the excerpts and the tree together and ask again.

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
