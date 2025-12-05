import itertools
import time
from python.helpers.misc import input_data, split_by_empty_line, time_function

INDEX = 0
VALUE = 1


def merge_ranges(ranges):
    current_index = 0
    while current_index <= len(ranges):
        for (i, val_i), (j, val_j) in itertools.combinations(list(enumerate(ranges)), 2):
            lowest, highest = ((i, val_i), (j, val_j)) if val_i[0] < val_j[0] else ((j, val_j), (i, val_i))

            if (lowest[VALUE][0] == highest[VALUE][0]):
                merged = [lowest[VALUE][0], max(lowest[VALUE][1], highest[VALUE][1])]
                ranges[lowest[INDEX]] = merged
                del ranges[highest[INDEX]]
                break

            elif (highest[VALUE][0] <= lowest[VALUE][1]):
                merged = [lowest[VALUE][0], max(lowest[VALUE][1], highest[VALUE][1])]
                ranges[lowest[INDEX]] = merged
                del ranges[highest[INDEX]]
                break
        current_index += 1
    return ranges


def part_one(puzzle_input):
    ranges, ids = split_by_empty_line(puzzle_input)
    fresh = 0

    for id in ids:
        for range in ranges:
            lower, upper = range.split("-")
            if int(lower) <= int(id) <= int(upper):
                fresh += 1
                break

    return fresh


def part_two(puzzle_input):
    ranges = [tuple(map(int, bound.split("-"))) for bound in split_by_empty_line(puzzle_input)[0]]
    fresh = 0
    merged_ranges = merge_ranges(ranges)
    for range in merged_ranges:
        fresh += range[1] - range[0] + 1
    return fresh


def main():
    puzzle_input = input_data("python/year_2025/day_05_cafeteria/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 05: cafeteria")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
