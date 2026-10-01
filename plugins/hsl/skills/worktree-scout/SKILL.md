---
name: worktree-scout
description: >-
  workflowz. Survey a repository with multiple Git worktrees after time away,
  reporting each worktree's divergence, local changes, purpose, shared topic
  ancestry, and clean duplicates before deciding whether to remove anything.
---

Create a compact, evidence-backed re-entry brief for every worktree in the
current repository. The scout is read-only until the user explicitly chooses
cleanup. Wherever the work splits into independent items, fan them out to
parallel subagents, then verify and integrate their results yourself; work
directly when the harness has no subagents or the items are few.

<!-- workflow-instructions 2 -->
This is a workflow skill. Work through the steps in order; the user may redo, skip,
or reorder them. Only the headings under `# Steps` are steps; any other section is
read when a step refers to it. Under each step, read everything listed before
acting: `skill: <name>` through the skill mechanism, and `[Name]` as the section
with that heading, or the link defined for it relative to this skill's folder. Say
what you read in each step.
<!-- workflow-instructions end -->

# Steps

## Survey
- [Running the scout]

## Report
- [Purpose evidence]
- [Report format]

## Clean up
Only when the survey found duplicate candidates.
- [Duplicate question]
- [Approve]

---

# Operations

## Approve
Once the step's work is done, present what it produced, then stop and wait for
the user. Their response applies to this gate only.

# Running the scout

Resolve `scripts/scout_worktrees.py` relative to this skill directory and
run it once:

```sh
python3 scripts/scout_worktrees.py --repo <current-worktree>
```

Use the context-mode execution tool when the JSON may be large. The script
performs the complete read-only Git survey: authoritative porcelain
inventory, baseline selection, Worktrunk metadata, local state, divergence,
pairwise shared ancestry, and clean duplicate detection.

Treat successful script output as the evidence source. Do not regenerate its
Git command sequence. If it returns `error`, report that repository survey
as unavailable; do not fetch, switch branches, invoke hooks, or alter a
worktree.

# Purpose evidence

Turn the returned records into the report below. Determine purpose only from
`description`, Worktrunk metadata, head subject, branch-only commits, and
changed paths. Prefix a conclusion not directly stated by a description or
metadata with **Inference:**. Leave purpose unspecified for empty or
unavailable worktrees.

# Report format

```markdown
## Worktree scout — <repository>

**Baseline:** `<baseline.ref>` at `<baseline.head short SHA>`; <N> worktrees discovered.

### <branch or detached SHA> — <short HEAD>
- **Path:** `<path>`
- **Purpose:** <evidence or **Inference:** …>
- **Local state:** clean | staged: …; unstaged: …; untracked: …
- **Main divergence:** <ahead>/<behind>; <diff.summary>; <notable branch commits>
- **Shared ancestry:** none after main | <peer relationships>
- **Attention:** <conflict, in-progress operation, lock, prunable state, unavailable, or none>

### Duplicate candidates
- `<sha>`: <clean members>; proposed survivor and redundant paths.
```

Put unfinished operations and local changes ahead of ordinary divergence.
Include full and abbreviated HEADs, commit subject/date, all changed-path
categories, branch descriptions, and relevant Worktrunk metadata. State a
missing baseline explicitly so it is never mistaken for a clean divergence.

For each `shared_ancestry` relationship, report its peer branch/path, shared
base SHA/subject, each side's commits beyond that base, exclusive commit counts,
and the diff summary when it clarifies the split. A clearly named group may
cover several relationships; distinguish branches that merely forked
independently from the baseline.

# Duplicate question

For every `duplicate_candidates` group, preserve the primary worktree as the
presumed survivor, name exact redundant paths, and ask:

> These clean worktrees point to `<sha>`: `<path> (<branch>)`, … . Keep the
> primary worktree and clean up the redundant worktrees?

Wait for the user's choice before removing a worktree or deleting a branch.
