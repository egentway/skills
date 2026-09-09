# Migrate existing documentation

Use for an authorized documentation reorganization. Read
[consultation](consultation.md) for purpose/status/freshness rules and
[installation](installation.md) for the project-local skill and root pointer.
Keep the main editing path easy to review; a move-only pass is insufficient when
individual documents mix implementation, proposals, and historical evidence.

## Inventory and propose the cut

1. Inventory all relevant documentation by purpose, including application detail
   embedded in root instructions. Follow existing indexes and entry points rather
   than browsing unrelated material. Respect confidentiality and generated docs.
2. Classify content—not only filenames—as current application guidance, design
   rationale/proposal/progress, reference evidence, or irrelevant historical
   material. Identify mixed documents, duplicated owners, missing current topics,
   broken links, and old behavior presented as current.
3. Check current claims against source, public contracts, tests, configuration,
   and actual runtime entry points. Recover design progress from evidence. A file
   named "proposal" can contain the only useful description of an implemented
   API; a document saying "current" may refer to a pinned historical baseline.
4. Recover original dates where available. Distinguish first-known Git addition
   from authorship time and snapshot revision; a document edited over months is
   not wholly authored at its filename timestamp.
5. Present the current state, proposed purpose layout, extraction/move/archive
   map, preservation risks, and verification plan. Get approval before reorganizing
   unless the user has already approved that concrete scope. Do not silently
   narrow the migration to easy renames or add unrelated code cleanup.

Use `docs/agents/current/`, `docs/agents/design/`, and
`docs/agents/reference/`, each with an index. Design and reference have separate
`archived/` indexes. `docs/` is the umbrella for all docs; leave unrelated human,
operator, or generated documentation in its appropriate purpose area.

## Extract current guidance first

Build the maintained current guides before retiring their mixed predecessors.
Choose topics from the actual application and start with small flat files.
Consolidate each rule or explanation under one clear owner. Preserve important
repository policy while moving detailed application knowledge out of `AGENTS.md`.
A topic should let a fresh reader locate an edit and its constraints directly.

Correct stale implementation claims in the extracted guides. Keep absence notes
where they prevent mistakes, but do not import future implementation blueprints.
Do not accidentally ban a deliberately deferred possibility while documenting
that it is not implemented. Keep scope and policy distinct from runtime guarantees.

## Preserve design and evidence honestly

- Move design records to UTC timestamped filenames and assign evidenced
  TODO/DOING/DONE labels to their agreed scope. Keep labels in headings/indexes,
  not filenames. Separate a completed prerequisite from the proposed feature.
- Identify implemented and remaining portions of a DOING record. Name excluded
  future scope on a DONE record. Unknown implementation is not proof of completion.
- Retain useful rationale even after a design is DONE. Archive by relevance, not
  by age, filename, or completion alone. Keep rejected/abandoned records honest
  rather than marking them DONE.
- Keep source studies and experiments under `docs/agents/reference/`. Preserve
  revision pins, evidence ledgers, conditions, negative-finding scope, and limits
  of claims. Do not convert source analysis into a claim of service execution.
- If a study mixes superseded benchmarks and still-useful results, preserve the
  original in the archive and extract an active reference with explicit provenance.
  An extraction is not a remeasurement; historical targets are not current limits.
- Historical bodies may retain obsolete terminology and imperative proposal text.
  Give them a visible snapshot/purpose header and replacement link, rather than
  silently rewriting the past. Distinguish later corrections or relocated notes.

## Install, connect, and remove the old path

Install the complete skill and the bounded consultation pointer using
[installation](installation.md). Keep the organization/consultation policy in the
installed guide, not duplicated in `AGENTS.md`. Retain unrelated instructions
outside the managed section. Project-specific indexes own topic catalogs.

Repair incoming and outgoing links and source references after moves. Preserve
pinned historical source identities instead of "fixing" them to today's symbols.
Update index statuses to match headings. Remove obsolete navigation, duplicate
current guides, and empty old directories once their content is accounted for;
do not leave forwarding stubs or delete unrelated documentation.

## Verify the migration as a reader

Check all local links, current source paths/symbols and commands, topic
reachability, status/filename agreement, installed-package completeness, and the
root marker boundary. Check repeat installation: no duplicate block or changes
to unrelated root content. Verify that preserved evidence bodies/ledgers remain
intact except for deliberate headers, relocation notes, and repaired links.

Try fresh-reader scenarios: locate a real state change or equivalent application
operation, a side effect or integration boundary, and a configuration/UI change
where those concepts exist. Separately ask which design is implemented, what is
outstanding, and why an archive is not a to-do list. Links can all work while
purpose discovery still fails. Do not invent app concepts solely for the exercise.

Report the resulting entry points, preservation checks, concrete verification,
and lessons. If the user requested a review checkpoint before further work, stop
there. Keep temporary verifiers or fixtures out of the finished project unless
there is an explicit ongoing need for them.
