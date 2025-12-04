from python.helpers.grid import Grid
from python.helpers.misc import input_data, time_function


def is_accessible(grid, i, j):
    return grid.get(i, j) == "@" and grid.count_neighbors(i, j, lambda v: v == "@", diagonals=True) < 4


def part_one(puzzle_input):
    grid = Grid.from_puzzle_input(puzzle_input)
    return sum(1 for i, j in grid.iterate() if is_accessible(grid, i, j))


def part_two(puzzle_input):
    grid = Grid.from_puzzle_input(puzzle_input)
    total = 0
    while True:
        to_remove = [(i, j) for i, j in grid.iterate() if is_accessible(grid, i, j)]
        if not to_remove:
            break
        for i, j in to_remove:
            grid.set(i, j, ".")
        total += len(to_remove)
    return total


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
