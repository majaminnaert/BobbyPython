# BobbyPython

## Learning python challenge: make Bob talk

*under supervision of BeCode AI Bootcamp and with some pair programming*

# Copied from the challenge files:

Bob answers 'Sure.' if you ask him a question.

He answers 'Whoa, chill out!' if you yell at him.

He says 'Fine. Be that way!' if you address him without actually saying
anything.

He answers 'Whatever.' to anything else.

## Instructions

Run the test file, and fix each of the errors in turn. When you get the
first test to pass, go to the first pending or skipped test, and make
that pass as well. When all of the tests are passing, feel free to
submit.

Remember that passing code is just the first step. The goal is to work
towards a solution that is as readable and expressive as you can make
it.

Please make your solution as general as possible. Good code doesn't just
pass the test suite, it works with any input that fits the
specification.

Have fun!

## Solution and workflow report

We (Maarten Vandaele and Maja Minnaert) each came up with a start of the solution
and reviewed these together, after which we worked together on the mini-
codebase we had on Maja's local repository. Using Discord screensharing, we could
both see the code and we tried to come up with solutions based on the error
and bug messages we received after running the tests, helped by the reading
of the tests. We needed to put our heads together for makings sense of it
and shared our knowledge where possible, so we could really think together
on improving the code. Since the latest update, you can find our solution to this
challenge in the bob.py file in this repository, along with the test as it was
executed during working time. It was not edited, though we first had a class
in our module bob and this didn't work well with the tests, so Maja tried first
to let the imports atop the test module refer to the class, which she didn't
really know how to and we decided it was better to mess with our own code to make
it conform to what the tests seemd to be going for, a single function inside the 
file "bob.py". We did keep in mind to make the code general and not test-specific 
while doing this. Overall, we both contributed with solutions and logic through
voice and chat conversation.

## Changelog

14-10-2020: added new branch for BobbyPython 0.2: The Class Edition
            In branch:
            wrapped Bobby in a class, so the kid can learn, in bob.py
            adapted import line in bob_test.py to refer to Bob class correctly
            (Maja)
