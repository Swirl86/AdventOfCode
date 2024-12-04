"""
https://adventofcode.com/2024/day/1
Advent of Code 2024 Day 1: Historian Hysteria
"""
import os


def parse_input(file_path):
    left_list = []
    right_list = []
    with open(file_path) as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    """
    Calculate the total distance between paired numbers from two lists.
    """
    left_list.sort()
    right_list.sort()

    distances = []
    for l, r in zip(left_list, right_list):
        distances.append(abs(l - r))

    return sum(distances)


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

left_list, right_list = parse_input(file_path)

result = calculate_total_distance(left_list, right_list)
print("Part1:", result)