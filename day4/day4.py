
#!/usr/bin/env python
import argparse
import numpy as np

# Trying to get a better understanding of numpy by using Joe's solution as a base:
# https://github.com/joeplattenburg/advent_of_code/blob/main/2024/problem_04.py
def convert_text_to_grid(path_to_file: str) -> list[list[str]]:
    '''
    Converts the text file at the path to a grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return [list(line.strip()) for line in file]

def get_count_at_index(i: int, j: int, mat: np.ndarray, word: str = "XMAS") -> int:
    l = len(word)
    counter = 0
    counter += int(safe_access((i, i + 1), (j, j + l), mat) == word)
    counter += int(safe_access((i, i + 1), (j, j - l), mat) == word)
    counter += int(safe_access((i, i + l), (j, j + 1), mat) == word)
    counter += int(safe_access((i, i - l), (j, j + 1), mat) == word)
    counter += int(safe_access((i, i + l), (j, j + l), mat, diag=True) == word)
    counter += int(safe_access((i, i - l), (j, j + l), mat, diag=True) == word)
    counter += int(safe_access((i, i + l), (j, j - l), mat, diag=True) == word)
    counter += int(safe_access((i, i - l), (j, j - l), mat, diag=True) == word)
    return counter

def find_all_instances_in_grid(character_grid: list[list[str]], word: str) -> int:
    '''
    Finds all instances of the word in the grid.
    '''
    # Create my numpy grid
    grid = np.array(character_grid)
    # get the rows and columns
    rows, cols = grid.shape
    counter1, counter2 = 0, 0
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 'X':
                # Problem 1
                counter1 += get_count_at_index(i, j, mat)
            if grid[i, j] == 'A':
                # Problem 2
                counter2 += int(is_xmas(i, j, mat))
    print(f'Part 1: {counter1}')
    print(f'Part 2: {counter2}')
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 4")
    parser.add_argument("--input", type=str, help="Path to input file.")
    parser.add_argument("--find_xmas", action='store_true', help="Find all the XMAS strings in the input.")
    args = parser.parse_args()
    character_grid = convert_text_to_grid(args.input)
    if args.find_xmas:
        word = 'XMAS'
        result = find_all_instances_in_grid(character_grid, word)
        print(f"Found {result} instances of {word} in the text file.")
