"""
https://adventofcode.com/2022/day/2
Advent of Code 2022 2: Rock Paper Scissors
"""
import os


file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    """
    X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    """
    score_mapping = {
        "X": {"A": 3, "B": 1, "C": 2, "base": 0},
        "Y": {"A": 1, "B": 2, "C": 3, "base": 3},
        "Z": {"A": 2, "B": 3, "C": 1, "base": 6}
    }
    draw_score = 3
    won_score = 6

    total_score = 0

    for line in f.readlines():
        opponent, me = line.split()

        total_score += score_mapping[me][opponent] + score_mapping[me]["base"]

    """
    What would your total score be if everything goes exactly according to your strategy guide?
    """
    print("Part2: ", total_score)