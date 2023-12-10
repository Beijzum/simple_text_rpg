import io
from unittest import TestCase
from unittest.mock import patch
from character import level_up


class TestLevelUp(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_up(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 10,
            "Max AP": 5,
            "Ability Points": 5,
            "Attack": 2,
            "Defence": 0,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Level": 1,
            "Experience Points": 10,
            "EXP to Level Up": 10,
        }
        level_up(character)
        actual = mock_output.getvalue()
        expected = ("Congratulations! You leveled up to Level 2!\n"
                    "Your Max HP is now 15.\n"
                    "Your Max AP is now 7.\n"
                    "Your Attack is now 3.\n"
                    "Your Defence is now 1.\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_up_level_3(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 10,
            "Max AP": 5,
            "Ability Points": 5,
            "Attack": 2,
            "Defence": 0,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Level": 2,
            "Experience Points": 10,
            "EXP to Level Up": 10,
        }
        level_up(character)
        actual = mock_output.getvalue()
        expected = ("Congratulations! You leveled up to Level 3!\n"
                    "Your Max HP is now 15.\n"
                    "Your Max AP is now 7.\n"
                    "Your Attack is now 3.\n"
                    "Your Defence is now 1.\n"
                    "You learned a new ability: Multi-Strike!\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_level_up_level_10(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 10,
            "Max AP": 5,
            "Ability Points": 5,
            "Attack": 2,
            "Defence": 0,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Level": 9,
            "Experience Points": 10,
            "EXP to Level Up": 10,
        }
        level_up(character)
        actual = mock_output.getvalue()
        expected = ("Congratulations! You leveled up to Level 10!\n"
                    "Your Max HP is now 15.\n"
                    "Your Max AP is now 7.\n"
                    "Your Attack is now 3.\n"
                    "Your Defence is now 1.\n"
                    "You learned a new ability: You're Playing Too Long!\n")
        self.assertEqual(actual, expected)
