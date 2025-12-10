from itertools import combinations
from operator import itemgetter
from python.helpers.misc import input_data, time_function

COORD_CACHE = {}


def rect_edge_coords(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    left = min(x1, x2)
    right = max(x1, x2)
    top = min(y1, y2)
    bottom = max(y1, y2)

    edges = set()

    # Top edge
    for x in range(left, right + 1):
        edges.add((x, top))

    # Bottom edge
    for x in range(left, right + 1):
        edges.add((x, bottom))

    # Left edge
    for y in range(top, bottom + 1):
        edges.add((left, y))

    # Right edge
    for y in range(top, bottom + 1):
        edges.add((right, y))

    return edges


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
    rectangles_by_size = get_distanced_rectangles(puzzle_input)[1]
    coords = [tuple(map(int, line.split(","))) for line in puzzle_input]
    pairs_to_check = len(rectangles_by_size)
    index = next(i for i, item in enumerate(rectangles_by_size) if item[0] == ((5254, 66490), (94821, 50072)))
    print(index)
    highest_area = 0

    edge_coords = set()
    for edge in range(len(coords)):
        c1 = coords[edge]
        c2 = coords[edge+1 if edge+1 < len(coords) else 0]

        if c1[0] == c2[0]:
            c1, c2 = (c1, c2) if c2[1] > c1[1] else (c2, c1)
            # print(f"adding {c1[0]}, {c1[1]}-{c2[1]}")
            for i in range(c1[1], c2[1]+1):
                edge_coords.add((c1[0], i))
        else:
            c1, c2 = (c1, c2) if c2[0] > c1[0] else (c2, c1)

            # print(f"adding {c1[0]}-{c2[0]}, {c1[1]}")
            for i in range(c1[0], c2[0]+1):
                edge_coords.add((i, c1[1]))

    for i in range(index, len(rectangles_by_size)):
        c, size = rectangles_by_size[i]
        # compute completion percentage for items checked from `index` to end
        completion_pct = (i / pairs_to_check) * 100
        print("verifying", c, "- completion", f"{completion_pct:.2f}%")

        c1 = c[0]
        c2 = c[1]
        edges_of_rect = rect_edge_coords(c1, c2)
        valid = True
        for coord in edges_of_rect:
            if coord in edge_coords:
                pass
                # print(coord, "on edge so is still valid so far")
            else:
                if coord not in COORD_CACHE:
                    # print(coord, "not on edge, so need to check - beginning ray trace")
                    crossover_count = 0
                    previously_hit_edge = False
                    for r in range(coord[0], 0, -1):
                        # print(r)
                        ray_hit_edge = True if (r, coord[1]) in edge_coords else False
                        if ray_hit_edge and not previously_hit_edge:
                            # print("hit new edge")
                            crossover_count += 1
                            previously_hit_edge = True
                        elif not ray_hit_edge and previously_hit_edge:
                            # print("hit new open space")
                            previously_hit_edge = False
                        # else:
                            # print("continuing")

                    # print(crossover_count)
                    if (crossover_count % 2 == 0):
                        # print("invalid coord")
                        valid = False
                        COORD_CACHE[coord] = False
                        break
                    else:
                        COORD_CACHE[coord] = True

                else:
                    valid = COORD_CACHE[coord]

        if valid:
            return size
            # print(c, "is valid shape, adding area", area, "to highest if higher")


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
