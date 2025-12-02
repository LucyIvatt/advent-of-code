from python.helpers.aoc_utils import input_data, time_function

FACTORS = {}


def get_factors(x):
    return [i for i in range(1, x + 1) if x % i == 0]


def parse_input(puzzle_input):
    return set([(L, R) for num_range in puzzle_input[0].split(",") for L, R in [num_range.split("-")]])


def part_one(puzzle_input):
    count = 0
    for L, R in parse_input(puzzle_input):
        if len(L) % 2 != 0 and len(L) == len(R):
            continue
        for num in range(int(L), int(R)+1):
            string_num = str(num)
            mid = len(string_num) // 2
            if (string_num[:mid] == string_num[mid:]):
                count += num

    return count


def part_two(puzzle_input):
    count = 0
    for L, R in parse_input(puzzle_input):
        for num in range(int(L), int(R)+1):
            string_num = str(num)
            if len(string_num) in FACTORS.keys():
                factors = FACTORS[len(string_num)]
            else:
                factors = get_factors(len(string_num))
                FACTORS[len(string_num)] = factors

            for multiple in factors:
                if multiple == len(string_num):
                    continue
                substrings = [string_num[i:i+multiple]
                              for i in range(0, len(string_num), multiple)]
                if len(set(substrings)) == 1:
                    count += num
                    break
    return count


def main():
    puzzle_input = input_data("python/year_2025/day_02_gift_shop/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 02: gift_shop")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
