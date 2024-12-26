#!/usr/bin/env python
import argparse
INPUT = "input.txt"

def parse_input(path_to_file: str) -> list[int]:
    with open(path_to_file, 'r') as file:
        # should be one line with numbers separated by a space
        for line in file:
            return [int(x) for x in line.strip().split(" ")]
    return []

def determine_new_numbers(list_of_numbers: list[int]) -> list[int]:
    '''
    If the number is 0, it is replaced by the number 1.
    If the number has an even number of digits, it is replaced by two numbers. The left half of the digits are one number, and the right half of the digits are the other. (The new numbers don't keep extra leading zeroes: 1000 would become 10 and 0.)
    If none of the other rules apply, the number is replaced by the old number multiplied by 2024.
    '''
    new_numbers = []
    for number in list_of_numbers:
        if number == 0:
            new_numbers.append(1)
        elif len(str(number)) % 2 == 0:
            number_str = str(number)
            half = len(number_str) // 2
            new_numbers.append(int(number_str[:half]))
            new_numbers.append(int(number_str[half:]))
        else:
            new_numbers.append(number * 2024)
    return new_numbers

def preform_iterations(starting_numbers: list[int], number_of_iterations: int) -> int:
    numbers = starting_numbers
    for i in range(number_of_iterations):
        numbers = determine_new_numbers(numbers)
    return len(numbers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number combination validator")
    parser.add_argument("--count_numbers", action='store_true',
                       help="Find the numbers generated after the input number of iterations")
    args = parser.parse_args()

    starting_numbers= parse_input(INPUT)
    if args.count_numbers:
        iterations = 25
        result = preform_iterations(starting_numbers, number_of_iterations=iterations)
        print(f"The number of numbers after {iterations} iterations: {result}")
