#!/usr/bin/env python
import argparse
import copy

VARIANCE_UPPER_LIMIT = 4
VARIANCE_LOWER_LIMIT = 0

def get_reports_from_file(input):
    reports = []
    with open(input, 'r') as file:
        for line in file:
            report =[int(num) for num in line.split()]
            reports.append(report)
    return reports

def is_within_variance_in_limit(num1: int, num2:int):
    variance = abs(num1 - num2)
    return variance < VARIANCE_UPPER_LIMIT and variance > VARIANCE_LOWER_LIMIT

def removing_one_item_makes_report_safe(index1: int, index2:int, report: list[int]):
    first_item_removed = copy.deepcopy(report)
    del first_item_removed[index1]
    second_item_removed = copy.deepcopy(report)
    del second_item_removed[index2]
    initial_item_removed = copy.deepcopy(report)
    del initial_item_removed[0]
    if report_is_safe(first_item_removed) or report_is_safe(second_item_removed) or report_is_safe(initial_item_removed):
        return True
    return False


def report_is_safe(report: list[int], can_remove_item=False) -> bool:
    '''
    A report is considered safe if it is either increasing or decreasing by 1
    and the variance between each pair of numbers is less than 4.

    param report: list[int] - a list of integers
    param can_remove_item: bool - a flag to determine if a removal of an item can be attempted
    Note: this function contains a lot of duplicate code but was my first pass focused on getting some thing working.
    '''
    is_decreasing = report[0] > report[1]
    if is_decreasing:
        for i in range(len(report) - 1):
            pair_decreasing = report[i] > report[i + 1]
            if not pair_decreasing:
                if can_remove_item:
                    return removing_one_item_makes_report_safe(i, i+1, report)
                return False
            if not is_within_variance_in_limit(report[i], report[i + 1]):
                if can_remove_item:
                    return removing_one_item_makes_report_safe(i, i+1, report)
                return False
        return True
    if not is_decreasing:
        for i in range(len(report) - 1):
            pair_increasing = report[i] < report[i + 1]
            if not pair_increasing:
                if can_remove_item:
                    return removing_one_item_makes_report_safe(i, i+1, report)
                return False
            if not is_within_variance_in_limit(report[i], report[i + 1]):
                if can_remove_item:
                    return removing_one_item_makes_report_safe(i, i+1, report)
                return False
        return True
    return False

def count_safe_reports(input, detect_variance, detect_variance_single_element_removed=False) -> int:
    reports = get_reports_from_file(input)
    if detect_variance:
        total_valid_reports = 0
        for report in reports:
            if report_is_safe(report):
                total_valid_reports += 1
        print(f"Total valid reports is {total_valid_reports}")
        return total_valid_reports
    if detect_variance_single_element_removed:
        total_valid_reports = 0
        for report in reports:
            if report_is_safe(report, detect_variance_single_element_removed):
                total_valid_reports += 1
        print(f"Total valid reports after removing an item is {total_valid_reports}")
        return total_valid_reports
    return -1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 2")
    parser.add_argument("--input", type=str, help="Path to input file.")
    parser.add_argument("--detect_variance", action='store_true', help="Calculate the number of safe reports in the file.")
    parser.add_argument("--detect_variance_single_element_removed")
    args = parser.parse_args()
    count_safe_reports(args.input, args.detect_variance, args.detect_variance_single_element_removed)
