import unittest

from python.year_2025.day_03_lobby.solution import input_data, part_one, part_two


class TestDay03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2025/day_03_lobby/example.txt")
        cls.puzzle_input = input_data(
            "python/year_2025/day_03_lobby/input.txt")

    def test_p1_example(self):
        """
        Tests Day 03 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 357)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 03 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 16973)
        pass

    def test_p2_example(self):
        """
        Tests Day 03 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 3121910778619)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 03 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 0)
        pass


if __name__ == '__main__':
    unittest.main()
