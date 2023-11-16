"""
Jason Chow
A00942129
"""
from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):
    @patch("random.choice", side_effect=["Empty Room"] * 8 + ["Chocolate Room"])
    def test_make_board_3_by_3_same_integer(self, _):
        rows = 3
        columns = 3
        expected = {
            (0, 0): "Starting Room",
            (0, 1): "Empty Room",
            (0, 2): "Empty Room",
            (1, 0): "Empty Room",
            (1, 1): "Empty Room",
            (1, 2): "Empty Room",
            (2, 0): "Empty Room",
            (2, 1): "Empty Room",
            (2, 2): "Chocolate Room",
        }

        test = make_board(rows, columns)
        self.assertEqual(expected, test)

    @patch("random.choice", side_effect=["Dark Room"] * 10 + ["Chocolate Room"])
    def test_make_board_4_by_3_different_integer(self, _):
        rows = 4
        columns = 3
        expected = {(0, 0): 'Starting Room',
                    (0, 1): 'Dark Room',
                    (0, 2): 'Dark Room',
                    (1, 0): 'Dark Room',
                    (1, 1): 'Dark Room',
                    (1, 2): 'Dark Room',
                    (2, 0): 'Dark Room',
                    (2, 1): 'Dark Room',
                    (2, 2): 'Dark Room',
                    (3, 0): 'Dark Room',
                    (3, 1): 'Dark Room',
                    (3, 2): 'Chocolate Room'}

        test = make_board(rows, columns)
        self.assertEqual(expected, test)
