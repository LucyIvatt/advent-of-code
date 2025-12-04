from python.helpers.misc import input_data, time_function


def find_highest_joltage(bank, n):
    stack, num_to_remove = [], len(bank) - n
    for digit in bank:
        while stack and stack[-1] < digit and num_to_remove > 0:
            stack.pop()
            num_to_remove -= 1
        stack.append(digit)
    return int("".join(str(stack[i]) for i in range(n)))


def solve(puzzle_input, n):
    return sum(find_highest_joltage([int(battery) for battery in bank], n) for bank in puzzle_input)


def part_one(puzzle_input):
    return solve(puzzle_input, 2)


def part_two(puzzle_input):
    return solve(puzzle_input, 12)


def main():
    puzzle_input = input_data("python/year_2025/day_03_lobby/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 03: lobby")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
