# Chronospatial Computer

Given a 3 a 3-bit computer: its program is a list of 3-bit numbers (0 through 7), like 0,1,2,3.
The computer also has three registers named A, B, and C, but these registers aren't limited to
3 bits and can instead hold any integer.

The computer knows eight instructions, each identified by a 3-bit number (called the instruction's opcode).
Each instruction also reads the 3-bit number after it as an input; this is called its operand.

A number called the `instruction pointer` identfies the position in the program from which the next opcode will
be read.It starts at 0, pointing at the first 3-bit number in the program. Except for jump instructions, the
instruction pointer increases by 2 after each instruction is processed (to move past the instruction's opcode
and its operand). If the computer tries to read an opcode past the end of the program, it instead halts.

So, the program 0,1,2,3 would run the instruction whose opcode is 0 and pass it the operand 1, then run the
instruction having opcode 2 and pass it the operand 3, then halt.

There are two types of operands; each instruction specifies the type of its operand. The value of a literal operand
is the operand itself. For example, the value of the literal operand 7 is the number 7. The value of a combo operand
can be found as follows:

    Combo operands 0 through 3 represent literal values 0 through 3.
    Combo operand 4 represents the value of register A.
    Combo operand 5 represents the value of register B.
    Combo operand 6 represents the value of register C.
    Combo operand 7 is reserved and will not appear in valid programs.

The eight instructions are as follows:

The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is
found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2);
an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then
written to the A register.

The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand,
then stores the result in register B.

The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3
bits), then writes that value to the B register.

The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by
setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer
is not increased by 2 after this instruction.

The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in
register B. (For legacy reasons, this instruction reads an operand but ignores it.)

The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program
outputs multiple values, they are separated by commas.)

The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register.
(The numerator is still read from the A register.)

The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register.
(The numerator is still read from the A register.)

Small input example:

```
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
```

Your first task is to determine what the program is trying to output. To do this, initialize the registers to the given values,
then run the given program, collecting any output produced by out instructions. (Always join the values produced by out
instructions with commas.)

After the above program halts, its final output will be: 4,6,3,5,6,3,5,2,1,0.

# Part 1
Once the program is run what do you get if you use commas to join the values it output into a single string?

# Part 2
Given the same input program, what is the value that needs to be put into register a to produce the same output
as the current input program.

So `1,5,7,4,1,6,0,3,0` was the answer in part 1. What is the lowest value that can be put into register A
to produce this output again?
