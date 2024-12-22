# Day 22: Monkey Market

Each buyer's secret number evolves into the next secret number inthe sequence via the
following process:

    Calculate the result of multiplying the secret number by 64. Then, mix this
    result into the secret number. Finally, prune the secret number.

    Calculate the result of dividing the secret number by 32. Round the result
    down to the nearest integer. Then, mix this result into the secret number.
    Finally, prune the secret number.

    Calculate the result of multiplying the secret number by 2048. Then, mix
    this result into the secret number. Finally, prune the secret number.

Each step of the above process involves mixing and pruning:

    To mix a value into the secret number, calculate the bitwise XOR of the given value
    and the secret number. Then, the secret number becomes the result of that operation.
    (If the secret number is 42 and you were to mix 15 into the secret number, the secret
    number would become 37.)

    To prune the secret number, calculate the value of the secret number modulo 16777216.
    Then, the secret number becomes the result of that operation. (If the secret number is
    100000000 and you were to prune the secret number, the secret number would become
    16113920.)

# Part 1
Given a list of buyers numbers predict the 2000th number for each buyer.

# Part 2
Assuming the price is the final digit in each number then the numbers and their price
differences look like this (for one buyer with a starting number of 123):

```
123: 3
15887950: 0 (-3)
16495136: 6 (6)
527345: 5 (-1)
704524: 4 (-1)
1553684: 4 (0)
12683156: 6 (2)
11100544: 4 (-2)
12249484: 4 (0)
7753432: 2 (-2)
```

If you want to find the sequence of 4 price changes with the largest price you could sell
for all the buyers what is the largest amount you could gain? The sequence must be the
same across all buyers.

Solution Notes:
For each buyer I need to generate a list of potential selections
