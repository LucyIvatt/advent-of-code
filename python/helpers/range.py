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
