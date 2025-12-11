from itertools import combinations
from operator import itemgetter
from python.helpers.misc import input_data, time_function

COORD_CACHE = {}


def get_distanced_rectangles(puzzle_input):
    highest_area = 0
    sizes = []

    coords = [tuple(map(int, line.split(","))) for line in puzzle_input]

    for c in combinations(coords, 2):
        area = abs(c[0][0]-c[1][0]+1) * abs(c[0][1] - c[1][1]+1)
        highest_area = max(highest_area, area)
        sizes.append([c, area])

    sorted_distances = sorted(sizes, key=itemgetter(1), reverse=True)
    return highest_area, sorted_distances


def part_one(puzzle_input):
    return get_distanced_rectangles(puzzle_input)[0]


def part_two(puzzle_input):
    coords = [tuple(map(int, line.split(","))) for line in puzzle_input]
    # sorted_distances = list of tuples: ( (point1, point2), area )
    sorted_distances = get_distanced_rectangles(puzzle_input)[1]

    # Build polygon edges as flat tuples (x1, y1, x2, y2)
    edges = []
    for i in range(len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % len(coords)]
        edges.append((x1, y1, x2, y2))

    for rect, area in sorted_distances:
        (rx1, ry1), (rx2, ry2) = rect

        rMinX = min(rx1, rx2)
        rMaxX = max(rx1, rx2)
        rMinY = min(ry1, ry2)
        rMaxY = max(ry1, ry2)

        valid = True
        for ex1, ey1, ex2, ey2 in edges:
            eMinX = min(ex1, ex2)
            eMaxX = max(ex1, ex2)
            eMinY = min(ey1, ey2)
            eMaxY = max(ey1, ey2)

            # Bounding-box overlap (strict), touching is OK
            if rMinX < eMaxX and rMaxX > eMinX and rMinY < eMaxY and rMaxY > eMinY:
                valid = False
                break

        if valid:
            # This is the first valid rectangle in sorted order → largest area
            return area


def main():
    puzzle_input = input_data("python/year_2025/day_09_movie_theatre/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 09: movie_theatre")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
