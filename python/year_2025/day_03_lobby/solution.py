from python.helpers.aoc_utils import input_data, time_function
from itertools import combinations
from collections import deque


def find_highest_joltage(bank, n):
    battery_stack, batteries_to_remove = [], len(bank) - n

    for digit in bank:
        while len(battery_stack) > 0 and battery_stack[-1] < digit and batteries_to_remove > 0:
            battery_stack.pop()
            batteries_to_remove -= 1
        battery_stack.append(digit)
    print(battery_stack)

    value = ""
    for digit in range(n):
        value += str(battery_stack[digit])
    return int(value)


def part_one(puzzle_input):
    total_joltage, n = 0, 2
    for bank in puzzle_input:
        batteries = [int(battery) for battery in bank]
        total_joltage += find_highest_joltage(batteries, n)
    return total_joltage


def part_two(puzzle_input):
    total_joltage, n = 0, 12
    for bank in puzzle_input:
        batteries = [int(battery) for battery in bank]
        total_joltage += find_highest_joltage(batteries, n)
    return total_joltage


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
