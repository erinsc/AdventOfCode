## Whoever said you cant do one-liners in python

I hate python. Its a mess of a language that lets you get away with basically anything, leading to sloppy unreadable code.
I also love python. It lets me get away with basically anything, even the messiest and sloppiest code youve ever seen.

So basically the idea here is to solve the Advent of Code in one line of python.
In another language this would be fairly trivial since you can put multiple statements,
but im python you can't. Instead im forced to use list expressions, lambdas, and weird python quirks.

For example, lets say we have a list of elements and we want to process them with a function, keeping an intermediate state.
Usually this is very simple:
```py
A = 0
L = [1, 2, 3, 4, 5]
for x in L:
    A = A*10 + x
```
However we're not allowed to create variables.
Instead we have to carry the intermediate value through the loop iterations.
We can achieve this by wrapping a list comprehension into a lambda, then feed that lambda a list initialized with the initial value.
The lambda will feed a reference of that list to the list comprehension, allowing it to append a new intermediate state into the list,
and pull from it again in the next iteration using `l[-1]`.
To extract the final state we simply take the last element of the generated array.
```py
L = [1, 2, 3, 4, 5]
(lambda l: [l.append(l[-1]*10 + x) or l[-1] for x in L])([0])[-1]
```
