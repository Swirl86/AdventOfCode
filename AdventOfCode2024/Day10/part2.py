"""
https://adventofcode.com/2024/day/10
Advent of Code 2024 Day 10: Hoof It
"""
from collections import deque
import os

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def parse_topographic_map(file_path):
    """Parses the file and returns a grid (topographic map), converting characters to integers."""
    topographic_map = []
    with open(file_path) as f:
        topographic_map = [list(map(int, line.strip())) for line in f.readlines()]
    return topographic_map

def find_trailheads(topographic_map):
    """Find all trailheads (positions with height 0)."""
    trailheads = []
    for row_index in range(len(topographic_map)):
        for col_index in range(len(topographic_map[0])):
            if topographic_map[row_index][col_index] == 0:
                trailheads.append((row_index, col_index))  # Store trailhead positions
    return trailheads

def get_neighbors(row, col, topographic_map):
    """Return the valid neighbors (up, down, left, right) for the position."""
    neighbors = []
    for row_offset, col_offset in DIRECTIONS:
        new_row, new_col = row + row_offset, col + col_offset
        if 0 <= new_row < len(topographic_map) and 0 <= new_col < len(topographic_map[0]):
            neighbors.append((new_row, new_col))
    return neighbors

def count_paths(row, col, current_height, topographic_map, memo):
    """Recursively counts all distinct paths from the current position using DFS."""
    # Check if the result is already calculated to avoid recalculating
    if (row, col, current_height) in memo:
        return memo[(row, col, current_height)]

    # If we reached the peak (height 9), we count this path as valid
    if topographic_map[row][col] == 9:
        return 1

    total_paths = 0

    # Explore neighboring positions to find valid paths (DFS)
    for neighbor_row, neighbor_col in get_neighbors(row, col, topographic_map):
        neighbor_height = topographic_map[neighbor_row][neighbor_col]
        if neighbor_height == current_height + 1:
            total_paths += count_paths(neighbor_row, neighbor_col, neighbor_height, topographic_map, memo)

    # Memoize the result to avoid redundant calculations
    memo[(row, col, current_height)] = total_paths
    return total_paths

def calculate_total_trailhead_rating(topographic_map):
    """Calculates the total trailhead rating by summing the number of distinct trails for each trailhead."""
    total_rating = 0
    trailheads = find_trailheads(topographic_map)
    memo = {}  # Memoization dictionary to store already computed paths

    for start_row, start_col in trailheads:
        total_rating += count_paths(start_row, start_col, 0, topographic_map, memo)  # Start from height 0

    return total_rating

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

topographic_map = parse_topographic_map(file_path)
result = calculate_total_trailhead_rating(topographic_map)
print("Part2:", result)