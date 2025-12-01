from python.helpers.aoc_utils import input_data, time_function

def calculateMove(position, direction, value):
    return position + value if direction == "R" else position - value


def part_one(puzzle_input):
    count = 0
    pos = 50

    for (direction, value) in [(line[0], int(line[1:])) for line in puzzle_input]: 
        pos = calculateMove(pos, direction, value)
        if abs(pos % 100) == 0: count += 1

    return count

def part_two(puzzle_input):
    pass

def main():
    puzzle_input = input_data("python/year_2025/day_01_secret_entrance/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 01: secret_entrance")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")

if __name__ == "__main__":
    main()
