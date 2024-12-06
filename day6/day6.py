#!/usr/bin/env python
import argparse
import numpy as np

def convert_text_to_grid(path_to_file: str) -> np.ndarray:
    '''
    Converts the text file at the path to a numpy array grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return np.array([list(line.strip()) for line in file])

def is_valid_position(current_position: tuple, shape: tuple) -> bool:
    '''Check if position is within map boundaries'''
    return 0 <= current_position[0] < shape[0] and 0 <= current_position[1] < shape[1]

def guard_walk_map(map_array: np.ndarray, start_pos: tuple) -> set:
    '''
    Guard walks map until they hit the edge of the map.
    Directions: < (left), > (right), ^ (up), v (down), # (obstacle)
    Returns set of visited positions.
    '''
    directions = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    turn_right = {
        '<': '^',
        '^': '>',
        '>': 'v',
        'v': '<'
    }

    visited = set()
    current_pos = start_pos
    visited.add(current_pos)

    # Keep track of position+direction combinations to detect cycles
    locations_visited = set()

    while True:
        current_symbol = map_array[current_pos]
        # Just adding some validation that probably isn't needed.'
        if current_symbol not in directions:
            break

        current_location = (current_pos, current_symbol)
        if current_location in locations_visited:
            break
        locations_visited.add(current_location)

        # Calculate next position
        dist_y, dist_x = directions[current_symbol]
        next_pos = (current_pos[0] + dist_y, current_pos[1] + dist_x)

        # Check if next position is valid and not an obstacle
        if not is_valid_position(next_pos, map_array.shape):
            break

        if map_array[next_pos] == '#':
            map_array[current_pos] = turn_right[current_symbol]
        else:
            # Move to next position
            map_array[current_pos] = '.'
            map_array[next_pos] = current_symbol
            current_pos = next_pos
            visited.add(current_pos)

    return visited

def find_all_points_visited(map_grid: np.ndarray) -> int:
    '''
    Find all points visited by the guard.
    '''
    # Find guard's starting position, should only be one
    guard_chars = {'<', '>', '^', 'v'}
    guard_positions = np.where(np.isin(map_grid, list(guard_chars)))
    if len(guard_positions[0]) == 0 or len(guard_positions[0]) > 1:
        return 0

    start_pos = (guard_positions[0][0], guard_positions[1][0])
    visited_positions = guard_walk_map(map_grid, start_pos)

    return len(visited_positions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guard Path Tracker")
    parser.add_argument("--input", type=str, help="Path to input file.")
    parser.add_argument("--find_points_visited", action='store_true',
                       help="Find all points visited by the guard.")
    parser.add_argument("--place_obstruction", action='store_true',
                       help="Find a place to set an obstruction so the guard gets stuck in a loop.")
    args = parser.parse_args()

    map_grid = convert_text_to_grid(args.input)

    if args.find_points_visited:
        result = find_all_points_visited(map_grid)
        print(f"Found {result} points visited by the guard.")
