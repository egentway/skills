# Presentation

Use present-for-review for message structure. If unavailable, use the main path
first, labeled excerpts, a file map, and an approval question for proposals.
This file adds the skill-specific review view.

## Show a skill

Entry → complete outline → opened sections

| Part | Show |
|---|---|
| Entry | Description and opening, abridged |
| Outline | Every file in reading order, with headings |
| Workflow step | Purpose, Gate, Stop if, and called operations or workflows |
| Shared section after a horizontal rule | First sentence |
| Opened sections | Requested or changed sections, labeled current or proposed |

Order SKILL.md first, then numbered references, then catalogues. Include tooling
and metadata in the file map. Generate existing Markdown outlines with
`python3 scripts/outline.py <skill-dir>`, resolving the script relative to this
skill. Write proposed outlines in the same form. Expand only the requested or
changed sections; keep the rest in the outline. Use this view for proposals,
reports, and requests to show or compare a skill. Proposal contents belong to
Propose in 01-workflow-issue.md.

## Collect authoring decisions

Gather the open authoring choices in one message.

| Part | Rule |
|---|---|
| Assumed | State what available context settles, as a line the user can veto |
| Questions | Number consequential unresolved choices; recommend an option with a brief reason |
| Always ask when unsettled | Destination, bundle, extraction boundary, activation |
| Shortcut | “Accept” takes only the numbered recommendations, not proposal-writing approval |

Infer only what is obvious. Assumptions stand unless vetoed; accepting recommendations
does not separately confirm them. Do not ask again about settled choices.

```text
Assumed (tell me if wrong): read-only; targets Claude Code, omp, Codex.
1. Bundle: workflow or quality? Recommend workflow (fits a release step).
2. Activation: automatic or request-only? Recommend automatic (read-only).
Reply “accept” to take both recommendations, or change any number.
```

## Report delivery

After writing, verification, and committing, report results with these fields:

```text
Files:
Commit:
Checks run:
Not run:
Open items:
```

Use 04-verification.md to distinguish actual check results from walkthroughs and
unverified behavior. Include forward-test results and rough cost when performed.
