from src.insert_sort import insertion_sort
import unittest


class InsertSortTest(unittest.TestCase):
    # Boundary test (-1000 to 1000) | Arrange Act Assert
    # this test ignore String, out boundry number, complex
    # default
    def test_15_16_2_8_50_35_should_sorted(self):
        data = [15, 16, 2, 8, 50, 35]
        result = insertion_sort(data)
        self.assertListEqual(result, [2, 8, 15, 16, 35, 50])

    # most left
    def test_negative_998_1000_999_should_sorted(self):
        data = [-998, -1000, -999]
        result = insertion_sort(data)
        self.assertListEqual(result, [-1000, -999, -998])

    # middle
    def test_500_501_498_should_sorted(self):
        data = [500, 501, 498]
        result = insertion_sort(data)
        self.assertListEqual(result, [498, 500, 501])

    # most right
    def test_999_998_1000_should_sorted(self):
        data = [999, 998, 1000]
        result = insertion_sort(data)
        self.assertListEqual(result, [998, 999, 1000])

    # mix case
    def test_postive_500_1000_negiative_1000_855_should_sorted(self):
        data = [500, -1000, 1000, -855]
        result = insertion_sort(data)
        self.assertListEqual(result, [-1000, -855, 500, 1000])

    def test_postive_5_88_412_519_124_negiative_42_12_7_555_666_should_sorted(self):
        data = [5, 88, 412, 519, 124, -42, -12, -7, -555, -666]
        result = insertion_sort(data)
        self.assertListEqual(result, [-666, -555, -42, -12, -7, 5, 88, 124, 412, 519])

    # double
    def test_double_postive_33_44_55_66__negiative_77_88_99_100_should_sorted(self):
        data = [6.6, 5.5, 4.4, 3.3, -7.7, -8.8, -10.0, -9.9]
        result = insertion_sort(data)
        self.assertListEqual(result, [-10.0, -9.9, -8.8, -7.7, 3.3, 4.4, 5.5, 6.6])
