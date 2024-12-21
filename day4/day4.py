
#!/usr/bin/env python
import argparse
import numpy as np
INPUT = 'input.txt'

directions = [
    (-1, -1), # up-left
    (-1, 0), # up
    (-1, 1), # up-right
    (0, -1), # left
    (0, 1), # right
    (1, -1), # down-left
    (1, 0), # down
    (1, 1) # down-right
]

def convert_text_to_grid(path_to_file: str) -> list[list[str]]:
    '''
    Converts the text file at the path to a grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return [list(line.strip()) for line in file]

def get_count_at_index(i: int, j: int, mat: np.ndarray) -> int:
   x_mas_count = 0
               # now check for As from this direction


   return h

def find_all_xmas_instances_in_grid(character_grid: list[list[str]]) -> int:
    '''
    Finds all instances of XMAS in the grid, but only in straight lines
    (horizontal, vertical, or diagonal).
    '''
    grid = np.array(character_grid)
    rows, cols = grid.shape

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0),  # up
        (1, 1),   # diagonal down-right
        (-1, -1), # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)   # diagonal up-right
    ]

    xmas_counter = 0
    set_of_x_mas_coords = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 'X':
                for dx, dy in directions:
                    # Calculate all three next positions at once using the same direction
                    m_pos = (i + dx, j + dy)
                    a_pos = (i + 2*dx, j + 2*dy)
                    s_pos = (i + 3*dx, j + 3*dy)

                    # Check if all positions are within bounds
                    if (0 <= m_pos[0] < rows and 0 <= m_pos[1] < cols and
                        0 <= a_pos[0] < rows and 0 <= a_pos[1] < cols and
                        0 <= s_pos[0] < rows and 0 <= s_pos[1] < cols):

                        # Check if the letters match in this direction
                        if (grid[m_pos] == 'M' and
                            grid[a_pos] == 'A' and
                            grid[s_pos] == 'S'):

                            # Create and store the instance
                            x_mas_instance = {
                                'X': (i, j),
                                'M': m_pos,
                                'A': a_pos,
                                'S': s_pos
                            }
                            set_of_x_mas_coords.add(frozenset(x_mas_instance.items()))
                            xmas_counter += 1

    return len(set_of_x_mas_coords)
    def find_all_x_mas_instances_in_grid(character_grid: list[list[str]]) -> int:
        '''
        Finds all instances of X-MAS in grid:

        M.S
        .A.
        M.S

        in the grid, but only in straight lines
        (horizontal, vertical, or diagonal).
        '''
        grid = np.array(character_grid)
        rows, cols = grid.shape

        directions = [
            (1, 1),   # diagonal down-right
            (-1, -1), # diagonal up-left
            (1, -1),  # diagonal down-left
            (-1, 1)   # diagonal up-right
        ]

        xmas_counter = 0
        set_of_x_mas_coords = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i, j] == 'M':
                    for dx, dy in directions:
                        # Calculate all three next positions at once using the same direction
                        a_pos = (i + dx, j + dy)
                        corner_pos_1 = (i + 2*dx, j + 2*dy)
                        corner_pos_2 = (i + 2*dx, j + 2*dy)
                        corner_pos_3 = (i + 2*dx, j + 2*dy)

                        # Check if all positions are within bounds
                        if (0 <= m_pos[0] < rows and 0 <= m_pos[1] < cols and
                            0 <= a_pos[0] < rows and 0 <= a_pos[1] < cols and
                            0 <= s_pos[0] < rows and 0 <= s_pos[1] < cols):

                            # Check if the letters match in this direction
                            if (grid[m_pos] == 'M' and
                                grid[a_pos] == 'A' and
                                grid[s_pos] == 'S'):

                                # Create and store the instance
                                x_mas_instance = {
                                    'M': (m_pos, m2_pos),
                                    'A': (a_pos, a2_pos),
                                    'S': (s_pos, s2_pos),
                                }
                                set_of_x_mas_coords.add(frozenset(x_mas_instance.items()))
                                xmas_counter += 1

        return len(set_of_x_mas_coords)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 4")
    parser.add_argument("--find_xmas", action='store_true', help="Find all the XMAS strings in the input.")
    args = parser.parse_args()
    character_grid = convert_text_to_grid(INPUT)
    if args.find_xmas:
        result = find_all_xmas_instances_in_grid(character_grid)
        print(f"Found {result} instances of XMAS in the text file.")
