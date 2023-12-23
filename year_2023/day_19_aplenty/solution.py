from helpers.aoc_utils import input_data, time_function

def part_one(puzzle_input):
    pass

def part_two(puzzle_input):
    pass

def main():
    puzzle_input = input_data("year_2023/day_19_aplenty/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 19: aplenty")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")

if __name__ == "__main__":
    main()
