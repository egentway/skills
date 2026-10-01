# Before Editing

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
