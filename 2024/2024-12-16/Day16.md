# Day 16: Reindeer Maze

Determine how to make it through the maze starting at 'S' and ending at 'E'. The score increases by 1 for each step taken and by 1000 for each
clockwize or counterclockwise rotation.

You always start facing East.

Example map:
```
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
```

There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a
total of 36 steps forward and turning 90 degrees a total of 7 times.

## Part 1:
What is the lowest score a reindeer could possibly get?

### Solution
Dijkstra's Algorithm is a good solution for this problem.

## Part 2:
Find the count of the number of unique points in all the best paths.
