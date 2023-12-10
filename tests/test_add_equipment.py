"""
Jason Chow
A00942129
"""
from unittest import TestCase
from loot import add_equipment


class TestAddEquipment(TestCase):
    def test_add_weapon(self):
        character = {
            "Attack": 2,
            "Defence": 0,
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
            },
        }
        add_equipment(character, "Iron Sword", 1, "Weapon")

        expected = {
            "Attack": 3,
            "Defence": 0,
            "Inventory": {
                "1": {"Name": "Iron Sword", "Power": 1, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
            },
        }
        self.assertEqual(character, expected)

    def test_add_armour(self):
        character = {
            "Attack": 2,
            "Defence": 0,
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Clothes", "Power": 0, "Type": "Armour"},
            },
        }

        add_equipment(character, "Iron Armour", 2, "Armour")

        expected = {
            "Attack": 2,
            "Defence": 2,
            "Inventory": {
                "1": {"Name": "Bronze Sword", "Power": 0, "Type": "Weapon"},
                "2": {"Name": "Iron Armour", "Power": 2, "Type": "Armour"},
            },
        }
        self.assertEqual(character, expected)
