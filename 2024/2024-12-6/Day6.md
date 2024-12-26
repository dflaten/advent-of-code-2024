# Day 6: Guard Gallivant

Given a map that looks like:

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```
# Part 1
Where the `^`, `v`, `<`, and `>` characters represent the starting position of a guard, and the `#` characters represent walls,
write a function that returns the number of steps it takes for the guard to walk through the map until he walks off.

Whenever the guard gets to an `#` they will turn 90 degrees to the right and continue walking.

## Solution
4977 on the input.

# Part 2
Given the same input as part one figure out how many different ways you can add an obstacle to the map to place the guard
into an infinite loop.
