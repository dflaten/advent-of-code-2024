#!/usr/bin/env python
# This first approach didn't work because I was only looking for straight line matches.
import argparse

def convert_text_to_grid(path_to_file: str) -> list[list[str]]:
    '''
    Converts the text file at the path to a grid for traversal.
    '''
    with open(path_to_file, 'r') as file:
        return [list(line.strip()) for line in file]

def search_direction(row: int, col: int, dir_x: int, dir_y: int, grid: list[list[str]], word: str):
    rows = len(grid)
    columns = len(grid[0])
    if grid[row][col] != word[0]:
        return False

    length = len(word)

    # Check if the word would fit in this direction
    end_row = row + (length - 1) * dir_x
    end_col = col + (length - 1) * dir_y

    if not (0 <= end_row < rows and 0 <= end_col < columns):
        return False

    # Check each character along the path
    for i in range(1, length):
        curr_row = row + i * dir_x
        curr_col = col + i * dir_y
        if grid[curr_row][curr_col] != word[i]:
            return False

    return True


def search_from_cell(row, col, word, grid) -> bool:
        # All 8 directions: right, down-right, down, down-left, left, up-left, up, up-right
        directions = [
            (0, 1), (1, 1), (1, 0), (1, -1),
            (0, -1), (-1, -1), (-1, 0), (-1, 1)
        ]

        for dir_x, dir_y in directions:
            if search_direction(row=row, col=col, dir_x =dir_x, dir_y=dir_y, grid=grid, word=word):
                return True
        return False

def find_all_instances_in_grid(character_grid: list[list[str]], word: str) -> int:
    '''
    Finds all instances of the word in the grid.
    '''
    number_of_instances = 0
    rows = len(character_grid)
    columns = len(character_grid[0])
    # Search from each cell as a starting point
    for row in range(rows):
        for col in range(columns):
            if search_from_cell(row=row, col=col, grid=character_grid, word=word):
               number_of_instances += 1
    return number_of_instances



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
