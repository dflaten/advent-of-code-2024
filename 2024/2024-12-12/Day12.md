# Day 12: Garden Groups
Given an input of a map which looks like:

```
AAAA
BBCD
BBCC
EEEC
```

Find the cost of fencing the groups of letters in the map. The cost is found by multiplying the Area by the Perimter of the group.
Area = Number of letters in the group.
Perimeter = Number of edges of the group. For example the perimiters of the group above:

A - 10
B - 8
C - 10
D - 4
E - 8

Region A has price 4 * 10 = 40, region B has price 4 * 8 = 32, region C has price 4 * 10 = 40, region D has price 1 * 4 = 4,
and region E has price 3 * 8 = 24. So, the total price for the first example is 140.

Perimter = 4 for each letter - the number of equivalent items touching the group.

# Part 1
Find the total cost of fences for the input map.
