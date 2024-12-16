
#!/usr/bin/env python
import argparse
import numpy as np

INPUT = "small-input.txt"

directions = {
    "<": (0, -1), # left
    ">": (0, 1),  # right
    "v": (1, 0), # down
    "^": (-1, 0)  # up
}
# Would expect my directions to be more like this... need to think about this one a bit more.
# directions = {
#     ">": (1, 0),
#     "<": (-1, 0),
#     "^": (0, -1),
#     "v": (0, 1)
# }

def build_map_and_instructions_from_input(path_to_file: str) -> tuple[np.ndarray, str]:
    '''
    Converts the text file at the path to a numpy map_and_instructionsay grid for traversal
    and a list of instructions for the traversal.
    '''
    map_and_instructions = None
    with open(path_to_file, 'r') as file:
        map_and_instructions = [line.strip() for line in file.readlines()]
    delimiter_row = None
    for i, row in enumerate(map_and_instructions):
        if all(char == '#' for char in row):
            delimiter_row = i
            if i > 0 and all(char == '#' for char in map_and_instructions[i-1]):  # Found the final delimiter
                break
    if delimiter_row is None:
        raise ValueError("No delimiter row found in input file")

    map = map_and_instructions[:delimiter_row + 1]
    map = map[:-1]
    numpy_map = np.array([list(row) for row in map])
    instructions = map_and_instructions[delimiter_row + 1:]
    instructions = ''.join(instructions)
    return numpy_map, instructions


def is_valid_position(current_position: tuple, shape: tuple) -> bool:
    '''Check if position is within map boundaries'''
    return 0 <= current_position[0] < shape[0] and 0 <= current_position[1] < shape[1]

def find_robot_location(map: np.ndarray) -> tuple:
    '''
    robot is at location with character @
    '''
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "@":
                return (i, j)
    raise ValueError("No robot found in map.")

def get_next_position(current_position: tuple, direction: tuple) -> tuple:
    return (current_position[0] + direction[0], current_position[1] + direction[1])

def traverse_map_calc_gps_sum(map: np.ndarray, instructions: str) -> int:
    '''
    Currently this isn't working right I'm pushing boxes through walls...
    '''
    robot_location = find_robot_location(map)
    updated_map = map.copy()
    print("Starting Map")
    print(updated_map)
    print("Instructions")
    print(instructions)
    for instruction in instructions:
        print("robot location")
        print(robot_location)
        print("updated map")
        print(updated_map)
        direction = directions[instruction]
        next_potential_location= get_next_position(robot_location, direction)
        if (updated_map[next_potential_location]) == "#":
            continue
        elif (updated_map[next_potential_location]) == ".":
            updated_map[robot_location] = "."
            updated_map[next_potential_location] = "@"
            robot_location = next_potential_location
            continue
        elif (updated_map[next_potential_location]) == "O":
            print("next potential location")
            print(next_potential_location)
            end_box_chain = next_potential_location
            if get_next_position(end_box_chain, direction) == "#":
                updated_map[robot_location] = "."
                updated_map[next_potential_location] = "@"
                robot_location = next_potential_location
                updated_map[end_box_chain] = "O"
            else:
                # Loop for chain of boxes
                while updated_map[end_box_chain] == "O":
                    if get_next_position(end_box_chain, direction) == "#":
                        break
                    end_box_chain = get_next_position(end_box_chain, direction)
                updated_map[robot_location] = "."
                updated_map[next_potential_location] = "@"
                robot_location = next_potential_location
                updated_map[end_box_chain] = "O"
            print("end box chain")
            print(end_box_chain)

    print("ending map")
    print(updated_map)

    #TODO: Calculate the gps sum of all boxes

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--calc_gps_sum", action='store_true',
                       help="Find the total sum of all GPS locations of the boxes after the robot has finished instructions.")
    args = parser.parse_args()
    map, instructions= build_map_and_instructions_from_input(INPUT)

    if args.calc_gps_sum:
        result = traverse_map_calc_gps_sum(map, instructions)
        print(f"The total gps sum of boxes in the map is: {result}")
