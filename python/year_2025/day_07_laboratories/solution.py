from python.helpers.misc import input_data, time_function


def part_one(puzzle_input):
    beam_locations = set([puzzle_input[0].index("S")])
    num_splits = 0

    for row in puzzle_input:
        new_beams = set()
        for beam in beam_locations:
            if row[beam] == "^":
                num_splits += 1
                if (beam-1 >= 0):
                    new_beams.add(beam-1)
                if (beam + 1 < len(row)):
                    new_beams.add(beam+1)
            else:
                new_beams.add(beam)
        beam_locations = new_beams
    return num_splits


def part_two(puzzle_input):
    pass


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
