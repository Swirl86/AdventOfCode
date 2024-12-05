"""
https://adventofcode.com/2024/day/5
Advent of Code 2024 Day 5: Print Queue
"""
import os
from collections import defaultdict, deque

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
        reverse_dict = defaultdict(list)

        for rule in ordering_rules:
            x, y = map(int, rule.split("|"))
            ordering_dict[x].append(y)
            reverse_dict[y].append(x)

        return ordering_dict, reverse_dict, pages_to_produce

def is_wrong_order(current, ordering_dict):
    indegree = defaultdict(int)

    # Calculate indegree (number of pages that must come before each page)
    for x in current:
        for y in ordering_dict[x]:
            indegree[y] += 1

    for page in current:
        if indegree[page] > 0:
            return True
        if page in ordering_dict:
            for neighbor in ordering_dict[page]:
                indegree[neighbor] -= 1

    return False

def topological_sort(pages, ordering_dict, reverse_dict):
    """
    Sorts the pages using topological sorting to ensure the correct order.

    Summary of the Topological Sort Algorithm:
        1. Indegree Calculation: For each page, calculate how many pages must come before it.
        2. Queue Initialization: Add pages with indegree 0 (i.e., those with no dependencies) to the queue.
        3. Processing: Repeatedly remove pages from the queue, add them to the sorted list, and decrease the indegree of their dependent pages. Add any pages with indegree 0 to the queue.
        4. Result: Once the queue is empty, the pages are sorted in topological order.

    https://en.wikipedia.org/wiki/Topological_sorting
    """
    new_order = []
    queue = deque([])  # Initialize the queue to store pages that can be processed
    in_degree = {i: len(set(reverse_dict[i]) & set(pages)) for i in pages}  # Calculate indegree (nodes in a tree) for each page

    # Add pages with zero indegree to the queue
    for i in pages:
        if in_degree[i] == 0:
            queue.append(i)

    # Process the pages in the queue and build the sorted order
    while queue:
        x = queue.popleft()
        new_order.append(x)
        for y in ordering_dict[x]:
            if y in in_degree:
                in_degree[y] -= 1
                if in_degree[y] == 0: # all pages y depends on have been processed
                    queue.append(y)

    return new_order

def count_middle_pages(ordering_dict, reverse_dict, pages_to_produce):
    """
    Args:
        ordering_dict (defaultdict): A dictionary of ordering rules.
        reverse_dict (defaultdict): A dictionary of reverse ordering rules.
        pages_to_produce (list): A list of pages to be processed and ordered.
    """
    middle_pages_sum = 0

    for pages in pages_to_produce:
        if is_wrong_order(pages, ordering_dict):
            sorted_page = topological_sort(pages, ordering_dict, reverse_dict)
            middle_page = sorted_page[len(sorted_page) // 2]
            middle_pages_sum += middle_page

    return middle_pages_sum

file_path_test = os.path.join(os.path.dirname(__file__), "test.txt")
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

ordering_dict, reverse_dict, pages_to_produce = read_file(file_path_test)

result = count_middle_pages(ordering_dict, reverse_dict, pages_to_produce)

print("Part 2:", result)
