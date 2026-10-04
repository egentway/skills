# Records and formats

The formats mod writes and reads in a target project. Decide, Initialize, Migrate,
and Audit read this file in full; ordinary consultation reads it when a change
needs **Decide**. Project paths below are relative to the target repository root.

## Layout

```text
AGENTS.md                         one marked block pointing to consultation
.agents/skills/mod/               the installed skill
docs/agents/
  mod.yaml                        format version and acceptance settings
  model/                          the project model: current requirements
    index.md                      application map and model files
  decisions/
    index.md                      accepted and pending records
    yyyymmdd-hhmm-<slug>.md       accepted decisions
    pending/                      proposals awaiting a decision
    archive/                      refused and withdrawn proposals
    pre-genesis/                  records imported from earlier systems
  implementation/                 what is built: owners, edit paths, checks, gaps
    index.md
  reference/                      evidence: studies, experiments, measurements
    index.md
```

Create only what exists; an index may state that it has no records yet. `docs/`
outside `docs/agents/` stays available for documentation with other purposes.

## Links and paths

Markdown links between project documents start with `/` and resolve from the
repository root, as GitHub and VS Code resolve them:
`/docs/agents/model/forms.md#validation`. Code-formatted paths are also
repository-relative. State this base to readers; it is not a filesystem path.

Links point upstream, toward what determines the linking document:

| From | May link to |
| --- | --- |
| A decision record | Earlier decisions, pre-genesis records, `reference/` evidence |
| A project-model section | The decision parts in force for it |
| An implementation guide | Project-model sections, code, other guides |
| A commit | A decision or project-model section, through `Refs:` |

A decision never links into the project model or the implementation guides. Both
can be reorganized; a decided record cannot be edited to follow them. Mentions of
code in a decision describe the situation when it was written and are not
maintained.

## Project model

`docs/agents/model/` describes what the application must be, as current
requirements rather than history. Organize files by area or by substantial
interaction surface, such as an API, a console, or module interfaces. `index.md`
gives the application map and routes to the files.

Each section summarizes its requirements well enough to understand what the
application does and to route a change, then links the decision parts in force
for it. Details stay in those parts.

```markdown
# Forms

Forms collect a draft that the user submits as a single operation
([D-20260911-0930](/docs/agents/decisions/20260911-0930-forms.md#drafts)).

## Validation

Errors appear beside the affected input, together with the action that fixes
them. Errors spanning several fields go to the form summary
([D-20261003-0930](/docs/agents/decisions/20261003-0930-field-local-validation.md#requirements)).
```

- A section links only decision parts in force for it. That link is what puts a
  part in force; history belongs in the decisions.

- A link applies to the section it appears in, up to the next heading.

- A section is identified by its file and heading anchor, such as
  `/docs/agents/model/forms.md#validation`. Renaming or moving a heading is an
  editorial change that must repair links to it.

- Its meaning changes only in the commit that records an accepted decision.
  Rewording or reorganizing without changing meaning is editorial and goes in its
  own commit.

## Decision records

A proposal and a decision are the same record at different stages: a proposal is
pending, a decision is accepted.

Name each record `yyyymmdd-hhmm-<slug>.md` with its UTC creation time; its ID is
`D-yyyymmdd-hhmm`. If the name is taken, use the next free minute.

```markdown
---
format: mod/1
id: D-20261003-0930
status: accepted
created: 2026-10-03T09:30Z
decided: 2026-10-04T14:12Z
is_human_approved: true
approved_by: heygent
supersedes:
  - decision: D-20260911-0930
    part: validation
---

# Field-local validation errors

## Requirements

An error about a single field appears directly below that field when the field
loses focus or the form is submitted. It says what to change, not only what is
wrong.

Errors involving several fields appear in the form summary above the submit
button, naming the fields involved. Page-wide banners are reserved for failures
of the whole operation and never repeat field errors.

## Context

## Options

## Rationale
```

### Front matter

| Field | Values | Present |
| --- | --- | --- |
| `format` | `mod/1` | Always |
| `id` | `D-yyyymmdd-hhmm`, matching the filename | Always |
| `status` | `pending`, `accepted`, `refused`, `withdrawn` | Always |
| `created` | ISO 8601 UTC timestamp | Always |
| `decided` | ISO 8601 UTC timestamp | Once decided |
| `is_human_approved` | `true` or `false` | Accepted records |
| `approved_by` | Identifier of the approver | Accepted records; optional unless `mod.yaml` requires it |
| `supersedes` | List of `decision` and optional `part` | When replacing earlier requirements |
| `kind` | `genesis` or `opening-balance` | Only for those records |
| `post_hoc` | `true` | Accepted after its code reached the main branch |

Keep free text out of the front matter; the title is the H1 heading.

### Sections

| Section | Holds | Keeps out | Present |
| --- | --- | --- | --- |
| Title (H1) | The decision named by its outcome, not its question | | Always |
| Requirements | What must be true while the decision is in force: complete, present tense, with applicability and exceptions | Reasons, history, alternatives, plans | Always, first |
| Context | What prompted the decision: the problem, the request, constraints, the earlier requirements, evidence links | The choice itself | Always; a paragraph can suffice |
| Options | Alternatives considered and their consequences | | When there were real alternatives |
| Rationale | Why this option, the trade-offs accepted, what a trial uncovered, and what would justify reconsidering it | Restated requirements | Always |
| Plan | How the implementation will reach the requirements and which gaps it opens | | Optional |
| Outcome | Why the proposal was not accepted | | Refused and withdrawn records |

Requirements may be split into parts, one H3 each, named in the record's own
terms. A part is the unit the project model links and a later decision replaces.
Headings within a record are unique, so their anchors are stable.

### Lifecycle

- **Pending:** in `decisions/pending/`, freely editable while it is drafted,
  revised, and tried.

- **Deciding** is the record's last edit, made in one commit. Set `status` and
  `decided`; for an accepted record also `is_human_approved` and, where known or
  required, `approved_by`; for a refused or withdrawn record write Outcome. Move
  the file to `decisions/` or `decisions/archive/`, keeping its name.

- **Decided:** frozen. Supersession is recorded on the newer decision, implementation
  progress as gaps in the implementation guides, and a mistaken requirement as a
  new decision. The approver approved the record's text, so that text is what was
  agreed.

A file moves at most once, when it is decided, so links to decided records stay
valid. Only a person refuses; a stale proposal is withdrawn.

### Supersession

A decision that changes requirements from an earlier decision replaces whole
parts, or the whole Requirements section, and restates them in full. List each
in `supersedes`; omit `part` to replace all of that decision's requirements. Never
amend part of a part: a requirement must be readable from one decision.

A decision part is in force while a project-model section links it. After the
recording commit, the superseded part has no links left.

### Approval

`is_human_approved` states whether a person or an agent accepted the record.
`approved_by` may add who: for a person, what they state or the repository's Git
identity; for an agent, an identity from a real identification system. Never
guess an identifier. When `mod.yaml` requires one that cannot be established, ask.

An agent may accept only when `mod.yaml` enables delegated acceptance, and only
as a reviewer with a fresh context that did not draft the proposal. It accepts or
escalates to a person; it never refuses.

### Genesis and opening balance

The first decision of a project is `kind: genesis`; for a project migrated from
an earlier system it is `kind: opening-balance`. Its Requirements has one part per
topic, so later decisions can replace it a part at a time. Its Context describes
the starting point, and it usually has no Options.

## Decisions index

`decisions/index.md` is a view for navigation; the records and the project
model's links are the data. Keep it in agreement with them.

```markdown
# Decisions

## Accepted

- [D-20261003-0930 Field-local validation errors](/docs/agents/decisions/20261003-0930-field-local-validation.md)
- [D-20260911-0930 Forms](/docs/agents/decisions/20260911-0930-forms.md): validation superseded by D-20261003-0930

## Pending

- [D-20261006-0910 Inline draft editing](/docs/agents/decisions/pending/20261006-0910-inline-draft-editing.md)

Refused and withdrawn proposals: [archive](/docs/agents/decisions/archive/).
Records from earlier systems: [pre-genesis](/docs/agents/decisions/pre-genesis/).
```

## Pre-genesis records

Records imported from an earlier system keep their original body and filename.
The import commit adds a header and repairs their links; after that they are
frozen.

```markdown
> Imported into mod on 2026-10-05 from `docs/agents/design/20260301-1200-sync.md`
> (agent-docs). Original date: 2026-03-01, first Git addition. Kept for its
> rationale; it does not govern current work.
```

## Implementation guides

`implementation/index.md` gives a short application map and task-to-topic
routing. A topic guide opens with when to consult it and a task-to-file or symbol
map, then the main flow, invariants, wrong edit boundaries, and focused checks.
It links code and project-model sections rather than copying either.

Where the implementation does not yet conform to the project model, the guide
says so under a fixed heading:

```markdown
## Gaps with the project model

- The settings page still shows validation errors in a page banner
  ([Forms › Validation](/docs/agents/model/forms.md#validation)).
```

## Reference records

`reference/` holds source studies, experiments, and measurements, reached through
its index. Preserve revisions, conditions, and limits of each claim, and
distinguish evidence from implications. Records do not move once written, because
decisions link to them; the index lists records that are no longer relevant
separately.

## Settings

```yaml
format: mod/1
acceptance:
  delegated: false
  approver_identity: optional    # optional | required
  approver_identity_rule: ""     # the project's own wording, if it has one
```

`docs/agents/mod.yaml` holds the project's acceptance settings. Only a person
changes them.

## Commit references

A commit may name what it follows in a Git trailer when that helps a reader:

```text
Refs: D-20261003-0930
Refs: /docs/agents/model/forms.md#validation
```

Nothing depends on it. A decision ID never goes stale; a section path can after a
reorganization.

## Format versions

`format` marks every record and `mod.yaml`. The format grows by adding fields or
sections, never by changing what an existing one means. Readers keep reading
every version, because decided records never change.
