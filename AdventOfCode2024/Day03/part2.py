"""
https://adventofcode.com/2024/day/3
Advent of Code 2024 Day 3: Mull It Over
"""
import os
import re


def get_text_file_value(file_path):
    with open(file_path) as f:
        return f.read()

def process_instructions(text):
    result = 0
    is_mul_enabled = True

    for line in text.splitlines():
        instructions = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line.strip())

        for instruction in instructions:
            if 'do()' == instruction:
                is_mul_enabled = True
            elif 'don\'t()' == instruction:
                is_mul_enabled = False
            else:
                x, y = map(int, re.findall(r'\d+', instruction))
                if is_mul_enabled:
                    result += x * y

    return result


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

text = get_text_file_value(file_path)
result = process_instructions(text)

print("Part2:", result)