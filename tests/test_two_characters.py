import unittest

from src.two_characters import two_characters


class TwoCharactersTest(unittest.TestCase):
    def test_asdcbsdcagfsdbgdfanfghbsfdab_should_be_8(self):
        result = two_characters("asdcbsdcagfsdbgdfanfghbsfdab")
        self.assertEqual(result, 8)

    def test_beabeefeab_should_be_5(self):
        result = two_characters("beabeefeab")
        self.assertEqual(result, 5)

    def test_asvkugfiugsalddlasguifgukvsa_should_be_0(self):
        result = two_characters("asvkugfiugsalddlasguifgukvsa")
        self.assertEqual(result, 0)
