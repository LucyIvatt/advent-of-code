import ast
import re
from python.helpers.misc import input_data, time_function  # f
from ast import literal_eval

pattern = r'^\[([^\]]+)\]\s*((?:\([^)]*\)\s*)+)\s*(\{[^}]+\})$'


def part_one(puzzle_input):
    total_presses = 0
    for line in puzzle_input:
        m = re.match(pattern, line)

        lights, buttons, joltage = m.groups()

        buttons = [
            [int(n) for n in c.strip("()").split(",") if n]
            for c in buttons.split()
        ]
        lights

        press_count = 0
        press_tracker = [(x, list("." * len(lights))) for x in range(len(buttons))]
        not_valid = True

        while not_valid:
            press_count += 1
            new_press_tracker = []
            for next_button, current_lights in press_tracker:
                for toggle in buttons[next_button]:
                    current_lights[toggle] = "." if current_lights[toggle] == "#" else "#"
                if "".join(current_lights) == lights:
                    not_valid = False
                    break
                else:
                    new_press_tracker += [(x, current_lights) for x in range(len(buttons))]

            press_tracker = new_press_tracker
        total_presses += press_count
        print(press_count)
    return total_presses


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("python/year_2025/day_10_factory/example.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 10: factory")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
