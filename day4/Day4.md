# Day 4: Ceres Search

Find all instances of `XMAS` in the input. The word can be forwards, backwards or diagonal.

Example:

This has 18 instances of `XMAS`:
```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```
## Solution Thoughts
This seems to be a graph traversal problem. I will need to traverse the graph in all directions checking for the word XMAS
and keeping track of the number of times it is found.
