"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from exploration import show_map


class TestShowMap(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_map_at_start(self, mock_value):
        character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
        }
        show_map(5, 5, character)
        actual = mock_value.getvalue()
        expected = "  ------------------------------------------------------\n" \
                   "  | @Player  | (0, 1)   | (0, 2)   | (0, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (1, 0)   | (1, 1)   | (1, 2)   | (1, 3)   | (1, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (2, 0)   | (2, 1)   | $Shop    | (2, 3)   | (2, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (3, 0)   | (3, 1)   | (3, 2)   | (3, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  |#Special  | (4, 1)   | (4, 2)   |#Special  | #Boss  |\n" \
                   "  ------------------------------------------------------\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_map_on_boss(self, mock_value):
        character = {
            "X-coordinate": 4,
            "Y-coordinate": 4,
        }
        show_map(5, 5, character)
        actual = mock_value.getvalue()
        expected = "  ------------------------------------------------------\n" \
                   "  | (0, 0)   | (0, 1)   | (0, 2)   | (0, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (1, 0)   | (1, 1)   | (1, 2)   | (1, 3)   | (1, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (2, 0)   | (2, 1)   | $Shop    | (2, 3)   | (2, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (3, 0)   | (3, 1)   | (3, 2)   | (3, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  |#Special  | (4, 1)   | (4, 2)   |#Special  | @Player|\n" \
                   "  ------------------------------------------------------\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_map_on_shop(self, mock_value):
        character = {
            "X-coordinate": 2,
            "Y-coordinate": 2,
        }
        show_map(5, 5, character)
        actual = mock_value.getvalue()
        expected = "  ------------------------------------------------------\n" \
                   "  | (0, 0)   | (0, 1)   | (0, 2)   | (0, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (1, 0)   | (1, 1)   | (1, 2)   | (1, 3)   | (1, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (2, 0)   | (2, 1)   | @Player  | (2, 3)   | (2, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (3, 0)   | (3, 1)   | (3, 2)   | (3, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  |#Special  | (4, 1)   | (4, 2)   |#Special  | #Boss  |\n" \
                   "  ------------------------------------------------------\n"
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_map_on_special(self, mock_value):
        character = {
            "X-coordinate": 4,
            "Y-coordinate": 0,
        }
        show_map(5, 5, character)
        actual = mock_value.getvalue()
        expected = "  ------------------------------------------------------\n" \
                   "  | (0, 0)   | (0, 1)   | (0, 2)   | (0, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (1, 0)   | (1, 1)   | (1, 2)   | (1, 3)   | (1, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (2, 0)   | (2, 1)   | $Shop    | (2, 3)   | (2, 4) |\n" \
                   "  ------------------------------------------------------\n" \
                   "  | (3, 0)   | (3, 1)   | (3, 2)   | (3, 3)   |#Special|\n" \
                   "  ------------------------------------------------------\n" \
                   "  | @Player  | (4, 1)   | (4, 2)   |#Special  | #Boss  |\n" \
                   "  ------------------------------------------------------\n"
        self.assertEqual(expected, actual)
