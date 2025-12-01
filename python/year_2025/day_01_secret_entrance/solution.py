from python.helpers.aoc_utils import input_data, time_function


def parse_input(puzzle_input):
    return [(line[0], int(line[1:])) for line in puzzle_input]


def calculateRotation(pos, direction, value):
    full_rotations = value // 100
    step = value if direction == "R" else -value
    new_pos = (pos + step) % 100

    crossed_zero = False
    if pos != 0:  # Don't re-count when starting at 0
        if new_pos == 0:  # Moved exactly to position 0
            crossed_zero = True
        elif direction == "L" and new_pos > pos:  # Position being higher after negative move must mean a wrap
            crossed_zero = True
        elif direction == "R" and new_pos < pos:  # Position being lower after positive move must mean a wrap
            crossed_zero = True
    rotations = full_rotations + (1 if crossed_zero else 0)

    return new_pos, rotations


def part_one(puzzle_input):
    count, pos = 0, 50
    for (direction, value) in parse_input(puzzle_input):
        pos, _ = calculateRotation(pos, direction, value)
        count += (pos == 0)
    return count


def part_two(puzzle_input):
    count, pos = 0, 50
    for (direction, value) in parse_input(puzzle_input):
        pos, passedZero = calculateRotation(pos, direction, value)
        count += passedZero
    return count


def main():
    puzzle_input = input_data(
        "python/year_2025/day_01_secret_entrance/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 01: secret_entrance")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
