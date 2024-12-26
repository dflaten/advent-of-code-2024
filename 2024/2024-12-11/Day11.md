# Day 11: Plutonian Pebbles

Rules
If the number is 0, it is replaced by the number 1.
If the number has an even number of digits, it is replaced by two numbers. The left half of the digits are one number, and the right half of the digits are the other. (The new numbers don't keep extra leading zeroes: 1000 would become 10 and 0.)
If none of the other rules apply, the number is replaced by the old number multiplied by 2024.

Example

```
Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
```

## Part 1
How many stones after 25 iterations given the input.
