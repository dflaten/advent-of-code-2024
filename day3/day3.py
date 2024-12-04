

#!/usr/bin/env python
import argparse
import re

def retrieve_string_from_path(path_to_file: str) -> str:
    '''
    Retrieves string from the file at the path, should get all lines in the file
    and combine them into a single string.
    '''
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        # combine all lines into a single string and use \n to separate them
        return "".join(lines)
        import re

DONT_DO_PATTERN = re.compile(r"don't\(\).*?(?:do\(\)|$)", re.DOTALL)

def remove_dont_substrings(text: str) -> str:
    """
    Removes text between "don't()" and "do()" pairs, and any trailing "don't()" content.
    param: text - string to remove don't/dos from
    returns: String with all don't/do blocks removed
    """
    prev_text = None
    current_text = text

    # Keep replacing until no more matches are found
    while prev_text != current_text:
        prev_text = current_text
        current_text = DONT_DO_PATTERN.sub('', current_text)

    return current_text

# See below for some approaches that didn't work.'
# def remove_dont_substrings(text: str) -> str:
#     # Pattern explanation:
#     # don't\(\)    - matches literal "don't()"
#     # .*?          - matches any characters (non-greedy)
#     # do\(\)       - matches literal "do()"
#     pattern = r"don't\(\).*?do\(\)"
#     # Special chars removed
#     #pattern = r"don't\(\)[^\S\r\n\x00-\x1F\x7F-\x9F]*?do\(\)"
#     string_with_dont_do_removed = re.sub(pattern, '', text)

#     # find the last "don't()" and remove it and everything after it
#     return re.sub(r"don't\(\).*$", "", string_with_dont_do_removed)

def find_execute_multiply_statements_expanded(string_to_parse: str) -> int:
    #74838033 is the correct answer
    string_with_dont_to_do_statements_removed = remove_dont_substrings(string_to_parse)
    multiply_statements = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", string_with_dont_to_do_statements_removed)
    pairs_to_multiply = []
    for statement in multiply_statements:
        pairs_to_multiply.append((int(statement[0]), int(statement[1])))
    total = 0
    for pair in pairs_to_multiply:
        total += pair[0] * pair[1]

    return total

def find_execute_multiply_statements(string_to_parse: str) -> int:
    # 170807108 is the correct answer
    pairs_to_multiply = []
    multiply_statements = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", string_to_parse)
    for statement in multiply_statements:
        pairs_to_multiply.append((int(statement[0]), int(statement[1])))
    print(pairs_to_multiply)
    total = 0
    for pair in pairs_to_multiply:
        total += pair[0] * pair[1]

    return total



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 3")
    parser.add_argument("--input", type=str, help="Path to input file.")
    parser.add_argument("--find_and_multiply", action='store_true', help="Find all the multiply statements in the text, calculate and sum them then return the result.")
    parser.add_argument("--find_and_multiply_expanded", action='store_true', help="Find all the multiply statements in the text, and sum, obey the dos and don'ts, then return the result.")
    args = parser.parse_args()
    string_to_parse = retrieve_string_from_path(args.input)
    if args.find_and_multiply:
        result = find_execute_multiply_statements(string_to_parse)
        print(f"Result of all the multiply statements is {result}")
    if args.find_and_multiply_expanded:
        # 110824057 is too large still
        # 94286334 is still too large (after adding the remove at the end of the string)
        result = find_execute_multiply_statements_expanded(string_to_parse)
        print(f"Result of all the multiply statements with expanded criteria is {result}")
