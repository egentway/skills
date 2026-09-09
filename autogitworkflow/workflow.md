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

4. Create one concise, imperative commit. Match the repository's established
   commit-subject convention when it is evident; otherwise use a plain subject
   that describes the user-visible change:

   ```sh
   git commit -m "<imperative summary>"
   ```

   Do not amend an existing commit, bypass hooks, force-push, or make a second
   cleanup commit unless the user explicitly asks. If staging or committing
   fails, preserve the worktree and report the failure.

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
