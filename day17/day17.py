#!/usr/bin/env python
import argparse

INPUT = "input.txt"
PROGRAM_OUTPUT_TO_GENERATE_REGISTER_A = 'program_output.txt'

def parse_input_into_registers_and_instructions(input) -> tuple[int, int, int, list[int]]:
    with open(input, 'r') as file:
        lines = file.readlines()
        register_a = int(lines[0].split()[2])
        register_b = int(lines[1].split()[2])
        register_c = int(lines[2].split()[2])
        instructions = [int(number) for number in lines[4].split()[1].split(',')]
        return register_a, register_b, register_c, instructions


def run_instructions(register_a, register_b, register_c, instructions) -> str:
    output = "None"
    register_a = register_a
    register_b = register_b
    register_c = register_c

    def get_combo_operand(operand) -> int:
        if operand >= 0 and operand <= 3:
            return operand
        elif operand == 4:
            return register_a
        elif operand == 5:
            return register_b
        elif operand == 6:
            return register_c
        else:
            raise ValueError(f"Invalid operand {operand}")
    i = 0
    while i <= len(instructions) - 1:
        if i == len(instructions) - 1:
            break
        if instructions[i] == 0:
            combo_operand = get_combo_operand(instructions[i+1])
            register_a = register_a // 2 ** combo_operand
            i = i + 2
        elif instructions[i] == 1:
            register_b = register_b ^ get_combo_operand(instructions[i+1])
            i = i + 2
        elif instructions[i] == 2:
            register_b = get_combo_operand(instructions[i+1]) % 8
            i = i + 2
        elif instructions[i] == 3:
            if register_a != 0:
                i = instructions[i+1]
            else:
                i = i + 2
        elif instructions[i] == 4:
            register_b = register_b ^ register_c
            i = i + 2
        elif instructions[i] == 5:
            new_output = str(get_combo_operand(instructions[i+1]) % 8)
            if output == "None":
                output = str(new_output)
            else:
                output = output + ',' + new_output
            i = i + 2
        elif instructions[i] == 6:
            combo_operand = get_combo_operand(instructions[i+1])
            register_b = register_a // 2 ** combo_operand
            i = i + 2
        elif instructions[i] == 7:
            combo_operand = get_combo_operand(instructions[i+1])
            register_c = register_a // 2 ** combo_operand
            i = i + 2
        else:
            raise ValueError(f"Invalid instruction {instructions[i]}")
    return output





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 17")
    parser.add_argument("--run_instructions", action='store_true', help="Run instructions on Chronospatial Computer")
    parser.add_argument("--generate_register_a", action='store_true', help="Generate Register A for program output")
    args = parser.parse_args()
    register_a, register_b, register_c, instructions = parse_input_into_registers_and_instructions(INPUT)
    if args.run_instructions:
        result = run_instructions(register_a, register_b, register_c, instructions)
        print(f"The output of the instructions is: {result}")
