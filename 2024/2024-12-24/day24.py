#!/usr/bin/env python
import argparse
from collections import deque
from collections import defaultdict

INPUT = "input.txt"


def parse_input_and_gates(
    path_to_file: str,
) -> tuple[defaultdict, list[tuple[str, str, str, str]]]:
    """
    Parse the inputs and gates from the file.

    The inputs are in the file first and looke like:
    x00: 1
    They are seperated by a blank line from the gates which look like:
    ntg XOR fgs -> mjb
    """
    inputs = defaultdict(int)
    commands = []
    with open(path_to_file, "r") as file:
        for line in file:
            if line == "\n":
                break
            input, value = line.strip().split(": ")
            inputs.update({input: int(value)})
        for line in file:
            command = line.strip().split(" ")
            command.remove("->")
            commands.append(command)
    return inputs, commands


operation_map = {
    "XOR": lambda x, y: x ^ y,
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
}


def produce_ouput_number(register: defaultdict) -> int:
    """
    The output number is the values of all the registers that start with z,
    ordered alphabetically. Each value is a 0 or 1 and when concatenated
    together form the binary equivalent of the output number.
    """
    z_registers_keys = sorted(
        [key for key in register if key.startswith("z")], reverse=True
    )
    binary_string = "".join(str(register[key]) for key in z_registers_keys)
    print(binary_string)
    return int(binary_string, 2)


def produce_output_number(
    inputs: defaultdict, commands: list[tuple[str, str, str, str]]
) -> int:
    """
    Produce the output number by running the commands against the inputs.
    Gates wait for imput so if you do not have the input the gates need to wait
    """
    # put the inputs into the register
    register = inputs.copy()
    # put the commands int a fifo stack
    command_stack = deque()
    for command in commands:
        command_stack.append(command)

    while command_stack:
        input1, operation, input2, result_location = command_stack.popleft()
        if input1 not in register or input2 not in register:
            command_stack.append((input1, operation, input2, result_location))
        else:
            result = operation_map[operation](register[input1], register[input2])
            register[result_location] = result

    return produce_ouput_number(register)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 24")
    parser.add_argument(
        "--produce_output_number",
        action="store_true",
        help="Parse the input and run the commands against the input to calculate an output number.",
    )
    args = parser.parse_args()
    input, gates = parse_input_and_gates(INPUT)
    if args.produce_output_number:
        result = produce_output_number(input, gates)
        print(f"The number produced is {result}")
