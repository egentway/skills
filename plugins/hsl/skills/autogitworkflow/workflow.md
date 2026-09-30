# Enabled Auto Git Workflow

Use these instructions only after the user explicitly opts in, explicitly asks
for this workflow, or invokes the skill manually for the current repository task.

## Before Editing

1. Resolve the repository root with `git rev-parse --show-toplevel`. Record this
   original worktree path.
2. Check all tracked, staged, and untracked state with:

   ```sh
   git status --porcelain=v1 --untracked-files=all
   ```

   Continue only when it produces no output. This applies even when a separate
   worktree could be created: otherwise the new branch would silently exclude the
   user's uncommitted starting state. If the worktree is not clean, show the
   status and ask the user how to proceed. Never stash, discard, reset, commit,
   or include existing changes without an explicit instruction.
3. Read the current branch with `git branch --show-current`. If HEAD is detached,
   stop and ask which local branch should be the task's base and merge target.
   Treat `main`, `master`, and common integration branches (`develop`,
   `development`, `staging`, `production`, `release/*`) as integration branches.
   Treat a named, task-oriented branch as a feature branch, including the common
   `feature/*`, `feat/*`, `fix/*`, and `bugfix/*` forms.
4. If already on a clear feature branch, use its current worktree and do not ask
   to create another workspace. Record whether it is the primary worktree or a
   linked worktree. Treat a linked worktree as Worktrunk mode after verifying
   that `wt` recognizes it; if `wt` is unavailable or does not recognize it, ask
   the user how its eventual cleanup should be handled before editing. Record an
   explicitly named merge target; otherwise prefer local `main`, then local
   `master`, and ask if neither exists.
5. Otherwise, record the current branch as the task's base and merge target. Ask
   the user to choose one of these workspace modes before editing:

   - **Worktrunk worktree** — create an isolated worktree and feature branch.
   - **In-place feature branch** — create and switch branches in the current
     worktree.

   Do not infer the choice or create either workspace before the user answers. If
   the user does not supply a branch name, use a descriptive
   `feature/<short-task-slug>`.
6. For an in-place feature branch, run:

   ```sh
   git switch -c feature/<short-task-slug>
   ```

   Record the repository root as the feature workspace path.
7. For a Worktrunk worktree, first verify that `wt` is available. If it is not,
   report the missing prerequisite and offer the in-place feature branch instead;
   do not silently fall back. Create the workspace with normal hooks enabled:

   ```sh
   wt switch --create feature/<short-task-slug> \
     --base=<recorded-target-branch> \
     --no-cd \
     --format=json
   ```

   Record the returned `path` as the feature workspace path. `--no-cd` is
   required because a tool subprocess cannot change the agent's persistent
   working directory. Run every subsequent repository read, edit, command, and
   verification in the returned path.

   Never pass `--yes` or `--no-hooks` to bypass Worktrunk hook approval. If a
   hook requires approval, stop and tell the user to run
   `wt config approvals add`, then resume after they approve the commands.

Once the workspace is established, continue the requested work there.

## When Proposing Work

When ready to present a work proposal to the user, include the intended commits
alongside the work to be done. Identify each commit's task boundary with a short
description of its scope, in the intended commit order. Propose separate commits
where the work has obvious, coherent task boundaries rather than deciding the
split only after implementation.

Approval of the proposal approves its commit grouping. Carry out that grouping
autonomously without asking again for each commit. Respect explicit user
instructions about grouping, and include any material change to the proposed
boundaries when presenting a revised work proposal.

Each commit must represent a complete, reviewable unit. Keep tightly coupled
implementation, callers, tests, and documentation together; do not split merely
by file or to reach a commit count. Order dependent commits so each leaves a
working state. If no clear split exists, propose one commit. Do not introduce a
separate planning checkpoint solely for commits when no work proposal is needed;
without an approved grouping, use one commit for the requested work.
Proposal approval does not authorize unapproved scope, branch changes, merges,
or pushes.

## After Editing

1. Complete the requested changes and any appropriate focused verification.
2. Inspect the final change set with `git status --short` and `git diff --check`.
   Do not commit a broken working tree or unrelated files introduced after the
   initial clean-state check. If there are no changes, do not create an empty
   commit.
3. For each commit, stage only the files or hunks belonging to that task boundary,
   including deletions. When entire files belong to the commit:

   ```sh
   git add -A -- <changed-path>...
   ```

   If a file spans multiple task boundaries, stage only the relevant hunks.
   Verify the staged change as a complete unit without relying on unstaged or
   later changes; keep changes together when they cannot be separated safely.

4. Create one concise commit per planned task boundary using this convention precedence:

   - Follow the repository's explicit commit convention first, including its
     instructions, contributor documentation, or commit-message configuration.
     Repository rules take precedence over examples in history.
   - If no convention is specified, inspect a representative sample of recent
     non-merge commits and mimic their style. For example:

     ```sh
     git log -30 --no-merges --format=%s
     ```

     When multiple styles appear, favor the most frequent convention rather than
     blindly copying the latest commit. Match its subject structure, prefix/scope
     usage, and capitalization; inspect bodies when their format matters. If
     styles are equally frequent, prefer the one used more recently.
   - If there is no useful history, use a plain, concise imperative subject
     describing the change. Do not invent a mandatory convention for the project.

   ```sh
   git commit -m "<subject matching the selected convention>"
   ```

   Repeat staging and committing for each task boundary. Do not amend an existing
   commit, bypass hooks, force-push, or make an unplanned cleanup commit unless
   the user explicitly asks. Fold cleanup into its task's commit before committing.
   If staging or committing fails, preserve the worktree and report the failure.

## Offer to Merge Substantial Work

After substantial work is complete, verified, and committed on a feature branch,
include a merge offer in the final plain-text response. Name the actual feature
branch and the recorded local target. State exactly what successful cleanup will
delete.

For a Worktrunk worktree:

> Would you like me to merge `feature/example` into `main` and delete its worktree and branch?

For an in-place feature branch:

> Would you like me to merge `feature/example` into `main` and delete the branch?

Ask conversationally, without the Ask tool, structured-choice dialogs, or similar
interactive question tools. Wait for explicit user approval before merging.
Enabling the automatic workflow is not itself merge approval. If the user has
already explicitly requested the merge of this completed work, follow that
request instead of asking again; do not carry approval from a different feature
branch forward.

If the user declines, leave the completed workspace and branch intact and do not
repeat the offer for the same work. The offer does not authorize a push or remote
branch deletion.

## Merge Requests and Local Cleanup

Before merging, confirm that the feature workspace is clean. Capture the feature
branch, recorded target branch, feature workspace path, and target worktree path
before any cleanup. Refuse a merge from a detached HEAD, an integration branch,
or an unspecified feature branch.

### Worktrunk worktree

Run the merge from the feature worktree:

```sh
wt merge --no-commit --no-rebase <recorded-target-branch>
```

Both flags are required. `--no-commit` prevents Worktrunk from committing or
squashing additional changes; `--no-rebase` preserves the prepared commit graph
and requires the target to fast-forward. Never use plain `wt merge` here because
its default squash and rebase behavior would rewrite the approved commits.

Keep normal hooks enabled. If Worktrunk reports that project hooks require
approval, stop and ask the user to run `wt config approvals add`; never bypass
the gate with `--yes` or `--no-hooks`.

On success, Worktrunk fast-forwards the target and removes the local feature
worktree and branch. Run every subsequent command from the captured target
worktree path because the feature path no longer exists. If merge or cleanup
fails, do not force removal or rewrite history; preserve the remaining state and
report exactly what completed.

### In-place feature branch

Use a fast-forward-only merge from the recorded target, then delete the merged
local feature branch:

```sh
git switch <recorded-target-branch>
git merge --ff-only <feature-branch>
git branch -d <feature-branch>
```

Run the deletion only after the merge succeeds. Never force-delete a feature
branch. If deletion fails after a successful merge, keep the merge and report the
cleanup failure. If the merge cannot fast-forward, leave both branches unchanged
and report that a merge commit or rebase would be required; do neither unless the
user asks.

Remote branch deletion always requires separate user approval.
