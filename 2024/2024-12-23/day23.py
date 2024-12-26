#!/usr/bin/env python
import argparse
import networkx as nx

INPUT = "input.txt"


def parse_computer_connections_from_file(path_to_file: str) -> list[tuple[str, str]]:
    """
    Parse the comptuer connections from the file
    """
    computer_connections: list[tuple[str, str]] = []
    with open(path_to_file, "r") as file:
        for line in file:
            pair_of_computers = line.strip().split("-")
            computer_connections.append((pair_of_computers[0], pair_of_computers[1]))
    return computer_connections


def find_sets_of_computer_connections(
    computer_connections: list[tuple[str, str]],
) -> set[tuple[str, str, str]]:
    """
    Find all the sets of 3 computer connections in which each computer is connected to
    the others.

    Essentially we have a list of edges and we need to find all the triangles.

    A triangle is made up of 3 vertices.

    """
    G = nx.Graph()
    G.add_edges_from(computer_connections)

    # Find all triangles and store them in a set using frozenset for uniqueness
    triangles_set = set()
    for triangle in nx.enumerate_all_cliques(G):
        if len(triangle) == 3:  # We only want triangles (3-cliques)
            triangles_set.add(frozenset(sorted(triangle)))
    return triangles_set


def find_a_set_with_t(set_of_computer_connections: tuple[str, str, str]) -> int:
    for computer_connection in set_of_computer_connections:
        # if any of the computers START with t
        if "t" == computer_connection[0]:
            return 1
    return 0


def find_sets_with_t(computer_connections: list[tuple[str, str]]) -> int:
    """
    Find all the computer sets with at least one t in them.
    """
    sets_of_computer_connections = find_sets_of_computer_connections(
        computer_connections
    )
    number_of_sets_with_t = 0
    for set in sets_of_computer_connections:
        number_of_sets_with_t += find_a_set_with_t(set)
    return number_of_sets_with_t


def find_largest_set(computer_connections: list[tuple[str, str]]) -> str:
    G = nx.Graph()
    G.add_edges_from(computer_connections)

    largest_set = set()
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) > len(largest_set):
            largest_set = clique
    return ",".join(sorted(largest_set))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 23")
    parser.add_argument(
        "--find_sets_with_t",
        action="store_true",
        help="Find all the computer connections with at least one t in them.",
    )
    parser.add_argument(
        "--find_largest_set", action="store_true", help="Find largest set of computers."
    )
    args = parser.parse_args()
    computer_connections = parse_computer_connections_from_file(INPUT)
    if args.find_sets_with_t:
        result = find_sets_with_t(computer_connections)
        print(f"Total number of computer sets with 't' is {result}")
    if args.find_largest_set:
        result = find_largest_set(computer_connections)
        print(f"Largest set of computer connections is {result}")
