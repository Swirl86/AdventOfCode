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

    def do_ranges_overlap(r1, r2):
        return not (r1.stop <= r2.start or r2.stop <= r1.start)

    overlap_count = 0
    for first, second in assignments:
        if do_ranges_overlap(first, second):
            overlap_count += 1

    print("Part2: ", overlap_count)