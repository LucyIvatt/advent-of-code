from python.helpers.misc import input_data, time_function
from collections import Counter


def track_beams(puzzle_input):
    start = puzzle_input[0].index("S")

    path_counts = Counter({start: 1})
    beams = {start}

    split_count = 0

    for row in puzzle_input:
        new_path_counts = Counter()
        new_beams = set()

        for beam in beams:
            path_count = path_counts[beam]

            if row[beam] == "^":
                split_count += 1
                for split_beam in (beam - 1, beam + 1):
                    new_beams.add(split_beam)
                    new_path_counts[split_beam] += path_count
            else:
                new_beams.add(beam)
                new_path_counts[beam] += path_count

        beams = new_beams
        path_counts = new_path_counts

    return split_count, path_counts


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
