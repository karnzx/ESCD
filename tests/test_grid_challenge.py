import unittest

from src.grid_challenge import grid_challenge


class GridChallengeTest(unittest.TestCase):
    def test_abc_lmp_qrt_should_be_YES(self):
        result = grid_challenge(["abc", "lmp", "qrt"])
        self.assertEqual(result, "YES")

    def test_eabcd_fghij_olkmn_trpqs_xywuv_should_be_YES(self):
        result = grid_challenge(["eabcd", "fghij", "olkmn", "trpqs", "xywuv"])
        self.assertEqual(result, "YES")

    def test_mpxz_abcd_wlmf_should_be_NO(self):
        result = grid_challenge(["mpxz", "abcd", "wlmf"])
        self.assertEqual(result, "NO")

    def test_abc_hjk_mpq_should_be_YES(self):
        result = grid_challenge(["abc", "hjk", "mpq"])
        self.assertEqual(result, "YES")
