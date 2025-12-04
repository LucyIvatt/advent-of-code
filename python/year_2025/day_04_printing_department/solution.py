from python.helpers.aoc_utils import DiagonalDirections, Direction, input_data, time_function


def part_one(puzzle_input):
    room = [[char for char in row] for row in puzzle_input]
    diffs = [direction.value for direction in Direction] + [dir.value for dir in DiagonalDirections]
    accessible = 0
    for i in range(len(room)):
        for j in range(len(room[i])):
            if (room[i][j]) == "@":
                adj = [room[i+di][j+dj] for di, dj in diffs if (0 <= i+di < len(room)) and (0 <= j+dj < len(room[i]))]
                if adj.count("@") < 4:
                    accessible += 1

    return accessible


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("python/year_2025/day_04_printing_department/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 04: printing_department")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
