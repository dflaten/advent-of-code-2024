#!/usr/bin/env python
import argparse
from collections import defaultdict
import networkx as nx

INPUT = "small-input.txt"

def parse_computer_connections_from_file(path_to_file: str) -> list[tuple[str, str]]:
    '''
    Parse the comptuer connections from the file
    '''
    computer_connections: list[tuple[str, str]] = []
    with open(path_to_file, 'r') as file:
        for line in file:
            pair_of_computers = line.strip().split("-")
            computer_connections.append((pair_of_computers[0], pair_of_computers[1]))
    return computer_connections

def find_sets_of_computer_connections(computer_connections: list[tuple[str, str]]) -> list[list[tuple[str, str]]]:
    '''
    Find all the sets of 3 computer connections in which each computer is connected to
    the others.

    Essentially we have a list of edges and we need to find all the triangles.
    '''
    # Create an undirected graph
    G = nx.Graph()
    G.add_edges_from(computer_connections)

    triangles = []
    # Check all possible combinations of 3 vertices
    for vertice_1 in G.nodes():
        for vertice_2 in G.neighbors(vertice_1):
            for vertice_3 in G.neighbors(vertice_2):
                # Make sure v3 is connected back to v1 to form a triangle
                if G.has_edge(vertice_3, vertice_1) and vertice_1 < vertice_2 < vertice_3:
                    triangles.append([vertice_1, vertice_2, vertice_3])

    return triangles



def find_sets_with_t(computer_connections: list[tuple[str, str]]) -> int:
    '''
    Find all the computer sets with at least one t in them.
    '''
    sets_of_computer_connections = find_sets_of_computer_connections(computer_connections)
    for set in sets_of_computer_connections:
        print(set)
    return 0



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 23")
    parser.add_argument("--find_sets_with_t", action='store_true', help="Find all the computer connections with at least one t in them.")
    args = parser.parse_args()
    computer_connections = parse_computer_connections_from_file(INPUT)
    if args.find_sets_with_t:
        result = find_sets_with_t(computer_connections)
        #print(f"Total number of computer sets with 't' is {result}")
