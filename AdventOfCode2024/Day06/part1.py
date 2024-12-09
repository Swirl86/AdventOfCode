"""
https://adventofcode.com/2024/day/6
Advent of Code 2024 Day 6: Guard Gallivant
"""
import os

GUARD = '^'
WALL = '#'
OPEN = '.'
DIRECTIONS = {
    '^': (0, -1),  # Up
    '>': (1, 0),   # Right
    'v': (0, 1),   # Down
    '<': (-1, 0),  # Left
}
ROTATIONS = {
    '^': '>',   # Up turns right
    '>': 'v',   # Right turns down
    'v': '<',   # Down turns left
    '<': '^',   # Left turns up
}

def read_file(file_path):
    grid = []
    with open(file_path) as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid

def find_guard_position(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == GUARD:
                return x, y
    return None

def navigate_guard(grid):
    '''
    Rules:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.
    '''
    start_x, start_y = find_guard_position(grid)

    if start_x is None:
        print("Guard not found in grid!")
        return

    x, y = start_x, start_y
    direction = GUARD
    visited_positions = set()
    visited_positions.add((x, y))

    while True:
        dx, dy = DIRECTIONS[direction]
        new_x, new_y = x + dx, y + dy

        if new_x < 0 or new_y < 0 or new_y >= len(grid) or new_x >= len(grid[0]):
            #print(f"Guard moved out of bounds at ({new_x}, {new_y}).")
            break

        if grid[new_y][new_x] == WALL:
            #print(f"Guard hit an obstacle (#) at ({new_x}, {new_y}).")
             direction = ROTATIONS[direction]  # Rotate direction if a wall is hit
        else:
            x, y = new_x, new_y
            visited_positions.add((x, y))
            #print(f"Guard moved to ({x}, {y}) facing {direction}.")

    return len(visited_positions)

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid = read_file(file_path)
result = navigate_guard(grid)


print("Part1 Total unique positions:", result)