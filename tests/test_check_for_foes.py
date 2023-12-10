"""
Jason Chow
A00942129
"""
from unittest import TestCase
from unittest.mock import patch
from enemy import check_for_foes


class TestCheckForFoes(TestCase):
    @patch("random.random", return_value=0.25)
    def test_check_for_foes_true(self, _):
        expected = True
        test = check_for_foes()
        self.assertEqual(expected, test)

    @patch("random.random", return_value=0.26)
    def test_check_for_foes_false(self, _):
        expected = False
        test = check_for_foes()
        self.assertEqual(expected, test)
