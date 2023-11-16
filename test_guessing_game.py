"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from game import guessing_game


class TestGuessingGame(TestCase):
    @patch("random.randint", return_value=3)
    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_guess_right_number(self, mock_output, _, __):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected = "\"Holy moly! How are you so smart?!\""
        self.assertIn(expected, the_game_printed_this)

    @patch("random.randint", return_value=3)
    @patch("builtins.input", return_value="5")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_guess_wrong_number(self, mock_output, _, __):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected = "The annoying little demon kicks your butt and you lose 1 HP."
        self.assertIn(expected, the_game_printed_this)

    @patch("random.randint", return_value=3)
    @patch("builtins.input", return_value="weewoo")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_guess_invalid_input(self, mock_output, _, __):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected = "\"That's not what I was asking for, idiot.\""
        self.assertIn(expected, the_game_printed_this)
