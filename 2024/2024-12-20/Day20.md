# Day 20 Race Condition

Given a map as input like:

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

The goal is to get to the end as fast as possible. You are allowed, however,
to cheat once for 2 moves at any point by passing through a wall.

## Part 1
Given the map determine how many cheats would save you at least 100 moves?

## Solution
My attempt creates a list of all the possible maps and then uses dijkstra's algorithm
to find the way through the maze.

It works on the small example but is too slow for the large input and even
when it finishes gives the wrong answer.
