# Offer to Merge Substantial Work

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

# Merge Requests and Local Cleanup

Before merging, confirm that the feature workspace is clean. Capture the feature
branch, recorded target branch, feature workspace path, and target worktree path
before any cleanup. Refuse a merge from a detached HEAD, an integration branch,
or an unspecified feature branch.

## Worktrunk worktree

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

## In-place feature branch

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
