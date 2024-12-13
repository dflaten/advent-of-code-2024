#!/usr/bin/env python
import argparse
from itertools import zip_longest
from dataclasses import dataclass
from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, value, PULP_CBC_CMD, LpStatusOptimal
import re
INPUT = "small-input.txt"

@dataclass
class PrizeMachine:
    def __init__(self,
        button_a_x: int,
        button_a_y: int,
        button_b_x: int,
        button_b_y: int,
        prize_location: tuple[int, int]):
        self.button_a_x = button_a_x
        self.button_a_y = button_a_y
        self.button_b_x = button_b_x
        self.button_b_y = button_b_y
        self.prize_location = prize_location

    def __str__(self) -> str:
            """Return a string representation of the PrizeMachine."""
            return (
                f"PrizeMachine:\n"
                f"  Button A: ({self.button_a_x}, {self.button_a_y})\n"
                f"  Button B: ({self.button_b_x}, {self.button_b_y})\n"
                f"  Prize: ({self.prize_location[0]}, {self.prize_location[1]})"
            )

def parse_input(path_to_file: str) -> list[PrizeMachine]:
    prize_machines = []
    with open(path_to_file, 'r') as file:
        # every four lines(one blank) contains the data for a prize machine, they look like:
        #Button A: X+94, Y+34
        #Button B: X+22, Y+67
        #Prize: X=8400, Y=5400
        #
        for lines in zip_longest(*([iter(file)] * 4)):
            button_a_numbers_as_string = re.findall(r'(?<=\+)\d+', lines[0].strip())
            button_b_numbers_as_string = re.findall(r'(?<=\+)\d+', lines[1].strip())
            prize_numbers_as_string = re.findall(r'(?<==)\d+', lines[2].strip())
            prize_machine = PrizeMachine(
                button_a_x=int(button_a_numbers_as_string[0]),
                button_a_y=int(button_a_numbers_as_string[1]),
                button_b_x=int(button_b_numbers_as_string[0]),
                button_b_y=int(button_b_numbers_as_string[1]),
                prize_location=(int(prize_numbers_as_string[0]), int(prize_numbers_as_string[1]))
            )
            prize_machines.append(prize_machine)

    return prize_machines


def get_min_tokens(prize_machine: PrizeMachine, adjusted=False) -> int:

    prob = LpProblem("Minimum_Number_Of_Tokens_Puzzle", LpMinimize)

    # LpInteger since we need whole numbers
    a_presses = LpVariable("a", lowBound=0, upBound=100000000000000, cat=LpInteger)
    b_presses = LpVariable("b", lowBound=0, upBound=100000000000000, cat=LpInteger)

    # Define objective function (minimize tokens)
    prob += 3 * a_presses + b_presses, "Number of tokens"

    # Define constraints
    x_prize_location = prize_machine.prize_location[0]
    y_prize_location = prize_machine.prize_location[1]
    if adjusted:
        x_prize_location = x_prize_location + 10000000000000
        y_prize_location = y_prize_location + 10000000000000
    print(x_prize_location, y_prize_location)
    prob += prize_machine.button_a_x * a_presses + prize_machine.button_b_x * b_presses == x_prize_location, "X Movement"
    prob += prize_machine.button_a_y * a_presses + prize_machine.button_b_y * b_presses == y_prize_location, "Y Movement"

    status = prob.solve(PULP_CBC_CMD(msg=True, presolved=False, options=['LpInteger=1*10**-100']))
    print(status)

    if status == LpStatusOptimal:
        a_value = int(value(a_presses))
        b_value = int(value(b_presses))

        tokens = 3 * a_value + b_value
        return tokens

    # If there is no solution, return 0
    return 0

def determine_min_tokens(list_of_prize_locations: list[PrizeMachine], adjusted=False) -> int:
    total_tokens = 0
    for prize_machine in list_of_prize_locations:
        total_tokens += get_min_tokens(prize_machine, adjusted)
    return total_tokens


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--determine_min_tokens", action='store_true',
                       help="Find the minimum number of tokens to win all prizes.")
    parser.add_argument("--determine_min_tokens_adjusted", action='store_true',
                       help="Find the minimum number of tokens to win all prizes if prize locations are adjusted by 10000000000000.")
    args = parser.parse_args()

    prize_machines = parse_input(INPUT)
    if args.determine_min_tokens:
        # 26599 for the input result
        # 480 for the small-input
        result = determine_min_tokens(prize_machines)
        print(f"The number of button presses: {result}")
    if args.determine_min_tokens_adjusted:
        # Here it isn't feasible due to the problems size to get a result using my current approach.'
        result = determine_min_tokens(prize_machines, adjusted=True)
        print(f"The number of button presses: {result}")
