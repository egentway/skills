For authorized installation or upgrade, including the Install step of Initialize
and Migrate. Ordinary readers use [01-consultation.md](01-consultation.md).
Skill-internal links resolve from the skill root; destinations such as
`.agents/skills/` refer to the target project root. Installation supplies
instructions, not a completed application guide or migration.

# Steps

## Place

Install the complete package in one self-contained location.

- **Input:** the supplied skill package; the target repository and any earlier
  installation.
- **Output:** the six package files at `.agents/skills/agent-docs/`, usable from a
  fresh clone.
- **Gate:** **Approve** before an update that would discard intentional local
  changes.

1. Resolve the target repository root and follow its Git/change-safety rules.
   Preserve pre-existing work; installing a skill does not authorize committing,
   stashing, deleting, or resetting unrelated files.

2. Install at `.agents/skills/agent-docs/` so multiple agent tools can discover
   the same project-local package. Do not choose a harness-specific location or
   add a second installed copy. When migrating an earlier installation, compare
   its contents, preserve intentional edits, and remove the superseded copy only
   after the new installation and root pointer are complete.

3. Install these six files together: `SKILL.md`, `01-consultation.md`,
   `02-workflow-initialize.md`, `03-workflow-migrate.md`, `04-workflow-audit.md`,
   and `05-workflow-install.md`. Copy actual files from the supplied skill
   package, not absolute-home symlinks. Internal guide links stay relative to the
   skill root. References in project documentation, including `AGENTS.md`, use
   project-root-relative targets.

4. An earlier installation may use unnumbered names: `consultation.md`,
   `initialization.md`, `migration.md`, `audit.md`, and `installation.md`. Treat
   them as the previous versions of the numbered files when comparing contents,
   and remove them once Point has moved the root pointer to `01-consultation.md`.

5. A project installation must be version-controlled and usable in a fresh clone
   without the author's home directory or globally installed skills. If its
   parent is ignored, add the narrowest ignore exception for this package only;
   do not expose unrelated tool settings, credentials, caches, or logs.

6. If source and destination resolve to the same directory, do not copy over
   themselves. If an existing installation differs, inspect the differences and
   identify intentional local changes before replacing it. Do not overwrite
   unrelated files, follow an unexpected destination symlink, or silently delete
   additional package files.

The shared source and project-local copy are a distribution boundary, not two
runtime owners. The installed package governs that checkout. Updates are explicit;
there is no automatic download, synchronization hook, or hidden global dependency.

## Point

Keep one root section pointing to consultation.

- **Input:** the root `AGENTS.md`, if any, and its marker boundaries.
- **Output:** exactly one ordered marker pair whose section points to the
  installed consultation guide.
- **Stop if:** the markers are duplicate, nested, reversed, or incomplete. Report
  the ambiguity; do not guess a range, delete content, or append another block.

Use these literal, standalone HTML comment markers in the root `AGENTS.md`:

```markdown
<!-- docs-organization:start -->
## Documentation

For repository work, first read the installed
[documentation consultation guide](.agents/skills/agent-docs/01-consultation.md).
Follow its purpose-specific index routing and maintenance rules.
<!-- docs-organization:end -->
```

This is the actual installed project-root path, not a template. Do not substitute
an absolute home path, `skill://` URI, or a setup guide as the routine entry point.
The section points directly to consultation; it does not repeat topic lists,
status definitions, or the full documentation policy.

Inspect existing documentation guidance and marker boundaries, then:

1. **No markers:** insert one section without rewriting unrelated instructions.
   If `AGENTS.md` does not exist, create a minimal root file containing this
   section; do not invent project policies.

2. **One ordered pair:** replace only that bounded section, preserving text
   outside it. If it already matches, leave it unchanged. A section that points to
   an earlier installation's `consultation.md` is replaced the same way.

3. **Old unmarked documentation rules:** during an approved migration, relocate
   applicable application detail to current guides and remove only the superseded
   organization rules. Preserve unrelated policy. Installation alone is not
   permission to erase arbitrary headings that happen to mention documentation.

Markers are an ownership boundary for repeatable edits, not an executable parser
or a new instruction hierarchy. Use the editing tools available to the agent;
this skill does not require an installer program.

## Check

Check the result.

- **Output:** confirmation of each check below, or what failed.

1. The installed six files are complete and their skill-root references resolve.
   The root consultation pointer resolves from the project root, not the skill
   root. No unnumbered files from an earlier installation remain.

2. Exactly one ordered marker pair exists. Text outside it is unchanged except for
   separately approved migration edits.

3. Project ignore rules include the package without exposing neighboring ignored
   content. Installation must survive checkout on another machine.

4. A repeat installation against identical files changes nothing and creates no
   duplicate block, copy, timestamp, or topic catalog.

5. A reader starting at `AGENTS.md` reaches consultation, then the task's index,
   without being directed to rerun setup.

6. An explicit user audit request reaches `04-workflow-audit.md`; ordinary
   consultation does not initiate it. The audit requires evidence review before
   edits and user feedback between refinement batches. Installing/updating the
   skill does not itself authorize an audit.

For an upgrade, compare the local package with the intended source after applying
approved changes. Check docs for links that still assign maintenance policy to an
old inline root section; route them to the installed consultation guide while
keeping unrelated repository instructions in `AGENTS.md`.
