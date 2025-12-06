import unittest

from python.year_2025.day_06_trash_compactor.solution import input_data, part_one, part_two


class TestDay06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2025/day_06_trash_compactor/example.txt", False)
        cls.puzzle_input = input_data("python/year_2025/day_06_trash_compactor/input.txt", False)

    def test_p1_example(self):
        """
        Tests Day 06 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 4277556)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 06 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 3261038365331)
        pass

    def test_p2_example(self):
        """
        Tests Day 06 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 3263827)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 06 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 8342588849093)
        pass


if __name__ == '__main__':
    unittest.main()
