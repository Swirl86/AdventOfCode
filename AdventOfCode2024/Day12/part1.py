"""
https://adventofcode.com/2024/day/12
Advent of Code 2024 Day 12: Garden Groups
"""
import os

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def read_file(file_path):
    """Reads the file and returns a 2D list of grid values."""
    garden_grid = []
    with open(file_path) as file:
        file_content = file.read()
        for row in file_content.splitlines():
            garden_grid.append(list(row))
    return garden_grid

def initialize_visited(rows, cols):
    """Initializes a visited matrix with False values."""
    return [[False] * cols for _ in range(rows)]

def calculate_perimeter(x, y, plant_type, grid, rows, cols):
    """Calculates the perimeter of a single garden plot (x, y)."""
    # Start with a full perimeter of 4 (because each plot has 4 sides)
    cell_perimeter = 4

    # Check each of the four possible directions (up, down, left, right)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy

        # Check if the neighbor is within bounds
        if 0 <= nx < rows and 0 <= ny < cols:
            # If the neighboring cell has the same plant type, it's not contributing to the perimeter
            if grid[nx][ny] == plant_type:
                cell_perimeter -= 1
    return cell_perimeter

def dfs(x, y, plant_type, grid, visited, rows, cols):
    """Performs DFS to explore the region and calculate the area and perimeter."""
    stack = [(x, y)]
    area = 0
    perimeter = 0
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        area += 1
        perimeter += calculate_perimeter(cx, cy, plant_type, grid, rows, cols)

        # Explore adjacent plots in the region
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == plant_type:
                stack.append((nx, ny))
                visited[nx][ny] = True

    return area, perimeter

def calculate_area_and_perimeter(grid):
    """Calculates the area and perimeter of each region of plants and computes the total price."""
    rows = len(grid)
    cols = len(grid[0])
    visited = initialize_visited(rows, cols)
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = grid[i][j]
                area, perimeter = dfs(i, j, plant_type, grid, visited, rows, cols)
                region_price = area * perimeter
                total_price += region_price

    return total_price

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

grid = read_file(file_path)
total_price  = calculate_area_and_perimeter(grid)

print("Part1:", total_price)