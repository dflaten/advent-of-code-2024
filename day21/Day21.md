# Keypad Conundrum
Given a numeric keypad like this one blow...
The numeric keypad has four rows of buttons: 789, 456, 123, and finally an
empty gap followed by 0A. Visually, they are arranged like this:

+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

And a robot that controls that keypad that looks like:
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

And another command pad that controls that robot that looks like:
+---+---+
| ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

And that you have a series of commands to enter in the original keypad that
look like:
029A

## Part 1
Determine what is the lowest number of commands across all pads it will take
to execute each command.

Calculate and return the 'complexity' of the command strings by taking the
lowest number of commands and multiplying it by the number in the command
and adding those numbers together.

So for:

```
029A
980A
179A
456A
379A
```

In the above example, complexity of the five codes can be found by calculating
68 * 29, 60 * 980, 68 * 179, 64 * 456, and 64 * 379. Adding these together
produces 126384.
