import unittest

from python.year_2025.day_11_reactor.solution import input_data, part_one, part_two
from python.year_2025.day_11_reactor import solution


class TestDay11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2025/day_11_reactor/example.txt")
        cls.example_2 = input_data("python/year_2025/day_11_reactor/example2.txt")
        cls.puzzle_input = input_data("python/year_2025/day_11_reactor/input.txt")

    def tearDown(self):
        """Clear cache after each test to prevent pollution between tests"""
        solution.CACHE.clear()

    def test_p1_example(self):
        """
        Tests Day 11 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 5)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 11 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 724)
        pass

    def test_p2_example(self):
        """
        Tests Day 11 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example_2), 2)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 11 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 473930047491888)
        pass


if __name__ == '__main__':
    unittest.main()
