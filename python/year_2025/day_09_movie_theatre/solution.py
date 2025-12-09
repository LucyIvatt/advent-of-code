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
    sorted_distances = get_distanced_rectangles(puzzle_input)[1]

    edge_pairs = set()
    for edge in range(len(coords)):
        c1 = coords[edge]
        c2 = coords[edge+1 if edge+1 < len(coords) else 0]
        edge_pairs.add((c1, c2))

    for rect, area in sorted_distances:
        rx1, ry1 = rect[0]
        rx2, ry2 = rect[1]

        rect_min_x = min(rx1, rx2)
        rect_max_x = max(rx1, rx2)
        rect_min_y = min(ry1, ry2)
        rect_max_y = max(ry1, ry2)

        valid = True
        for edge in edge_pairs:
            ex1, ey1 = edge[0]
            ex2, ey2 = edge[1]

            edge_min_x = min(ex1, ex2)
            edge_max_x = max(ex1, ex2)
            edge_min_y = min(ey1, ey2)
            edge_max_y = max(ey1, ey2)

            # rect_min_x < edge_max_x and
            # rect_max_x > edge_min_x and
            # rect_min_y < edge_max_y and
            # rect_max_y > edge_min_y

            if (rect_min_x < edge_max_x and rect_max_x > edge_min_x and rect_min_y < edge_max_y and rect_max_y > edge_min_y):
                valid = False
                break
        if valid:
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
