"""
https://adventofcode.com/2022/day/2
Advent of Code 2022 2: Rock Paper Scissors
"""
import os


file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    moves = {
        "A": "Rock", "B": "Paper", "C": "Scissors",
        "X": ("Rock", 1), "Y": ("Paper", 2), "Z": ("Scissors", 3)
    }

    draw_score = 3
    won_score = 6

    total_score = 0

    for line in f.readlines():
        opponent, me = line.split()

        opponents_move = moves[opponent]
        my_move, shape_score = moves[me]

        if opponents_move == my_move:
            total_score += shape_score + draw_score
        elif my_move == "Rock" and opponents_move == "Scissors":
            total_score += shape_score + won_score
        elif my_move == "Paper" and opponents_move == "Rock":
            total_score += shape_score + won_score
        elif my_move == "Scissors" and opponents_move == "Paper":
            total_score += shape_score + won_score
        else:
            total_score += shape_score # Lost

    """
    What would your total score be if everything goes exactly according to your strategy guide?
    """
    print("Part1: ", total_score)