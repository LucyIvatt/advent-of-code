from collections import defaultdict
import math
from python.helpers.misc import input_data, time_function

CACHE = {}


def count_paths(start_node, end_node, graph):
    if start_node == end_node:
        return 1
    if (start_node, end_node) in CACHE:
        return CACHE[(start_node, end_node)]

    total = 0
    for next_node in graph[start_node]:
        total += count_paths(next_node, end_node, graph)

    CACHE[(start_node, end_node)] = total

    return total


def part_one(puzzle_input):
    graph = defaultdict(set)

    for line in puzzle_input:
        node, connections = line.split(":")
        for connection in connections.strip().split(" "):
            graph[node].add(connection)

    start_node = "you"
    end_node = "out"

    num_paths = 0
    possibilities = [[start_node]]

    while possibilities:
        new_possibilities = []
        for possibility in possibilities:
            prev_node = possibility[-1]
            if prev_node == end_node:
                num_paths += 1

            else:
                new_paths = []
                for next_node in graph[prev_node]:
                    new_path = [x for x in possibility] + [next_node]
                    new_paths.append(new_path)
                new_possibilities.extend(new_paths)
        possibilities = new_possibilities
    return num_paths


def part_two(puzzle_input):
    graph = defaultdict(set)

    for line in puzzle_input:
        node, connections = line.split(":")
        for connection in connections.strip().split(" "):
            graph[node].add(connection)

    # Path(Start->Node1) * Path(Node1->Node2) * Path(Node2->End))
    # need to convert to DFS and use memo i think
    perms = [[("svr", "dac"), ("dac", "fft"), ("fft", "out")], [("svr", "fft"), ("fft", "dac"), ("dac", "out")]]
    total = 0

    for perm in perms:
        counts = []
        for start_node, end_node in perm:
            counts.append(count_paths(start_node, end_node, graph))
        total += math.prod(counts)
    return total


def main():
    puzzle_input = input_data("python/year_2025/day_11_reactor/example2.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 11: reactor")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
