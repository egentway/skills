# When Proposing Work

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
