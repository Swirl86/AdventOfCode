"""
https://adventofcode.com/2022/day/6
Advent of Code 2022 Day 6: Tuning Trouble
"""
import os

sequence_part1 = 4
sequence_part2 = 14

char_array = []

def has_unique_chars(s):
    return len(s) == len(set(s))

def add_to_array(value):
    char_array.append(value)
    if len(char_array) > 4:
        char_array.pop(0)

file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    str = f.readline()

    sequence = sequence_part2 # Change based on part

    char_array = list(str[:sequence])
    if has_unique_chars(char_array):
        print(f"UNIQUE marker appears at index {sequence}")
    else:
        for i, char in enumerate(str[sequence:], start=sequence):
            add_to_array(char)
            if has_unique_chars(char_array):
                print(f"UNIQUE marker appears at index {i+1}")
                break
