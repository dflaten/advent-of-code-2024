#!/usr/bin/env python
import argparse
from functools import cmp_to_key

INPUT = "small-input.txt"

def parse_towels_and_patterns_from_file(path_to_file: str) -> tuple[set[str], list[str]]:
    '''
    Finds the towels and patterns from the file.
    '''
    towels: set[str] = set()
    patterns: list[str] = []
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        towels = set(lines[0].strip().split(','))
        for index, line in enumerate(lines):
            if index >= 2:
                patterns.append(line.strip())

    return towels, patterns

def can_create_pattern(towels: set[str], towel_pattern: str) -> bool:
    # check if a substring from the towel is in the pattern, starting with the whole string
    # and then moving to smaller substrings starting at the beginning of the string.
    # If the entire string can be made by substring in towels return true else return false.
    print(f"Checking if {towel_pattern} can be made with {towels}")
    if not towel_pattern:
        return True
    for i in range(1, len(towel_pattern) + 1):
        prefix = towel_pattern[:i]
        if prefix in towels:
            remaining = towel_pattern[i:]
            if can_create_pattern(towels, remaining):
                return True
    print(f"Cannot make {towel_pattern} with {towels}")
    return False

def find_possible_count_of_patterns(towels: set[str], towel_patterns: list[str]) -> int:
    '''
    Finds the possible count of patterns that can be made.
    '''
    count_of_possible_patterns = 0
    for pattern in towel_patterns:
        if can_create_pattern(towels, pattern):
            count_of_possible_patterns += 1
    return count_of_possible_patterns

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 19")
    parser.add_argument("--find_possible_pattern_count", action='store_true', help="Find all possible patterns you can create with input.")
    args = parser.parse_args()
    towels, towel_patterns= parse_towels_and_patterns_from_file(INPUT)
    print(towels)
    print(towel_patterns)
    if args.find_possible_pattern_count:
        result = find_possible_count_of_patterns(towels, towel_patterns)
        print(f"Total number of possible patterns is {result}")
