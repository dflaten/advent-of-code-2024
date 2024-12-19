#!/usr/bin/env python
import argparse
from functools import cmp_to_key

INPUT = "input.txt"

def parse_towels_and_patterns_from_file(path_to_file: str) -> tuple[set[str], list[str]]:
    '''
    Finds the towels and patterns from the file.
    '''
    towels: set[str] = set()
    patterns: list[str] = []
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        towels = set(towel.strip() for towel in lines[0].strip().split(','))
        for index, line in enumerate(lines):
            if index >= 2:
                patterns.append(line.strip())

    return towels, patterns

def can_create_pattern(towels: set[str], towel_pattern: str) -> bool:
    # Use memoization to store results of subproblems
    memo = {}

    def check_pattern_dynamic(start: int) -> bool:
        # Base case: if we've reached the end of the pattern
        if start == len(towel_pattern):
            return True

        # If we've already solved this subproblem
        if start in memo:
            return memo[start]

        # Try all possible prefixes from this position
        for i in range(start + 1, len(towel_pattern) + 1):
            prefix = towel_pattern[start:i]
            if prefix in towels and check_pattern_dynamic(i):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return check_pattern_dynamic(0)

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
    if args.find_possible_pattern_count:
        result = find_possible_count_of_patterns(towels, towel_patterns)
        print(f"Total number of possible patterns is {result}")
