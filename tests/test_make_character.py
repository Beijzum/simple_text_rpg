"""
Jason Chow
A00942129
"""
from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {
            'X-coordinate': 0,
            'Y-coordinate': 0,
            'Max HP': 10,
            'Current HP': 10,
            'Max AP': 5,
            'Ability Points': 5,
            'Attack': 2,
            'Defence': 0,
            'Abilities': {
                '1': {'Name': 'Power Strike', 'Power': 2, 'AP Cost': 1}
            },
            'Inventory': {
                '1': {'Name': 'Bronze Sword', 'Power': 0, 'Type': 'Weapon'},
                '2': {'Name': 'Clothes', 'Power': 0, 'Type': 'Armour'}
            },
            'Gold': 0,
            'Level': 1,
            'Experience Points': 0,
            'EXP to Level Up': 10,
            'Stronger Enemies': False
        }

        test = make_character()
        self.assertEqual(expected, test)
