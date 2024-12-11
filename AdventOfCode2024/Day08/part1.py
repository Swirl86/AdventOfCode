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

def check_antinode_pairs(antenna_1, antenna_2, coordinates_map):
    """Calculates antinodes between two antennas based on their relative positions."""
    antinode_positions = set()

    delta_x = antenna_1[0] - antenna_2[0]
    delta_y = antenna_1[1] - antenna_2[1]

    # Calculate two possible antinode positions
    antinode_position_1 = (antenna_1[0] - 2 * delta_x, antenna_1[1] - 2 * delta_y)
    antinode_position_2 = (antenna_2[0] + 2 * delta_x, antenna_2[1] + 2 * delta_y)

    if antinode_position_1 in coordinates_map:
        antinode_positions.add(antinode_position_1)
    if antinode_position_2 in coordinates_map:
        antinode_positions.add(antinode_position_2)

    # Return antinodes that are not the original antenna positions
    return antinode_positions - set((antenna_1, antenna_2))

def find_antinodes(antenna_positions_by_type, coordinates_map):
    """Finds all unique antinode positions from the antenna positions."""
    all_antinodes = set()

    for _, positions in antenna_positions_by_type.items():
        for antenna_1, antenna_2 in permutations(positions, 2):
            all_antinodes |= check_antinode_pairs(antenna_1, antenna_2, coordinates_map) # '|=' is a short form for "union" and is used to update a set with the elements from another set

    return all_antinodes

def count_unique_antinodes(coordinates_map):
    antenna_positions_by_type = locate_antenna_positions(coordinates_map)
    antinodes = find_antinodes(antenna_positions_by_type, coordinates_map)

    return len(antinodes)

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid  = read_file(file_path)
result = count_unique_antinodes(grid)

print("Part1", result)
