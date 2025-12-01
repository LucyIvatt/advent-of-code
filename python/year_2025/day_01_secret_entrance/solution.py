from python.helpers.aoc_utils import input_data, time_function

def calculateRotation(pos, dir, val):
    rotations = val // 100
    newPos = abs((pos + val * (1 if dir == "R" else -1)) % 100) 

    if (newPos == 0 or (dir == "L" and newPos > pos) or (dir == "R" and newPos < pos)) and pos != 0:
        rotations += 1

    return (newPos, rotations)

def part_one(puzzle_input):
    count, pos = 0, 50

    for (direction, value) in [(line[0], int(line[1:])) for line in puzzle_input]: 
        pos, _ = calculateRotation(pos, direction, value)
        if pos == 0: count += 1

    return count

def part_two(puzzle_input):
    count, pos = 0, 50

    for (direction, value) in [(line[0], int(line[1:])) for line in puzzle_input]: 
        pos, passedZero = calculateRotation(pos, direction, value)
        count += passedZero

    return count

    

def main():
    puzzle_input = input_data("python/year_2025/day_01_secret_entrance/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 01: secret_entrance")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")

if __name__ == "__main__":
    main()
