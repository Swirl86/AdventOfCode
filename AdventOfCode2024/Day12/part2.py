"""
https://adventofcode.com/2024/day/12
Advent of Code 2024 Day 12: Garden Groups
"""
import os
from collections import defaultdict

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def read_file(file_path):
    """Reads the file and returns a 2D list of grid values."""
    garden_grid = []
    with open(file_path) as file:
        file_content = file.read()
        for row in file_content.splitlines():
            garden_grid.append(list(row))
    return garden_grid

def initialize_visited(num_rows, num_cols):
    """Initializes a 2D matrix to track visited cells."""
    return [[False] * num_cols for _ in range(num_rows)]

def depth_first_search(start_x, start_y, plant_type, grid, visited, num_rows, num_cols, region_matrix, region_id):
    """DFS to mark all connected cells of the same plant type with a region ID."""
    stack = [(start_x, start_y)]
    visited[start_y][start_x] = True
    region_matrix[start_y][start_x] = region_id

    while stack:
        current_x, current_y = stack.pop()
        # Explore adjacent cells
        for dx, dy in DIRECTIONS:
            neighbor_x, neighbor_y = current_x + dx, current_y + dy
            if (
                0 <= neighbor_x < num_cols and 0 <= neighbor_y < num_rows and  # Within bounds
                not visited[neighbor_y][neighbor_x] and  # Not yet visited
                grid[neighbor_y][neighbor_x] == plant_type  # Same plant type
            ):
                stack.append((neighbor_x, neighbor_y))
                visited[neighbor_y][neighbor_x] = True
                region_matrix[neighbor_y][neighbor_x] = region_id

def get_region_id(x, y, region_matrix, num_rows, num_cols):
    """Helper function to safely access the region ID matrix."""
    if 0 <= x < num_cols and 0 <= y < num_rows:
        return region_matrix[y][x]
    return -1

def calculate_area_and_corners(grid):
    """Calculates the area and corners for each plant region."""
    num_rows = len(grid)
    num_cols = len(grid[0])
    visited = initialize_visited(num_rows, num_cols)
    region_matrix = [[-1] * num_cols for _ in range(num_rows)]
    region_id = 0

    region_areas = defaultdict(int)
    region_corners = defaultdict(int)

    # Mark regions using DFS
    for y in range(num_rows):
        for x in range(num_cols):
            if not visited[y][x]:
                depth_first_search(x, y, grid[y][x], grid, visited, num_rows, num_cols, region_matrix, region_id)
                region_id += 1

    # Calculate area and corner count for each region
    for y in range(num_rows):
        for x in range(num_cols):
            current_region_id = region_matrix[y][x]
            region_areas[current_region_id] += 1

            # Count corners using diagonal neighbors
            for dx, dy in DIAGONAL_DIRECTIONS:
                a = get_region_id(x, y, region_matrix, num_rows, num_cols)
                b = get_region_id(x + dx, y, region_matrix, num_rows, num_cols)
                c = get_region_id(x, y + dy, region_matrix, num_rows, num_cols)
                d = get_region_id(x + dx, y + dy, region_matrix, num_rows, num_cols)

                # Corner conditions
                if (a != b and a != c) or (a == b and a == c and a != d):
                    region_corners[current_region_id] += 1

    return region_areas, region_corners

def calculate_total_price(area, corners):
    """Calculates the total price by multiplying the area by the corners for each region."""
    return sum(area[x] * corners[x] for x in area)

def print_results(area, corners, total_price):
    for region_id in area:
        print(f"Region {region_id}: Area = {area[region_id]}, Corners = {corners[region_id]}, Price = {area[region_id] * corners[region_id]}")
    print("Total Price:", total_price)

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

grid = read_file(file_path)
area, corners = calculate_area_and_corners(grid)
total_price = calculate_total_price(area, corners)

print("Part2:", total_price)