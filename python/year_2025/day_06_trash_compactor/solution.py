import math
from python.helpers.misc import input_data, time_function, transpose_list


def part_one(puzzle_input):
    transpose = transpose_list([line.split() for line in puzzle_input])
    ans = 0

    for problem in transpose:
        op = problem[-1]
        nums = map(int, problem[:-1])
        ans += sum(nums) if op == "+" else math.prod(nums)

    return ans


def part_two(puzzle_input):
    symbols = puzzle_input[-1]
    indexes = [i for i, ch in enumerate(symbols) if ch in {"*", "+"}]
    split_problems = []

    # Split the numerical columns by using the index locations of the operators
    for line in [line.rstrip("\n") for line in puzzle_input]:
        parts = [line[start:end-1] for start, end in zip(indexes, indexes[1:])]
        parts.append(line[indexes[-1]:])   # last slice stays the same
        split_problems.append(parts)

    transpose = transpose_list(split_problems)
    ans = 0

    # Joins digits by columns to make the numbers in the equation and applies operator
    for problem in transpose:
        values, op = problem[:-1], problem[-1][0]
        nums = [int("".join(col[digit] for col in values)) for digit in range(len(values[0]))]
        ans += sum(nums) if op == "+" else math.prod(nums)

    return ans


def main():
    puzzle_input = input_data("python/year_2025/day_06_trash_compactor/example.txt", False)

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 06: trash_compactor")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
