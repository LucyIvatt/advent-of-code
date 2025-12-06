from functools import reduce
import operator
from python.helpers.misc import input_data, time_function, transpose_list


def part_one(puzzle_input):
    print(puzzle_input)
    transpose = transpose_list([line.split() for line in puzzle_input])
    total = 0

    for problem in transpose:
        if problem[-1] == "*":
            total += reduce(operator.mul, map(int, problem[:-1]), 1)
        else:
            total += sum(map(int, problem[:-1]))

    return total


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("python/year_2025/day_06_trash_compactor/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 06: trash_compactor")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
