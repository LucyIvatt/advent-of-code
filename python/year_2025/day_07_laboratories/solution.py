from python.helpers.misc import input_data, time_function
from collections import defaultdict


def track_beams(puzzle_input):
    start_location = puzzle_input[0].index("S")

    paths = defaultdict(lambda: 0)
    paths[start_location] = 1

    beam_locations = set([start_location])
    split_count = 0

    for row in puzzle_input:
        new_beams = set()
        new_paths = defaultdict(lambda: 0)
        for beam in beam_locations:
            if row[beam] == "^":
                split_count += 1
                new_beams.add(beam-1)
                new_beams.add(beam+1)
                new_paths[beam-1] += paths[beam]
                new_paths[beam+1] += paths[beam]
            else:
                new_beams.add(beam)
                new_paths[beam] += paths[beam]

        beam_locations = new_beams
        paths = new_paths
    return split_count, paths


def part_one(puzzle_input):
    return track_beams(puzzle_input)[0]


def part_two(puzzle_input):

    return sum(track_beams(puzzle_input)[1].values())


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
