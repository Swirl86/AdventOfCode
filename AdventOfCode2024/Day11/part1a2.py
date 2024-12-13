"""
https://adventofcode.com/2024/day/11
Advent of Code 2024 Day 11: Plutonian Pebbles
"""
import os
from collections import Counter # More memory-efficient

def read_file(file_path):
    """Read the input file and return a Counter of stones."""
    with open(file_path) as f:
        stones = f.read().strip().split(" ")
    return Counter(int(stone) for stone in stones)

def simulate_stones(stones, blinks):
    """
    Simulate the process of stones evolving based on specified rules over multiple blinks.

    Args:
        stones (Counter): A Counter containing the current stones and their quantities.
        blinks (int): The number of times the stones should evolve according to the rules.

    Returns:
        Counter: The updated stones and their quantities after the specified number of blinks.
    """
    for _ in range(blinks):
        new_stones = Counter()
        for stone, qty in stones.items():  # Iterate through current stones and their quantities
            if stone == 0:
                # Rule 1: If the stone is 0, it becomes 1
                new_stones[1] += qty
            elif len(str(stone)) % 2 == 0:
                # Rule 2: If the stone has an even number of digits, split it into two stones
                num_str = str(stone)
                mid = len(num_str) // 2
                left = int(num_str[:mid])
                right = int(num_str[mid:])
                new_stones[left] += qty
                new_stones[right] += qty
            else:
                # Rule 3: If the stone has an odd number of digits, multiply it by 2024
                new_stones[stone * 2024] += qty
        stones = new_stones
    return stones

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

stones = read_file(file_path)
blinks = 25
result_stones = simulate_stones(stones, blinks)

print("Part1:", sum(result_stones.values()))

blinks = 75
result_stones = simulate_stones(stones, blinks)
print("Part2:", sum(result_stones.values()))