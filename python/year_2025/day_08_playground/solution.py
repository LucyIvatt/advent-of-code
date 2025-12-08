from collections import defaultdict
import math
from operator import itemgetter
import time
from python.helpers.misc import input_data, time_function
from itertools import combinations


def straight_line_distance(first, second):
    return math.sqrt(math.pow(second[0]-first[0], 2) + math.pow(second[1]-first[1], 2) + math.pow(second[2]-first[2], 2))


def part_one(puzzle_input, connections):
    coords = [tuple(map(int, line.split(','))) for line in puzzle_input]
    distances = [((tuple(pair[0]), tuple(pair[1])), straight_line_distance(pair[0], pair[1]))
                 for pair in combinations(coords, 2)]
    sorted_distances = sorted(distances, key=itemgetter(1))

    circuits = [[coord] for coord in coords]

    i = 0
    while i < connections:
        pair = sorted_distances[i][0]
        i += 1
        a = next((j for j, sublist in enumerate(circuits) if pair[0] in sublist), -1)
        b = next((j for j, sublist in enumerate(circuits) if pair[1] in sublist), -1)

        if (a == b):
            continue
        else:
            circuits[a].extend(circuits[b])
            circuits.pop(b)

    return math.prod(sorted([len(c) for c in circuits])[-3:])


def part_two(puzzle_input):
    coords = [tuple(map(int, line.split(','))) for line in puzzle_input]
    distances = [((tuple(pair[0]), tuple(pair[1])), straight_line_distance(pair[0], pair[1]))
                 for pair in combinations(coords, 2)]
    sorted_distances = sorted(distances, key=itemgetter(1))

    circuits = [[coord] for coord in coords]

    i = 0
    last_pair = None
    while len(circuits) > 1:
        pair = sorted_distances[i][0]
        last_pair = pair
        i += 1
        a = next((j for j, sublist in enumerate(circuits) if pair[0] in sublist), -1)
        b = next((j for j, sublist in enumerate(circuits) if pair[1] in sublist), -1)

        if (a == b):
            continue
        else:
            circuits[a].extend(circuits[b])
            circuits.pop(b)

    return last_pair[0][0] * last_pair[1][0]


def main():
    example = False
    puzzle_input = input_data(f"python/year_2025/day_08_playground/{'example' if example else 'input'}.txt")

    p1, p1_time = time_function(part_one, puzzle_input, 10 if example else 1000)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 08: playground")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
