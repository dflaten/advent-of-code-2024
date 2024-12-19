#!/usr/bin/env python
import argparse
from functools import cache

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
        # Base case
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

def find_possible_patterns(towels: set[str], towel_patterns: list[str]) -> list[str]:
    '''
    Finds the possible count of patterns that can be made.
    '''
    patterns_made = list()
    for pattern in towel_patterns:
        if can_create_pattern(towels, pattern):
            patterns_made.append(pattern)
    return patterns_made

@cache
def find_possible_ways_to_make_patterns(pattern: str) -> int:
    found_pattern_combination_count = 0
    for towel in towels:
        if pattern.startswith(towel):
            if len(towel) == len(pattern):
                found_pattern_combination_count += 1
            else:
                found_pattern_combination_count += find_possible_ways_to_make_patterns(pattern[len(towel):])
    return found_pattern_combination_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 19")
    parser.add_argument("--find_possible_pattern_count", action='store_true', help="Find all possible patterns you can create with input.")
    parser.add_argument("--find_ways_to_make_patterns", action='store_true', help="From the possible patterns, find how many ways each can be made.")
    args = parser.parse_args()
    towels, towel_patterns= parse_towels_and_patterns_from_file(INPUT)
    if args.find_possible_pattern_count:
        result = len(find_possible_patterns(towels, towel_patterns))
        print(f"Total number of possible patterns is {result}")
    if args.find_ways_to_make_patterns:
        possible_patterns = find_possible_patterns(towels, towel_patterns)
        sum_of_possible_ways_to_make_patterns = [find_possible_ways_to_make_patterns(pattern) for pattern in possible_patterns]
        print(f"Total number of possible patterns is {sum(sum_of_possible_ways_to_make_patterns)}")
