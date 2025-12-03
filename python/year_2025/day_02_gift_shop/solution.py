from python.helpers.aoc_utils import input_data, time_function, get_factors


FACTORS_CACHE = {}


def digit_length_ranges(start, end):
    """Creates ranges so that each range has the same number of digits.
    E.g. 95–105 -> gives: (95, 99, 2-digit) & (100, 105, 3-digit)"""
    current = start
    while current <= end:
        length = len(str(current))
        upper = min(end, 10 ** length - 1)
        yield current, upper, length
        current = upper + 1


def is_invalid_p1(num_str, length):
    """Check if a number is invalid for part one (has matching halves)."""
    if length % 2 != 0:
        return False
    mid = length // 2
    return num_str[:mid] == num_str[mid:]


def is_invalid_p2(num_str, length):
    """Check if a number is invalid for part two (has repeating segments)."""
    if length not in FACTORS_CACHE:
        FACTORS_CACHE[length] = get_factors(length)

    for segment in FACTORS_CACHE[length]:
        if segment == length:
            continue
        repetitions = length // segment
        segment = num_str[:segment]
        if segment * repetitions == num_str:
            return True
    return False


def solve(puzzle_input, invalid_id_check_fn):
    invalid_ids = 0
    for start, end in [tuple(map(int, part.split("-"))) for part in puzzle_input[0].split(",")]:
        for low, high, length in digit_length_ranges(start, end):
            for num in range(low, high + 1):
                if invalid_id_check_fn(str(num), length):
                    invalid_ids += num
    return invalid_ids


def part_one(puzzle_input):
    return solve(puzzle_input, is_invalid_p1)


def part_two(puzzle_input):
    return solve(puzzle_input, is_invalid_p2)


def main():
    puzzle_input = input_data("python/year_2025/day_02_gift_shop/input.txt")

    p1, t1 = time_function(part_one, puzzle_input)
    p2, t2 = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 02: gift_shop")
    print(f"Part One Answer: {p1} - [{t1:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{t2:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
