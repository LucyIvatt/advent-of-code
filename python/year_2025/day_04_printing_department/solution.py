from python.helpers.grid import Grid
from python.helpers.misc import input_data, time_function


def part_one(puzzle_input):
    grid = Grid.from_puzzle_input(puzzle_input)
    accessible = 0
    for i, j in grid.iterate():
        if grid.get(i, j) == "@" and grid.count_neighbors(i, j, lambda v: v == "@", diagonals=True) < 4:
            accessible += 1
    return accessible


def part_two(puzzle_input):
    grid = Grid.from_puzzle_input(puzzle_input)
    accessible = 0
    updates = True
    while updates:
        updates = False
        for i, j in grid.iterate():
            if grid.get(i, j) == "@" and grid.count_neighbors(i, j, lambda v: v == "@", diagonals=True) < 4:
                accessible += 1
                updates = True
                grid.array[i][j] = "."
    return accessible


def main():
    puzzle_input = input_data("python/year_2025/day_04_printing_department/example.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 04: printing_department")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
