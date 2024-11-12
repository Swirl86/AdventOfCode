"""
https://adventofcode.com/2022/day/7
Advent of Code 2022 Day 7: No Space Left On Device
"""
import os

def parse_input():
    """Build the directory structure as a nested dictionary"""
    root = {}
    cwd = root
    stack = []

    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(file_path) as f:
        for line in f:
            row = line.strip()
            if row.startswith("$ cd"):
                dir_name = row[5:]
                if dir_name == "/":
                    cwd = root
                    stack = []
                elif dir_name == "..":
                    cwd = stack.pop()
                else:
                    cwd.setdefault(dir_name, {})
                    stack.append(cwd)
                    cwd = cwd[dir_name]
            elif row.startswith("$ ls"):
                continue
            else:
                size, name = row.split(maxsplit=1)
                if size == "dir":
                    cwd.setdefault(name, {})
                else:
                    cwd[name] = int(size)

    return root

def calculate_directory_sizes(directory):
    """Recursively calculate the size of each directory and storing the sizes"""
    total_size = 0
    for _, content in directory.items():
        if isinstance(content, dict):
            subdir_size = calculate_directory_sizes(content)
            content['_size'] = subdir_size  # Store subdirectory size
            total_size += subdir_size
        else:
            total_size += content  # File size
    return total_size

def find_smallest_sufficient_directory(directory, needed_size):
    """Find the smallest directory that can free up enough space."""
    smallest_sufficient_size = float('inf')
    for content in directory.values():
        if isinstance(content, dict):
            dir_size = content.get('_size', 0)
            if needed_size <= dir_size < smallest_sufficient_size:
                smallest_sufficient_size = dir_size
            # Recursively check subdirectories
            smallest_in_subdir = find_smallest_sufficient_directory(content, needed_size)
            if needed_size <= smallest_in_subdir < smallest_sufficient_size:
                smallest_sufficient_size = smallest_in_subdir
    return smallest_sufficient_size


root = parse_input()
total_used_space = calculate_directory_sizes(root)

total_space = 70000000
required_space_for_update = 30000000

current_free_space = total_space - total_used_space
space_needed = required_space_for_update - current_free_space

smallest_dir_size = find_smallest_sufficient_directory(root, space_needed)

print("Part2:", smallest_dir_size)

