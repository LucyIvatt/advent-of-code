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
        for node, neighbors in other.graph.items():
            if node not in self.graph:
                self.graph[node] = set()
            self.graph[node].update(neighbors)
        # Ensure all neighbors point back to the node
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in self.graph:
                    self.graph[neighbor] = set()
                self.graph[neighbor].add(node)

    def clear(self):
        self.graph = defaultdict(set)

    def get_size(self):
        return len(self.graph.keys())


def straight_line_distance(first, second):
    return math.sqrt(math.pow(second[0]-first[0], 2) + math.pow(second[1]-first[1], 2) + math.pow(second[2]-first[2], 2))


def part_one(puzzle_input):
    num_pairs = 10
    coords = [list(map(int, line.split(','))) for line in puzzle_input]
    distances = [((tuple(pair[0]), tuple(pair[1])), straight_line_distance(pair[0], pair[1]))
                 for pair in combinations(coords, 2)]
    sorted_distances = sorted(distances, key=itemgetter(1))

    circuits = []
    connections = 0
    i = 0
    start_time = time.time()

    # Simple prints: provide readable runtime info for debugging
    print(f"part_one: starting loop, num_pairs={num_pairs} total_candidates={len(sorted_distances)}")
    while connections < num_pairs:
        pair, distance = sorted_distances[i]
        i += 1

        box1, box2 = pair

        elapsed = time.time() - start_time
        print(f"loop iter: i={i} connections={connections} elapsed={elapsed:.4f}s pair={pair} distance={distance:.4f} circuits={len(circuits)}")

        # No circuit contains either box
        if all(not circuit.hasNode(box1) and not circuit.hasNode(box2) for circuit in circuits):
            print(f"creating new circuit for {box1} <-> {box2} (distance={distance:.4f})")
            circuits.append(Circuit(box1, box2))
            connections += 1

        # A circuit contains both boxes
        elif any(circuit.hasNode(box1) and circuit.hasNode(box2) for circuit in circuits):
            print(f"both boxes already connected: {box1} & {box2} -- skipping")
            continue

        #
        elif any(circuit.hasNode(box1) for circuit in circuits) and all(not circuit.hasNode(box2) for circuit in circuits):
            aaaa = next(i for i, c in enumerate(circuits) if c.hasNode(box1))
            print(f"adding connection {box1} -> {box2} into circuit index {aaaa}")
            circuits[aaaa].add_connection(box1, box2)
            connections += 1

        elif any(circuit.hasNode(box2) for circuit in circuits) and all(not circuit.hasNode(box1) for circuit in circuits):
            aaaa = next(i for i, c in enumerate(circuits) if c.hasNode(box2))
            print(f"adding connection {box1} -> {box2} into circuit index {aaaa}")
            circuits[aaaa].add_connection(box1, box2)
            connections += 1

        else:
            # Two different circuits contain the boxes
            a = next(i for i, c in enumerate(circuits) if c.hasNode(box1))
            b = next(i for i, c in enumerate(circuits) if c.hasNode(box2))
            print(f"merging circuits: index {a} (box1) and index {b} (box2)")

            if a > b:
                a, b = b, a  # ensure b > a
            circuits[a].merge(circuits[b])
            circuits.pop(b)

            connections += 1

        # End of iteration summary
        print(f"after iter: connections={connections} circuits={len(circuits)} top_sizes={sorted([c.get_size() for c in circuits], reverse=True)[:5]}")

    return math.prod(sorted([c.get_size() for c in circuits])[-3:])


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("python/year_2025/day_08_playground/example.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 08: playground")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
