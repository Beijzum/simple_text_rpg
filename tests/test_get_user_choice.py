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
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_up(self, mock_output, _):
        board = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        get_user_choice(1, 1, board, character)
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "1. Up\n" \
                   "2. Down\n" \
                   "3. Left\n" \
                   "4. Right\n" \
                   "xX------------------------------------------------------Xx\n" \
                   "You chose to go up...\n"
        self.assertEqual(expected, actual)

    @patch("builtins.input", return_value="2")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_down(self, mock_output, _):
        board = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        get_user_choice(1, 1, board, character)
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "1. Up\n" \
                   "2. Down\n" \
                   "3. Left\n" \
                   "4. Right\n" \
                   "xX------------------------------------------------------Xx\n" \
                   "You chose to go down...\n"
        self.assertEqual(expected, actual)

    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_left(self, mock_output, _):
        board = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        get_user_choice(1, 1, board, character)
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "1. Up\n" \
                   "2. Down\n" \
                   "3. Left\n" \
                   "4. Right\n" \
                   "xX------------------------------------------------------Xx\n" \
                   "You chose to go left...\n"
        self.assertEqual(expected, actual)

    @patch("builtins.input", return_value="4")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_right(self, mock_output, _):
        board = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        get_user_choice(1, 1, board, character)
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "1. Up\n" \
                   "2. Down\n" \
                   "3. Left\n" \
                   "4. Right\n" \
                   "xX------------------------------------------------------Xx\n" \
                   "You chose to go right...\n"
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Invalid"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_invalid(self, mock_output, _):
        board = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        with self.assertRaises(StopIteration):
            get_user_choice(1, 1, character, board)
        actual = mock_output.getvalue()
        expected = "Invalid choice."
        self.assertIn(expected, actual)

    @patch("builtins.input", side_effect=["Invalid", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_choice_invalid_input_then_valid(self, mock_output, _):
        board = {(0, 0): "Starting Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        get_user_choice(1, 1, character, board)
        actual = mock_output.getvalue()
        expected = "Invalid choice."
        self.assertIn(expected, actual)
