from collections import defaultdict
import math
from operator import itemgetter
import time
from python.helpers.misc import input_data, time_function
from itertools import combinations


class Circuit:
    def __init__(self, node1, node2):
        self.graph = defaultdict(set)
        self.add_connection(node1, node2)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

    def add_connection(self, node1, node2):
        n1 = tuple(node1)
        n2 = tuple(node2)
        self.graph[n1].add(n2)
        self.graph[n2].add(n1)

    def hasNode(self, node):
        return tuple(node) in self.graph

    def merge(self, other):
        dd = defaultdict(set)
        for d in (self.graph, other.graph):
            for key, neighbours in d.items():
                for n in neighbours:
                    dd[key].add(n)
                    dd[n].add(key)
        self.graph = dd

    def clear(self):
        self.graph = defaultdict(set)

    def get_size(self):
        return len(self.graph.keys())


def straight_line_distance(first, second):
    return math.sqrt(math.pow(second[0]-first[0], 2) + math.pow(second[1]-first[1], 2) + math.pow(second[2]-first[2], 2))


def part_one(puzzle_input):
    num_pairs = 1000
    coords = [list(map(int, line.split(','))) for line in puzzle_input]
    distances = [((tuple(pair[0]), tuple(pair[1])), straight_line_distance(pair[0], pair[1]))
                 for pair in combinations(coords, 2)]
    sorted_distances = sorted(distances, key=itemgetter(1))

    circuits = []
    connections = 0
    i = 0
    while connections < num_pairs:
        pair, distance = sorted_distances[i]
        i += 1

        box1, box2 = pair
        # print("Attempting to connect ", box1, " and ", box2)

        # No circuit containers either box
        if all(not circuit.hasNode(box1) and not circuit.hasNode(box2) for circuit in circuits):
            circuits.append(Circuit(box1, box2))
            connections += 1
            # print("No circuit contains the boxes - creating new circuit")
            # print([str(c) for c in circuits])

        # A circuit contains both boxes
        elif any(circuit.hasNode(box1) and circuit.hasNode(box2) for circuit in circuits):
            # print("A circuit contains both boxes - skipping!")
            continue

        else:
            for j in range(len(circuits)):
                # A circuit contains one box (box 1)
                if circuits[j].hasNode(box1) and all(not c.hasNode(box1) for c in circuits if c != circuits[j]):
                    circuits[j].add_connection(box1, box2)
                    connections += 1
                    # print("A circuit contains box 1 - adding connection to box2")
                    break

                    # A circuit contains one box (box 2)
                elif circuits[j].hasNode(box2) and all(not c.hasNode(box2) for c in circuits if c != circuits[j]):
                    circuits[j].add_connection(box2, box1)
                    connections += 1
                    # print("A circuit contains box 2 - adding connection to box1")
                    break

                # two diff circuits contain box
                elif circuits[j].hasNode(box1) and any(c.hasNode(box2) for c in circuits if c != circuits[j]):
                    index_2_c = next(i for i, c in enumerate(circuits) if c.hasNode(box2))
                    circuits[j].merge(circuits[index_2_c])
                    circuits.pop(index_2_c)
                    connections += 1
                    # print("Two diff circuits contain the boxes - merging")
                    # print(str(c) for c in circuits)
                    break

            # print("----")
            # print("ERROR I SHOULD NEVER GET HERE")
            # print("box1", box1)
            # print("box2", box2)
            # print("circuits", [str(c) for c in circuits])
            # print("----")
            # break

    return math.prod(sorted([c.get_size() for c in circuits])[-3:])


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("python/year_2025/day_08_playground/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 08: playground")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
