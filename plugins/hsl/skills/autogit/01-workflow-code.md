Run the requested coding task in the recorded feature workspace. Workspace
selection and merge approval are distinct decisions; commit grouping follows the
work proposal when one exists.

<!-- workflow-instructions 6 -->
This is a workflow skill. Its steps are the `##` headings under `# Steps`. When
SKILL.md lists several workflows under `# Workflows`, read only the file of the
one that fits the request; its steps are the run. Work through the steps in
order; the user may redo, skip, or reorder them. When a step names another
section, file, or skill, read it then. A bold name, such as **Approve**, runs that
operation from `# Operations` or that workflow from `# Workflows`.
<!-- workflow-instructions end -->

# Steps

## Prepare

Establish a clean feature workspace before editing.

- **Input:** Current repository and requested coding task.
- **Output:** Feature branch, workspace path, merge target, and workspace mode.
- **Gate:** Resolve dirty state, detached HEAD, uncertain branch role, cleanup
  handling, and any required workspace choice before editing.

1. Resolve the repository root with `git rev-parse --show-toplevel` and record
   the original worktree path.

2. Inspect all tracked, staged, and untracked state:

   ```sh
   git status --porcelain=v1 --untracked-files=all
   ```

   Continue only if empty, even when creating another worktree: it would otherwise
   omit the user's uncommitted starting state. Show dirty status and ask how to
   proceed. Never stash, discard, reset, commit, or include existing changes
   without explicit instruction.

3. Read the current branch with `git branch --show-current` and use the following
   table. Treat `main`, `master`, `develop`, `development`, `staging`, `production`,
   and `release/*` as integration branches. Clear task-oriented names, including
   `feature/*`, `feat/*`, `fix/*`, and `bugfix/*`, identify feature branches.

   | Starting state | Action |
   |---|---|
   | Detached HEAD | Ask for the local base and merge target |
   | Clear feature branch | Reuse its workspace; do not ask to create another |
   | Integration branch | Ask: Worktrunk worktree or in-place feature branch |
   | Branch role unclear | Ask whether to reuse it as the feature branch or treat it as the base |
   | Existing linked worktree | Verify wt recognizes it; otherwise settle cleanup handling before editing |

4. Record the merge target. Honor an explicit local target. Otherwise, for a reused
   feature branch prefer local `main`, then `master`, and ask if neither exists.
   For a new feature branch, use the agreed base (the current integration branch,
   unless the user selected another base). Record whether the workspace is primary
   or linked; recognized linked worktrees use Worktrunk mode.

5. If a workspace is needed, wait for the user's mode choice, then follow
   In-place workspace or Worktrunk workspace. Use the supplied branch name or a
   descriptive `feature/<short-task-slug>`. Do not infer the mode or create a
   workspace before the answer. Run subsequent repository reads, edits, commands,
   and verification in the recorded feature workspace.

### In-place workspace

Create and switch to the agreed feature branch:

```sh
git switch -c <feature-branch>
```

Record the repository root as the feature workspace path.

### Worktrunk workspace

Verify `wt` is available. If absent, report the prerequisite and offer the in-place
mode; do not silently fall back. Create with the recorded base:

```sh
wt switch --create <feature-branch> \
  --base=<recorded-target-branch> \
  --no-cd \
  --format=json
```

Apply Worktrunk hook approval. Record the returned `path` as the feature workspace.
`--no-cd` is required because a tool subprocess cannot change the agent's persistent
working directory. If workspace creation fails, preserve the state and report it;
do not begin editing in an assumed path.

## Work

Complete the requested coding task in the recorded workspace.

- **Input:** Requested task and prepared workspace.
- **Output:** Completed changes and settled commit boundaries.

1. Follow applicable task instructions in the recorded feature workspace.

2. When presenting a work proposal, include intended commits in order, naming
   each task boundary and its scope. Approval settles that grouping; carry it out
   without asking again for each commit. Respect explicit grouping instructions
   and include material boundary changes in revised proposals.

3. Keep tightly coupled implementation, callers, tests, and documentation together.
   Each commit is a complete, reviewable unit leaving a working state. Split at
   coherent task boundaries, not by file or to reach a count. If no clear split
   exists, propose one commit.

4. Do not introduce a separate planning checkpoint solely for commits. Without an
   approved grouping, use one commit for the requested work. Proposal approval
   does not authorize unapproved scope, branch changes, merging, or pushing.

## Commit

Verify and commit complete units along the settled boundaries.

- **Input:** Completed changes and commit grouping.
- **Output:** Verified commits and recorded feature branch.
- **Stop if:** No changes exist, or verification, staging, or committing fails;
  preserve work and report the outcome instead of proceeding to Merge.

1. Complete appropriate focused verification. Inspect `git status --short` and
   `git diff --check`. Do not commit broken work or unrelated files introduced
   after the initial clean-state check. Do not create empty commits.

2. Stage only the paths or hunks belonging to each complete task unit, including
   deletions. For entire files belonging to that unit:

   ```sh
   git add -A -- <changed-path>...
   ```

   If a file spans boundaries, stage relevant hunks. Verify the staged unit without
   relying on unstaged or later changes; keep inseparable changes together.

3. Select the repository's commit convention using Commit message selection.
   Create one concise commit per settled boundary:

   ```sh
   git commit -m "<subject matching the selected convention>"
   ```

4. Repeat staging and committing for remaining boundaries. Do not amend existing
   commits, bypass hooks, force-push, or create unplanned cleanup commits unless
   explicitly requested. Fold cleanup into its task unit before committing.
   On failure preserve the worktree and report the blocker.

### Commit message selection

| Priority | Convention |
|---|---|
| 1 | Explicit repository instructions, contributor documentation, or configuration |
| 2 | Dominant recent non-merge style; resolve equal frequency by recency |
| 3 | Plain concise imperative subject when useful history is absent |

For history, inspect a representative sample such as
`git log -30 --no-merges --format=%s`. Match subject structure, prefix/scope, and
capitalization; inspect bodies when relevant. Explicit rules outrank history.
Do not invent a mandatory convention for the project.

## Merge

Offer to integrate the completed feature and perform named local cleanup.

- **Input:** Verified task commits, feature branch, target, and workspace mode.
- **Output:** Preserved feature workspace, or merged target and cleanup result.
- **Gate:** Explicit approval naming the merge and exact cleanup.
- **Stop if:** Approval is declined or integration cannot proceed safely.

1. After a completed, verified task produces feature-branch commits, offer the
   merge in the final conversational reply. Name the actual feature branch,
   recorded local target, and exactly which worktree and branch cleanup deletes.
   Ask in plain text rather than a structured question tool and wait for approval.

   Worktrunk: “Would you like me to merge `<feature>` into `<target>` and delete
   its worktree and branch?”

   In-place: “Would you like me to merge `<feature>` into `<target>` and delete
   the branch?”

   Enabling the workflow is not merge approval. An explicit request to merge this
   completed feature satisfies the gate; do not transfer approval from another
   feature. On refusal retain the workspace and branch and do not repeat the offer.

2. Before merging, confirm the feature workspace is clean. Capture the feature
   branch, target, feature workspace, and target worktree path before cleanup.
   Refuse detached HEAD, an integration branch as the feature, or an unspecified
   feature branch. Use the appropriate mode below.

3. Report merge and cleanup outcomes separately if either fails. Preserve remaining
   state; do not force removal or rewrite history. A merge requiring rebase or a
   merge commit needs a separate user request. This offer authorizes neither a
   push nor remote branch deletion.

### Merge Worktrunk worktree

From the feature workspace, apply Worktrunk hook approval and run:

```sh
wt merge --no-commit --no-rebase <recorded-target-branch>
```

Both flags are required: prevent additional commits or squash, preserve the
prepared graph, and require fast-forward integration. Plain `wt merge` can squash
and rebase the approved commits. Keep normal hooks enabled.

On success, Worktrunk fast-forwards the target and removes the local feature
worktree and branch. Use the captured target worktree path for subsequent commands
because the feature path no longer exists. On merge or cleanup failure, inspect and
report what completed without forcing removal or rewriting history.

### Merge in-place feature branch

Switch to the recorded target and fast-forward only:

```sh
git switch <recorded-target-branch>
git merge --ff-only <feature-branch>
```

Only after successful merging, delete the merged local branch:

```sh
git branch -d <feature-branch>
```

Never force-delete. If cleanup fails, keep the successful merge and report that
failure. If fast-forward merging fails, preserve both branch tips and report that
a merge commit or rebase would be required; do neither without a user request.

---

# Worktrunk hook approval

Keep normal hooks enabled. If Worktrunk requires project-hook approval, stop and
tell the user to run `wt config approvals add`, then resume after approval.
Do not bypass the gate with `--yes` or `--no-hooks`, or approve the hooks on the
user's behalf.
