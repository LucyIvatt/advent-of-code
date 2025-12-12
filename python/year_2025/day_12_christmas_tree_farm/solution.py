import re
from python.helpers.misc import input_data, split_by_empty_line, time_function

REGION_PATTERN = re.compile(r'(\d+)\s*x\s*(\d+):')


def part_one(puzzle_input):
    groups = split_by_empty_line(puzzle_input)
    count = 0
    for region in groups[-1]:
        dims, values = region.split(":")
        width, height = map(int, dims.split("x"))
        shapes = list(map(int, values.split()))

        if 3 * (3 * sum(shapes)) <= width * height:
            count += 1
    return count


def main():
    puzzle_input = input_data("python/year_2025/day_12_christmas_tree_farm/example.txt")

    p1, p1_time = time_function(part_one, puzzle_input)

    print("--------------------------------------")
    print("Day 12: christmas_tree_farm")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
