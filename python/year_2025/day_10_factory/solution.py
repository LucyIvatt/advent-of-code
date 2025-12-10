import ast
from collections import defaultdict
import re
import time
from python.helpers.misc import input_data, time_function  # f
from ast import literal_eval

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

        joltage_target = tuple(int(x) for x in joltage.strip("{}").split(","))

        print(joltage)

        buttons = [[int(n) for n in c.strip("()").split(",") if n] for c in buttons.split()]

        press_count = 0
        not_valid = True
        visited = {}
        first = (tuple(0 for _ in joltage_target))
        press_tracker = [first]
        visited = {first}

        while not_valid:
            press_count += 1
            new_press_tracker = []

            for current_joltage in press_tracker:
                for button in buttons:
                    new_joltage = list(current_joltage)

                    for i in button:
                        new_joltage[i] += 1
                    new_joltage = tuple(new_joltage)

                    if joltage_target == new_joltage:
                        not_valid = False
                        break
                    else:
                        if not any([a > b for a, b in zip(new_joltage, joltage_target)]) and new_joltage not in visited:
                            visited.add(new_joltage)
                            new_press_tracker.append(new_joltage)

            press_tracker = new_press_tracker
        total_presses += press_count
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
