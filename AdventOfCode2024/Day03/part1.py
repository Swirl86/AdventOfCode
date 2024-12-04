"""
https://adventofcode.com/2024/day/3
Advent of Code 2024 Day 3: Mull It Over
"""
import os
import re


def parse_input(file_path):
    matches = []
    with open(file_path) as f:
        pattern = r'mul\((\d+),(\d+)\)'
        for line in f:
            match  = re.findall(pattern, line)
            for x, y in match:
                matches.append((int(x), int(y)))

    return matches

def multiply_some_numbers(matches):
    result = 0
    for x, y in matches:
        result += x * y
    return result

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

matches = parse_input(file_path)
result = multiply_some_numbers(matches)

print("Part1:", result)