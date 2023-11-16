"""
Jason Chow
A00942129
"""
from unittest import TestCase
from game import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_true(self):
        expected = True
        self.assertEqual(expected, is_alive({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}))

    def test_is_alive_false(self):
        expected = False
        self.assertEqual(expected, is_alive({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0}))
