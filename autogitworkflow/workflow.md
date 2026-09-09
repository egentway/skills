# Enabled Auto Git Workflow

Use these instructions only after the user explicitly opts in to the automatic
Git workflow for the current repository task.

## Before Editing

1. Resolve the repository root with `git rev-parse --show-toplevel` and operate
   only in that worktree.
2. Check all tracked, staged, and untracked state with:

   ```sh
   git status --porcelain=v1 --untracked-files=all
   ```

   Continue only when it produces no output. If it is not clean, show the
   status and ask the user how to proceed. Never stash, discard, reset, commit,
   or include existing changes without an explicit instruction.
3. Read the current branch with `git branch --show-current`. A detached HEAD,
   `main`, `master`, and common integration branches (`develop`, `development`,
   `staging`, `production`, `release/*`) are not feature branches. Treat a
   named, task-oriented branch as a feature branch, including the common
   `feature/*`, `feat/*`, `fix/*`, and `bugfix/*` forms.
4. If the branch is not clearly a feature branch, ask whether to create a new
   feature branch before making any edits. Do not create or switch a branch
   until the user agrees. If they agree but do not supply a name, create a
   descriptive `feature/<short-task-slug>` branch from the current clean HEAD:

   ```sh
   git switch -c feature/<short-task-slug>
   ```

   Once on a feature branch, continue the requested work.

## After Editing

1. Complete the requested changes and any appropriate focused verification.
2. Inspect the final change set with `git status --short` and `git diff --check`.
   Do not commit a broken working tree or unrelated files introduced after the
   initial clean-state check. If there are no changes, do not create an empty
   commit.
3. Stage only files changed for the request, including deletions:

   ```sh
   git add -A -- <changed-path>...
   ```

4. Create one concise commit using this convention precedence:

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

   Do not amend an existing commit, bypass hooks, force-push, or make a second
   cleanup commit unless the user explicitly asks. If staging or committing
   fails, preserve the worktree and report the failure.

## Offer to Merge Substantial Work

After substantial work is complete, verified, and committed on a feature branch,
include a merge offer in the final plain-text response. Name the actual feature
branch and the local target: prefer `main`, otherwise `master`. If neither exists,
ask which target to use rather than inventing one.

For example:

> Would you like me to merge `feature/example` into `main`?

Ask conversationally, without the Ask tool, structured-choice dialogs, or similar
interactive question tools. Wait for explicit user approval before switching
branches or merging. Enabling the automatic workflow is not itself merge approval.
If the user has already explicitly requested the merge of this completed work,
follow that request instead of asking again; do not carry approval from a
different feature branch forward.

If the user declines, leave the completed work on its feature branch and do not
repeat the offer for the same work. Approved merges still follow the clean-worktree
and fast-forward-only procedure below; the offer does not authorize a push.

## Fast-Forward Merge Requests

When the user asks to merge the completed feature branch, capture the named
feature branch (or the current feature branch) before switching. First confirm
the worktree is clean and identify the target branch: prefer local `main`, then
local `master`. If neither exists, ask the user for the target. Refuse a merge
from a detached HEAD, an integration branch, or an unspecified feature branch.

Use a fast-forward-only merge from the target branch:

```sh
git switch <main-or-master>
git merge --ff-only <feature-branch>
```

`--ff-only` belongs to `git merge`, not `git checkout`. The equivalent command
using the older checkout syntax is:

```sh
git checkout <main-or-master>
git merge --ff-only <feature-branch>
```

If the merge cannot fast-forward, leave both branches unchanged and report that
a merge commit or rebase would be required; do neither unless the user asks.
