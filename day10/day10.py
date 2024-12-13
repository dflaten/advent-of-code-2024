#!/usr/bin/env python
import argparse
import numpy as np
from typing import Optional

INPUT = "input.txt"
directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
]
def build_map_from_input(path_to_file: str) -> np.ndarray:
    '''
    Converts the text file at the path to a numpy array grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return np.array([list(line.strip()) for line in file])

def is_valid_position(current_position: tuple, shape: tuple) -> bool:
    '''Check if position is within map boundaries'''
    return 0 <= current_position[0] < shape[0] and 0 <= current_position[1] < shape[1]


def find_reachable_nines(current_position: tuple[int, int], map: np.ndarray, current_path: Optional[list[tuple[int, int]]] = None) -> set:
    if current_path is None:
        current_path = [current_position]

    current_value = map[current_position]
    reachable_nines = set()
    if current_value == 9:
        reachable_nines.add(current_position)
        return reachable_nines
    for direction in directions:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if is_valid_position(next_position, map.shape) and map[next_position] == map[current_position] + 1:
            if next_position not in current_path:
                new_path = current_path + [next_position]
                reachable_nines.update(find_reachable_nines(next_position, map, new_path))
    return reachable_nines

def recurse_find_paths(current_position: tuple[int, int], map: np.ndarray, current_path: Optional[list[tuple[int, int]]] = None) -> set:
    if current_path is None:
        current_path = [current_position]
    if map[current_position] == 9:
        return {tuple(current_path)}
    paths = set()
    for direction in directions:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if is_valid_position(next_position, map.shape) and map[next_position] == map[current_position] + 1:
            if next_position not in current_path:
                new_path = current_path + [next_position]
                paths.update(recurse_find_paths(next_position, map, new_path))
    return paths

def find_trail_scores_from_position(x: int, y: int, map: np.ndarray) -> int:
    '''
    From the starting position, traverse the map counting how many ways you can
    get to 9 on the map from the starting position.
    '''
    all_paths = find_reachable_nines((x,y), map,)
    # for path in all_paths:
    # # print the map with only the path characters in it, all others should have a '.'
    #     print()
    #     for x in range(map.shape[0]):
    #         for y in range(map.shape[1]):
    #             if (x, y) in path:
    #                 print(map[x, y], end="")
    #             else:
    #                 print(".", end="")
    #         print()



    return len(all_paths)


def find_sum_of_trail_scores(map: np.ndarray) -> int:
   trail_scores = []
   for x in range(map.shape[0]):
       for y in range(map.shape[1]):
           current_number = int(map[x, y])
           if current_number == 0:
               trail_scores.append(find_trail_scores_from_position(x, y, map))
   return sum(trail_scores)

def find_sum_of_trail_ratings(map: np.ndarray) -> int:
    trail_scores = []
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            current_number = int(map[x, y])
            if current_number == 0:
                trail_scores.append(recurse_find_paths((x, y), map))
    return sum(len(trail) for trail in trail_scores)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--find_unique_nines", action='store_true',
                       help="Find the score of all trails and return their sum.")
    parser.add_argument("--find_paths", action='store_true',
                       help="Find the number of unique paths and return their count.")
    args = parser.parse_args()
    topographical_map = build_map_from_input(INPUT)
    topographical_map = topographical_map.astype(int)
    print (topographical_map)

    if args.find_unique_nines:
        result = find_sum_of_trail_scores(topographical_map)
        # Small input should be 36
        # Regular input 825
        print(f"The sum of all valid trail scores in the grid is: {result}")

    if args.find_paths:
        result = find_sum_of_trail_ratings(topographical_map)
        # Small input should be 36
        # Regular input 825
        print(f"The sum of all valid trail scores in the grid is: {result}")
