class Range:
    def __init__(self, lower, upper):
        self.lower = int(lower)
        self.upper = int(upper)

    def __str__(self):
        return f"Range({self.lower}-{self.upper} - length={self.length})"

    def __repr__(self):
        return f"Range({self.lower}-{self.upper} - length={self.length})"

    @classmethod
    def from_string(cls, range_string):
        return cls(*range_string.split("-"))

    @property
    def length(self): return self.upper - self.lower + 1

    def is_within_range(self, value):
        return self.lower <= int(value) <= self.upper

    def overlaps(self, other):
        return self.lower <= other.upper and other.lower <= self.upper

    def merge(self, other):
        if not self.overlaps(other):
            raise ValueError("Cannot merge ranges which do not overlap")
        else:
            return Range(min(self.lower, other.lower), max(self.upper, other.upper))


def merge_ranges(ranges):
    """Merge overlapping ranges using sorting."""

    ranges.sort(key=lambda r: r.lower)
    merged = [ranges[0]]

    for current in ranges[1:]:
        last = merged[-1]
        if last.overlaps(current):
            merged[-1] = last.merge(current)
        else:
            merged.append(current)

    return merged
