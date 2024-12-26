# Day 5: Print Queue
Given a list of rules that looks like:
```
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
```

and a list of pages to produce that looks like:

```
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,4
```

Determine which list of pages follow the rules. Then add the middle of each of those lists together and return it.


## Solution Thoughts
I need to put the list of rules into a data structure that makes it easy to assess whether or not a given pair of
numbers is in the correct order. I'm thinking a dictionary where the key is the first number and the value is a list
of the numbers that need to come after it.

## Solutions
### Solution 1
5747 is the correct answer

### Solution 2
5502 is the correct answer
