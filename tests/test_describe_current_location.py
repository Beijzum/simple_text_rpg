"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_starting_room(self, mock_output):
        board = {(0, 0): "Starting Room"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        describe_current_location(board, character)
        mock_destination = mock_output.getvalue()
        expected = "Starting Room (0, 0)\nThis is the beginning of your adventure.\n"
        self.assertEqual(expected, mock_destination)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_enchanted_chamber(self, mock_output):
        board = {(0, 0): "Treasure Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        describe_current_location(board, character)
        mock_destination = mock_output.getvalue()
        expected = "Enchanted Chamber (1, 1)\nYou feel magic everywhere in this chamber.\n"
        self.assertEqual(expected, mock_destination)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_treasure_room(self, mock_output):
        board = {(0, 0): "Treasure Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        describe_current_location(board, character)
        mock_destination = mock_output.getvalue()
        expected = "Treasure Room (0, 0)\nYou see lots of treasure in this room.\n"
        self.assertEqual(expected, mock_destination)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_dark_room(self, mock_output):
        board = {(0, 0): "Treasure Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        describe_current_location(board, character)
        mock_destination = mock_output.getvalue()
        expected = "Dark Room (1, 0)\nYou see nothing but darkness in this room.\n"
        self.assertEqual(expected, mock_destination)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_describe_empty_room(self, mock_output):
        board = {(0, 0): "Treasure Room", (0, 1): "Empty Room", (1, 0): "Dark Room", (1, 1): "Enchanted Chamber"}
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        describe_current_location(board, character)
        mock_destination = mock_output.getvalue()
        expected = "Empty Room (0, 1)\nYou see nothing interesting in this room.\n"
        self.assertEqual(expected, mock_destination)
