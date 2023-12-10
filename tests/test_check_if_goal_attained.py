"""
Jason Chow
A00942129
"""
from unittest import TestCase
from exploration import check_win_condition


class TestCheckWinCondition(TestCase):
    def test_goal_attained_true(self):
        board = {(1, 1): "Whatever Room", (2, 2): "Final Room"}
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Inventory": {"1": {"Name": "Orb of Time"}}}
        test = check_win_condition(board, character)
        expected = True
        self.assertEqual(expected, test)

    def test_goal_attained_false(self):
        board = {(1, 1): "Whatever Room", (2, 2): "Final Room"}
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Inventory": {}}
        test = check_win_condition(board, character)
        expected = False
        self.assertEqual(expected, test)
