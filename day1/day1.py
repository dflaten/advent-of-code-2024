#!/usr/bin/env python
import argparse

def get_lists_from_file(input):
    list1 = []
    list2 = []
    with open(input, 'r') as file:
        numbers = file.read().split()
        numbers = [int(num) for num in numbers]

        # Each line has two numbers, one for each list
        for i in range(0, len(numbers), 2):
            list1.append(numbers[i])
            list2.append(numbers[i + 1])
    return list1, list2

def calculate_differences(list1, list2):
    sum_of_differences = 0
    for i in range(len(list1)):
        sum_of_differences += abs(list1[i] - list2[i])
    print(f"The sum of differences is {sum_of_differences}")

def calculate_similarity(list1, list2):
    similarity_score = 0
    for number in list1:
        occurences_in_list2 = list2.count(number)
        similarity_score += number * occurences_in_list2
    print(f"The similarity score is {similarity_score}")

def main(input, calc_diff, calc_sim) -> None:
    list1, list2 = get_lists_from_file(input)
    list1.sort()
    list2.sort()
    if len(list1) != len(list2):
        print("Lists are not the same length")
        return
    if calc_diff:
        calculate_differences(list1, list2)
    if  calc_sim:
        calculate_similarity(list1, list2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 1")
    parser.add_argument("--input", type=str, help="Path to input file")
    parser.add_argument("--calc_diff", action='store_true', help="Calculate differences between two lists")
    parser.add_argument("--calc_sim", action='store_true', help="Calculate differences between two lists")
    args = parser.parse_args()
    main(args.input, args.calc_diff, args.calc_sim )
