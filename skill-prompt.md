Help me author a skill, @feedback-driven-execution/ .

My main problem is that I very often find myself asking coding agents to implement certain features.
I ask the agent to give me some proposals and ask me which one I prefer, and start at the end of this process.

Problem is, a lot of decisions in writing the code aren't necessarily visible before writing part of the implementation, and seeing how things integrate with each other.
What agents find themselves doing is just picking a choice for you, which is reasonable in a lot of circumstances. In others, for certain choices, asking the user whether the direction is right or wrong would save a big sweeping implementation from being written and having to correct it later.

To keep things straight, primary goal of this skill is reducing the cognitive load of the user, so that he can keep being maximally engaged with the actual codebase. This influences both the way the code is written, as having overly-verbose code can lead to the user just ignoring it and going "meh, good enough". Code has to be concise, the right amount of clever, and readable, as in both clear and not overly cognitively-demanding.

Here's an even better way to put it: there are things that require cognitive energy. Those things are useful, even necessary in programming, but using them consumes part of a cognitive budget you have. That's true for different scales: variable names, class and module composition, as well as file hyerarchy and structure.

Part of good programming is balancing those things in order to use the cognitive budget in the best way possible, to let the reader understand the basic mechanisms of the code with the least amount of effort possible.

Here's some potentially contradicting ways to save on cognitive budget, which have to be balanced to get the right result:
- shortness: less stuff is less cognitive stuff
- self-containedness: a name that specifies context in full doesn't lend itself to amiguities and the user asking "what does this refer to?". Also, specifying stuff is longer

There's gonna be tension between those two, and there are also gonna be cases in which it's very obvious which criteria is to be preferred.
To further expand on the second point, indirection is a very high-cost thing, which should be considered basically EVERYWHERE it appears. A very good way to deal with indirection is batching it in "single points of entrance", especially when it appears in multiple points referring to something that has a common ancestor that can be exploited as an entry point.

Of course there are gonna be different possible balances for those, and what is more cognitively demanding is gonna change based of the user, so we can delineate some further constraints to make a choice about which to pick.
- one of them is previous conventions used in the project. The user is going to be used to the way things are already done, so using something that's already there can be a cognitive budget saver.
- naming conventions is a big part of that, and they should be respected when seen
- consistency in naming also helps a lot.

Here's how I would synthetize this:

- the freedom the code allows you beyound its function should be used to make it clear
  and narrative, making it tell the story of what it does.

this of course has to be balanced with the rest of the elements, like consistency in
conventions, both of the language and of the user, since inconsistencies become
distracting and take away from the focus of the user.

I guess this isn't feedback-driven-execution anymore, but it has to be a part of it,
since the user understanding of the presented code is really important for feedback to
work. So let's give this another name and start with this.
