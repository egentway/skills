Change what the project model requires: draft a proposal, have it decided, and
record it. Runs when Check fit in [01-consultation.md](01-consultation.md) finds
that a change needs requirements, for the genesis and opening-balance decisions,
or when the user asks to propose or record a decision. Forming good requirements
is design work; this workflow makes them explicit, gets them approved, and keeps
the records honest.

# Steps

## Draft

Write the proposal and choose how it will be decided.

- **Input:** [07-records.md](07-records.md); the request; the project-model
  sections the change touches and the decision parts in force for them.
- **Output:** a pending record in `docs/agents/decisions/pending/`, and a path:
  decide first or try first.

1. Create the record with `status: pending` and an H1 title naming the outcome,
   and list it under Pending in the decisions index.

2. Write Requirements: complete, present tense, with applicability and
   exceptions. Write them before any trial, so later revisions stay visible.

3. When the change replaces earlier requirements, restate each affected part in
   full and list it in `supersedes`. Never amend part of a part. Adding to a
   topic an earlier part covers counts as a change when that part, read alone,
   would then mislead a reader.

4. Write Context and Rationale, and Options when there were real alternatives.
   Add a Plan when the route to conforming code is not obvious.

5. Choose the path. Decide first when the requirements are clear. Try first when
   constraints are uncertain, such as an unfamiliar integration or an interaction
   that needs to be seen working. Say which and why; the user may choose the
   other.

## Try

Build a small representative slice before the decision, on the try-first path.

- **Input:** the pending record.
- **Output:** a working slice off the main branch, and the record revised by what
  it showed.

On the decide-first path, skip this step.

1. Keep the slice small: ordinary use, a relevant failure or rejection, and the
   communication and recovery around it. A large trial makes refusal costly.

2. Keep its code on a branch or worktree; it reaches the main branch only with
   acceptance. If the repository works without branches, ask before committing
   trial code.

3. Commit the first draft of the record on that branch before any trial code, so
   Present can show how the record changed with one diff.

4. Revise the pending record as constraints appear, and note what the trial
   uncovered in Rationale. Do not reshape the requirements to match accidental
   implementation choices.

5. Update the implementation guides with the trial code, as for any
   implementation change.

## Present

Bring the proposal to its approver.

- **Input:** the pending record; on the try-first path, the slice.
- **Output:** the proposal accepted, refused, or withdrawn, or a revision to
  make.
- **Gate:** **Approve**. The user accepts, asks for revisions, refuses, or
  withdraws it. When delegated acceptance is enabled, a reviewer agent may
  accept instead, as described below.

1. Show the record's text. It is what gets approved, so show Requirements in
   full.

2. Show how the project model would change: the sections affected, their new
   summary, and the links that move. This is part of the presentation, not of the
   record.

3. Show the parts it supersedes and the gaps it opens.

4. On the try-first path, show the working result and how the record changed since
   its first draft, and why.

5. For a revision, edit the record and present again. A question, a correction,
   or silence is not acceptance.

When `docs/agents/mod.yaml` sets `acceptance.delegated: true`, a reviewer agent
may decide instead of the user. It must start from a fresh context and must not
have drafted the proposal. Give it what Present would show the user: the record,
the proposed project-model change, the parts superseded and gaps opened, and on
the try-first path the slice and the diff since the first draft.

The reviewer accepts a proposal whose Requirements are complete and unambiguous,
whose `supersedes` covers and restates every part it changes, and which, once in
force, contradicts no requirement it leaves in force. Otherwise, or when unsure,
it escalates to the user with its reasons. It never refuses. Without such a
reviewer, the proposal goes to the user.

## Record

Make the decision the record's last edit.

- **Input:** the decided proposal and what Present showed.
- **Output:** one commit containing the frozen record and the project model, gap
  notes, and indexes it affects.
- **Stop if:** a part the proposal supersedes is no longer in force because
  another decision replaced it since drafting. Return to Draft.

1. Set `status` and `decided`. For an accepted record, set `is_human_approved`
   and `approved_by` as [07-records.md](07-records.md) describes, never guessing
   an identifier. For a refused or withdrawn record, write Outcome.

2. Move the file, keeping its name: accepted records to `docs/agents/decisions/`,
   refused and withdrawn ones to `docs/agents/decisions/archive/`.

3. For an accepted record, change the project model as presented: summarize the
   new requirements, link the new parts, and remove links to superseded parts.
   Change only what the decision states.

4. Add a gap note to each implementation guide where the code does not yet
   conform; with no topic guide yet, note it in the implementation index. On the
   try-first path, the slice may already close some.

5. Update the decisions index, and the model index if files changed.

6. Commit these together. For an accepted record on the try-first path, commit on
   the trial branch, then integrate the branch the way the project usually
   integrates branches, or by fast-forward when it has no convention, so the
   code and its acceptance reach the main branch together. For a refused or
   withdrawn one, commit the archived record to the main branch and leave the
   trial code out of it.

The record is now frozen. Implementation continues through the ordinary path in
01-consultation.md, closing gap notes as the code conforms.
