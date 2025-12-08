import unittest

from python.year_2025.day_08_playground.solution import input_data, part_one, part_two


class TestDay08(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2025/day_08_playground/example.txt")
        cls.puzzle_input = input_data("python/year_2025/day_08_playground/input.txt")

    def test_p1_example(self):
        """
        Tests Day 08 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example, 10), 40)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 08 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input, 1000), 79560)
        pass

    def test_p2_example(self):
        """
        Tests Day 08 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 25272)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 08 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 31182420)
        pass


if __name__ == '__main__':
    unittest.main()
