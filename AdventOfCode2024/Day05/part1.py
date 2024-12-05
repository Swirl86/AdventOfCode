"""
https://adventofcode.com/2024/day/5
Advent of Code 2024 Day 5: Print Queue
"""
import os
from collections import defaultdict


def read_file(file_path):
    with open(file_path) as f:
        content = f.read()
        ordering_rules, pages_to_produce = [
            part.split("\n") for part in content.split("\n\n")
        ]

        pages_to_produce = [
            [int(num) for num in page.split(",")]
            for page in pages_to_produce
        ]

        ordering_dict = defaultdict(list)
        for rule in ordering_rules:
            x, y = map(int, rule.split("|"))
            ordering_dict[x].append(y)

        return ordering_dict, pages_to_produce

def is_correct_order(update, ordering_dict):
    indegree = defaultdict(int)

    # Calculate indegree (number of pages that must come before each page)
    for x in update:
        for y in ordering_dict[x]:
            indegree[y] += 1

    for page in update:
        if indegree[page] > 0:
            return False
        if page in ordering_dict:
            for neighbor in ordering_dict[page]:
                indegree[neighbor] -= 1

    return True


def count_middle_pages(ordering_dict, pages_to_produce):
    middle_pages_sum = 0
    for update in pages_to_produce:
        if is_correct_order(update, ordering_dict):
            middle_page = update[len(update) // 2]
            middle_pages_sum += middle_page

    return middle_pages_sum

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

ordering_dict, pages_to_produce = read_file(file_path)

result = count_middle_pages(ordering_dict, pages_to_produce)

print("Part1:", result)