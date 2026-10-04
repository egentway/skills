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

<!-- workflow-instructions 6 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`.
<!-- workflow-instructions end -->

# Operations

## Approve

Present what was produced up to this point, then stop and wait for the user. Their
response applies to this gate only.

# Steps

## Survey

Collect repository and worktree state through the read-only survey script.

- **Input:** the current repository or worktree.
- **Output:** the script's JSON survey.
- **Stop if:** the script returns `error`; report the survey as unavailable and
  end the run without changing any worktree.

1. Resolve `scripts/scout_worktrees.py` relative to this skill directory and run
   it once:

   ```sh
   python3 scripts/scout_worktrees.py --repo <current-worktree>
   ```

2. Use the context-mode execution tool when the JSON may be large. The script
   performs the complete read-only Git survey: authoritative porcelain
   inventory, baseline selection, Worktrunk metadata, local state, divergence,
   pairwise shared ancestry, and clean duplicate detection.

3. Treat successful script output as the evidence source. Do not regenerate its
   Git command sequence. On a survey error, do not fetch, switch branches, invoke
   hooks, or alter a worktree.

## Report

Explain each worktree's purpose, divergence, local state, and relationships.

- **Input:** the JSON survey from Survey.
- **Output:** a re-entry brief covering every worktree and any duplicate candidates.

1. Determine purpose only from `description`, Worktrunk metadata, head subject,
   branch-only commits, and changed paths. Prefix a conclusion not directly
   stated by a description or metadata with **Inference:**. Leave purpose
   unspecified for empty or unavailable worktrees.

2. Present the returned records using Report format below. Put unfinished
   operations and local changes ahead of ordinary divergence. Include full and
   abbreviated HEADs, commit subject/date, all changed-path categories, branch
   descriptions, and relevant Worktrunk metadata. State a missing baseline
   explicitly so it is never mistaken for a clean divergence.

3. For each `shared_ancestry` relationship, report its peer branch/path, shared
   base SHA/subject, each side's commits beyond that base, exclusive commit
   counts, and the diff summary when it clarifies the split. A clearly named
   group may cover several relationships; distinguish branches that merely
   forked independently from the baseline.

### Report format

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

## Clean up

Let the user decide which duplicate candidates to remove.

- **Input:** the `duplicate_candidates` groups from Report.
- **Output:** the user's choice and only the local cleanup they approved.
- **Gate:** **Approve** before removing a worktree or deleting a branch.
- **Stop if:** the survey found no duplicate candidates.

1. For every group, identify the members by exact path and branch. Preserve the
   primary worktree; when it belongs to the group, use it as the presumed
   survivor. When the group contains only linked worktrees, ask which member to
   keep. State the exact worktrees and any local branches proposed for deletion.

2. Present the cleanup proposal and run **Approve**. If the user declines, leave
   the worktrees and branches intact. If they approve, carry out only their
   chosen removals; permission to remove a worktree does not by itself authorize
   deleting its branch.
