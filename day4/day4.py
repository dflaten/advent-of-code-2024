#!/usr/bin/env python
import argparse

def convert_text_to_grid(path_to_file: str) -> list[list[str]]:
    '''
    Converts the text file at the path to a grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return [list(line.strip()) for line in file]

def find_all_instances_in_grid(character_grid: list[list[str]], word: str) -> int:
    '''
    Finds all instances of the word in the grid.
    '''
    rows = len(character_grid)
    columns = len(character_grid[0])
    paths = set()
    # Start from each cell
    for row in range(rows):
        for col in range(columns):
            if character_grid[row][col] == word[0]:
                path = dfs(row, col, word, [(row, col)], character_grid)
                paths.add(path)
    # for path in paths:
    #     print(path)
    for path in paths:
        for row in range(rows):
            for col in range(columns):
                if (row, col) in path:
                    print(character_grid[row][col], end="")
                else:
                    print(".", end="")
            print()
        print()


    return len(paths)

def dfs(row, col, word, current_path, character_grid):
    rows = len(character_grid)
    columns = len(character_grid[0])
    # If we've found the complete word
    if len(current_path) == len(word):
        # Convert path to tuple so it can be added to set
        return tuple(current_path)

    # Check all 8 adjacent cells
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_row = row + dx
            new_col = col + dy
            # Skip if out of bounds
            if not (0 <= new_row < rows and 0 <= new_col < columns):
                continue
            # Skip if already in current path
            if (new_row, new_col) in current_path:
                continue
            # Check if next character matches
            if len(current_path) < len(word) and character_grid[new_row][new_col] == word[len(current_path)]:
                return dfs(new_row, new_col, word, current_path + [(new_row, new_col)], character_grid)

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
