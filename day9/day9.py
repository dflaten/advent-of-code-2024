#!/usr/bin/env python
import argparse
from typing import Union

INPUT = "small-input.txt"

def build_disk_file_from_memory(path_to_file: str) -> list[Union[str, int]]:
    '''
    Retrive the memory file and build the array of memory.
    '''
    memory_array = []
    items_index = 0
    with open(path_to_file, 'r') as file:
        line = file.readlines()
        if len(line) > 1:
            raise ValueError("File should only have one line.")
        for i, number in enumerate(line[0].strip()):
           # if i odd add a number of . to the memory array equal to the number
           # if i even add a number of items_index to the memory array equal to the number
           # increment items_index
           number = int(number)
           if i == 0:
               for j in range(number):
                   memory_array.append(0)
               items_index += 1
           elif i % 2 == 1:
               for j in range(number):
                   memory_array.append('.')
           elif i % 2 == 0:
               for j in range(number):
                   memory_array.append(items_index)
               items_index += 1
    return memory_array

def defrag_disk_file(disk_memory: list[Union[str, int]]) -> list[Union[str, int]]:
    defraged_disk_memory = disk_memory.copy()
    end_pointer = len(defraged_disk_memory) - 1
    start_pointer = 0
    print(start_pointer)
    print(end_pointer)
    while(start_pointer < end_pointer):
        if defraged_disk_memory[start_pointer] != '.':
            start_pointer += 1
            continue
        if defraged_disk_memory[end_pointer] == '.':
            end_pointer -= 1
            continue
        if defraged_disk_memory[start_pointer] == '.':
            defraged_disk_memory[start_pointer] = defraged_disk_memory[end_pointer]
            defraged_disk_memory[end_pointer] = '.'
            end_pointer -= 1
            start_pointer += 1
            continue
        start_pointer += 1
    return defraged_disk_memory

def find_current_block_of_blank_space(disk_memory: list[Union[str, int]], start_pointer: int) -> int:
    block_of_blank_space = 0
    for i in range(start_pointer, len(disk_memory)):
        if disk_memory[i] == '.':
            block_of_blank_space += 1
        else:
            return block_of_blank_space
    return block_of_blank_space

def find_current_file_block(disk_memory: list[Union[str, int]], end_pointer: int) -> int:
    file_block = 0
    type = disk_memory[end_pointer]
    for i in range(end_pointer, 0, -1):
        if disk_memory[i] != type:
            file_block += 1
        else:
            return file_block
    return file_block

def defrag_disk_whole_files(disk_memory: list[Union[str, int]]) -> list[Union[str, int]]:
    defraged_disk_memory = disk_memory.copy()
    end_pointer = len(defraged_disk_memory) - 1
    start_pointer = 0
    print(start_pointer)
    print(end_pointer)
    while(start_pointer < end_pointer):
        block_of_blank_space = find_current_block_of_blank_space(defraged_disk_memory, start_pointer)
        file_block = find_current_file_block(defraged_disk_memory, end_pointer)
        # Here is where I had to stop.
        print(f"blank space: {disk_memory[start_pointer]")
        if defraged_disk_memory[start_pointer] != '.':
            start_pointer += 1
            continue
        if defraged_disk_memory[end_pointer] == '.':
            end_pointer -= 1
            continue
        if defraged_disk_memory[start_pointer] == '.':
            defraged_disk_memory[start_pointer] = defraged_disk_memory[end_pointer]
            defraged_disk_memory[end_pointer] = '.'
            end_pointer -= 1
            start_pointer += 1
            continue
        start_pointer += 1
    return defraged_disk_memory


def calculate_checksum(disk_memory: list[Union[str, int]]) -> int:
    checksum = 0
    for i, item in enumerate(disk_memory):
        if type(item) == str:
            continue
        checksum += i * item
    return checksum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 5")
    parser.add_argument("--defrag", action='store_true', help="Defrag the file at INPUT.")
    parser.add_argument("--defrag_whole_file", action='store_true', help="Defrag the file at INPUT.")
    args = parser.parse_args()
    disk_memory = build_disk_file_from_memory(INPUT)
    if args.defrag:
        defraged = defrag_disk_file(disk_memory)
        result = calculate_checksum(defraged)
        print(f"Checksum is {result}")
