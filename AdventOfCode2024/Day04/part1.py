"""
https://adventofcode.com/2024/day/4
Advent of Code 2024 Day 4: Ceres Search
"""
import os
import re


# How many times does XMAS appear?
def count_xmas(file_path):
    with open(file_path) as f:
        word_search = [line.strip() for line in f.readlines()]

    word = "XMAS"
    n_rows = len(word_search)
    n_cols = len(word_search[0])
    count = 0

    # Check horizontal and vertical directions
    for row in range(n_rows):
        for col in range(n_cols):
            # Check horizontal (right direction)
            if col + len(word) <= n_cols and all(word_search[row][col + i] == word[i] for i in range(len(word))):
                count += 1
            # Check vertical (down direction)
            if row + len(word) <= n_rows and all(word_search[row + i][col] == word[i] for i in range(len(word))):
                count += 1
            # Check diagonal (down-right direction)
            if row + len(word) <= n_rows and col + len(word) <= n_cols and all(word_search[row + i][col + i] == word[i] for i in range(len(word))):
                count += 1
            # Check diagonal (up-right direction)
            if row - len(word) + 1 >= 0 and col + len(word) <= n_cols and all(word_search[row - i][col + i] == word[i] for i in range(len(word))):
                count += 1

            # Check for reversed horizontal (left direction)
            if col - len(word) + 1 >= 0 and all(word_search[row][col - i] == word[i] for i in range(len(word))):
                count += 1
            # Check for reversed vertical (up direction)
            if row - len(word) + 1 >= 0 and all(word_search[row - i][col] == word[i] for i in range(len(word))):
                count += 1
            # Check for reversed diagonal (up-left direction)
            if row - len(word) + 1 >= 0 and col - len(word) + 1 >= 0 and all(word_search[row - i][col - i] == word[i] for i in range(len(word))):
                count += 1
            # Check for reversed diagonal (down-left direction)
            if row + len(word) <= n_rows and col - len(word) + 1 >= 0 and all(word_search[row + i][col - i] == word[i] for i in range(len(word))):
                count += 1

    return count

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

result = count_xmas(file_path_test)
print("Part1:", result)