import io
from unittest import TestCase
from unittest.mock import patch

from character import get_character_stats


class TestGetCharacterStats(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_character_stats(self, mock_output):
        character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Max HP": 10,
            "Current HP": 10,
            "Max AP": 5,
            "Ability Points": 5,
            "Attack": 2,
            "Defence": 0,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"}
            },
            "Gold": 0,
            "Level": 1,
            "Experience Points": 0,
            "EXP to Level Up": 10,
            "Stronger Enemies": False
        }
        get_character_stats(character)
        actual = mock_output.getvalue()
        expected = ("Your current Level is 1.\n"
                    "Your current Max HP is 10.\n"
                    "Your current HP is 10.\n"
                    "Your current Max AP is 5.\n"
                    "Your current Ability Points is 5.\n"
                    "Your current Attack is 2.\n"
                    "Your current Defence is 0.\n"
                    "Your current Abilities are {'1': {'Name': 'Power Strike', 'Power': 2, 'AP Cost': 1}}.\n"
                    "Your current Experience Points is 0.\n"
                    "Your current EXP to Level Up is 10.\n"
                    "Your current Gold is 0.\n"
                    "Your current coordinates are (0,0).\n")
        self.assertEqual(actual, expected)
