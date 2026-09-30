---
name: worktree-scout
description: >-
  workflowz. Survey a repository with multiple Git worktrees after time away,
  reporting each worktree's divergence, local changes, purpose, shared topic
  ancestry, and clean duplicates before deciding whether to remove anything.
---

# Worktree Scout

Create a compact, evidence-backed re-entry brief for every worktree in the
current repository. The scout is read-only until the user explicitly chooses
cleanup.

## Survey

1. Resolve `scripts/scout_worktrees.py` relative to this skill directory and
   run it once:

   ```sh
   python3 scripts/scout_worktrees.py --repo <current-worktree>
   ```

   Use the context-mode execution tool when the JSON may be large. The script
   performs the complete read-only Git survey: authoritative porcelain
   inventory, baseline selection, Worktrunk metadata, local state, divergence,
   pairwise shared ancestry, and clean duplicate detection.
2. Treat successful script output as the evidence source. Do not regenerate its
   Git command sequence. If it returns `error`, report that repository survey
   as unavailable; do not fetch, switch branches, invoke hooks, or alter a
   worktree.
3. Turn the returned records into the report below. Determine purpose only from
   `description`, Worktrunk metadata, head subject, branch-only commits, and
   changed paths. Prefix a conclusion not directly stated by a description or
   metadata with **Inference:**. Leave purpose unspecified for empty or
   unavailable worktrees.

## Report

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

For every `duplicate_candidates` group, preserve the primary worktree as the
presumed survivor, name exact redundant paths, and ask:

> These clean worktrees point to `<sha>`: `<path> (<branch>)`, … . Keep the
> primary worktree and clean up the redundant worktrees?

Wait for the user's choice before removing a worktree or deleting a branch.
