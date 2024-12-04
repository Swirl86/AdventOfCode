"""
https://adventofcode.com/2024/day/2
Advent of Code 2024 Day 2: Red-Nosed Reports
"""
import os


def parse_input(file_path):
    reports = []
    with open(file_path) as f:
        for line in f:
            parts = line.split()
            reports.append([int(x) for x in parts])

    return reports

def is_safe(report):
    """
    Check if a report is safe.
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    differences = []
    for i in range(len(report) - 1):
        # Calculate differences between adjacent levels
        difference = report[i + 1] - report[i]
        differences.append(difference)

    # Check if the differences are within [-3, -1] (decreasing)
    if all(-3 <= diff <= -1 for diff in differences):
        return True

    # Check if the differences are within [1, 3] (increasing)
    if all(1 <= diff <= 3 for diff in differences):
        return True

    # Report is not safe
    return False

def is_safe_with_one_removal(report):
    """
    Check if a report is safe by removing a level. (safety systems tolerate a single bad level)
    """
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]

        if is_safe(modified_report):
            return True

    return False


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report) or is_safe_with_one_removal(report):
            safe_count += 1
    return safe_count

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

reports = parse_input(file_path) #List of reports (each report is a list of integers).

safe_reports = count_safe_reports(reports)
print("Part2:", safe_reports)