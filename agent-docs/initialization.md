# Initialize purpose-based documentation

Use for an authorized greenfield or genuinely undocumented project. If useful
application docs or design/history already exist, use [migration](migration.md)
instead of overwriting them. Read [consultation](consultation.md) for the shared
purpose, status, freshness, and archival rules.

## Ground the guide in the project

Inspect the current source layout, entry points, configuration, public boundaries,
tests, and runtime commands. Identify the few editing intentions a fresh agent is
likely to have. Source and explicit project policy—not an example project in this
skill—determine the topic names.

If the project has no implementation yet, say so. Document only existing scaffold
or setup and known constraints; do not invent services, state owners, tests, or a
future architecture to make the guide look complete. No design is approved merely
because it has been written down.

## Establish the purpose boundary

Use this layout for agent-facing documentation:

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
The indexes may accurately state that no records exist yet. Do not fabricate
sample design documents, studies, or archived decisions to populate directories.

Write a short `current/index.md` with the actual application map, current scope,
and task-to-topic routing. Create only the topic guides warranted by existing code.
Start flat; split a topic into a folder and local index when it genuinely improves
discovery. Each guide should identify edit owners, main flow, important contracts,
and scoped verification, with direct source links rather than implementation dumps.

The design and reference indexes explain their purpose and link their archives
separately. Design records, if any, have an evidenced TODO/DOING/DONE scope and UTC
`yyyymmdd-hhmm-title.md` filename. Reference evidence has no implementation status.
Current guides never depend on reading those records to explain today's code.

## Install the consultation entry point

Follow [installation](installation.md) to put the full skill in the project and
add the single delimited consultation pointer to root `AGENTS.md`. Do not copy the
consultation rules into `AGENTS.md` or turn this generic skill into the project's
application-topic catalog. Keep repository-specific engineering instructions
outside the managed block.

## Verify and hand off

Check links, source paths/symbols, commands, status/filename consistency, and
index reachability. Exercise a few fresh-reader scenarios grounded in the project:
can an agent find where a relevant change belongs and what boundary not to cross,
without reading designs or archives? For an empty project, can it correctly
recognize the absence of implementation rather than following invented guidance?

Also check repeat installation and preservation of unrelated root instructions.
Documentation proof is navigation, factual checking, and preserved boundaries;
unrelated application test runs are not a substitute. Report the entry points,
known evidence limits, and any user decision still needed. Do not claim code,
service, or hardware verification that was not performed.
