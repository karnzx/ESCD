import unittest

from src.funny_strings import funny_strings


class FunnyStringsTest(unittest.TestCase):
    def test_acxz_should_funny(self):
        result = funny_strings("acxz")
        self.assertEqual(result, "Funny")

    def test_bcxz_should_not_funny(self):
        result = funny_strings("bcxz")
        self.assertEqual(result, "Not Funny")

    def test_ivvkxq_should_not_funny(self):
        result = funny_strings("ivvkxq")
        self.assertEqual(result, "Not Funny")

    def test_ivvkx_should_not_funny(self):
        result = funny_strings("ivvkx")
        self.assertEqual(result, "Not Funny")

    def test_asdbx_should_not_funny(self):
        result = funny_strings("asdbx")
        self.assertEqual(result, "Not Funny")
