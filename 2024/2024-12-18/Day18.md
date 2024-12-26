# Day 18: RAM Run
You have a 2 dimensional space where things will be falling. The items falling are represented by a list that
looks like:

```
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
```

Each position is given as an X,Y coordinate, where X is the distance from the left edge of your
space and Y is the distance from the top edge of your space.

You will need to simulate the falling of the items and plan a safe route to take to avoid them all.
Once an item has fallen, that space will be corrupted and you will not be able to pass through it.

# Part 1
What is the minimum number of steps needed to reach the exit safetly?

You start at the top left and end at the bottom right.

# Part 2
Say you need to know at what number of blockers dropped the map becomes completely blocked?

## Solution
Use binary search to find at what time the path becomes blocked.
