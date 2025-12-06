import itertools
from python.helpers.misc import input_data, split_by_empty_line, time_function
from python.helpers.range import Range, merge_ranges


def part_one(puzzle_input):
    ranges, ids = split_by_empty_line(puzzle_input)
    return sum(1 for id in ids if any(r.is_within_range(id) for r in [Range.from_string(r) for r in ranges]))


def part_two(puzzle_input):
    ranges = split_by_empty_line(puzzle_input)[0]
    return sum(r.length for r in merge_ranges([Range.from_string(r) for r in ranges]))


def main():
    puzzle_input = input_data("python/year_2025/day_05_cafeteria/example.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 05: cafeteria")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
