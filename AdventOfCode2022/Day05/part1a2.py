"""
https://adventofcode.com/2022/day/5
Advent of Code 2022 Day 5: Supply Stacks
"""
import copy
import os

def parse_stacks(stack_lines):
    """Parse the initial stack configuration from the input lines."""
    stacks = {}
    for line in reversed(stack_lines[:-1]):  # Start from the bottom of each stack
        for i, crate in enumerate(line[1::4], start=1):  # Get every 4th character
            if crate.strip():  # Check if there's a crate (ignore empty spaces)
                stacks.setdefault(i, []).append(crate)
    return stacks

def apply_instructions(stacks, instructions, first_part):
    """Parse and apply each instruction to the stacks."""
    for instruction in instructions:
        parts = instruction.split()
        quantity = int(parts[1])
        from_stack = int(parts[3])
        to_stack = int(parts[5])

        # Move crates as per the instruction
        move_crates(stacks, quantity, from_stack, to_stack, first_part)

def move_crates(stacks, quantity, from_stack, to_stack, first_part):
    if first_part:
        for _ in range(quantity):
            if stacks[from_stack]:
                crate = stacks[from_stack].pop()  # Remove the top crate from from_stack
                stacks[to_stack].append(crate) # Add the crate to to_stack
    else:
        # Move crates in a batch from `from_stack` to `to_stack`
        crates_to_move = stacks[from_stack][-quantity:]  # Take the top 'quantity' crates
        stacks[from_stack] = stacks[from_stack][:-quantity]  # Remove them from `from_stack`
        stacks[to_stack].extend(crates_to_move)  # Add them to `to_stack`

def get_top_crates_message(stacks):
    """Build a message from the top crate of each stack."""
    return ''.join(stacks[i][-1] for i in sorted(stacks.keys()) if stacks[i])

file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    # Read and separate stack configuration from instructions
    lines = f.read().split('\n\n')
    stackinput = lines[0].splitlines()
    instructions = lines[1].strip().splitlines()

    # Parse the initial stack configuration
    original_stacks = parse_stacks(stackinput)

    stacks_part1 = copy.deepcopy(original_stacks)
    apply_instructions(stacks_part1, instructions, True)
    top_crates_message_part1 = get_top_crates_message(stacks_part1)
    print("Part1:", top_crates_message_part1)

    stacks_part2 = copy.deepcopy(original_stacks)
    apply_instructions(stacks_part2, instructions, False)
    top_crates_message_part2 = get_top_crates_message(stacks_part2)
    print("Part2:", top_crates_message_part2)
