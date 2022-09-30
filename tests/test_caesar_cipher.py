import unittest

from src.caesar_cipher import caesar_cipher


class FunnyStringsTest(unittest.TestCase):
    def test_middle_Outz_with_2_should_be_okffng_Qwvb(self):
        result = caesar_cipher("middle-Outz", 2)
        self.assertEqual(result, "okffng-Qwvb")

    def test_Always_Look_on_the_Bright_Side_of_Life_with_5_should_be_Fqbfdx_Qttp_ts_ymj_Gwnlmy_Xnij_tk_Qnkj(
        self,
    ):
        result = caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5)
        self.assertEqual(result, "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")

    def test_hello_wahti_year_is_hisss_with_8_should_be_pmttw_eipbq_gmiz_qa_pqaaa(self):
        result = caesar_cipher("hello_wahti_year_is_hisss", 8)
        self.assertEqual(result, "pmttw_eipbq_gmiz_qa_pqaaa")

    def test_abcdefghijklmnopqrstuvwxyz_with_12_should_be_mnopqrstuvwxyzabcdefghijkl(
        self,
    ):
        result = caesar_cipher("abcdefghijklmnopqrstuvwxyz", 12)
        self.assertEqual(result, "mnopqrstuvwxyzabcdefghijkl")

    def test_abcdefghijklmnopqrstuvwxyz_with_12_should_be_nopqrstuvwxyzabcdefghijklm(
        self,
    ):
        result = caesar_cipher("abcdefghijklmnopqrstuvwxyz", 13)
        self.assertEqual(result, "nopqrstuvwxyzabcdefghijklm")
