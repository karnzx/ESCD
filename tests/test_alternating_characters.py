import unittest

from src.alternating_characters import alternating_characters


class FunnyStringsTest(unittest.TestCase):
    def test_AAAA_should_be_3(self):
        result = alternating_characters("AAAA")
        self.assertEqual(result, 3)

    def test_BBBBB_should_be_4(self):
        result = alternating_characters("BBBBB")
        self.assertEqual(result, 4)

    def test_ABABABAB_should_be_0(self):
        result = alternating_characters("ABABABAB")
        self.assertEqual(result, 0)

    def test_BABABA_should_be_0(self):
        result = alternating_characters("BABABA")
        self.assertEqual(result, 0)

    def test_AAABBB_should_be_4(self):
        result = alternating_characters("AAABBB")
        self.assertEqual(result, 4)
