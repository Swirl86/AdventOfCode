"""
https://adventofcode.com/2023/day/1
Advent of Code 2023 Day 1: Trebuchet?!
"""
import os
import re


def parse_input(file_path):
    calibration_value = 0
    with open(file_path) as f:
        for line in f.readlines():
            res = re.sub(r'[^\d]+', '', line)
            first_digit = res[0]
            last_digit = res[-1]
            calibration_value += int(first_digit + last_digit)
    return calibration_value



file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sum = parse_input(file_path)
print("Part1:", sum)