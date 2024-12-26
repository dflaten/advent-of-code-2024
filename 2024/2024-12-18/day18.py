
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
START = (0, 0)
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

def is_item_the_final_safe_path(falling_items: list[tuple[int, int]], item_index: int) -> bool:
    # First index will never block
    if item_index == 0:
        return False
    updated_map_for_left = simulate_items_falling(MAP, falling_items, item_index - 1)
    if find_shortest_route(updated_map_for_left, START, END) is not None:
        updated_map_for_potential_blocking = simulate_items_falling(MAP, falling_items, item_index)
        if find_shortest_route(updated_map_for_potential_blocking, START, END) is None:
            return True
    return False

def is_item_to_the_right(falling_items: list[tuple[int, int]], item_index: int) -> bool:
    updated_map_for_item = simulate_items_falling(MAP, falling_items, item_index)
    if find_shortest_route(updated_map_for_item, START, END) is not None:
        return True
    return False

def find_when_path_blocked(map: np.ndarray, falling_items: list[tuple[int, int]]) -> tuple[int, int]:
    left, right = 0, len(falling_items) - 1
    while left<= right:
        mid = (left + right) // 2
        if is_item_the_final_safe_path(falling_items, mid):
            return falling_items[mid - 1]
        elif is_item_to_the_right(falling_items, mid):
            left = mid + 1
        else:
            right = mid -1
    # no blocking item found
    return (-1, -1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--find_way_out", action='store_true',
                       help="Find the shortest way out of the map.")
    parser.add_argument("--find_when_way_out_blocked", action='store_true',
                       help="Find at what point in dropping items the path becomes blocked.")
    args = parser.parse_args()
    falling_items = get_list_of_falling_items(INPUT)

    if args.find_way_out:
        map_to_traverse = simulate_items_falling(MAP, falling_items, ITEMS_TO_FALL)
        result = find_shortest_route(map_to_traverse, START, END)
        print(f"The score of the shortest map is: {result}")
    if args.find_when_way_out_blocked:
        result = find_when_path_blocked(MAP, falling_items)
        print(f"The item that blocks is: {result}")
