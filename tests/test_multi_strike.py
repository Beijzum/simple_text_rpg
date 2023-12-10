"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from combat import multi_strike


class TestMultiStrike(TestCase):
    @patch("random.random", return_value=0.8)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_multi_strike_default(self, mock_output, _):
        multi_strike(2)
        actual = mock_output.getvalue()
        expected = "You swing your weapon!\n" \
                   "Your attack hits 2 times!\n"
        self.assertEqual(actual, expected)

    @patch("random.random", return_value=0.2)
    @patch("random.randint", return_value=3)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_multi_strike_three_hits(self, mock_output, _, __):
        multi_strike(2)
        actual = mock_output.getvalue()
        expected = "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "Your attack hits 3 times!\n"
        self.assertEqual(actual, expected)

    @patch("random.random", return_value=0.2)
    @patch("random.randint", return_value=4)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_multi_strike_four_hits(self, mock_output, _, __):
        multi_strike(2)
        actual = mock_output.getvalue()
        expected = "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "Your attack hits 4 times!\n"
        self.assertEqual(actual, expected)

    @patch("random.random", return_value=0.2)
    @patch("random.randint", return_value=5)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_multi_strike_five_hits(self, mock_output, _, __):
        multi_strike(2)
        actual = mock_output.getvalue()
        expected = "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "You swing your weapon!\n" \
                   "Your attack hits 5 times!\n"
        self.assertEqual(actual, expected)
