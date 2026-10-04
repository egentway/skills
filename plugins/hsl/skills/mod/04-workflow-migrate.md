For an authorized move of a project's documentation into mod, from any earlier
system: agent-docs, architecture decision records, spec-driven tools, agent
instruction files, wikis, or plain documentation. Classify content by the role it
plays, not by the tool that produced it; one document often plays several roles.
A move-only pass is insufficient when documents mix descriptions, intent, and
history.

# Steps

## Inventory

Classify the existing documentation by role and check its claims.

- **Input:** [01-consultation.md](01-consultation.md) and
  [07-records.md](07-records.md); the existing documentation, instruction files,
  and earlier installations, including application detail embedded in root
  instructions.
- **Output:** each document's content classified by role, with stale claims,
  recovered dates, candidate requirements, and contradictions identified.

1. Identify the earlier systems and their entry points. Follow their indexes and
   instruction files rather than browsing unrelated material. Respect
   confidentiality and leave generated documentation alone.

2. Classify content, not filenames, using Roles below. A file named "proposal"
   may hold the only description of an implemented API; a document called
   "current" may describe a pinned historical baseline.

3. Check descriptions against source, public contracts, tests, configuration,
   and runtime entry points.

4. Recover original dates where available. Distinguish first Git addition from
   authorship and snapshot revision, and never present a file mtime as authorship
   evidence.

5. List candidate requirements with their sources, marking each as stated intent
   or only observed in code, and note contradictions between them.

### Roles

| Content | Role | Destination |
| --- | --- | --- |
| What exists now: current guides, READMEs, architecture notes, design documents describing built behavior | Description | `implementation/`, after checking against the code |
| Agreed intent: constitutions, steering files, accepted decision records, written policy, specs of record | Intent | Candidate requirements for the opening balance |
| Conventions seen only in code | Observation | Candidates that govern only once ratified |
| Past decisions and proposals: decision logs, agent-docs design records, archived change proposals, per-feature spec folders | History | `decisions/pre-genesis/` |
| Unfinished proposals that are still relevant | Proposal | `decisions/pending/`, rewritten as mod records |
| Research, experiments, measurements | Evidence | `reference/` |
| Task logs, agent handoffs, scratch plans | None | Outside `docs/agents/`; leave in place, or remove with approval |

## Propose

Present the cut before reorganizing.

- **Input:** the inventory.
- **Output:** the proposed layout, an extraction and move map, the candidate
  requirements, the earlier system's installation and root sections to remove,
  preservation risks, and a verification plan.
- **Gate:** **Approve** before reorganizing, unless the user has already approved
  that concrete scope.

Do not silently narrow the migration to easy moves or add unrelated code cleanup.

## Extract

Build the implementation guides before retiring their mixed predecessors.

- **Input:** the approved map; the documents with descriptive content and the
  source they describe.
- **Output:** small, flat implementation guides with each explanation under one
  owner and stale claims corrected.

Choose topics from the actual application. Move detailed application knowledge
out of root instructions while preserving repository policy. Correct stale
claims against the code. Record known nonconformance as gaps only after the
opening balance establishes the requirements it departs from.

## Preserve

Import history and evidence honestly.

- **Input:** the approved map; the historical, proposal, and evidence content.
- **Output:** pre-genesis records, pending mod proposals, and reference records,
  with original bodies intact.

1. Import historical records into `decisions/pre-genesis/` with their original
   body and filename. In the import commit, add the header from 07-records.md and
   repair their links; after that they are frozen.

2. Rewrite still-relevant unfinished proposals as pending mod records, linking
   their origin from Context. Stale ones become pre-genesis records.

3. Move evidence to `reference/`, preserving revision pins, ledgers, conditions,
   and limits of claims. An extraction is not a new measurement.

## Opening balance

Ratify the requirements the project starts from.

- **Input:** the candidate requirements and contradictions from Inventory.
- **Output:** an accepted opening-balance decision and the project model built
  from it.

1. Run **Decide** with `kind: opening-balance`, one Requirements part per topic,
   built only from candidates the user ratifies. Present each candidate with its
   source and whether it is stated intent or only observed, and let the user
   settle contradictions.

2. In Context, describe the earlier system and link the pre-genesis records that
   explain the requirements. In Rationale, note which candidates were left out
   and why.

3. Conventions the user does not ratify stay described in the implementation
   guides as current practice, not as requirements.

4. Add gap notes where the implementation departs from the ratified requirements.

## Install

Install mod, then remove the earlier path.

- **Output:** the installed skill and root pointer, repaired links, and no
  obsolete navigation, duplicate guides, or empty directories.

1. Run **Install**.

2. Remove the earlier system's installed package and its root instruction
   sections once their content is accounted for, within the approved scope. Keep
   unrelated instructions.

3. Repair incoming and outgoing links. Preserve pinned historical source
   identities instead of updating them to today's symbols.

4. Remove obsolete navigation, duplicate guides, and emptied directories. Do not
   leave forwarding stubs or delete unrelated documentation.

## Verify

Verify the migration as a reader.

- **Output:** the entry points, preservation checks, concrete verification, and
  lessons.
- **Gate:** **Approve** here if the user asked for a review checkpoint before
  further work.

1. Check local links, front matter, source paths and symbols, commands, index
   reachability, the installed package, and the root marker boundary.

2. Check that a repeat installation changes nothing outside the managed section.

3. Check that pre-genesis bodies and evidence ledgers are intact except for
   import headers and repaired links.

4. **Check discovery** with real scenarios: a state change or equivalent
   operation, an integration boundary, and a configuration or UI change where
   those exist. Separately, ask why a requirement exists, what is pending, and why
   pre-genesis records are not instructions.

5. Report the resulting entry points, preservation checks, concrete
   verification, and lessons.

Keep temporary verifiers and fixtures out of the finished project unless there is
an explicit ongoing need for them.
