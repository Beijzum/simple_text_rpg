"""
Jason Chow
A00942129
"""
from unittest import TestCase
from game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_goal_attained_true(self):
        board = {(1, 1): "Whatever Room", (2, 2): "Chocolate Room"}
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}
        test = check_if_goal_attained(board, character)
        expected = True
        self.assertEqual(expected, test)

    def test_goal_attained_false(self):
        board = {(1, 1): "Whatever Room", (2, 2): "Chocolate Room"}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        test = check_if_goal_attained(board, character)
        expected = False
        self.assertEqual(expected, test)
