

from enum import Enum


STRAIGHT_DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N E S W
DIAGONAL_DIRS = [(1, -1), (1, 1), (-1, 1), (-1, -1)]  # NE SE SW NW
ALL_DIRS = STRAIGHT_DIRS + DIAGONAL_DIRS


def coord_equals(a, b) -> bool:
    """Return True if coordinates `a` and `b` are equal."""
    return a[0] == b[0] and a[1] == b[1]


class Grid:
    def __init__(self, array):
        self.array = array
        self.height = len(array)
        self.width = len(array[0])

    @classmethod
    def from_puzzle_input(cls, lines):
        return cls([list(line) for line in lines])

    def get(self, i, j):
        return self.array[i][j]

    def set(self, i, j, value):
        self.array[i][j] = value

    def iterate(self):
        for i in range(self.height):
            for j in range(self.width):
                yield i, j

    def in_bounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    def neighbour_coords(self, i, j, diagonals=False):
        """Yield neighbour coordinate tuples."""
        dirs = ALL_DIRS if diagonals else STRAIGHT_DIRS
        h, w = self.height, self.width

        for di, dj in dirs:
            ni = i + di
            nj = j + dj
            if 0 <= ni < h and 0 <= nj < w:
                yield (ni, nj)

    def get_neighbours(self, i, j, diagonals=False):
        """Yield (value, (i,j)) pairs of neighbours."""
        arr = self.array
        for ni, nj in self.neighbour_coords(i, j, diagonals=diagonals):
            yield arr[ni][nj], (ni, nj)

    def count_neighbors(self, i, j, value, diagonals=True):
        """Count neighbours whose value == `value`"""
        arr = self.array
        h, w = self.height, self.width
        count = 0

        for di, dj in ALL_DIRS if diagonals else STRAIGHT_DIRS:
            ni = i + di
            nj = j + dj
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == value:
                count += 1

        return count
