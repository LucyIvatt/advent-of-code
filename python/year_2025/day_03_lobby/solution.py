from python.helpers.aoc_utils import input_data, time_function
from itertools import combinations
from collections import deque


def part_one(puzzle_input):
    total_joltage = 0
    for bank in puzzle_input:
        highest = 0
        for perm in combinations(range(len(bank)), 2):
            joltage = int(f"{bank[perm[0]]}{bank[perm[1]]}")
            if (joltage > highest):
                highest = joltage
        total_joltage += highest
    return total_joltage


def part_two(puzzle_input):
    total_joltage = 0
    n = 12
    total_banks = len(puzzle_input)

    for bank_idx, bank in enumerate(puzzle_input, 1):
        queue = deque([(int(bank[i]), i + 1)
                      for i in range(len(bank) - n + 1)])
        highest = 0
        while len(queue) > 0:
            sequence, next_index = queue.popleft()

            if sequence > highest and len(str(sequence)) == n:
                highest = sequence

            if len(str(sequence)) < n:
                remaining_len = n - len(str(sequence))
                max_possible = int(f"{sequence}{'9' * remaining_len}")
                if max_possible <= highest:
                    continue

                for j in range(next_index, len(bank)):
                    queue.append((sequence * 10 + int(bank[j]), j + 1))
        total_joltage += highest
        print(f"Completed bank {bank_idx}/{total_banks}")
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
