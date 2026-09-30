# hsl — heygent's skill lab

Agent skills, packaged as a plugin marketplace for Claude Code, Codex and omp.

## Layout

```
.claude-plugin/marketplace.json     marketplace "hsl" (also read by Codex and omp)
plugins/<bundle>/
  .claude-plugin/plugin.json        Claude Code manifest
  .codex-plugin/plugin.json         Codex manifest (keep identical to the above)
  package.json                      only needed for `omp plugin link`
  skills/<skill>/SKILL.md
```

Each bundle is a self-contained plugin: paths can't reach outside its directory.
Today there is one bundle, `hsl`. To add another, create `plugins/<bundle>/`
with the same files and add an entry to `marketplace.json`.

## Install (published)

| Tool | Commands |
|---|---|
| Claude Code | `claude plugin marketplace add egentway/skills` then `claude plugin install hsl@hsl` |
| Codex | `codex plugin marketplace add egentway/skills` then `codex plugin add hsl@hsl` |
| omp | `omp plugin marketplace add egentway/skills` then `omp plugin install hsl@hsl` |

Claude Code namespaces skills as `/hsl:<skill>`.

## Install (local checkout, edits show up live)

Assuming the checkout is at `~/skills`:

**Claude Code** reads a local marketplace in place. Restart, or run
`/reload-plugins`, after edits.

```sh
claude plugin marketplace add ~/skills
claude plugin install hsl@hsl
```

**omp** symlinks the plugin directory:

```sh
omp plugin link ~/skills/plugins/hsl
```

**Codex** copies plugins into a cache and does not follow symlinks inside it,
so a local `plugin add` goes stale. Symlink into Codex's own skills directory
instead (skills appear as `hsl:<skill>`):

```sh
ln -s ~/skills/plugins/hsl/skills ~/.codex/skills/hsl
```

Keep `~/.agents/skills` for machine-specific skills. It is a global lookup
that other harnesses read too, so putting `hsl` there hooks it up everywhere
at once. omp reportedly also reads Codex's skills directory, so hooking up
both Codex this way and omp via `omp plugin link` may list every skill twice;
pick one for omp if you see duplicates.

## Releasing

Bump `version` in both `plugin.json` files (and `package.json`) together.
Validate with:

```sh
claude plugin validate .
claude plugin validate plugins/hsl
```
