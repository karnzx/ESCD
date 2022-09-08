import unittest

from src.super_fizz_buzz import SuperFizzBuzz


class SuperFizzBuzzTest(unittest.TestCase):
    # common
    def test_3_should_fizz(self):
        result = SuperFizzBuzz(3).get_fizz_buzz()
        self.assertEqual(result, "Fizz")

    def test_5_should_buzz(self):
        result = SuperFizzBuzz(5).get_fizz_buzz()
        self.assertEqual(result, "Buzz")

    def test_15_should_fizzbuzz(self):
        result = SuperFizzBuzz(15).get_fizz_buzz()
        self.assertEqual(result, "FizzBuzz")

    def test_9_should_fizzfizz(self):
        result = SuperFizzBuzz(9).get_fizz_buzz()
        self.assertEqual(result, "FizzFizz")

    def test_25_should_buzzbuzz(self):
        result = SuperFizzBuzz(25).get_fizz_buzz()
        self.assertEqual(result, "BuzzBuzz")

    def test_225_should_fizzfizzbuzzbuzz(self):
        result = SuperFizzBuzz(225).get_fizz_buzz()
        self.assertEqual(result, "FizzFizzBuzzBuzz")

    # -Boundary test postive number(0-10,000)
    # most left
    def test_0_should_fizzfizzbuzzbuzz(self):
        result = SuperFizzBuzz(0).get_fizz_buzz()
        self.assertEqual(result, "FizzFizzBuzzBuzz")

    def test_1_should_nofizzbuzz(self):
        result = SuperFizzBuzz(1).get_fizz_buzz()
        self.assertEqual(result, "NoFizzBuzz")

    # middle
    def test_500_should_buzzbuzz(self):
        result = SuperFizzBuzz(500).get_fizz_buzz()
        self.assertEqual(result, "BuzzBuzz")

    # most right
    def test_9999_should_fizzfizz(self):
        result = SuperFizzBuzz(9999).get_fizz_buzz()
        self.assertEqual(result, "FizzFizz")

    def test_10000_should_buzzbuzz(self):
        result = SuperFizzBuzz(10000).get_fizz_buzz()
        self.assertEqual(result, "BuzzBuzz")
