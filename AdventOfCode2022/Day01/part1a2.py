"""
https://adventofcode.com/2022/day/1
Advent of Code 2022 Day 1: Calorie Counting
"""

import os


file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    all_elf_calories = []
    current_elf = 0

    for line in f.readlines():
        if len(line.strip()) == 0:
            all_elf_calories.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)

    all_elf_calories.append(current_elf)

    """
    Find the Elf carrying the most Calories.
    How many total Calories is that Elf carrying?
    """
    print("Part1: ", max(all_elf_calories))

    """
    Find the top three Elves carrying the most Calories.
    How many Calories are those Elves carrying in total?
    """

    print("Part2: ", sum(sorted(all_elf_calories, reverse=True)[:3]))
