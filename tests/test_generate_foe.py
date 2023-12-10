"""
Jason Chow
A00942129
"""
from unittest import TestCase
from unittest.mock import patch
from enemy import generate_foe


class TestGenerateFoe(TestCase):
    @patch('random.choice', return_value='Goblin')
    def test_generate_goblin(self, _):
        expected = {
            "Name": "Goblin",
            "Attack": 1,
            "Current HP": 3,
            "Defence": 0,
            "Gold": 5,
            "Experience Points": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 10, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_foe(), expected)

    @patch('random.choice', return_value='Orc')
    def test_generate_orc(self, _):
        expected = {
            "Name": "Orc",
            "Attack": 2,
            "Current HP": 6,
            "Defence": 1,
            "Gold": 10,
            "Experience Points": 10,
            "Loot": {
                "Cheap Trinket": {"Price": 10, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_foe(), expected)

    @patch('random.choice', return_value='Skeleton')
    def test_generate_skeleton(self, _):
        expected = {
            "Name": "Skeleton",
            "Attack": 2,
            "Current HP": 3,
            "Defence": 1,
            "Gold": 5,
            "Experience Points": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 10, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_foe(), expected)

    @patch('random.choice', return_value='Ghoul')
    def test_generate_ghoul(self, _):
        expected = {
            "Name": "Ghoul",
            "Attack": 1,
            "Current HP": 8,
            "Defence": 0,
            "Gold": 5,
            "Experience Points": 10,
            "Loot": {
                "Cheap Trinket": {"Price": 10, "Type": "Miscellaneous"},
            }
        }
        self.assertEqual(generate_foe(), expected)
