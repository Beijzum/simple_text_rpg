"""
Jason Chow
A00942129
"""
from unittest import TestCase
from loot import add_inventory


class TestAddInventory(TestCase):
    def test_add_inventory_special(self):
        character = {"Inventory": {
            "1": {"Name": "Health Potion", "Power": 5, 'Price': 0, "Quantity": 2, "Type": "Consumable"},
            "2": {"Name": "Frozen Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"}
        },
        }

        add_inventory(character, "Flame Orb", 0, 1, "Special")

        expected = {"Inventory": {
            "1": {"Name": "Health Potion", "Power": 5, 'Price': 0, "Quantity": 2, "Type": "Consumable"},
            "2": {"Name": "Frozen Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"},
            "3": {"Name": "Flame Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"}
        },
        }
        self.assertEqual(character, expected)

    def test_add_inventory_consumable(self):
        character = {"Inventory": {
            "1": {"Name": "Health Potion", "Power": 5, 'Price': 0, "Quantity": 2, "Type": "Consumable"},
            "2": {"Name": "Frozen Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"}
        },
        }

        add_inventory(character, "Health Potion", 15, 1, "Consumable")

        expected = {"Inventory": {
            "1": {"Name": "Health Potion", "Power": 5, 'Price': 0, "Quantity": 3, "Type": "Consumable"},
            "2": {"Name": "Frozen Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"}
        },
        }
        self.assertEqual(character, expected)

    def test_add_inventory_special_duplicate(self):
        character = {"Inventory": {
            "1": {"Name": "Health Potion", "Power": 5, 'Price': 0, "Quantity": 2, "Type": "Consumable"},
            "2": {"Name": "Frozen Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"}
        },
        }

        add_inventory(character, "Frozen Orb", 0, 1, "Special")

        expected = {"Inventory": {
            "1": {"Name": "Health Potion", "Power": 5, 'Price': 0, "Quantity": 2, "Type": "Consumable"},
            "2": {"Name": "Frozen Orb", "Power": 0, 'Price': 0, "Quantity": 1, "Type": "Special"}
        },
        }
        self.assertEqual(character, expected)
