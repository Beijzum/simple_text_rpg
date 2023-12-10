"""
Jason Chow
A00942129
"""
from unittest import TestCase
from character import learn_ability


class TestLearnAbility(TestCase):
    def test_learn_ability_multi_strike(self):
        character = {
            "Level": 3,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1}},
        }

        learn_ability(character)
        actual = character
        expected = {
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2}},
            "Level": 3
        }
        self.assertEqual(actual, expected)

    def test_learn_ability_holy_strike(self):
        character = {
            "Level": 5,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2}},
        }

        learn_ability(character)
        actual = character
        expected = {
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2},
                          "3": {"Name": "Holy Strike", "Power": 7, "AP Cost": 3}},
            "Level": 5
        }
        self.assertEqual(actual, expected)

    def test_learn_ability_ultimate_strike(self):
        character = {
            "Level": 7,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2},
                          "3": {"Name": "Holy Strike", "Power": 7, "AP Cost": 3}},
        }

        learn_ability(character)
        actual = character
        expected = {
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2},
                          "3": {"Name": "Holy Strike", "Power": 7, "AP Cost": 3},
                          "4": {"Name": "Ultimate Strike", "Power": 10, "AP Cost": 5}},
            "Level": 7
        }
        self.assertEqual(actual, expected)

    def test_learn_ability_too_long(self):
        character = {
            "Level": 10,
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2},
                          "3": {"Name": "Holy Strike", "Power": 7, "AP Cost": 3},
                          "4": {"Name": "Ultimate Strike", "Power": 10, "AP Cost": 5}},
        }

        learn_ability(character)
        actual = character
        expected = {
            "Abilities": {"1": {"Name": "Power Strike", "Power": 2, "AP Cost": 1},
                          "2": {"Name": "Multi-Strike", "Power": 2, "AP Cost": 2},
                          "3": {"Name": "Holy Strike", "Power": 7, "AP Cost": 3},
                          "4": {"Name": "Ultimate Strike", "Power": 10, "AP Cost": 5},
                          "5": {"Name": "You're Playing Too Long", "Power": 999, "AP Cost": 10}},
            "Level": 10
        }
        self.assertEqual(actual, expected)
