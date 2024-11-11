"""
https://adventofcode.com/2022/day/3
Advent of Code 2022 3: Rucksack Reorganization
"""
import os


file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    rucksack_sum = 0
    lines = [line.strip() for line in f.readlines()]

    for i in range(0, len(lines), 3): # Elves are divided into groups of three
        group = lines[i:i+3]

        if len(group) == 3:
            common_chars = set(group[0]) & set(group[1]) & set(group[2])
            for char in common_chars:
                if 'a' <= char <= 'z':
                    rucksack_sum += ord(char) - ord('a') + 1
                elif 'A' <= char <= 'Z':
                    rucksack_sum += ord(char) - ord('A') + 27

    print("Part2: ", rucksack_sum)