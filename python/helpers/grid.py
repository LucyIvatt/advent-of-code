

from enum import Enum


class Direction(str, Enum):
    """Compass directions used for grid navigation."""
    North = "North"
    NorthEast = "NorthEast"
    East = "East"
    SouthEast = "SouthEast"
    South = "South"
    SouthWest = "SouthWest"
    West = "West"
    NorthWest = "NorthWest"


STRAIGHT_DIRECTIONS = [Direction.North, Direction.East, Direction.South, Direction.West]
DIAGONAL_DIRECTIONS = [Direction.NorthEast, Direction.SouthEast, Direction.SouthWest, Direction.NorthWest]

""" Mapping from `Direction` to (dx, dy) offsets for a single-step move in that direction."""
DIRECTION_OFFSETS = {
    Direction.North: (0, -1),
    Direction.NorthEast: (1, -1),
    Direction.East: (1, 0),
    Direction.SouthEast: (1, 1),
    Direction.South: (0, 1),
    Direction.SouthWest: (-1, 1),
    Direction.West: (-1, 0),
    Direction.NorthWest: (-1, -1),
}


def coord_equals(a, b) -> bool:
    """Return True if coordinates `a` and `b` are equal.

    Args:
      a: A (x, y) coordinate tuple.
      b: A (x, y) coordinate tuple.
    """
    return a[0] == b[0] and a[1] == b[1]


class Grid:
    def __init__(self, array):
        self.array = array

    @property
    def height(self): return len(self.array)
    @property
    def width(self): return len(self.array[0])

    def get(self, i, j):
        return self.array[i][j]

    def set(self, i, j, value):
        self.array[i][j] = value

    def iterate(self):
        for i in range(self.height):
            for j in range(len(self.array[i])):
                yield i, j

    def in_bounds(self, i, j):
        return i >= 0 and i < len(self.array) and j >= 0 and j < len(self.array[i])

    def get_neighbours(self, i, j, diagonals=False):
        directions = [e.value for e in Direction] if diagonals else STRAIGHT_DIRECTIONS
        result = []
        for direction in directions:
            di, dj = DIRECTION_OFFSETS[direction]
            ni, nj = i + di, j + dj
            if self.in_bounds(ni, nj):
                result.append((self.array[ni][nj], (ni, nj)))
        return result

    def count_neighbors(self, i, j, predicate, diagonals=True):
        return sum(1 for v, _ in self.get_neighbours(i, j, diagonals=diagonals) if predicate(v))
