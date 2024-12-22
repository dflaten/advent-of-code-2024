#!/usr/bin/env python
import argparse
from collections import defaultdict

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

def two_thousandth_secret_number_for_all_buyers(initial_numbers: list[int]) -> list[int]:
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
    return two_thousandth_secret_numbers

def determine_most_bananas(initial_numbers: list[int]) -> int:
    '''
    Determines the most bananas you could obtain by iterating through all the
    initial secret numbers generating a sequence of 2000 numbers for each. While
    doing this it keeps track of the differences between the prices of the bananas
    and the sequence that was generated before it in a map. The price of which is
    updated as the sequence is generated.

    At the end you can take the max in the sequence tracker since that will have the
    largest value for all the sequences.
    '''
    sequence_tracker = defaultdict(int)
    for secret_number in initial_numbers:
        price = secret_number % 10
        differences_in_price = []
        already_seen = set()
        for i in range(2000):
            new_secret_number = calculate_next_secret_number(secret_number)
            new_price = new_secret_number % 10
            differences_in_price.append(new_price - price)
            if len(differences_in_price) > 4:
                differences_in_price.pop(0)
            if len(differences_in_price) == 4:
                sequence = tuple(differences_in_price)
                if sequence not in already_seen:
                    already_seen.add(sequence)
                    sequence_tracker[sequence] += new_price
            price = new_price
            secret_number = new_secret_number

    #print(sequence_tracker)
    return max(sequence_tracker.values())




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 22")
    parser.add_argument("--generate_secret_numbers", action='store_true', help="Generate the 2000th secret number for the given buyers.")
    parser.add_argument("--determine_most_bananas", action='store_true', help="Determine the most bananas you couls obtain.")
    args = parser.parse_args()
    initial_numbers = parse_numbers_from_file(INPUT)
    if args.generate_secret_numbers:
        result = sum(two_thousandth_secret_number_for_all_buyers(initial_numbers))
        print(f"Total sum of 2000th secret numbers is {result}")
    if args.determine_most_bananas:
        result = determine_most_bananas(initial_numbers)
        print(f"The most bananas you can get is {result}")
