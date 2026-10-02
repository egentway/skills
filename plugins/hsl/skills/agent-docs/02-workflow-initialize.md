For an authorized greenfield or genuinely undocumented project. If useful
application docs or design/history already exist, run **Migrate** instead of
overwriting them.

# Steps

## Ground

Learn the project before writing about it.

- **Input:** the purpose, status, freshness, and archival rules in
  [01-consultation.md](01-consultation.md); the project's source.
- **Output:** the few editing intentions a fresh agent will have, with topic names
  taken from source and explicit project policy.

1. Inspect the current source layout, entry points, configuration, public
   boundaries, tests, and runtime commands.

2. Identify the few editing intentions a fresh agent is likely to have. Source and
   explicit project policy—not an example project in this skill—determine the
   topic names.

3. If the project has no implementation yet, say so. Document only existing
   scaffold or setup and known constraints; do not invent services, state owners,
   tests, or a future architecture to make the guide look complete. No design is
   approved merely because it has been written down.

## Lay out

Create the purpose layout with only what exists.

- **Input:** the editing intentions and topic names from Ground.
- **Output:** the agent documentation tree, with a current index and topic guides,
  and design and reference indexes.

1. Create the tree in Layout. The indexes may accurately state that no records
   exist yet; do not fabricate sample design documents, studies, or archived
   decisions to populate directories.

2. Write a short `current/index.md` with the actual application map, current
   scope, and task-to-topic routing.

3. Create only the topic guides warranted by existing code. Start flat; split a
   topic into a folder and local index when it genuinely improves discovery. Each
   guide should identify edit owners, main flow, important contracts, and scoped
   verification, with direct source links rather than implementation dumps.

4. Have the design and reference indexes explain their purpose and link their
   archives separately. Design records, if any, have an evidenced TODO/DOING/DONE
   scope and UTC `yyyymmdd-hhmm-title.md` filename. Reference evidence has no
   implementation status.

Current guides never depend on reading design or reference records to explain
today's code.

### Layout

```text
docs/
  agents/
    current/
      index.md
    design/
      index.md
      archived/
        index.md
    reference/
      index.md
      archived/
        index.md
```

`docs/` remains available for non-agent-facing documentation with other purposes;
do not move unrelated user manuals or generated API docs into the agent tree.

## Install

Put the consultation entry point in place.

- **Output:** the full skill installed in the project and one delimited
  consultation pointer in root `AGENTS.md`.

Run **Install**. Do not copy the consultation rules into `AGENTS.md` or turn this
generic skill into the project's application-topic catalog. Keep
repository-specific engineering instructions outside the managed block.

## Verify

Check the docs as a fresh reader would.

- **Output:** a hand-off naming the entry points, known evidence limits, and any
  user decision still needed.

1. Check links, source paths/symbols, commands, status/filename consistency, and
   index reachability.

2. **Check discovery** with scenarios grounded in the project: can an agent find
   where a relevant change belongs and what boundary not to cross, without reading
   designs or archives? For an empty project, can it correctly recognize the
   absence of implementation rather than following invented guidance?

3. Check repeat installation and preservation of unrelated root instructions.

4. Report the entry points, known evidence limits, and any user decision still
   needed.

Documentation proof is navigation, factual checking, and preserved boundaries;
unrelated application test runs are not a substitute. Do not claim code, service,
or hardware verification that was not performed.
