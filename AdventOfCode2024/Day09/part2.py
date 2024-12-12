"""
https://adventofcode.com/2024/day/9
Advent of Code 2024 Day 9: Disk Fragmenter
"""
from collections import deque
import os

FREE_SPACE = None

def read_file(file_path):
    """Reads the file and returns its content as a string."""
    with open(file_path) as file:
        return file.read().strip()

def build_disk_layout(disk_map):
    """Builds the initial disk layout with files and free spaces."""
    file_positions = deque([])
    free_spaces = deque([])
    current_file_id = 0
    disk_layout = []
    current_position = 0

    # Build the initial layout of the disk with files and free spaces
    for index, value in enumerate(disk_map):
        if index % 2 == 0:  # Even indices represent file sizes
            file_size = int(value)
            file_positions.append((current_position, file_size, current_file_id)) # Store position, size, and file ID
            for _ in range(int(value)):
                disk_layout.append(current_file_id)  # Add the file block
                current_position += 1
            current_file_id += 1
        else:  # Odd indices represent free spaces
            free_spaces.append((current_position, int(value)))  # Store position and size of free space
            for _ in range(int(value)):
                disk_layout.append(FREE_SPACE)
                current_position += 1

    return disk_layout, file_positions, free_spaces

def move_files_to_left(disk_layout, file_positions, free_spaces):
    """Moves the files to the left to fill gaps."""
    for (file_position, file_size, file_id) in reversed(file_positions):  # Process files from right to left
        for free_space_index, (space_position, space_size) in enumerate(free_spaces):
            if space_position < file_position and file_size <= space_size:  # Check if file fits into free space
                for i in range(file_size):
                    disk_layout[file_position + i] = None  # Remove file block from the old position
                    disk_layout[space_position + i] = file_id  # Move the file block to the free space
                free_spaces[free_space_index] = (space_position + file_size, space_size - file_size)
                break

    return disk_layout

def move_files(disk_map):
    """Moves the files to the left until there are no gaps between them and return disk layout."""
    disk_layout, file_positions, free_spaces = build_disk_layout(disk_map)
    disk_layout = move_files_to_left(disk_layout, file_positions, free_spaces)
    return disk_layout

def calculate_checksum(layout):
    """Calculates the checksum based on the files positions."""
    checksum = 0
    for index, file_id in enumerate(layout):
        if file_id is not FREE_SPACE:  # Skip free space
            checksum += index * file_id  # Position * File ID
    return checksum

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

disk_map = read_file(file_path)
layout = move_files(disk_map)
checksum = calculate_checksum(layout)
print("Part2:", checksum)