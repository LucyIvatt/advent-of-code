from python.helpers.misc import input_data, time_function
from collections import defaultdict


def part_one(puzzle_input):
    beam_locations = set([puzzle_input[0].index("S")])
    num_splits = 0

    for row in puzzle_input:
        new_beams = set()
        for beam in beam_locations:
            if row[beam] == "^":
                num_splits += 1
                new_beams.add(beam-1)
                new_beams.add(beam+1)
            else:
                new_beams.add(beam)
        beam_locations = new_beams
    print(beam_locations)
    return num_splits


def part_two(puzzle_input):
    paths = defaultdict(lambda: 0)
    paths[puzzle_input[0].index("S")] = 1

    beam_locations = set([puzzle_input[0].index("S")])

    for row in puzzle_input:
        new_beams = set()
        new_paths = defaultdict(lambda: 0)
        for beam in beam_locations:
            if row[beam] == "^":
                print("splitting")
                new_beams.add(beam-1)
                new_beams.add(beam+1)
                new_paths[beam-1] += paths[beam]
                new_paths[beam+1] += paths[beam]
            else:
                new_beams.add(beam)
                new_paths[beam] += paths[beam]

        beam_locations = new_beams
        paths = new_paths
        print(paths)
        print(beam_locations)
        print("----")
    return sum(paths.values())


#     s = Node(name="root", location=puzzle_input[0].index("S"))
#     num_splits = 0

#     for i in range(1, len(puzzle_input)):
#         for beam in [n for n in PreOrderIter(s) if n.is_leaf]:
#             if puzzle_input[i][beam.location] == "^":
#                 num_splits += 1

#                 if (beam.location - 1 >= 0):
#                     Node(name=f"left-{beam.location}-row{i}", location=beam.location-1, parent=beam)
#                 if (beam.location + 1 < len(puzzle_input[i])):
#                     Node(name=f"right-{beam.location}-row{i}", location=beam.location+1, parent=beam)

#     return num_splits


def main():
    puzzle_input = input_data("python/year_2025/day_07_laboratories/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 07: laboratories")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
