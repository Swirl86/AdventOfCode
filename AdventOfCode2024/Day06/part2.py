"""
https://adventofcode.com/2024/day/6
Advent of Code 2024 Day 6: Guard Gallivant
"""
import os

WALL = "#"

def read_file(file_path):
    '''
    Reads a file and converts it into a grid representation using complex numbers as keys.

    Each row and column in the file is mapped to a position in a 2D grid,
    where the position is represented as a complex number. For example,
    row 3 and column 5 are represented by the key `5 + 3j`.
    '''
    grid = {}
    with open(file_path) as f:
        lines = f.read().strip().split("\n")
        for y, line in enumerate(lines):  # Iterate over the rows by row index
            for x, e in enumerate(line.strip()):  # Iterate over each character by column index
                position = x + y * 1j  # Create a key representing the position as a complex number (x + yj)
                grid[position] = e
    return grid

def find_guard_position(grid):
    for position, value in grid.items():
        if value not in '.#':  # Find the guard (not wall or open area)
            direction = {'>': 1, 'v': 1j, '<': -1, '^': -1j}[value]
            return position, direction
    return None, None

def is_inbounds(x, y, grid):
    return (x, y) in grid

def count_loop_positions(grid):
    """
    Finds all positions where placing an obstacle results in the guard getting stuck in a loop.
    """
    guard_pos, guard_direction = find_guard_position(grid)
    visited_positions, direction_cache, loop_obstacles = set(), set(), set()

    while guard_pos in grid:
        visited_positions.add(guard_pos)
        direction_cache.add((guard_pos, guard_direction))
        if grid.get(guard_pos + guard_direction) == WALL:
            guard_direction *= 1j # Rotate the direction by 90 degrees (multiply by 1j)
        else:
            obstacle_pos = guard_pos + guard_direction
            # If the obstacle is within the grid and hasn't been visited yet
            if obstacle_pos in grid and obstacle_pos not in visited_positions:
                temp_pos, temp_direction, temp_cache = guard_pos, guard_direction * 1j, direction_cache.copy()

                # Simulates the movement of the guard and checks if an obstacle leads to a loop.
                while temp_pos in grid:
                    temp_cache.add((temp_pos, temp_direction))
                    if grid.get(temp_pos + temp_direction) == WALL or (temp_pos + temp_direction) == obstacle_pos:
                        temp_direction *= 1j # Rotate the direction again if a wall or obstacle is encountered
                    else:
                        # Move to the next position in the current direction
                        temp_pos += temp_direction

                    # If we've revisited a position and direction pair, it indicates a loop
                    if (temp_pos, temp_direction) in temp_cache:
                        loop_obstacles.add(obstacle_pos)
                        break

            # Move the guard to the next position
            guard_pos += guard_direction

    return len(set(loop_obstacles))

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
grid = read_file(file_path)
loop_count = count_loop_positions(grid)

print("Part2:", loop_count)