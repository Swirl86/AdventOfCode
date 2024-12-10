"""
https://adventofcode.com/2024/day/7
Advent of Code 2024 Day 7: Bridge Repair
"""
import os
from itertools import product

def read_file(file_path):
    with open(file_path) as f:
        return f.readlines()

def process_line(line):
    line = line.strip()
    if line:
        result, numbers = int(line.split(":")[0]), [int(x) for x in line.split(":")[1].strip().split()]
        return result, numbers
    return None, None

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        op = operators[i-1]
        if op == 'add':
            result += numbers[i]
        elif op == 'mul':
            result *= numbers[i]
    return result

def calibrate_equations(lines):
    calibration_result = 0
    operators = ['add', 'mul']

    for line in lines:
        result, numbers = process_line(line)

        if result is None or len(numbers) == 1:
            continue

        operator_combinations = product(operators, repeat=len(numbers) - 1)

        for op_order in operator_combinations:
            calc_result = evaluate_expression(numbers, op_order)

            if calc_result == result:
                calibration_result += result
                break

    return calibration_result


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
lines  = read_file(file_path)
result = calibrate_equations(lines)

print("Part1", result)