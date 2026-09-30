---
name: present-for-review
description: >-
  Load this skill before writing any message that presents a plan, proposal,
  findings, report, or a set of decisions for the user to review, approve, or
  answer. Shapes the message: orient first, main path first, representative
  abridged excerpts labeled proposed vs current, visible connections, a map of
  affected files, and an explicit approval question. Presentation only; it does not
  decide what to do.
---

# Present for review

Make what you show something the user can evaluate as a connected whole, not a list
of promises or a pile of disconnected snippets. The user should always know what is
happening, what is proposed, and what is being asked of them.

This is a working draft. Refine it through observed use; do not present an untried
process as validated practice.

## Orient

Open any message that needs the user's input with a short status block:

```markdown
**Where we are:** Step 2 of 7, choosing where the skill goes and how it activates.
**Settled:** a changelog-from-diff skill; destination is the skills repository.
**Need from you:** the two decisions below.
**Next:** once you answer, I show the full proposal. Nothing is written yet.
```

Keep each line to one sentence. A progress-only message may use just the first two.

## Main path first

Begin with the selected scope and a short end-to-end flow: the real entry point and
the user-visible result. Follow that flow through the explanation rather than
touring parts alphabetically. Show the connecting piece early, the one that ties the
parts together, and introduce its collaborators after it. Use the same names and
signatures throughout.

For each substantive part, include:

- **Responsibility:** what it owns and why it belongs here.
- **Location:** the exact path, marked `+` new, `~` modified, `-` removed, or
  `>` moved (show old and new).
- **Abridged excerpt:** the relevant structure, not everything.
- **Connection:** what reads or calls it, what it depends on, what it produces.
- **Consequential choice:** anything the user should evaluate.

Do not create a new part or file only to give each section its own home.

## Honest excerpts

- Introduce excerpts as proposed content, not changes already made. Label each with
  its path and status, and keep any comparison with current content separate.
- Keep what makes the design reviewable: interfaces, gates and conditions, the order
  of steps, accepted, rejected and failed outcomes, and the concrete links between
  parts. Omit boilerplate and secondary branches, and say what was omitted when its
  absence could mislead.
- If a condition is essential to correctness, show it or say where it is enforced.
  Never make an unsafe happy path look like the complete behavior.
- Ground anything that already exists in what you actually read. New things may be
  proposed but must be coherent, with named owners and consumers. Never invent
  placeholder bodies or stubs to make a sketch look complete.
- Before presenting, trace one success and one meaningful rejection or failure
  through the excerpts. Check that names, arguments and results agree across parts
  and that affected callers and tests appear.

## Size to the content

A small change gets a compact form: the part, its key excerpt, and the question.
Skip the map and connection notes when there is one part.

Larger or divided work gets a short overview naming the units, their outcomes, and
their real dependencies, then a separate plan per unit. Finish with one combined map
that annotates shared files with the units that touch them.

## Map of affected files

Place a brief tree immediately before the question. It is the index of what came
before, not an additional scope list:

- Give each file a short annotation, and keep the tree shallow through grouped
  prefixes without losing exact locations.
- Cover the content itself plus tests, documentation, configuration, and packaging.
- Add a short **Intentionally untouched** list for adjacent areas a reader might
  expect to change, and name the main integration risk.
- Label it as planned impact. If a location cannot yet be resolved, say so rather
  than inventing a confident path.

## Ask, then stop

End with a direct question, for example: "Do you approve this, or would you like to
change any of these boundaries or excerpts first?" Briefly surface consequential
choices that would otherwise be buried. Then stop.

Approval covers exactly what the question named, and approval of a subset covers
only that subset. Praise, a clarification, a scope answer, or a presentation
improvement is not approval. When the user requests a change, update the affected
excerpts, connections and map together, and ask again.

## Contributions

Other active policies or workflows may ask for additional content, such as a
proposed commit grouping. Include it where it belongs in this structure rather than
as an appendix.
