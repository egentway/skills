# Common frontend problems

Editable knowledge for [implementation.md](implementation.md). Each entry is a
signal to investigate, not an automatic defect. Consult relevant entries during
frontend work; do not impose every pattern on every interface.

A request to add, revise, or remove a problem edits this file without initiating
frontend implementation. Do not silently expand it during ordinary work. Keep
reusable lessons rather than a diary of individual screens. Change the procedure
only when the requested criterion changes how work must run. Verify and commit
completed package changes using the policy in [SKILL.md](SKILL.md).

## Placeholder copy masquerading as product messaging

**Signals:** an unfinished region contains a slogan, promises of future features,
or polished prose that could be mistaken for final product copy.

**Why it matters:** users cannot tell whether they are evaluating layout, product
messaging, or implemented functionality. Agents invent unnecessary content and
make incomplete work look deliberate or complete.

**Preferred correction:** use Lorem ipsum when text only occupies future-content
space. Remove unnecessary text rather than filling every region. Keep synthetic
examples visibly distinguishable from actual observations.

**Exceptions:** real control labels, accessibility descriptions, actionable errors,
and concise preview/sample labels must remain meaningful. An explicit copywriting
task calls for authored copy, not Lorem ipsum. Synthetic event payloads and domain
fixtures need meaningful data when their structure is what the user is evaluating.

## Redundant subtitles and explanatory decoration

**Signals:** a heading such as Events is followed by a sentence explaining that
events appear below it; multiple footers repeat preview status; an empty workspace
contains promotional copy or duplicate launch controls without a task need.

**Why it matters:** explanation competes with useful content, creates visual noise,
and makes small interfaces feel larger than their capabilities warrant.

**Preferred correction:** keep the heading and functional controls. Retain concise
status or help only where it resolves uncertainty. Remove decorative explanation
instead of rewriting it into a more polished slogan.

**Exceptions:** unfamiliar workflows, destructive consequences, accessibility help,
and genuine empty/error states may need explanations. Judge the information added,
not the presence of a subtitle alone.

## Excessive space for little information

**Signals:** sparse event or table entries always occupy several rows; large cards
contain little data; spacing reflects a template rather than the reading task.

**Why it matters:** users scan less information at once and scroll unnecessarily.

**Preferred correction:** match height and grouping to actual content. Use a compact
single-row presentation when fields fit, then reflow to multiple rows as the
component becomes narrow. Check the panel's available width, including resizing,
not just viewport breakpoints. Contain long values without silently losing meaning.

**Exceptions:** touch targets, readability, grouping, and task emphasis can justify
space. Dense does not mean tiny type, inaccessible controls, or compressed prose.

## Rigid sidebars and panels

**Signals:** a substantial inspector or navigation panel has one fixed width even
when its content and the user's focus vary; widening the window is the only way
to inspect long values comfortably.

**Why it matters:** a single allocation forces users to choose between truncated
information and wasted space.

**Preferred correction:** provide resizing where users benefit from reallocating
space, especially when requested. Use an established accessible resizing primitive,
labeled separators, sensible limits, and keyboard controls. Verify content reflow,
workspace minimums, and overflow. On small screens, a drawer may be more usable.

**Exceptions:** fixed compact navigation or constrained device layouts can be
appropriate. Do not make every card resizable or add persistence, drag machinery,
or layout customization without a useful task.

## Navigation and content disagree

**Signals:** a module-specific item is selected but the workspace presents data
from several unrelated modules; every backend module becomes a navigation item;
future views appear as dead links merely to complete a menu.

**Why it matters:** users cannot predict where information or actions belong.

**Preferred correction:** organize navigation around intentional views and tasks.
Name a cross-domain summary Overview or an equally clear term. Add navigation when
a view is usable. Domain ownership does not dictate the UI's page hierarchy.

**Exceptions:** a contextual related-data section can help a focused view; establish
its relationship rather than banning all cross-domain content.

## Global tools incorrectly owned by a page

**Signals:** event inspection, global commands, or connection status disappear or
reset when changing views, despite serving the application as a whole.

**Why it matters:** navigation disrupts observation and makes global functionality
appear specific to the current page.

**Preferred correction:** put genuinely global tools and their state in the shell.
Keep view-specific tools local. Make global filtering explicit rather than silently
hiding events when the selected view changes.

**Exceptions:** some inspectors deliberately follow selection. That relationship
should be apparent and should not masquerade as an unfiltered global feed. Not
every application needs a persistent event inspector or command palette.

## Inconsistent components and parallel styling systems

**Signals:** each feature invents its own button, badge, panel, dialog, spacing, or
status colors; multiple primitive libraries solve the same interaction without a
clear reason; visual similarity conceals different keyboard behavior.

**Why it matters:** interfaces lose cohesion and every correction has many owners.

**Preferred correction:** reuse established tokens, components, and variants. Use
libraries such as Radix-backed shadcn/ui where they fit. Keep domain data out of
shared primitives and combine them in feature-local components. Verify keyboard
and focus behavior after customization.

**Exceptions:** different frameworks or specialized widgets may need other tools.
Existing conventions outrank a preferred library; this signal does not authorize a
stack migration or wholesale restyling.

## Premature generic UI machinery

**Signals:** universal card renderers, form builders, plugin registries, or wrappers
appear before multiple concrete requirements justify them; readers must learn a
custom configuration language to understand a simple screen.

**Why it matters:** speculative reuse adds indirection, hides domain meaning, and
makes visual iteration harder.

**Preferred correction:** compose simple primitives directly. Extract a component
when it owns a useful repeated presentation or interaction contract. Share real
action flows between palette entries and contextual controls instead of duplicating
execution logic.

**Exceptions:** mature, repeated, schema-driven requirements may justify generic
rendering. Require demonstrated needs and a clearer reader path, not minimum line
count or imagined future screens.

## Preview content presented as working integration

**Signals:** static examples appear under Live or Connected labels; a test command
claims a domain mutation; optimistic UI reports success merely because a request
was sent; fabricated data replaces failed live data without disclosure.

**Why it matters:** the user cannot distinguish UI progress from actual system
behavior, and failures become invisible.

**Preferred correction:** identify samples and test actions concisely. Distinguish
requested, sent, applied, unavailable, and stale states where the real contract
supports them. Keep preview input separate from presentation and remove it from the
live path when integration replaces it. Do not implement unrelated backend work
merely to avoid an explicitly authorized preview.

**Exceptions:** prototypes may intentionally simulate interaction. Their boundary
must remain clear. No amount of preview labeling proves backend, hardware, or
vehicle behavior.
