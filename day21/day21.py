import numpy as np
import argparse

INPUT = "small-input.txt"

class KeyPad():
    def __init__(self):
        self.keys = np.array([
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "9"],
            ["NA", "0", "A"],
        ])


class RobotControlPad():
    def __init__(self, being_controlled):
        self.keys = np.array([
            ["NA", "^", "A",],
            ["<", "v", ">",],
        ])
        self.pointer = (3, 2)
        self.pad_in_control_of = being_controlled

    def current_pointer(self):
        return str(self.keys[self.pointer])

    def move_pointer_to(self, target_number) -> int:
        '''
        Move pointer to the target number.
        param target_number: int of the target number
        returns: int of the number of moves made
        #TODO: Avoid the NA key for all moves
        '''
        moves_made = 0
        number_location = np.where(self.pad_in_control_of.keys == target_number)
        print(f"Number location: {number_location}")
        print(f"Current pointer: {self.pointer}")
        # move vertically
        print(f"Pointer0: {self.pointer[0]}, Number0: {number_location[0][0]}")
        while self.pointer[0] != number_location[0][0]:
            if self.pointer[0] < number_location[0][0]:
                self.pointer = (self.pointer[0] + 1, self.pointer[1])
            else:
                self.pointer = (self.pointer[0] - 1, self.pointer[1])
            moves_made += 1
        # move horizontally
        while self.pointer[1] != number_location[1][0]:
            if self.pointer[1] < number_location[1][0]:
                self.pointer = (self.pointer[0], self.pointer[1] + 1)
            else:
                self.pointer = (self.pointer[0], self.pointer[1] - 1)
            moves_made += 1
        print(f"New pointer: {self.pointer}")
        print(f"Moves made: {moves_made}")
        return moves_made

class HumanControlPad():
    def __init__(self, being_controlled):
        self.keys = np.array([
            ["NA", "^", "A",],
            ["<", "v", ">",],
        ])
        self.pointer = (0, 2)
        self.pad_in_control_of = being_controlled

    def current_command(self):
        return str(self.keys[self.pointer])

    # Key is with the move_pointer method never pass through the NA key
    def move_pointer(self, new_pointer_location) -> int:
        '''
        Move pointer to the new location without going through the NA key.
        param new_pointer_location: tuple of new pointer location
        returns: int of the number of moves made
        '''
        return 0




def parse_codes(path_to_file: str) -> list[str]:
    with open(path_to_file, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_sum_of_code_complexity(codes: list[str]) -> int:
    my_directional_pad = KeyPad()
    new_robot_pad = RobotControlPad(my_directional_pad)
    new_robot_pad.move_pointer_to("0")
    new_robot_pad.move_pointer_to("8")
    new_robot_pad.move_pointer_to("A")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 21 of Advent of Code - Keypad Conundrum")
    parser.add_argument("--find_sum_of_code_complexity", action='store_true',
                        help="Find the sum of the code complexities in the INPUT file.")
    args = parser.parse_args()
    codes = parse_codes(INPUT)

    if args.find_sum_of_code_complexity:
        code_complexity= find_sum_of_code_complexity(codes)
        print(f"The code complexity is: {code_complexity}")
