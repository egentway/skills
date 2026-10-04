For authorized installation or upgrade, including the Install step of Initialize
and Migrate. Ordinary readers use [01-consultation.md](01-consultation.md).
Skill-internal links resolve from the skill root; destinations such as
`.agents/skills/` refer to the target repository root. Installation supplies
instructions, not documentation or a completed migration.

# Steps

## Place

Install the complete package in one self-contained location.

- **Input:** the supplied skill package; the target repository and any earlier
  installation.
- **Output:** the eight package files at `.agents/skills/mod/`, usable from a
  fresh clone.
- **Gate:** **Approve** before an update that would discard intentional local
  changes.
- **Stop if:** the project is documented in an earlier system, such as an
  agent-docs installation or a `docs-organization` section in `AGENTS.md`, and
  this run is not part of Migrate. Report it and offer **Migrate**; installing
  alone would point agents at a layout that does not exist yet.

1. Resolve the target repository root and follow its change-safety rules.
   Installing does not authorize committing, stashing, deleting, or resetting
   unrelated files.

2. Install at `.agents/skills/mod/`, so several agent tools discover the same
   package. Do not choose a harness-specific location or add a second copy.

3. Install these files together: `SKILL.md`, `01-consultation.md`,
   `02-workflow-decide.md`, `03-workflow-initialize.md`,
   `04-workflow-migrate.md`, `05-workflow-audit.md`, `06-workflow-install.md`,
   and `07-records.md`. Copy actual files, not symlinks to a home directory.

4. Keep the installation version-controlled and usable without the author's home
   directory or globally installed skills. If its parent is ignored, add the
   narrowest ignore exception for this package only.

5. If source and destination are the same directory, do not copy over them. If an
   existing installation differs, inspect the differences and identify
   intentional local changes before replacing it. Do not follow an unexpected
   destination symlink or silently delete extra files.

The shared source and the project copy are a distribution boundary, not two
runtime owners: the installed package governs that checkout, and updates are
explicit.

## Point

Keep one root section pointing to consultation.

- **Input:** the root `AGENTS.md`, if any, and its marker boundaries.
- **Output:** exactly one ordered marker pair whose section points to the
  installed consultation guide.
- **Stop if:** the markers are duplicated, nested, reversed, or incomplete.
  Report the ambiguity; do not guess a range, delete content, or append another
  block.

Use these literal, standalone markers in the root `AGENTS.md`:

```markdown
<!-- mod:start -->
## Requirements and documentation

For repository work, first read the installed
[consultation guide](/.agents/skills/mod/01-consultation.md). Changes follow the
project model in `docs/agents/model/`; a change it does not allow needs an
accepted decision first.
<!-- mod:end -->
```

1. **No markers:** insert the section without rewriting unrelated instructions.
   If `AGENTS.md` does not exist, create a minimal file containing only this
   section.

2. **One ordered pair:** replace only the bounded section. If it already
   matches, leave it unchanged.

3. **An earlier system's section,** such as agent-docs' `docs-organization`
   block: remove it only within an approved migration, after its content is
   accounted for.

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If the project has a `CLAUDE.md`
that neither imports nor links `AGENTS.md`, report it and offer to add the
import; do not edit it unasked.

## Check

Check the result.

- **Output:** confirmation of each check below, or what failed.

1. The eight installed files are complete and their skill-root links resolve. The
   root pointer resolves from the repository root.

2. Exactly one ordered marker pair exists, and text outside it is unchanged
   except for separately approved migration edits.

3. Ignore rules include the package without exposing neighboring ignored content.

4. A repeat installation against identical files changes nothing and creates no
   duplicate block or copy.

5. A reader starting at `AGENTS.md` reaches consultation and then the project
   model without being sent back to setup.

6. Ordinary consultation does not start Initialize, Migrate, Install, or Audit,
   and an explicit audit request reaches 05-workflow-audit.md.
