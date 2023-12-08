"""
Jason Chow
A00942129
"""
from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_up(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = "up"
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        self.assertEqual(expected, move_character(character, direction))

    def test_move_down(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = "down"
        expected = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}
        self.assertEqual(expected, move_character(character, direction))

    def test_move_left(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = "left"
        expected = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(expected, move_character(character, direction))

    def test_move_right(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        direction = "right"
        expected = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5}
        self.assertEqual(expected, move_character(character, direction))
