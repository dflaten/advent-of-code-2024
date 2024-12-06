
#!/usr/bin/env python
import argparse
import numpy as np

def convert_text_to_grid(path_to_file: str) -> list[list[str]]:
    '''
    Converts the text file at the path to a grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return [list(line.strip()) for line in file]
        # Direction vectors for up, right, down, left

def guard_walk_map(map, guard, locations_visited) -> tuple[np.ndarray, np.ndarray]:
    '''
    Guard walks map until they hit the edge of the map.
    Directions
    < - left
    > - right
    ^ - up
    v - down
    # - obstacle
    '''
    updated_locations_visited = locations_visited
    current_guard_location = guard

    directions = {
        'up': np.array([-1, 0]),
        'right': np.array([0, 1]),
        'down': np.array([1, 0]),
        'left': np.array([0, -1])
    }

    while True:
        if map[current_guard_location] == '<':
            #check for end of map, if end of map, move to off map location and return results.
            possible_guard_location = directions['left'] + current_guard_location
            if not np.isin(map, possible_guard_location):
                return updated_locations_visited
            # if obstacle then turn right
            if possible_guard_location == '#':
                map[current_guard_location] = '^'
            else:
                # Traverse to left
                possible_guard_location = '<'
                current_guard_location = '.'
                current_guard_location = possible_guard_location
                updated_locations_visited.append(current_guard_location)
                continue

        if map[current_guard_location] == '>':
            #check for end of map, if end of map, move to off map location and return results.
            possible_guard_location = directions['right'] + current_guard_location
            if not np.isin(map, possible_guard_location):
                return updated_locations_visited
            # if obstacle then turn right
            if possible_guard_location == '#':
                map[current_guard_location] = 'v'
            else:
                # Traverse to left
                possible_guard_location = '>'
                current_guard_location = '.'
                current_guard_location = possible_guard_location
                updated_locations_visited.append(current_guard_location)
                continue

        if map[current_guard_location] == 'v':
            #check for end of map, if end of map, move to off map location and return results.
            possible_guard_location = directions['down'] + current_guard_location
            if not np.isin(map, possible_guard_location):
                return updated_locations_visited
            # if obstacle then turn right
            if possible_guard_location == '#':
                map[current_guard_location] = '<'
            else:
                # Traverse down
                possible_guard_location = 'v'
                current_guard_location = '.'
                current_guard_location = possible_guard_location
                updated_locations_visited.append(current_guard_location)
                continue

        if map[current_guard_location] == '^':
            #check for end of map, if end of map, move to off map location and return results.
            print('before')
            print(current_guard_location)
            direction = directions['up']
            possible_guard_location = current_guard_location + direction
            print('possum')
            print(possible_guard_location)
            if not np.isin(map, possible_guard_location):
                return updated_locations_visited
            # if obstacle then turn right
            if possible_guard_location == '#':
                map[current_guard_location] = '>'
            else:
                # Traverse down
                possible_guard_location = '^'
                current_guard_location = '.'
                current_guard_location = possible_guard_location
                updated_locations_visited.append(current_guard_location)
                continue

    return current_guard_location


def find_all_points_visited(map_grid: list[list[str]]) -> int:
    '''
    Find all points visited by the guard.
    '''
    locations_visited = []
    map = np.array(map_grid)
    print(map)
    # find the guard where the guard is the character <, >, ^, or v
    guard_current_location = np.where(np.isin(map, ['<', '>', '^', 'v']))
    guard_current_location = [tuple(guard_current_location)]
    #guard_direction_facing = map[guard_current_location]
    #print(guard_direction_facing[0])
    locations_visited.append(guard_current_location)
    locations_visited = guard_walk_map(map, guard_current_location, locations_visited)

    return len(locations_visited)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 6")
    parser.add_argument("--input", type=str, help="Path to input file.")
    parser.add_argument("--find_points_visited", action='store_true', help="Find all the valid page orderings in the pages to produce file that follow the rules in the rule file.")
    args = parser.parse_args()
    map_grid = convert_text_to_grid(args.input)
    print('grid')
    if args.find_points_visited:
        result = find_all_points_visited(map_grid)
        print(f"Found {result} points visited by the guard.")
