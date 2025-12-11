from collections import defaultdict
import time
from python.helpers.misc import input_data, time_function


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
    perms = (("svr", "dac"), ("svr", "fft"), ("dac", "fft"), ("fft", "dac"), ("fft", "out"), ("dac", "out"))
    counts = []

    for start_node, end_node in perms:
        num_paths = 0
        possibilities = [start_node]

        while possibilities:
            new_possibilities = []
            for node in possibilities:
                if node == end_node:
                    num_paths += 1

                else:
                    new_paths = []
                    for next_node in graph[node]:
                        new_paths.append(next_node)
                    new_possibilities.extend(new_paths)
            possibilities = new_possibilities
        counts.append(num_paths)

    for i in range(len(perms)):
        print(perms[i], counts[i])
    return


def main():
    puzzle_input = input_data("python/year_2025/day_11_reactor/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 11: reactor")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
