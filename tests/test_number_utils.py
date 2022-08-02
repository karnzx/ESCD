from src.number_utils import is_prime_list

import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_2_3_is_prime(self):
        prime_list = [2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_89_97_is_prime(self):
        prime_list = [89, 97]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_89_99_is_not_prime(self):
        prime_list = [89, 99]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_negative_1_2_3_is_not_prime(self):
        prime_list = [-1, -2, -3]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_0_is_not_prime(self):
        prime_list = [0]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_string_1_is_not_prime(self):
        prime_list = [1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
