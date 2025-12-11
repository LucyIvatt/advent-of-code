import re
import string
from python.helpers.misc import input_data, time_function
from z3 import *


pattern = r'^\[([^\]]+)\]\s*((?:\([^)]*\)\s*)+)\s*(\{[^}]+\})$'


def part_one(puzzle_input):
    total_presses = 0
    for line in puzzle_input:
        m = re.match(pattern, line)

        lights, buttons, _ = m.groups()

        buttons = [[int(n) for n in c.strip("()").split(",") if n] for c in buttons.split()]

        button_masks = []
        for btn in buttons:
            mask = 0
            for idx in btn:
                mask |= (1 << idx)
            button_masks.append(mask)

        lights_mask = 0
        for i, ch in enumerate(lights):
            if ch == "#":
                lights_mask |= (1 << i)

        not_valid = True
        press_count = 0

        press_tracker = [(x, 0) for x in range(len(button_masks))]
        visited = {f"{x}-{y}" for x, y in press_tracker}

        while not_valid:
            press_count += 1
            new_press_tracker = []

            for next_button, current_lights in press_tracker:
                current_lights ^= button_masks[next_button]

                if current_lights == lights_mask:
                    not_valid = False
                    break
                else:
                    for x in range(len(button_masks)):
                        state = f"{x}-{current_lights}"
                        if state not in visited:
                            visited.add(state)
                            new_press_tracker.append((x, current_lights))

            press_tracker = new_press_tracker
        total_presses += press_count
    return total_presses


def part_two(puzzle_input):
    total_presses = 0
    for line in puzzle_input:
        m = re.match(pattern, line)

        _, buttons, joltage = m.groups()

        joltage = [int(n) for n in joltage.strip("{}").split(",")]
        buttons = [[int(n) for n in c.strip("()").split(",") if n] for c in buttons.split()]

        button_vars = {b_i: Int(string.ascii_lowercase[b_i]) for b_i in range(len(buttons))}

        o = Optimize()

        for var in button_vars.values():
            o.add(var >= 0)

        for i in range(len(joltage)):
            o.add(sum(button_vars[j] for j in range(len(button_vars)) if i in buttons[j]) == joltage[i])

        o.minimize(sum(button_vars.values()))
        o.check()
        model = o.model()

        total = sum(model[v].as_long() for v in button_vars.values())
        total_presses += total
    return total_presses


def main():
    puzzle_input = input_data("python/year_2025/day_10_factory/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 10: factory")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
