import itertools
from python.helpers.misc import input_data, split_by_empty_line, time_function
from python.helpers.range import Range

INDEX = 0
VALUE = 1


def merge_ranges(ranges):
    current_index = 0
    while current_index <= len(ranges):
        for (i, val_i), (j, val_j) in itertools.combinations(list(enumerate(ranges)), 2):

            lowest, highest = ((i, val_i), (j, val_j)) if val_i.lower < val_j.lower else ((j, val_j), (i, val_i))

            if (lowest[VALUE].lower == highest[VALUE].lower):
                merged = Range(lowest[VALUE].lower, max(lowest[VALUE].upper, highest[VALUE].upper))
                ranges[lowest[INDEX]] = merged
                del ranges[highest[INDEX]]
                break

            elif (highest[VALUE].lower <= lowest[VALUE].upper):
                merged = Range(lowest[VALUE].lower, max(lowest[VALUE].upper, highest[VALUE].upper))
                ranges[lowest[INDEX]] = merged
                del ranges[highest[INDEX]]
                break
        current_index += 1
    return ranges


def part_one(puzzle_input):
    ranges, ids = split_by_empty_line(puzzle_input)
    range_objs = [Range.from_string(r) for r in ranges]
    return sum(1 for id in ids if any(r.is_within_range(id) for r in range_objs))


def part_two(puzzle_input):
    range_objs = [Range.from_string(r) for r in split_by_empty_line(puzzle_input)[0]]
    fresh = 0
    merged_ranges = merge_ranges(range_objs)
    print(merged_ranges)
    return sum(r.length for r in merged_ranges)


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
