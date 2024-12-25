
#!/usr/bin/env python
import argparse
import numpy as np
import heapq
from typing import Optional

INPUT = "small-input.txt"

directions = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1), # left
    (-1, 0)  # up
]

def parse_locks_and_keys(path_to_file: str) -> tuple[list[np.ndarray], list[np.ndarray]]:
    '''
    Converts the input file to two lists of numpy arrays. One for locks and one for keys.

    Each possible Lock or key is a series of characters seperated by a newline.
    '''
    locks = []
    keys = []
    locks_and_keys = None
    with open(path_to_file, 'r') as file:
        locks_and_keys = file.read().strip().split('\n\n')

    for item in locks_and_keys:
        # if first row is all '#' then we have a lock, if not it is a key.
        if item[0][0] == '#':
            lock = np.array([list(row) for row in item.split('\n')])
            # remove the first row of the lock
            lock = lock[1:]
            locks.append(lock)
        if item[0][0] == '.':
            key = np.array([list(row) for row in item.split('\n')])
            # remove last row of the key
            key = key[:-1]
            keys.append(key)
    return locks, keys

def find_key_lock_combos(locks: list[np.ndarray], keys: list[np.ndarray]) -> int:
    '''
    Find how many unique lock/key pairs "fit".
    To fit a key must have a smaller number or less "#" in each column than the lock.
    '''
    for lock in locks:
        for key in keys:
            if lock.shape == key.shape:
                print(f"Lock: {lock}")
                print(f"Key: {key}")
                print()
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 25 of Advent of Code 2024")
    parser.add_argument("--find_key_lock_combos", action='store_true',
                       help="Find the locks and keys that are possible matches.")
    args = parser.parse_args()

    if args.find_key_lock_combos:
        locks, keys= parse_locks_and_keys(INPUT)
