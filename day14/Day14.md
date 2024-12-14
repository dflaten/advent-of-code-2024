# Restroom Redoubt

Given a list of robots with a location and a velocity (one grid per second) like this:

```
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,
```

and a grid with dimenions like `[11, 7]` (11 wide, 7 tall), simulate the robots moving around the grid.
The robots move in a straight line at the velocity assigned to them. The robots will not collid if they
are at the same location at the same time. If a robot moves off the grid, it will wrap around to the
other side.

## Part 1
What is the safety factor after 100 seconds?
Safety factor is number of robots in each quadrant multiplied together (Robots in the middle don't count)

So if your grid looks like this:

```
......2..1.
...........
1..........
.11........
.....1.....
...12......
.1....1....
```
Robots to count looks like:
```
..... 2..1.
..... .....
1.... .....

..... .....
...12 .....
.1... 1....
```

Safety factor is:
12 = 1 * 3 * 4 * 1
