# Create and refine a frontend

Use with [SKILL.md](SKILL.md) and the editable
[common-problems.md](common-problems.md) catalogue. Deliver a working interface
within the requested scope, not merely a screenshot or a collection of components.
An explicitly requested mockup or preview has its own narrower completion boundary.

## Understand the interface

Recover the user's task, prior decisions, existing design system, component
library, and implementation boundary. Inspect the actual entry points and nearby
patterns before inventing another convention. Distinguish functioning features,
intentional previews, and future scope.

Decide what belongs to the application shell, selected view, and contextual
controls. Navigation labels and displayed content must describe the same
organizational model. A cross-domain overview should be named as such; global
tools should not be accidentally owned by a page they must outlive.

Resolve routine details from the project. Ask a focused question when plausible
choices materially change ownership, user behavior, or integration scope and the
available evidence does not select one. Do not infer an entire dashboard, command
palette, backend, or navigation system from a request for a single component.

## Reuse before inventing

Use existing visual tokens, component APIs, and interaction patterns. In a new
React project without conflicting requirements, prefer pnpm and established
components such as Radix-backed shadcn/ui when suitable. These are defaults, not
permission to migrate an existing stack. Other frameworks and established design
systems remain valid.

Understand library boundaries: Radix Primitives supplies interaction and
accessibility behavior; shadcn/ui supplies locally owned component implementations
and styling. Not every shadcn component uses Radix. Choose the intended component
variant rather than inadvertently installing a competing primitive system. Do not
add Radix Themes alongside shadcn merely because both use the Radix name.

Keep shared primitives independent of domain data. Keep feature-specific
composition near the feature. Share action behavior between different launch
points. Extract reuse when it clarifies a real repeated responsibility, not to
build a framework for hypothetical screens. Add only needed components and their
necessary dependencies. Do not wrap every library component without a reason.

Prefer established accessible dialogs, menus, command selectors, and resizing
components to homemade interaction machinery. Preserve labels, keyboard behavior,
focus handling, and meaningful status text when styling them.

## Build a useful first slice

When early visual feedback matters, deliver the smallest interactive surface the
user can evaluate. Backend integration need not precede an explicitly requested UI
preview. Agree which interactions are real and which are intentionally synthetic.

Label sample data and test actions concisely. Do not present them as live behavior,
fabricate connectivity or freshness, or retain them as silent fallbacks after
integration. Keep preview sources separate from presentation so replacement is
straightforward, without building an elaborate mock service.

Show a concrete result while the user can still influence consequential choices.
Do not turn every small adjustment into a new approval ceremony. Follow existing
planning/approval requirements and complete the agreed slice before claiming it is
done. A preview is not proof of backend behavior.

## Review content and layout

Consult applicable entries in [common-problems.md](common-problems.md) before
extending the design and before handoff. Treat signals as prompts for judgment,
not blanket bans. Do not launch an unrelated audit of the whole application.

Use Lorem ipsum for text whose only purpose is to occupy future-content space.
Use meaningful labels for real controls, statuses, errors, help, and accessibility
descriptions. Do not replace those with filler. Remove redundant subtitles and
marketing-like explanations rather than replacing every unnecessary sentence with
Lorem ipsum.

Match density to the content and task. Adjust layout to space available to the
component, not only the browser viewport. A resizable panel may be narrow on a wide
screen. Preserve readable content, interaction targets, and contained overflow.

Do not require a particular theme, framework, sidebar position, or command palette
unless the task or project establishes it.

## Verify the rendered result

Open the actual application. Inspect layout and exercise relevant controls with
pointer and keyboard. Check focus entry/restoration, dismissal, overflow, narrow
screens, and meaningful loading/empty/error states where those states exist.

For resizable regions, check both boundaries and content reflow, keyboard resizing,
and whether resizing or navigation unintentionally resets useful state. Do not
introduce persistence solely to remember panel dimensions without a requirement.

Run project checks and verify the production build when styling or behavior may
differ from development. Use browser evidence for visual claims; compilation alone
does not establish interaction correctness. If browser execution is unavailable,
state that limit rather than claiming visual verification.

Remove obsolete styles, duplicate components, and throwaway verification artifacts
within the changed scope. Update existing source guidance when behavior changes.
Do not create documentation or permanent tests merely to decorate the work.

At handoff, name the delivered slice, important choices, exercised behavior, and
remaining limits. Invite feedback on the actual layout or interaction, rather than
asserting that subjective design quality has been proved. New recurring problems
may be proposed for the catalogue, but only an authorized maintenance request adds
them. Skill-package changes follow the commit policy in [SKILL.md](SKILL.md).
