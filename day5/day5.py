#!/usr/bin/env python
import argparse
from functools import cmp_to_key

RULES_FILE_PATH = "rules.txt"
PAGES_TO_PRODUCE_FILE_PATH = "pages_to_produce.txt"

def retrieve_rules(path_to_file: str) -> list[tuple[int, int]]:
    '''
    Retrieves the rules from the file path.
    '''
    rules = []
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            val1, val2 = line.split('|')
            rules.append((int(val1), int(val2)))
    return rules

def rules_map(rules: list[tuple[int, int]]) -> dict[int, list[int]]:
    rules_map = {}
    for rule in rules:
        if rule[0] in rules_map:
            rules_map[rule[0]].append(rule[1])
        else:
            rules_map[rule[0]] = [rule[1]]
    return rules_map

def retrieve_pages_to_produce(path_to_file: str) -> list[list[int]]:
    '''
    Retrieves the pages to produce from the file path.
    '''
    list_of_sections = []
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            pages_section = []
            for val in line.split(','):
               pages_section.append(int(val))
            list_of_sections.append(pages_section)
    return list_of_sections

def sum_middle_elements(sections: list[list[int]]) -> int:
    sum = 0
    print(f"Number of valid sections: {len(sections)}")
    for section in sections:
        # Assuming there is always and odd number of elements.
        sum += section[int(len(section)/2)]
    return sum

def is_valid_section(section: list[int], rules: dict[int, list[int]]) -> bool:
    for i in range(len(section) - 1):
        # First two if statements are for the case where the last element in the section is not in the rules.
        # and is it is either the last element in the section or it is an invalid section.
        if section[i] not in rules and i == len(section)-1:
            return True
        if section[i] not in rules:
            return False
        if section[i+1] not in rules[section[i]]:
            return False
    return True

def find_valid_page_ordering(rules, pages_to_produce):
    vald_sections = []
    for section in pages_to_produce:
        if is_valid_section(section, rules):
            vald_sections.append(section)
    return sum_middle_elements(vald_sections)

def sort_by_rules(rules, update):
    return sorted(update, key=cmp_to_key(lambda x, y: -1 if (x,y) in rules else 1))

def fix_incorrectly_ordered_sections(rules, rules_map, pages_to_produce):
    invalid_sections = []
    fixed_sections = []
    for section in pages_to_produce:
        if not is_valid_section(section, rules_map):
            invalid_sections.append(section)
    for invalid_section in invalid_sections:
        fixed_sections.append(sort_by_rules(rules, invalid_section))
    return sum_middle_elements(fixed_sections)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 5")
    parser.add_argument("--find_valid_page_ordering", action='store_true', help="Find all the valid page orderings in the pages to produce file that follow the rules in the rule file.")
    parser.add_argument("--fix_incorrectly_ordered_sections", action='store_true', help="Make all the invalid page orderings ordered by reording as needed.")
    args = parser.parse_args()
    rules = retrieve_rules(RULES_FILE_PATH)
    rules_map = rules_map(rules)
    pages_to_produce = retrieve_pages_to_produce(PAGES_TO_PRODUCE_FILE_PATH)
    if args.find_valid_page_ordering:
        result = find_valid_page_ordering(rules_map, pages_to_produce)
        print(f"Result of adding all middle elements in the valid page ordering is {result}")
    if args.fix_incorrectly_ordered_sections:
        result = fix_incorrectly_ordered_sections(rules, rules_map, pages_to_produce)
        print(f"Result of adding all middle elements in the fixed page ordering is {result}")
