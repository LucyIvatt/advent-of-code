from itertools import combinations
from python.helpers.misc import input_data, time_function


def part_one(puzzle_input):
    highest_area = 0

    coords = [tuple(map(int, line.split(","))) for line in puzzle_input]
    for c in combinations(coords, 2):
        print(c)
        area = abs(c[0][0]-c[1][0]+1) * abs(c[0][1] - c[1][1]+1)
        highest_area = max(highest_area, area)
    return highest_area


def part_two(puzzle_input):
    # extrapolate all the edge so we have a list of all edge coordinates
    # for all four corners of the rectangle, cast a ray out until its out of bounds,
    #   if coord is in the edge set, add to count of boundsary crosses
    # if it crosses the boundary odd number of times its within the shape
    # if its even its outside
    pass


def main():
    puzzle_input = input_data("python/year_2025/day_09_movie_theatre/example.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 09: movie_theatre")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
