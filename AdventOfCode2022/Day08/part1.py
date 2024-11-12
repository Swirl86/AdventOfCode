"""
https://adventofcode.com/2022/day/8
Advent of Code 2022 Day 8: Treetop Tree House
"""
import os


def parse_input(file_path):
    grid = []
    with open(file_path) as f:
        grid = [list(map(int, line.strip())) for line in f]
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def is_visible_in_direction(grid, row, col, dr, dc):
    """
    Check visibility in a given direction (dr, dc).
    A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
    """
    current_height = grid[row][col]
    r, c = row + dr, col + dc
    while 0 <= r < len(grid) and 0 <= c < len(grid[row]):
        if grid[r][c] >= current_height:
            return False
        r, c = r + dr, c + dc
    return True

def check_visible_trees(grid):
    visible_trees = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (is_visible_in_direction(grid, row, col, 0, -1) or  # Left
                is_visible_in_direction(grid, row, col, 0, 1) or   # Right
                is_visible_in_direction(grid, row, col, -1, 0) or  # Up
                is_visible_in_direction(grid, row, col, 1, 0)):    # Down
                visible_trees += 1
    print("Part1:",visible_trees)


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid = parse_input(file_path)
#print_grid(grid)
check_visible_trees(grid)