"""
https://adventofcode.com/2024/day/1
Advent of Code 2024 Day 1: Historian Hysteria
"""
import os
from collections import Counter


def parse_input(file_path):
    left_list = []
    right_list = []
    with open(file_path) as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    """
    Calculate a similarity score based on how often each number
    from the left list appears in the right list.
    """
    right_counts = Counter(right_list)
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts.get(num, 0)

    return similarity_score


file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

left_list, right_list = parse_input(file_path)

result = calculate_similarity_score(left_list, right_list)
print("Part2:", result)