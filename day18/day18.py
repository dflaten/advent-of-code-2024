
#!/usr/bin/env python
import argparse
import numpy as np
import heapq
from typing import Optional

INPUT = "input.txt"

DIRECTIONS = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1), # left
    (-1, 0)  # up
]
SMALL = (7,7)
REGULAR = (71,71)
# How many items should fall before we attempt to create a path?
ITEMS_TO_FALL = 1024
MAP = np.full(REGULAR, ".")
END = (MAP.shape[0] - 1, MAP.shape[1] - 1)

def get_list_of_falling_items(path_to_file: str) -> list[tuple[int, int]]:
    '''
    Converts the text file at the path to a list of tuples.
    '''
    falling_locations = []
    with open(path_to_file, 'r') as file:
        for line in file:
            numbers = line.strip().split(",")
            falling_locations.append((int(numbers[0]), int(numbers[1])))
    return falling_locations

def simulate_items_falling(map: np.ndarray, all_falling_items: list[tuple[int, int]], count_of_items_to_fall: int) -> np.ndarray:
    '''
    Simulates the falling of items on the map.
    '''
    falling_items = all_falling_items[:count_of_items_to_fall]
    map_with_items_fallen = map.copy()
    for item in falling_items:
        map_with_items_fallen[item] = "#"
    return map_with_items_fallen

def find_shortest_route(map: np.ndarray, start: tuple[int, int], end: tuple[int, int]) -> Optional[int]:
    '''
    Finds the shortest route between two points on the map.
    '''
    visited = set()
    queue = [(0, start)]
    while queue:
        distance, current = heapq.heappop(queue)
        if current == end:
            return distance
        if current in visited:
            continue
        visited.add(current)
        for direction in DIRECTIONS:
            new_location = (current[0] + direction[0], current[1] + direction[1])
            # if item is in the map
            if all(0 <= point < shape for point, shape in zip(new_location, map.shape)):
                # and the location is not blocked
                if map[new_location] == ".":
                    heapq.heappush(queue, (distance + 1, new_location))
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--find_way_out", action='store_true',
                       help="Find the shortest way out of the map.")
    args = parser.parse_args()
    falling_items = get_list_of_falling_items(INPUT)

    if args.find_way_out:
        map_to_traverse = simulate_items_falling(MAP, falling_items, ITEMS_TO_FALL)
        result = find_shortest_route(map_to_traverse, (0, 0), END)
        print(f"The score of the shortest map is: {result}")
