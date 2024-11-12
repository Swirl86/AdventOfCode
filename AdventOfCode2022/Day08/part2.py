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

def calculate_view_distance(grid, row, col, dr, dc):
    """
    Check visibility in a given direction (dr, dc).
    A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
    """
    current_height = grid[row][col]
    r, c = row + dr, col + dc
    distance = 0
    while 0 <= r < len(grid) and 0 <= c < len(grid[row]):
        distance += 1
        if grid[r][c] >= current_height:
            break
        r, c = r + dr, c + dc
    return distance

def calculate_scenic_score(grid, row, col):
    """Calculate the scenic score for a given tree at (row, col)."""
    up = calculate_view_distance(grid, row, col, -1, 0)
    down = calculate_view_distance(grid, row, col, 1, 0)
    left = calculate_view_distance(grid, row, col, 0, -1)
    right = calculate_view_distance(grid, row, col, 0, 1)

    return up * down * left * right

def find_highest_scenic_score(grid):
    """
    A tree's scenic score is found by multiplying together its viewing distance
    in each of the four directions.
    """
    max_scenic_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            scenic_score = calculate_scenic_score(grid, row, col)
            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid = parse_input(file_path)
#print_grid(grid)
print("Part2:", find_highest_scenic_score(grid))