#!/usr/bin/env python
import argparse

INPUT = "input.txt"

def parse_numbers_from_file(path_to_file: str) -> list[int]:
    '''
    Finds the towels and patterns from the file.
    '''
    numbers: list[int] = []
    with open(path_to_file, 'r') as file:
        numbers = list(int(number.strip()) for number in file.readlines())

    return numbers

def mix(secret_number: int, given_value: int) -> int:
    return secret_number ^ given_value

def prune(secret_number: int) -> int:
    return secret_number % 16777216

def calculate_next_secret_number(initial_number) -> int:
    '''
    Calculates the next secret number in the sequence.
    '''
    step_1_result = prune(mix(initial_number, initial_number * 64))
    step_2_result = prune(mix(step_1_result, step_1_result // 32))
    return prune(mix(step_2_result, step_2_result * 2048))

def sum_of_2000th_secret_number_for_all_buyers(initial_numbers: list[int]) -> int:
    '''
    Finds the 2000th secret number for all buyers.
    '''
    # iterate a loop 2000 times
    two_thousandth_secret_numbers = list()
    for number in initial_numbers:
        secret_number = number
        for i in range(2000):
            secret_number = calculate_next_secret_number(secret_number)
            #print(secret_number)
        two_thousandth_secret_numbers.append(secret_number)

    #print(two_thousandth_secret_numbers)
    return sum(two_thousandth_secret_numbers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 22")
    parser.add_argument("--generate_secret_numbers", action='store_true', help="Generate the 2000th secret number for the given buyers.")
    args = parser.parse_args()
    initial_numbers = parse_numbers_from_file(INPUT)
    if args.generate_secret_numbers:
        result = sum_of_2000th_secret_number_for_all_buyers(initial_numbers)
        print(f"Total sum of 2000th secret numbers is {result}")
