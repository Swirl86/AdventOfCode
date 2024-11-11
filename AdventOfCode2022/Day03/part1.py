"""
https://adventofcode.com/2022/day/3
Advent of Code 2022 3: Rucksack Reorganization
"""
import os


file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    rucksack_sum = 0
    for line in f.readlines():
        first_comp, second_comp = line[:len(line)//2], line[len(line)//2:]

        common_chars = set(first_comp) & set(second_comp)
        for char in common_chars:
            if 'a' <= char <= 'z': # Lowercase item types a through z have priorities 1 through 26
                rucksack_sum += ord(char) - ord('a') + 1
            elif 'A' <= char <= 'Z': # Uppercase item types A through Z have priorities 27 through 52
                rucksack_sum += ord(char) - ord('A') + 27

    print("Part1: ", rucksack_sum)