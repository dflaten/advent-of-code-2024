# Day 7: Bridge Repair
Given an input that looks like:

```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Where each line represents an equation. The test value is before the column and we must determine if we can
combine the remaining numbers in some way to get to that value. Operators are always evaluated left to right
and the possible operators are add '+', and multiply '*'.

## Part 1
Determine which lines are valid and return the sum of the test values of the valid lines.

### Solution Thoughts
Brute force is an option, we can try putting all possible combinations of operators between the numbers and
determine if one gets us to the test value.

The hard part is determining how to build the list of possible combinations. Recursion feels like a good option...

## Part 2
Add a new operator `||` which concatenates numbers together instead of adding or multiplying them.

This was pretty simple just needed to add another block to my recurssion function to handle the new operator.
