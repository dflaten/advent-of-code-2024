#!/usr/bin/env python
import argparse
from typing import Optional

def parse_input(path_to_file: str) -> list[list[int]]:
    result = []
    with open(path_to_file, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) != 2:
                continue
            numbers = [int(x) for x in parts[0].strip().split() + parts[1].strip().split() if x]
            result.append(numbers)
    return result

def can_reach_target(target: int, nums: list[int], current: Optional[int], index: int = 0, use_concat = False ) -> bool:
    '''
    Check if it's possible to reach target using numbers from nums starting at index,
    using only + and * operations in the original order
    '''
    if current is None:
        return can_reach_target(target, nums, nums[0], 1,use_concat)

    if index >= len(nums):
        return current == target

    if can_reach_target(target, nums, current + nums[index], index + 1, use_concat):
        return True

    if can_reach_target(target, nums,  current * nums[index], index + 1, use_concat):
        return True

    if use_concat:
        if can_reach_target(target, nums, int(str(current) + str(nums[index])), index + 1, use_concat):
            return True

    return False

def find_valid_lines(lines: list[list[int]], use_concat = False) -> int:
    '''
    Returns sum of target values from valid lines.
    A line is valid if its target (first number) can be obtained by combining the
    remaining numbers with + and * operations in their original order.
    '''
    total = 0
    for line in lines:
        target = line[0]
        operands = line[1:]
        if can_reach_target(target=target, nums=operands, current=None, use_concat=use_concat):
            total += target
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--input", type=str, required=True, help="Path to input file")
    parser.add_argument("--find_valid_lines", action='store_true',
                       help="Find and sum valid line results")
    parser.add_argument("--find_valid_lines_with_concat", action='store_true',
                       help="Find and sum valid line results, you can alos concatenate numbers")
    args = parser.parse_args()

    test_lines = parse_input(args.input)
    if args.find_valid_lines:
        result = find_valid_lines(test_lines)
        print(f"The sum of all valid line results is: {result}")
    if args.find_valid_lines_with_concat:
        result = find_valid_lines(test_lines, use_concat=True)
        print(f"The sum of all valid line results is: {result}")
