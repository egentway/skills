---
name: feedback-driven-execution
description: >-
  Use when implementation is likely to reveal consequential choices that could
  not be settled from requirements alone, especially at unfamiliar integration
  seams, in projects without a governing convention, or whenever a solution
  starts to feel patched together or hacky. Ask a technical user for focused,
  concrete feedback when it is cheaper than silently choosing and later
  reworking the result. Use with cognitive-budget-coding so the implementation
  and the choices presented remain easy to evaluate.
---

# Feedback-Driven Execution

Optimize implementation for alignment, not uninterrupted autonomy.

Requirements cannot expose every decision. Some choices become real only after
code reaches an integration seam and the constraints on both sides are visible.
Surface those choices when the user's answer can still change the direction
cheaply. Do not make the user discover a consequential compromise in the final
review.

Every question also spends attention. Ask only when the expected benefit of
feedback exceeds the interruption cost, except that hacky integration must
always be surfaced.

## Working contract

During implementation:

1. Find the explicit requirements, prior user choices, and relevant project
   conventions before inventing a new choice.
2. Implement until a decision is supported by concrete evidence. Do not ask
   speculative questions merely because alternatives can be imagined.
3. Stop before an unresolved choice spreads through call sites, schemas,
   storage, public APIs, or control flow.
4. Ask the user when the choice meets the feedback threshold below.
5. Continue autonomously when precedent or a cheap, reversible default resolves
   the matter.
6. Never hide or normalize a hack because work has already started.

Correctness, safety, and the explicit contract constrain the available options.
Do not offer an invalid option for the sake of presenting a choice.

## Decide whether feedback pays for itself

Use this model:

> feedback value = risk of choosing against the user's preference × cost of
> correcting that choice later

Compare it with the context switch, explanation, and delay imposed by asking.
Ask when feedback value is materially higher.

Feedback value rises when:

- two or more technically sound choices express different product behavior,
  domain boundaries, APIs, data ownership, failure semantics, or maintenance
  tradeoffs;
- the repository has no established convention, or nearby precedents conflict;
- requirements and previous answers do not select a choice;
- the decision is difficult to reverse after it reaches more files or users;
- one choice creates a new abstraction, dependency direction, compatibility
  policy, or source of truth;
- implementation has exposed evidence that was unavailable during planning;
- a reasonable technical user could care which result they will review and
  maintain.

Interruption cost dominates when:

- one existing convention clearly applies;
- only one option preserves correctness or the stated contract;
- the choice is local, routine, reversible, and has no observable consequence;
- the difference is formatting, syntax, or a minor name governed by nearby
  code;
- asking would require the user to reconstruct more context than the decision
  is worth;
- a boring project-standard default contains the choice behind a stable
  boundary.

In those cases, make the smallest conventional choice and continue. Do not turn
ordinary implementation details into a questionnaire.

When uncertain, evaluate three concrete questions:

1. Would plausible choices produce meaningfully different code or behavior?
2. Is project evidence insufficient to predict the user's preference?
3. Will waiting until final review make correction substantially more costly?

Two strong yeses usually justify a checkpoint. A hack signal always does.

## Treat hackiness as a mandatory checkpoint

A hack is not merely code that could be prettier. It is integration whose
correctness or maintainability depends on an incidental condition rather than a
clear boundary or invariant. Signals include:

- duplicated or competing sources of truth;
- state passed through a layer that should not know about it;
- order, timing, or initialization coupling not expressed by the API;
- an unsafe cast, stringly convention, mutable sentinel, or global escape hatch;
- special cases added only to reconcile incompatible models;
- a wrapper that conceals incompatible lifecycles instead of resolving them;
- behavior split across competing entry points;
- a dependency direction that contradicts the surrounding architecture;
- a temporary workaround that is about to become a durable interface.

If the integration merely *feels* hacky and the reason is not yet crisp, that
uncertainty is itself enough to stop and inspect the seam. Do not wait for the
user to identify it in the completed change.

Before entrenching a hack:

1. Name the exact seam and the incidental condition it would rely on.
2. Explain why the two pieces do not compose cleanly.
3. Distinguish cosmetic awkwardness from correctness or maintenance risk.
4. Present the viable choices. Include a contained workaround and a cleaner
   boundary change when both genuinely exist.
5. Recommend one choice and state its cost.
6. Ask the user to choose.

Do not disguise the compromise behind a helper, abstraction, comment, fallback,
or TODO. If external constraints make a workaround unavoidable, keep it at one
boundary and make its invariant reviewable after the user accepts it.

## Ask at an implementation checkpoint

Reach the smallest concrete state that reveals the decision, then pause the
work that depends on it. Complete unrelated work only when it cannot bias or
entrench the disputed choice.

Keep the checkpoint compact:

- **Decision:** the one choice the user is making.
- **Discovered:** the implementation evidence that made it visible now.
- **Project evidence:** the governing precedent, conflicting precedents, or the
  fact that none was found.
- **Recommendation:** the preferred option and its decisive reason.
- **Options:** two to four concrete alternatives, each with its effect on the
  code, behavior, and future review burden.
- **Hack alert:** the exact compromise and failure mode, whenever applicable.
- **Question:** a direct choice that can be answered without redesigning the
  whole feature.

Use the available structured question tool and mark the recommendation. Compare
options by consequences, not labels such as “clean,” “simple,” or “flexible.”
Show exact files, symbols, boundaries, or flows when available. Do not make the
user infer where the choice lands.

Bundle choices only when they share the same evidence and must be decided
together. Separate unrelated decisions so the user does not have to hold the
entire implementation in mind. Never bury the important choice in a progress
report or a tour of files.

## Incorporate the answer

After feedback:

1. Implement the selected direction through every affected call site and
   boundary; leave no abandoned alternate path.
2. Preserve the reason in code only when a future maintainer cannot recover the
   constraint from the implementation itself.
3. Keep an accepted workaround localized and verify the invariant on which it
   depends.
4. If further implementation invalidates an assumption behind the answer,
   surface the new evidence rather than silently reinterpret the choice.
5. In the final handoff, briefly identify the consequential choices the user
   confirmed and any accepted compromise that remains.

Do not create a decision log or process artifact unless the project already
uses one or the user requests it. The code and concise handoff should carry only
the context worth retaining.

## Review feedback-sensitive decisions

When reviewing work produced under this skill, inspect the seams rather than
only the final happy path:

- Does each confirmed choice appear in the implementation as described?
- Did any unresolved alternative survive as a second path, shim, or fallback?
- Are there integration exceptions that were never surfaced to the user?
- Does a workaround depend on hidden ordering, duplicated state, or an
  unenforced convention?
- Is an accepted hack contained at one boundary with a visible invariant?
- Did a supposedly local choice spread into public behavior or architecture?
- Would a maintainer know where to replace the compromise without tracing the
  whole system?
- Is the main implementation still cheap enough to understand that the user can
  meaningfully evaluate the chosen direction?

A newly discovered hack during review is still a mandatory checkpoint. Report
it as a choice with concrete remediation options, not as a vague quality note.

## Work with cognitive-budget-coding

`cognitive-budget-coding` makes code and proposals cheap to understand. This
skill decides when spending the user's attention prevents a larger mismatch.
Use them together:

1. Reuse established terminology and conventions; familiar context is cheap.
2. Keep the main path and integration boundary obvious.
3. Surface only consequential uncertainty, at the point where evidence appears.
4. Present alternatives in the smallest local frame that supports a decision.
5. Prefer the option that reduces future mental-model and review cost when
   behavior and project fit are otherwise equivalent.

Conciseness must not conceal a compromise. Conversely, transparency does not
require dumping every implementation detail on the user. Spend attention on the
choice, its evidence, and its consequence.

## Calibration examples

- Nearby modules all normalize external data at ingress, and the new module has
  the same boundary. Follow that convention without asking.
- An integration can assign cache invalidation to either of two components, and
  each choice changes ownership and failure behavior. No nearby precedent
  applies. Pause at that seam and ask.
- Two libraries can interoperate only through duplicated state or an
  order-dependent flag. Raise a hack alert before adding the bridge, even if the
  bridge is small.
- A local intermediate variable can be named two reasonable ways and both are
  obvious in its short scope. Choose the project-consistent name and continue.
- A user previously selected a contained adapter, but implementation reveals
  that it must alter a public schema. Ask again because the original choice now
  has a materially different consequence.
