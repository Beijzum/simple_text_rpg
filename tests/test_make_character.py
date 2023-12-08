"""
Jason Chow
A00942129
"""
from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        test = make_character()
        self.assertEqual(expected, test)
