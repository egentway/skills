For an authorized documentation reorganization. Keep the main editing path easy to
review; a move-only pass is insufficient when individual documents mix
implementation, proposals, and historical evidence.

# Steps

## Inventory

Classify the existing docs by purpose and check their claims.

- **Input:** the purpose, status, and freshness rules in
  [01-consultation.md](01-consultation.md); the existing documentation, including
  application detail embedded in root instructions.
- **Output:** each document classified by purpose, with mixed documents,
  duplicated owners, missing topics, broken links, stale claims, and recovered
  dates identified.

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

## Propose

Present the cut before reorganizing.

- **Input:** the inventory.
- **Output:** the current state, proposed purpose layout, extraction/move/archive
  map, preservation risks, and verification plan.
- **Gate:** **Approve** before reorganizing, unless the user has already approved
  that concrete scope.

Use `docs/agents/current/`, `docs/agents/design/`, and `docs/agents/reference/`,
each with an index. Design and reference have separate `archived/` indexes.
`docs/` is the umbrella for all docs; leave unrelated human, operator, or
generated documentation in its appropriate purpose area.

Do not silently narrow the migration to easy renames or add unrelated code
cleanup.

## Extract

Build the current guides before retiring their mixed predecessors.

- **Input:** the approved map; the mixed documents and the source they describe.
- **Output:** small, flat current guides with each rule under one owner and stale
  claims corrected.

Choose topics from the actual application and start with small flat files.
Consolidate each rule or explanation under one clear owner. Preserve important
repository policy while moving detailed application knowledge out of `AGENTS.md`.
A topic should let a fresh reader locate an edit and its constraints directly.

Correct stale implementation claims in the extracted guides. Keep absence notes
where they prevent mistakes, but do not import future implementation blueprints.
Do not accidentally ban a deliberately deferred possibility while documenting
that it is not implemented. Keep scope and policy distinct from runtime guarantees.

## Preserve

Move design and evidence records honestly.

- **Input:** the approved map; the design and reference records it covers.
- **Output:** timestamped, labelled design records and preserved reference
  evidence, with historical bodies intact.

Rules for moving records:

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

## Install

Install the package, then connect and remove the old path.

- **Output:** the installed skill and root pointer, repaired links and statuses,
  and no obsolete navigation, duplicate guides, or empty old directories.

1. Run **Install**. Keep the organization/consultation policy in the installed
   guide, not duplicated in `AGENTS.md`. Retain unrelated instructions outside the
   managed section. Project-specific indexes own topic catalogs.

2. Repair incoming and outgoing links and source references after moves. Preserve
   pinned historical source identities instead of "fixing" them to today's
   symbols.

3. Update index statuses to match headings.

4. Remove obsolete navigation, duplicate current guides, and empty old directories
   once their content is accounted for; do not leave forwarding stubs or delete
   unrelated documentation.

## Verify

Verify the migration as a reader.

- **Output:** the resulting entry points, preservation checks, concrete
  verification, and lessons.
- **Gate:** **Approve** here if the user requested a review checkpoint before
  further work.

1. Check all local links, current source paths/symbols and commands, topic
   reachability, status/filename agreement, installed-package completeness, and
   the root marker boundary.

2. Check repeat installation: no duplicate block or changes to unrelated root
   content.

3. Verify that preserved evidence bodies/ledgers remain intact except for
   deliberate headers, relocation notes, and repaired links.

4. **Check discovery**: locate a real state change or equivalent application
   operation, a side effect or integration boundary, and a configuration/UI change
   where those concepts exist. Separately ask which design is implemented, what is
   outstanding, and why an archive is not a to-do list.

5. Report the resulting entry points, preservation checks, concrete verification,
   and lessons.

Keep temporary verifiers or fixtures out of the finished project unless there is
an explicit ongoing need for them.
