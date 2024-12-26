# Day 13 Claw Contraptions
Given machines that look like the examples below determine the minimum tokens it will take to win the prize (if it can be won):

Press A: 3 Tokens
Press B: 1 Token


```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
```

# Part 1
Solve the problem as is.

# Part 2
Imagine the
X and Y coordinates for the prizes are off by `10000000000000`. Now what is the
minimum number of tokens needed to win the prize?

Issues: pulp doesn't work here due to the large parameter values. Basically would
need another solver or to write my own solver to solve this problem. Will have to
look more into this.
