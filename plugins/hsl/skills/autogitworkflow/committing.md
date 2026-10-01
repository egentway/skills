# After Editing

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
