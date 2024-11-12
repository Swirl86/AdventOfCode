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

def calculate_sizes(directory):
    """Recursively calculate the size of each directory and storing the sizes"""
    total_size = 0
    for name, content in directory.items():
        if isinstance(content, dict):  # It's a subdirectory
            subdir_size = calculate_sizes(content)
            directory[name]['_size'] = subdir_size  # Store size separately in each subdirectory
            total_size += subdir_size
        else:
            total_size += content  # It's a file, so add its size directly
    return total_size

def find_directories_with_max_size(directory, max_size):
    """Recursively find all directories with a total size"""
    eligible_sizes = []
    for _, content in directory.items():
        if isinstance(content, dict):
            subdir_size = content.get('_size', 0)
            if subdir_size <= max_size:
                eligible_sizes.append(subdir_size)
            # Recurse into subdirectories to find other eligible directories
            eligible_sizes.extend(find_directories_with_max_size(content, max_size))
    return eligible_sizes


root = parse_input()

calculate_sizes(root)

eligible_sizes = find_directories_with_max_size(root, 100000)

print("Part1:", sum(eligible_sizes))

