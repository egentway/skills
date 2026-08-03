---
name: cognitive-budget-coding
description: >-
  Use when implementing, reviewing, or refactoring code whose readability is a
  first-class concern: naming, abstraction boundaries, indirection, module or
  file structure, and choices between similarly correct designs. Trigger when
  the user asks for clear, narrative, concise-but-readable, low-cognitive-load
  code, or wants code that is easy to evaluate and give feedback on. Optimize
  for the reader's limited cognitive budget while preserving correctness and
  local conventions.
---

# Cognitive-Budget Coding

Write code that spends the reader's attention on the problem, not on recovering
context or decoding structure.

Do not minimize line count or maximize explicitness. Minimize the total effort
needed to build an accurate mental model.

## Decision order

When several designs are correct, prefer them in this order:

1. Preserve established project terminology and conventions.
2. Expose the main story from one obvious entry point.
3. Keep information near the code that needs it.
4. Remove indirection that does not carry its cost.
5. Use the least mechanism that states the intent clearly.
6. Shorten only while the result remains unambiguous.

Earlier criteria outrank later ones. Do not copy a local pattern that creates a
correctness or safety problem; make the deviation explicit instead.

## Start from the reader's path

Before editing:

1. Find the entry point a maintainer will open first.
2. Identify the project vocabulary for the concepts involved.
3. State the operation's main path in a short sequence of domain actions.
4. Arrange the implementation so a reader encounters those actions in that
   order.

The entry point should reveal policy and flow. Details may live below it, but a
reader should not need to chase them merely to learn what happens.

```ts
async function placeOrder(order: Order) {
  await validateOrder(order);
  const reservation = await reserveInventory(order.items);
  const payment = await chargeCustomer(order.customer, order.total);
  return confirmOrder(order, reservation, payment);
}
```

This earns its helpers: each call names a domain step, and the entry point tells
the whole story. Do not extract helpers that merely rename syntax or hide a
single obvious expression.

## Balance brevity and self-containment

Choose name length by the amount of context already available:

- In a small, typed local scope, use short names when the role is unmistakable.
- At module and API boundaries, include the context needed to prevent ambiguity.
- Do not repeat context already supplied by the owner: prefer `invoice.total` to
  `invoice.invoiceTotal`.
- Do not rely on context that is distant or unstable: prefer a precise boundary
  name to a generic `data`, `item`, `manager`, or `helper`.
- Use one term for one concept. Reuse the project's term rather than inventing a
  synonym.

A name is too short when the reader must search for its meaning. It is too long
when it repeatedly restates nearby context.

## Make indirection pay rent

Every wrapper, callback, registry, inheritance layer, helper, re-export, and
cross-file jump charges the reader. Keep one only when it does at least one of
these jobs:

- centralizes an invariant or policy;
- creates a stable boundary around volatile details;
- collapses repeated, meaningful complexity;
- names a domain operation used as a unit;
- provides one entrance to behavior that would otherwise be scattered.

Batch unavoidable indirection behind that single entrance. Do not expose both
the entrance and several lower-level paths to the same behavior.

Prefer direct code when an abstraction only forwards arguments, serves one
obvious call site, or requires learning more structure than it removes.

Potential reuse or hypothetical alternate implementations do not pay rent.
Require a present invariant, policy, boundary, or repeated complexity.

## Keep the story local

- Keep state, invariants, and the operations that maintain them close together.
- Order major operations by execution or dependency, not alphabetically.
- Place exceptional branches where they interrupt the normal story least while
  remaining visible.
- Use intermediate names when they expose a domain step, not for every
  subexpression.
- Prefer familiar language and project idioms over bespoke cleverness.
- Comment constraints, reasons, and non-obvious tradeoffs. Do not narrate syntax.

Concise code removes ceremony. Compressed code makes the reader simulate it.
Choose concise, never compressed.

## Preserve useful consistency

Familiarity is already-loaded context and therefore cheap.

- Search nearby code before introducing a name, shape, or file boundary.
- Give parallel concepts parallel names and APIs.
- Match the project's ordinary level of abstraction unless doing so obscures the
  domain story.
- Avoid a second convention beside an existing one.
- If a new concept needs a new pattern, introduce it at one clear boundary.

Consistency is a means, not an excuse. A familiar design wins when its costs are
close; it does not excuse hidden behavior or unnecessary layers.

## Present code for feedback

Make feedback cheap to give:

1. Show the entry point or main path first.
2. Explain only constraints the code cannot communicate by itself.
3. Name the consequential design choice, not every small implementation choice.
4. Point to the exact boundary, name, or flow the user should evaluate.
5. Keep alternatives concrete enough to compare by their effect on the code.
6. Never invent types, APIs, behavior, or placeholder bodies to illustrate a
   decision. If code is not grounded in the implementation, omit it and use
   prose.

Treat schematic APIs such as `loadAccount(id)` as prose unless their exact
types and behavior are known. A body containing only comments, ellipses,
`pass`, `throw`, or a TODO is always worse than no body.

Do not bury the decision under a tour of files or a long defense of the chosen
implementation.

## Cognitive-load audit

Before finishing, read the change as a maintainer unfamiliar with the work:

- Is there one obvious place to start?
- Can the main behavior be understood by skimming names and control flow?
- Which facts must be remembered while reading, and can any be made local?
- Which file or abstraction jumps are unavoidable, and what does each buy?
- Is any concept reachable through competing paths?
- Are names precise at boundaries and economical in local scopes?
- Does terminology match the surrounding project?
- Can any layer, helper, comment, or temporary name disappear without losing
  meaning?

Spend cognitive budget where the domain is genuinely complex. Remove the costs
created only by the implementation.
