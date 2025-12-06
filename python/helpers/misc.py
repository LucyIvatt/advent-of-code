from itertools import groupby
import time
from enum import Enum
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def input_data(filename, strip=True):
    """Returns the data imported from file, resolving paths relative to project root."""
    if not os.path.isabs(filename):
        filename = os.path.join(PROJECT_ROOT, filename)

    with open(filename, "r") as file:
        return [line.strip() if strip else line for line in file.readlines()]


def get_adjacent_coords(coords, x_limit, y_limit, diagonal=False):
    '''Returns all of the adjacent coordinates, including diagonals) for a list of coordinates. Removes any duplicates and any coordinates
    that were present in the original input.'''
    if diagonal:
        directions = [(dx, dy) for dx in range(-1, 2)
                      for dy in range(-1, 2) if (dx, dy) != (0, 0)]
    else:
        directions = [(dx, dy) for dx in range(-1, 2)
                      for dy in range(-1, 2) if (dx, dy) != (0, 0) and (dx == 0 or dy == 0)]

    adjacent_coords = []

    for coord in coords:
        x, y = coord
        adjacent_coords += [
            (x + dx, y + dy) for dx, dy in directions
            if 0 <= x + dx < x_limit and 0 <= y + dy < y_limit
        ]

    return set([coord for coord in adjacent_coords if coord not in coords])


def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    elapsed_time = time.time() - start_time
    return result, elapsed_time


def find_element_location_2d_list(matrix, target):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == target:
                return (i, j)
    return None


def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def transpose_list(lst):
    return [list(map(str, column)) for column in zip(*lst)]


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


class DiagonalDirections(Enum):
    SOUTH_EAST = (1, 1)
    SOUTH_WEST = (1, -1)
    NORTH_WEST = (-1, -1)
    NORTH_EAST = (-1, 1)


def split_by_empty_line(puzzle_input):
    """Splits the puzzle input into patterns by empty line."""
    return [list(group) for key, group in groupby(puzzle_input, key=lambda x: x == "") if not key]


def get_factors(x):
    """Return all positive factors of n."""
    return [i for i in range(1, x + 1) if x % i == 0]
