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

def count_reachable_nines(topographic_map, start_row, start_col):
    """Performs a BFS from the start position to count the number of reachable 9's."""
    rows, cols = len(topographic_map), len(topographic_map[0])
    positions_to_explore = deque([(start_row, start_col)])
    explored_positions = set([(start_row, start_col)])
    reachable_nine_count = 0

    while positions_to_explore:
        row, col = positions_to_explore.popleft()

        if topographic_map[row][col] == 9:
            reachable_nine_count += 1

        # Explore the neighbors (up, down, left, right)
        for dr, dc in DIRECTIONS:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in explored_positions:
                if topographic_map[new_row][new_col] == topographic_map[row][col] + 1:  # Only allow valid uphill moves
                    explored_positions.add((new_row, new_col))
                    positions_to_explore.append((new_row, new_col))

    return reachable_nine_count

def calculate_total_trailhead_score(topographic_map):
    """Calculates the total score by summing the reachable 9's from each trailhead."""
    rows, cols = len(topographic_map), len(topographic_map[0])
    total_score = 0

    for row in range(rows):
        for col in range(cols):
            if topographic_map[row][col] == 0:
                score = count_reachable_nines(topographic_map, row, col)
                total_score += score

    return total_score


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

topographic_map = parse_topographic_map(file_path)
result = calculate_total_trailhead_score(topographic_map)

print("Part1:", result)