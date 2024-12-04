"""
https://adventofcode.com/2024/day/4
Advent of Code 2024 Day 4: Ceres Search
"""
import os
import re


'''
It's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.
M.S  S.M
.A.  .A.
M.S  S.M

M.M  S.S
.A.  .A.
S.S  M.M
'''
def count_xmas(file_path):
    with open(file_path) as f:
        word_search = [line.strip() for line in f.readlines()]

    rows, cols = len(word_search), len(word_search[0])
    count = 0

    for r in range(1, rows - 1): # ensure we don't go off the grid with -1 when look at the diagonals around each "A"
        for c in range(1, cols - 1):
            if word_search[r][c] == "A":
                # Get the relevant diagonal characters
                top_left = word_search[r - 1][c - 1]
                bottom_right = word_search[r + 1][c + 1]
                top_right = word_search[r - 1][c + 1]
                bottom_left = word_search[r + 1][c - 1]

                # Check if the diagonals contain exactly one "M" and one "S"
                if ((top_left == "M" and bottom_right == "S") or
                    (top_left == "S" and bottom_right == "M")) and \
                   ((top_right == "M" and bottom_left == "S") or
                    (top_right == "S" and bottom_left == "M")):
                    count += 1

    return count

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

result = count_xmas(file_path)
print("Part2:", result)