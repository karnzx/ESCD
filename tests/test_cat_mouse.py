import unittest

from src.cat_mouse import cat_mouse


class CatMouseTest(unittest.TestCase):
    def test_1_2_3_should_be_cat_b(self):
        result = cat_mouse(1, 2, 3)
        self.assertEqual(result, "Cat B")

    def test_1_3_2_should_be_mouse_c(self):
        result = cat_mouse(1, 3, 2)
        self.assertEqual(result, "Mouse C")

    def test_1_5_4_should_be_cat_b(self):
        result = cat_mouse(1, 5, 4)
        self.assertEqual(result, "Cat B")

    def test_100_23_80_should_be_cat_b(self):
        result = cat_mouse(100, 24, 80)
        self.assertEqual(result, "Cat A")

    def test_n49_50_0_should_be_cat_b(self):
        result = cat_mouse(-49, 50, 0)
        self.assertEqual(result, "Cat A")
