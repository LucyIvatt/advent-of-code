import unittest

from python.year_2025.day_01_secret_entrance.solution import input_data, part_one, part_two, calculate_rotation


class TestDay01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2025/day_01_secret_entrance/example.txt")
        cls.puzzle_input = input_data("python/year_2025/day_01_secret_entrance/input.txt")

    def test_calculate_rotation(self):
        test_cases = [
            # Basic moves (no wrap)
            {"pos": 50, "dir": "L", "steps": 50, "expected": (0, 1), "name": "Left exact wrap"},
            {"pos": 50, "dir": "R", "steps": 50, "expected": (0, 1), "name": "Right exact wrap"},
            {"pos": 0,  "dir": "L", "steps": 50, "expected": (50, 0), "name": "Left from zero"},
            {"pos": 0,  "dir": "R", "steps": 50, "expected": (50, 0), "name": "Right from zero"},

            # Larger moves with multiple wraps
            {"pos": 5,  "dir": "L", "steps": 105, "expected": (0, 2), "name": "Left wrap"},
            {"pos": 5,  "dir": "R", "steps": 105, "expected": (10, 1), "name": "Right wrap"},
            {"pos": 42, "dir": "L", "steps": 200, "expected": (42, 2), "name": "Left large exact"},
            {"pos": 42, "dir": "R", "steps": 200, "expected": (42, 2), "name": "Right large exact"},

            # Boundary conditions
            {"pos": 0,  "dir": "L", "steps": 1,   "expected": (99, 0), "name": "Left from 0 wrap"},
            {"pos": 0,  "dir": "R", "steps": 1,   "expected": (1, 0),  "name": "Right from 0"},
            {"pos": 99, "dir": "R", "steps": 1,   "expected": (0, 1),  "name": "Right into wrap"},
            {"pos": 99, "dir": "L", "steps": 1,   "expected": (98, 0), "name": "Left from max"},
            {"pos": 0,  "dir": "R", "steps": 100, "expected": (0, 1),  "name": "Right full rotation"},
            {"pos": 0,  "dir": "L", "steps": 100, "expected": (0, 1),  "name": "Left full rotation"},
        ]

        for case in test_cases:
            with self.subTest(case=case["name"]):
                result = calculate_rotation(case["pos"], case["dir"], case["steps"])
                self.assertEqual(result, case["expected"])

    def test_p1_example(self):
        """
        Tests Day 01 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 3)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 01 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 1145)
        pass

    def test_p2_example(self):
        """
        Tests Day 01 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 6)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 01 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 6561)
        pass


if __name__ == '__main__':
    unittest.main()
