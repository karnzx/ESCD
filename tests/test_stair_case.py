from src.stair_case import stair_case

import unittest


class StairCaseTest(unittest.TestCase):
    # AAA (Arrange Act Assert)
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = "#"
        expected_output = " #\n" + "##\n"

        # act
        result = stair_case(n, pattern)
        print(result)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")
