import math

DIRECTION = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def input_data(filename):
    """Returns the data imported from file - pairs of directions and number of steps
    """
    file = open(filename, "r")
    input = [line.strip() for line in file.readlines()]
    file.close()
    input = [(pair[0], int(pair[2])) for pair in input]
    return input


def move_tail(head, tail):
    """Moves the tail based on the distances to the head of the rope.
    """
    tx, ty = tail
    dx, dy = head[0]-tail[0], head[1]-tail[1]

    # if they are within 1 of each other or overlapping - no change
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail

    # if on same row or on a diagonal
    if abs(dx) == 2 or abs(dx) + abs(dy) == 3:
        if dx == 0:
            print("Help")
        tx += int(math.copysign(1, dx))

    # if on same column or a diagonal
    if abs(dy) == 2 or abs(dx) + abs(dy) == 3:
        if dy == 0:
            print("Help")
        ty += int(math.copysign(1, dy))

    return (tx, ty)


def part_one(input):
    h, t = (0, 0), (0, 0)
    t_positions = [(0, 0)]
    for direction, num in input:
        for _ in range(num):
            h = tuple(map(sum, zip(h, DIRECTION[direction[0]])))
            t = move_tail(h, t)

            if t not in t_positions:
                t_positions.append(t)

    return len(t_positions)


input = input_data("day9/input.txt")

print("--------------------------------------")
print("Day 9: Rope Bridge")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: ")
print("--------------------------------------")