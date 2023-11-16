"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch("builtins.input", return_value="1")
    def test_get_user_choice_up(self, _):
        expected = "up"
        self.assertEqual(expected, get_user_choice())

    @patch("builtins.input", return_value="2")
    def test_get_user_choice_down(self, _):
        expected = "down"
        self.assertEqual(expected, get_user_choice())

    @patch("builtins.input", return_value="3")
    def test_get_user_choice_left(self, _):
        expected = "left"
        self.assertEqual(expected, get_user_choice())

    @patch("builtins.input", return_value="4")
    def test_get_user_choice_right(self, _):
        expected = "right"
        self.assertEqual(expected, get_user_choice())

    @patch("builtins.input", side_effect=["Invalid"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_invalid(self, mock_output, _):
        with self.assertRaises(StopIteration):
            get_user_choice()
        expected = "Invalid choice. Please choose a valid option (1, 2, 3, or 4)."
        test = mock_output.getvalue()
        self.assertIn(expected, test)

    @patch("builtins.input", side_effect=["5", "2"])
    def test_get_user_choice_invalid_then_valid(self, _):
        test = get_user_choice()
        expected = "down"
        self.assertEqual(expected, test)
