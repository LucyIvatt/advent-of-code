import unittest

from python.year_2025.day_04_printing_department.solution import input_data, part_one, part_two


class TestDay04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2025/day_04_printing_department/example.txt")
        cls.puzzle_input = input_data("python/year_2025/day_04_printing_department/input.txt")

    def test_p1_example(self):
        """
        Tests Day 04 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 13)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 04 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 1416)
        pass

    def test_p2_example(self):
        """
        Tests Day 04 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 43)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 04 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 9086)
        pass


if __name__ == '__main__':
    unittest.main()
