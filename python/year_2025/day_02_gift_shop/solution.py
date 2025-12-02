from python.helpers.aoc_utils import input_data, time_function, get_factors


FACTORS_CACHE = {}


def parse_input(puzzle_input):
    return [tuple(map(int, part.split("-"))) for part in puzzle_input[0].split(",")]


def digit_length_ranges(start, end):
    """
    Creates ranges so that each range has the same number of digits.
    Example: 95–105 -> gives:
        (95, 99, 2-digit)
        (100, 105, 3-digit)
    """
    current = start
    while current <= end:
        length = len(str(current))
        upper = min(end, 10 ** length - 1)
        yield current, upper, length
        current = upper + 1


def part_one(puzzle_input):
    invalid_ids = 0

    for start, end in parse_input(puzzle_input):
        for low, high, length in digit_length_ranges(start, end):

            if length % 2 != 0:
                continue  # Only even lengths can have matching pairs

            mid = length // 2
            for num in range(low, high + 1):
                num_str = str(num)
                if num_str[:mid] == num_str[mid:]:
                    invalid_ids += num

    return invalid_ids


def part_two(puzzle_input):
    invalid_ids = 0

    for start, end in parse_input(puzzle_input):
        for low, high, length in digit_length_ranges(start, end):

            if length not in FACTORS_CACHE:
                FACTORS_CACHE[length] = get_factors(length)

            # Remove segment which is equal to the full number length as this doesn't make an invalid ID
            segments = [seg for seg in FACTORS_CACHE[length] if seg != length]

            if not segments:
                continue

            for num in range(low, high + 1):
                num_str = str(num)

                for segment_length in segments:
                    repetitions = length // segment_length
                    segment = num_str[:segment_length]

                    if segment * repetitions == num_str:
                        invalid_ids += num
                        break
    return invalid_ids


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
