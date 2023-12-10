"""
Jason Chow
A00942129
"""
from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):
    @patch("random.choice", side_effect=["Empty Room"] * 2)
    def test_make_board_3_by_3(self, _):
        rows = 3
        columns = 3
        expected = {
            (0, 0): "Starting Room",
            (0, 1): "Empty Room",
            (0, 2): 'Winter Sanctum',
            (1, 0): "Empty Room",
            (1, 1): 'Traveling Merchant',
            (1, 2): 'Ice Guardian Room',
            (2, 0): 'Inferno Lair',
            (2, 1): 'Fire Guardian Room',
            (2, 2): "Final Room",
        }

        test = make_board(rows, columns)
        self.assertEqual(expected, test)
