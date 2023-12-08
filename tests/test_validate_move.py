"""
Jason Chow
A00942129
"""
from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_true(self):
        board = {(1, 1): "Whatever Room", (1, 2): "Whatever Room", (0, 0): "Whatever Room", (2, 2): "Whatever Room"}
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        direction = "up"  # x - 1
        expected = True
        self.assertEqual(expected, validate_move(board, character, direction))  # (0,0) exists

    def test_validate_move_false(self):
        board = {(1, 1): "Whatever Room", (1, 2): "Whatever Room", (0, 0): "Whatever Room", (2, 2): "Whatever Room"}
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        direction = "down"  # x + 1
        expected = False
        self.assertEqual(expected, validate_move(board, character, direction))  # (2,0) does not exist
