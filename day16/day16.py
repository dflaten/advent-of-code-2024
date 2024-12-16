
#!/usr/bin/env python
import argparse
import numpy as np
import heapq
from typing import Optional

INPUT = "input.txt"

directions = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1), # left
    (-1, 0)  # up
]

def build_maze_and_instructions_from_input(path_to_file: str) -> np.ndarray:
    '''
    Converts the text file at the path to a numpy array grid for traversal.
    '''
    raw_maze = None
    with open(path_to_file, 'r') as file:
        raw_maze = [line.strip() for line in file.readlines()]
    delimiter_row = None
    for i, row in enumerate(raw_maze):
        if all(char == '#' for char in row):
            delimiter_row = i
            if i > 0 and all(char == '#' for char in raw_maze[i-1]):  # Found the final delimiter
                break
    if delimiter_row is None:
        raise ValueError("No delimiter row found in input file")

    map = raw_maze
    numpy_maze = np.array([list(row) for row in map])
    return numpy_maze


def find_start_and_end(maze: np.ndarray) -> tuple[tuple, tuple]:
    '''
    Reindeer (start_pos) is at location with character S
    End is at location with character E
    '''

    # Find start and end positions
    start_pos = None
    end_pos = None
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i][j] == 'S':
                start_pos = (i, j)
            elif maze[i][j] == 'E':
                end_pos = (i, j)
    if start_pos is None or end_pos is None:
        raise ValueError("Could not find start or end position")
    return start_pos, end_pos

def get_next_position(current_position: tuple, direction: tuple) -> tuple:
    return (current_position[0] + direction[0], current_position[1] + direction[1])

def build_graph(maze):
    rows, cols = maze.shape
    vertices = {}
    edges = {}

    # Each position will have 4 vertices, one for each direction we could be facing
    # 0: facing right, 1: facing down, 2: facing left, 3: facing up

    # Build vertices
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] != '#':
                # Create a vertex for each direction at this position
                for direction in range(4):
                    vertices[(row, col, direction)] = maze[row][col]
                    edges[(row, col, direction)] = {}

    # Build edges
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] != '#':
                for from_dir in range(4):  # Current direction
                    for to_dir, (y_offset, x_offset) in enumerate(directions):
                        new_row, new_col = row + y_offset, col + x_offset

                        if (0 <= new_row < rows and
                            0 <= new_col < cols and
                            maze[new_row][new_col] != '#'):

                            # Base movement cost
                            weight = 1

                            # Add turn cost if direction changes
                            # Check if it's a 90-degree turn
                            if (from_dir != to_dir):
                                if abs(from_dir - to_dir) != 2:  # Not a 180-degree turn
                                    weight += 1000

                            edges[(row, col, from_dir)][(new_row, new_col, to_dir)] = weight

    return vertices, edges

def find_way_out_with_lowest_score(map: np.ndarray) -> Optional[float]:
    '''
    Find the way out of the map with the lowest score.
    '''
    start_pos, end_pos = find_start_and_end(map)

    # Build graph and run Dijkstra's
    vertices, edges = build_graph(map)

    # Start facing right (0, 1), (direction 0)
    start_vertex = (start_pos[0], start_pos[1], 0)

    # Run Dijkstra's algorithm
    distances, previous = dijkstra(vertices, edges, start_vertex)

    # Check all possible end directions and find minimum
    min_distance = float('infinity')
    for direction in range(4):
        end_vertex = (end_pos[0], end_pos[1], direction)
        if end_vertex in distances:
            min_distance = min(min_distance, distances[end_vertex])

    return min_distance if min_distance != float('infinity') else None


def dijkstra(vertices, edges, start):
    distances = {vertex: float('infinity') for vertex in vertices}
    distances[start] = 0
    pq = [(0, start)]
    previous = {vertex: None for vertex in vertices}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in edges[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--find_way_out", action='store_true',
                       help="Find the way out of the map with the lowest score.")
    args = parser.parse_args()
    maze = build_maze_and_instructions_from_input(INPUT)

    if args.find_way_out:
        result = find_way_out_with_lowest_score(maze)
        print(f"The score of the shortest map is: {result}")