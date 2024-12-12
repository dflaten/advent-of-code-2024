
#!/usr/bin/env python
import argparse
import numpy as np
from typing import Optional, List, Tuple, Set

INPUT = "input.txt"

directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
]

BULK_DISCOUNT = False

def build_map_from_input(path_to_file: str) -> np.ndarray:
    '''
    Converts the text file at the path to a numpy array grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return np.array([list(line.strip()) for line in file])

def is_valid_position(current_position: tuple, shape: tuple) -> bool:
    '''Check if position is within map boundaries'''
    return 0 <= current_position[0] < shape[0] and 0 <= current_position[1] < shape[1]


def determine_fence_group(current_position: tuple[int, int], map: np.ndarray, group_type: str, current_group: Optional[set[tuple[int, int]]] = None) -> set:
    if current_group is None:
        current_group = set()
        current_group.add(current_position)

    current_value = map[current_position]
    if current_value == group_type:
        current_group.add(current_position)
        for direction in directions:
            next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            if is_valid_position(next_position, map.shape) and next_position not in current_group:
                determine_fence_group(next_position, map, group_type, current_group)
    return current_group

def fence_group(x: int, y: int, map: np.ndarray) -> set[tuple[int, int]]:
    '''
    From the starting position, traverse the map to determine the fence group,
    where a group is equal to all points that have the same value as x,y and are touching.
    '''
    group = determine_fence_group((x,y), map, map[x, y])
    # for path in group:
    # # print the map with only the path characters in it, all others should have a '.'
    #     print()
    #     for x in range(map.shape[0]):
    #         for y in range(map.shape[1]):
    #             if (x, y) in path:
    #                 print(map[x, y], end="")
    #             else:
    #                 print(".", end="")
    #         print()



    return group

def calculate_perimeter(group: Set[Tuple[int, int]]) -> int:
    '''
    Calculate the perimeter of the group by counting the number of edges that are not in the group.
    '''
    perimeter = 0
    for point in group:
        for direction in directions:
            next_point = (point[0] + direction[0], point[1] + direction[1])
            if next_point not in group:
                perimeter += 1
    return perimeter

def calculate_perimeter_with_sides(group: Set[Tuple[int, int]]) -> int:
    '''
    Calculate the perimeter of the group by counting the number of edges that are not in the group.
    An edge here is defined as a continuous group of points that are not in the group.
    '''
    perimeter = 0
    # How do I track that I have already counted a side?
    sides = set()
    for point in group:
        for direction in directions:
            next_point = (point[0] + direction[0], point[1] + direction[1])
            if next_point not in group and :
                sides.add(next_point)



def determine_fence_cost(fence_groups: List[Set[Tuple[int, int]]]) -> int:
    '''
    Find the cost of fencing the groups of letters in the map. The cost is found by multiplying
    the Area by the Perimter of the group.
    Area = Number of letters in the group.
    Perimeter = Number of edges of the group.:
    '''
    total_cost = 0
    if not BULK_DISCOUNT:
        for group in fence_groups:
            total_cost += len(group) * calculate_perimeter(group)
    else:
        for group in fence_groups:
            total_cost = len(group) * calculate_perimeter_with_sides(group)

    return total_cost

def calculate_fence_cost(map: np.ndarray) -> int:
    fence_groups: List[Set[Tuple[int, int]]] = []
    fenced_points: Set[Tuple[int, int]] = set()
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            if (x, y) not in fenced_points:
                new_fenced_group = fence_group(x, y, map)
                #print(f"fenced points before update: {fenced_points}")
                fenced_points.update(new_fenced_group)
                #print(f"fenced points after update: {fenced_points}")
                fence_groups.append(new_fenced_group)
    # print(f"Found {len(fence_groups)} fenced groups")
    # for group in fence_groups:
    #     print(group)
    # print(f"Found {len(fenced_points)} fenced points")

    return determine_fence_cost(fence_groups)
    # return the sum and perimter of the fenced groups

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--calc_fence_cost", action='store_true',
                       help="Find the total fence cost for the map.")
    parser.add_argument("--calc_fence_cost_bulk_discount", action='store_true',
                       help="Find the total fence cost for the map with the bulk discount.")
    args = parser.parse_args()
    topographical_map = build_map_from_input(INPUT)
    print (topographical_map)

    if args.calc_fence_cost:
        result = calculate_fence_cost(topographical_map)
        print(f"The total fence cost in the map is: {result}")
    if args.calc_fence_cost_bulk_discount:
        BULK_DISCOUNT = True
        result = calculate_fence_cost(topographical_map)
        print(f"The total fence cost in the map is: {result}")
