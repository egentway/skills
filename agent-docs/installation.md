# Install or update the project-local skill

Use for authorized installation or upgrade, including the installation step of
[initialization](initialization.md) or [migration](migration.md). Ordinary readers
use [consultation](consultation.md). Skill-internal links resolve from the skill
root; destinations such as `.agents/skills/` refer to the target project root.
Installation supplies instructions, not a completed application guide or migration.

## Choose one self-contained installation

1. Resolve the target repository root and follow its Git/change-safety rules.
   Preserve pre-existing work; installing a skill does not authorize committing,
   stashing, deleting, or resetting unrelated files.
2. Install at `.agents/skills/agent-docs/` so multiple agent tools can discover
   the same project-local package. Do not choose a harness-specific location or
   add a second installed copy. When migrating an earlier installation, compare
   its contents, preserve intentional edits, and remove the superseded copy only
   after the new installation and root pointer are complete.
3. Install these five files together: `SKILL.md`, `consultation.md`,
   `installation.md`, `initialization.md`, and `migration.md`. Copy actual files
   from the supplied skill package, not absolute-home symlinks. Internal guide
   links stay relative to the skill root. References in project documentation,
   including `AGENTS.md`, use project-root-relative targets.
4. A project installation must be version-controlled and usable in a fresh clone
   without the author's home directory or globally installed skills. If its
   parent is ignored, add the narrowest ignore exception for this package only;
   do not expose unrelated tool settings, credentials, caches, or logs.
5. If source and destination resolve to the same directory, do not copy over
   themselves. If an existing installation differs, inspect the differences and
   identify intentional local changes before replacing it. Do not overwrite
   unrelated files, follow an unexpected destination symlink, or silently delete
   additional package files. Stop for a decision if an update would discard work.

The shared source and project-local copy are a distribution boundary, not two
runtime owners. The installed package governs that checkout. Updates are explicit;
there is no automatic download, synchronization hook, or hidden global dependency.

## Manage one root instruction section

Use these literal, standalone HTML comment markers in the root `AGENTS.md`:

```markdown
<!-- docs-organization:start -->
## Documentation

For repository work, first read the installed
[documentation consultation guide](.agents/skills/agent-docs/consultation.md).
Follow its purpose-specific index routing and maintenance rules.
<!-- docs-organization:end -->
```

This is the actual installed project-root path, not a template. Do not substitute
an absolute home path, `skill://` URI, or a setup guide as the routine entry point.
The section points directly to consultation; it does not repeat topic lists,
status definitions, or the full documentation policy.

Before editing, inspect existing documentation guidance and marker boundaries:

- **No markers:** insert one section without rewriting unrelated instructions.
  If `AGENTS.md` does not exist, create a minimal root file containing this section;
  do not invent project policies.
- **One ordered pair:** replace only that bounded section, preserving text outside
  it. If it already matches, leave it unchanged.
- **Duplicate, nested, reversed, or incomplete markers:** stop and report the
  ambiguity. Do not guess a range, delete content, or append another block.
- **Old unmarked documentation rules:** during an approved migration, relocate
  applicable application detail to current guides and remove only the superseded
  organization rules. Preserve unrelated policy. Installation alone is not
  permission to erase arbitrary headings that happen to mention documentation.

Markers are an ownership boundary for repeatable edits, not an executable parser
or a new instruction hierarchy. Use the editing tools available to the agent;
this skill does not require an installer program.

## Check the result

- The installed five files are complete and their skill-root references resolve.
  The root consultation pointer resolves from the project root, not the skill root.
- Exactly one ordered marker pair exists. Text outside it is unchanged except for
  separately approved migration edits.
- Project ignore rules include the package without exposing neighboring ignored
  content. Installation must survive checkout on another machine.
- A repeat installation against identical files changes nothing and creates no
  duplicate block, copy, timestamp, or topic catalog.
- A reader starting at `AGENTS.md` reaches consultation, then the task's index,
  without being directed to rerun setup.

For an upgrade, compare the local package with the intended source after applying
approved changes. Check docs for links that still assign maintenance policy to an
old inline root section; route them to the installed consultation guide while
keeping unrelated repository instructions in `AGENTS.md`.
