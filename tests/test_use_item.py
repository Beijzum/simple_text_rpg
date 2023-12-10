"""
Jason Chow
A00942129
"""
import io
from unittest import TestCase
from unittest.mock import patch
from combat import use_item


class TestUseItem(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_health_potion_max_hp(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 10,
            "Max AP": 5,
            "Ability Points": 5,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "Health Potion", "Power": 15, "Quantity": 2, "Type": "Consumable"},
            },
        }
        use_item(character, "3")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You used a Health Potion and healed 0 health!\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_health_potion_not_full_hp(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 5,
            "Max AP": 5,
            "Ability Points": 5,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "Health Potion", "Power": 15, "Quantity": 2, "Type": "Consumable"},
            },
        }
        use_item(character, "3")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You used a Health Potion and healed 5 health!\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_health_potion_not_enough_potion(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 5,
            "Max AP": 5,
            "Ability Points": 5,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "Health Potion", "Power": 15, "Quantity": 0, "Type": "Consumable"},
            },
        }
        use_item(character, "3")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You don't have any Health Potion left.\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_ap_potion_max_ap(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 5,
            "Max AP": 5,
            "Ability Points": 5,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "AP Potion", "Power": 10, "Quantity": 2, "Type": "Consumable"},
            },
        }
        use_item(character, "3")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You used a AP Potion and restored 0 AP!\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_ap_potion_not_full_ap(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 5,
            "Max AP": 5,
            "Ability Points": 2,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "AP Potion", "Power": 10, "Quantity": 2, "Type": "Consumable"},
            },
        }
        use_item(character, "3")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You used a AP Potion and restored 3 AP!\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_ap_potion_not_enough_potion(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 5,
            "Max AP": 5,
            "Ability Points": 2,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "AP Potion", "Power": 10, "Quantity": 0, "Type": "Consumable"},
            },
        }
        use_item(character, "3")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "You don't have any AP Potion left.\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_use_invalid_item(self, mock_output):
        character = {
            "Max HP": 10,
            "Current HP": 5,
            "Max AP": 5,
            "Ability Points": 2,

            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
                "3": {"Name": "AP Potion", "Power": 10, "Quantity": 0, "Type": "Consumable"},
            },
        }
        use_item(character, "4")
        actual = mock_output.getvalue()
        expected = "xX------------------------------------------------------Xx\n" \
                   "Invalid item selection.\n"
        self.assertEqual(actual, expected)
