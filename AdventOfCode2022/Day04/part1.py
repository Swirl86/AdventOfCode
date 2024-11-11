"""
https://adventofcode.com/2022/day/4
Advent of Code 2022 4: Camp Cleanup
"""
import os


file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    assignments = []
    for line in f.readlines():
        value1, value2 = line.split(",")
        nr1, nr2 = value1.split("-")
        nr3, nr4 = value2.split("-")
        first = range(int(nr1), int(nr2) + 1)
        second = range(int(nr3), int(nr4) + 1)
        assignments.append((first, second))

    def is_contained(r1, r2):
        return r1.start >= r2.start and r1.stop <= r2.stop

    contained_count = 0
    for first, second in assignments:
        if is_contained(first, second) or is_contained(second, first):
            contained_count += 1

    print("Part1: ", contained_count)