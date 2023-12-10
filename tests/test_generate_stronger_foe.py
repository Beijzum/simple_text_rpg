"""
Jason Chow
A00942129
"""
from unittest import TestCase
from unittest.mock import patch
from enemy import generate_stronger_foe


class TestGenerateStrongerFoe(TestCase):
    @patch('random.choice', return_value='Hobgoblin')
    def test_generate_hobgoblin(self, _):
        expected = {
            "Name": "Hobgoblin",
            "Attack": 5,
            "Current HP": 8,
            "Defence": 1,
            "Ability": {
                "Reckless Attack": {"Power": 2, "Description": "The Hobgoblin is charging at you!"},
            },
            "Gold": 10,
            "Experience Points": 10,
            "Loot": {
                "Rare Relic": {"Price": 20, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_stronger_foe(), expected)

    @patch('random.choice', return_value='High Orc')
    def test_generate_high_orc(self, _):
        expected = {
            "Name": "High Orc",
            "Attack": 7,
            "Current HP": 16,
            "Defence": 2,
            "Ability": {
                "Spear Throw": {"Power": 4, "Description": "The High Orc aims its spear at you!"},
            },
            "Gold": 20,
            "Experience Points": 20,
            "Loot": {
                "Rare Relic": {"Price": 20, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_stronger_foe(), expected)

    @patch('random.choice', return_value='Iron-Clad Skeleton')
    def test_generate_iron_clad_skeleton(self, _):
        expected = {
            "Name": "Iron-Clad Skeleton",
            "Attack": 6,
            "Current HP": 10,
            "Defence": 5,
            "Ability": {
                "Downward Smash": {"Power": 3, "Description": "The Iron-Clad Skeleton raises its weapon!"},
            },
            "Gold": 10,
            "Experience Points": 20,
            "Loot": {
                "Rare Relic": {"Price": 20, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_stronger_foe(), expected)

    @patch('random.choice', return_value='Draugr')
    def test_generate_draugr(self, _):
        expected = {
            "Name": "Draugr",
            "Attack": 5,
            "Current HP": 23,
            "Defence": 1,
            "Ability": {
                "Deadly Bite": {"Power": 4, "Description": "The Draugr lunges at you!"},
            },
            "Gold": 10,
            "Experience Points": 20,
            "Loot": {
                "Rare Relic": {"Price": 20, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_stronger_foe(), expected)

    @patch('random.choice', return_value='Wyvern')
    def test_generate_wyvern(self, _):
        expected = {
            "Name": "Wyvern",
            "Attack": 9,
            "Current HP": 30,
            "Defence": 3,
            "Ability": {
                "Wyvern's Breath": {"Power": 6, "Description": "The Wvyern reveals its wide maw!"},
            },
            "Gold": 20,
            "Experience Points": 30,
            "Loot": {
                "Rare Relic": {"Price": 20, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_stronger_foe(), expected)
