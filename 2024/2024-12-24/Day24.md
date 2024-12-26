# Day 24 Crossed Wires

Given an input that looks like the following where `x00` is a an input

```
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
```

# Part 1
Run all the commands through the gates (gates wait for input to execute) and return the
integer value of the binary equivalent of all the sorted z gates.
