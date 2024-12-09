#!/usr/bin/env python
import argparse
import numpy as np

def convert_text_to_grid(path_to_file: str) -> np.ndarray:
    '''
    Converts the text file at the path to a numpy array grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return np.array([list(line.strip()) for line in file])

def find_satellites_positions(grid: np.ndarray) -> dict[str, list[tuple]]:
    satellite_positions_map = {}
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            current_char = str(grid[i, j])
            if current_char == '.':
                continue
            if current_char in satellite_positions_map:
                satellite_positions_map[current_char].append((i, j))
            else:
                satellite_positions_map[current_char] = [(i, j)]

    return satellite_positions_map

def is_valid_position(current_position: tuple, shape: tuple) -> bool:
    '''Check if position is within map boundaries'''
    return 0 <= current_position[0] < shape[0] and 0 <= current_position[1] < shape[1]

def create_anti_nodes_from_satellites(first_antenna: tuple, second_antenna: tuple, grid: np.ndarray) -> list[tuple]:
    #print(f"first {first_antenna} second {second_antenna}")
    valid_antinode_positions = []
    dx = second_antenna[0] - first_antenna[0]
    dy = second_antenna[1] - first_antenna[1]
    first_satellite_possible_location = (first_antenna[0] - dx, first_antenna[1] - dy)
    second_satellite_possible_location = (second_antenna[0] + dx, second_antenna[1] + dy)
    if is_valid_position(first_satellite_possible_location, grid.shape):
        #print(f"first {first_satellite_possible_location}")
        valid_antinode_positions.append(first_satellite_possible_location)
    if is_valid_position(second_satellite_possible_location, grid.shape):
        #print(f"second {second_satellite_possible_location}")
        valid_antinode_positions.append(second_satellite_possible_location)
    return valid_antinode_positions


def find_anti_nodes(grid: np.ndarray):
    anti_node_positions =  set()
    satellites_positions: dict[str, list[tuple]] = find_satellites_positions(grid)
    for _, positions in satellites_positions.items():
        # For each satellite, determine its anti-node by creating each possible pair of satellites
        # and calculating the two anti nodes for each pai, Each anit-node is on the line connecting the
        # two satellites and they are twice as far from the center of the line as the satellites are.
        for i, first_antenna in enumerate(positions):
            for second_antenna in positions[:i]:
                for anti_node in create_anti_nodes_from_satellites(first_antenna, second_antenna, grid):
                    anti_node_positions.add(anti_node)
    #Print out anti-nodes in a grid with '.' for empty and 'x' for anti-nodes
    # for i in range(grid.shape[0]):
    #     print()
    #     for j in range(grid.shape[1]):
    #         if (i, j) in anti_node_positions:
    #             print("x", end="")
    #         else:
    #             print(".", end="")
    # print()
    return len(anti_node_positions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--input", type=str, required=True, help="Path to input file")
    parser.add_argument("--find_anti_node_count", action='store_true',
                       help="Find the number of anti-nodes in the grid")
    args = parser.parse_args()

    antennas_grid = convert_text_to_grid(args.input)
    if args.find_anti_node_count:
        result = find_anti_nodes(antennas_grid)
        print(f"The number of anti-nodes in the grid is: {result}")
