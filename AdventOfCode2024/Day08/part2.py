"""
https://adventofcode.com/2024/day/8
Advent of Code 2024 Day 8: Resonant Collinearity
"""
import os
from collections import defaultdict
from itertools import permutations

def read_file(file_path):
    """Reads the file and returns a dictionary of grid coordinates and values."""
    coordinates_map = {}
    with open(file_path) as file:
        file_content = file.read()
        for i, row in enumerate(file_content.splitlines()):
            for j, cell_value in enumerate(row):
                coordinates_map[(i, j)] = cell_value
    return coordinates_map

def locate_antenna_positions(coordinates_map):
    """Finds the positions of antennas in the grid."""
    antenna_positions_by_type = defaultdict(list)
    for coord, cell_value in coordinates_map.items():
        if cell_value != '.':
            antenna_positions_by_type[cell_value].append(coord)
    return antenna_positions_by_type

def check_antinode_harmonics(antenna_1, antenna_2, coordinates_map):
    """Calculates all antinode harmonic positions between two antennas based on their relative positions."""
    antinode_harmonics_positions = set()

    delta_x = antenna_1[0] - antenna_2[0]
    delta_y = antenna_1[1] - antenna_2[1]

    i = 1
    while True:
        position_1 = (i * delta_x + antenna_1[0], i * delta_y + antenna_1[1])
        if position_1 not in coordinates_map:
            break
        antinode_harmonics_positions.add(position_1)
        i += 1

    j = 1
    while True:
        position_2 = (j * delta_x + antenna_1[0], j * delta_y + antenna_1[1])
        if position_2 not in coordinates_map:
            break
        antinode_harmonics_positions.add(position_2)
        j += 1

    return antinode_harmonics_positions | {antenna_1, antenna_2}

def find_antinodes(antenna_positions_by_type, coordinates_map):
    """Finds all unique antinode harmonic positions by iterating over all pairs of antennas
    of the same type and calculating the harmonic antinode positions between them. """
    antinodes_harmonics = set()

    for _, positions in antenna_positions_by_type.items():
        for antenna_1, antenna_2 in permutations(positions, 2):
            antinodes_harmonics |= check_antinode_harmonics(antenna_1, antenna_2, coordinates_map)

    return antinodes_harmonics

def count_unique_antinodes(coordinates_map):
    antenna_positions_by_type = locate_antenna_positions(coordinates_map)
    antinodes = find_antinodes(antenna_positions_by_type, coordinates_map)

    return len(antinodes)

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid  = read_file(file_path)
result = count_unique_antinodes(grid)

print("Part2", result)
