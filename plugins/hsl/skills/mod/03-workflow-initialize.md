For an authorized new or undocumented project. If useful documentation from an
earlier system exists, run **Migrate** instead of overwriting it.

# Steps

## Ground

Learn the project before writing about it.

- **Input:** [01-consultation.md](01-consultation.md) and
  [07-records.md](07-records.md); the project's source; what the user has said
  about its requirements.
- **Output:** what exists, the editing intentions a fresh agent will have, and
  the requirements the user has actually stated.

1. Inspect the source layout, entry points, configuration, public boundaries,
   tests, and runtime commands.

2. Identify the few editing intentions a fresh agent is likely to have. Source
   and explicit project policy, not an example in this skill, determine topic
   names.

3. If the project has no implementation yet, say so. Document only existing
   scaffold and known constraints; do not invent services, owners, tests, or a
   future architecture.

4. Collect requirements the user has stated or explicitly agreed. Conventions
   observed only in code are candidates for the user to ratify, not
   requirements.

## Lay out

Create the layout with only what exists.

- **Input:** the findings from Ground.
- **Output:** the documentation tree, with indexes, settings, and implementation
  guides.

1. Create the layout described in 07-records.md. Indexes may state that no
   records exist yet; do not fabricate sample decisions or studies.

2. Write `implementation/index.md` with the actual application map and
   task-to-topic routing, and only the topic guides existing code warrants.

3. Write `model/index.md`, `decisions/index.md`, and `reference/index.md`, and
   `mod.yaml` with delegated acceptance off and approver identity optional.

## Genesis

Record the first requirements.

- **Input:** the requirements and candidates from Ground.
- **Output:** an accepted genesis decision and the project model built from it,
  or a project model stating that no requirements are accepted yet.

Run **Decide** with `kind: genesis`, one Requirements part per topic. Keep the
first set small; trying a representative slice first shows whether its
requirements are useful. If the user has no requirements to state yet, skip this
step and leave the project model index saying so. The first later decision then
becomes the genesis decision.

## Install

Put the consultation entry point in place.

- **Output:** the skill installed in the project and one marked pointer in the
  root `AGENTS.md`.

Run **Install**. Do not copy consultation rules into `AGENTS.md`.

## Verify

Check the documentation as a fresh reader would.

- **Output:** a hand-off naming the entry points, evidence limits, and decisions
  still pending.

1. Check links, front matter, source paths and symbols, commands, and index
   reachability.

2. **Check discovery** with scenarios grounded in the project. For an empty
   project, check that an agent recognizes the absence of implementation and of
   accepted requirements instead of following invented guidance.

3. Check that a repeat installation changes nothing and that unrelated root
   instructions are preserved.

4. Report the entry points, known evidence limits, and decisions still pending.

Documentation proof is navigation, factual checking, and preserved boundaries;
unrelated application test runs are not a substitute.
