import unittest

from src.fizz_buzz import get_fizz_buzz


class FizBuzzTesst(unittest.TestCase):
    def test_3_should_fizz(self):
        result = get_fizz_buzz(3)
        self.assertEqual(result, "Fizz")

    def test_5_should_buzz(self):
        result = get_fizz_buzz(5)
        self.assertEqual(result, "Buzz")

    def test_15_should_fizzbuzz(self):
        result = get_fizz_buzz(15)
        self.assertEqual(result, "FizzBuzz")

    # -Boundary test (1-1000)
    # most left
    def test_negative_should_none(self):
        result = get_fizz_buzz(-1)
        self.assertEqual(result, "")

    def test_0_should_fizzbuzz(self):
        result = get_fizz_buzz(0)
        self.assertEqual(result, "FizzBuzz")

    def test_1_should_none(self):
        result = get_fizz_buzz(1)
        self.assertEqual(result, "")

    # middle
    def test_500_should_buzz(self):
        result = get_fizz_buzz(500)
        self.assertEqual(result, "Buzz")

    # most right
    def test_999_should_fizz(self):
        result = get_fizz_buzz(999)
        self.assertEqual(result, "Fizz")

    def test_1000_should_buzz(self):
        result = get_fizz_buzz(1000)
        self.assertEqual(result, "Buzz")

    def test_1001_should_none(self):
        result = get_fizz_buzz(1001)
        self.assertEqual(result, "")
