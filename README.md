# TobyHML
TobyHML is a command line tool to check an LTS against HML formulas.

## Description
In TobyHML you're able to build up a labeled transition system (LTS) and input Hennessy-Milner logic (HML) formulas to find those states that fulfill these formulas.

For now TobyHML only knows the standard HML syntax (no recursion), that is (in BNF):<br>
`F ::= true | false | (F and F) | (F or F) | <a>F | [a]F`<br>
Where a is a transition's name.

## Instruction
First you have to build up an LTS. You can do that by typing in multiple `add`-commands like this:
- `add p1 a p2`, which creates two states `p1` and `p2` and connects them from `p1` to `p2` via `a`.
- `add p3`, which creates a state `p3` that has no outgoing or incoming transitions (yet).
- `add p1 b p4`, which creates `p4` and connects it from `p1` to `p4`via `b`.
- `add true`, which would cause an error - your state and transition names *must* be alphanumeric and *may not* be `true`, `false`, `and` or `or`.

Use `print` to get an LTS print on screen. You can remove all states and transitions by entering `reset` (removal of specific states and transitions are yet to be added to TobyHML).

Then you can check HML formulas which will give you a set of states that fulfill said formulas. Here are some examples:
- `evaluate true`, which returns every state in the LTS.
- `evaluate false`, which returns an empty set.
- `evaluate <a>true', which returns every state that has an outgoing `a`-transition.
- `evaluate [b] false`, which returns every state that *doesn't* have an outgoing `b`-transition. (Notice that spaces between <a> or [b] and the following part of the formula *are* allowed.)
- `evaluate (<a>true and (<b>true and [c]false))`, which returns every state that has outgoing `a` and `b` but no `c` transitions. (Notice how binary operations *need* brackets, sadly the parser doesn't allow you to leave them out.)
- `evaluate <a><b><c><a><b>true`, which returns every states from which there is a way `a->b->c->a->b`.

Finally enter `exit` to quit TobyHML.

TobyHML also has a `help` command to give you a quick reference.

## To Do
- Remove states/transitions from LTS
- Read LTS from file
- Possibly add recursion
