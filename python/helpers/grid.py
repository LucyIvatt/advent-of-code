

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
DIAGONAL_DIRECTIONS = [Direction.NorthEast, Direction.SouthEast, Direction.SouthWest, Direction.NorthWest, ]

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
