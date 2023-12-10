"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch

from character import get_character_inventory


class TestGetCharacterInventory(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_character_inventory(self, mock_output):
        character = {
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "Health Potion", "Power": 5, "Quantity": 2, "Type": "Consumable"},
                "4": {"Name": "Frozen Orb", "Power": 0, "Quantity": 1, "Type": "Special"}
            },
        }
        get_character_inventory(character)
        actual = mock_output.getvalue()
        expected = ("Item #1 {'Name': 'Bronze Sword', 'Power': 0, 'Type': 'Weapon'}.\n"
                    "Item #2 {'Name': 'Clothes', 'Power': 0, 'Type': 'Armour'}.\n"
                    "Item #3 {'Name': 'Health Potion', 'Power': 5, 'Quantity': 2, 'Type': 'Consumable'}.\n"
                    "Item #4 {'Name': 'Frozen Orb', 'Power': 0, 'Quantity': 1, 'Type': 'Special'}.\n")
        self.assertEqual(actual, expected)
