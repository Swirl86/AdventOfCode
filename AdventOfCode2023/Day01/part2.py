"""
https://adventofcode.com/2023/day/1
Advent of Code 2023 Day 1: Trebuchet?!
"""
import os
import re

word_to_number = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}
number_matcher = "(?=(" + "|".join(word_to_number.keys()) + "|\\d))"

def parse_input(file_path):
    total_calibration_value = 0
    with open(file_path) as f:
        for line in f:
            digits = [*map(extract_numbers, re.findall(number_matcher , line.lower()))]
            if digits:
                calibration_value = int(digits[0] + digits[-1])
                total_calibration_value += calibration_value
    return total_calibration_value

def extract_numbers(input_string):
    if input_string in word_to_number:
        return str(word_to_number[input_string])
    return input_string

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sum = parse_input(file_path)
print("Part2:", sum)