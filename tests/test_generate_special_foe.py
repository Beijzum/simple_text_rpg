"""
Jason Chow
A00942129
"""
from unittest import TestCase
from enemy import generate_special_foe


class TestGenerateSpecialFoe(TestCase):
    def test_abominable_snowman_player_in_winter_sanctum(self):
        expected = {
            "Name": "Abominable Snowman",
            "Attack": 4,
            "Current HP": 30,
            "Defence": 2,
            "Ability": {
                "Snowball": {"Power": 4, "Description": "The Abominable Snowman throws a giant snowball at you!"},
            },
            "Gold": 30,
            "Experience Points": 30,
            "Loot": {
                "Frozen Orb": {"Type": "Special"},
            }
        }

        actual = generate_special_foe(
            {(0, 0): "Winter Sanctum"},
            {"X-coordinate": 0, "Y-coordinate": 0}
        )
        self.assertEqual(expected, actual)

    def test_dragon_player_in_inferno_lair(self):
        expected = {
            "Name": "Dragon",
            "Attack": 6,
            "Current HP": 50,
            "Defence": 3,
            "Ability": {
                "Flame Breath": {"Power": 4, "Description": "The Dragon unleashes a fiery breath!"},
            },
            "Gold": 40,
            "Experience Points": 40,
            "Loot": {
                "Flame Orb": {"Type": "Special"},
            }
        }
        actual = generate_special_foe(
            {(0, 0): "Inferno Lair"},
            {"X-coordinate": 0, "Y-coordinate": 0}
        )
        self.assertEqual(expected, actual)

    def test_ice_guardian_player_in_ice_guardian_room(self):
        expected = {
            "Name": "Ice Guardian",
            "Attack": 12,
            "Current HP": 80,
            "Defence": 4,
            "Ability": {
                "Snowstorm": {"Power": 8, "Description": "The Ice Guardian is creating a snowstorm!"},
                "Frostbite": {"Power": 10, "Description": "The Ice Guardian is rapidly lowering the temperature!"},
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Guardian Armour": {"Type": "Equipment"},
            }
        }
        actual = generate_special_foe(
            {(0, 0): "Ice Guardian Room"},
            {"X-coordinate": 0, "Y-coordinate": 0}
        )
        self.assertEqual(expected, actual)

    def test_fire_guardian_player_in_fire_guardian_room(self):
        expected = {
            "Name": "Fire Guardian",
            "Attack": 12,
            "Current HP": 80,
            "Defence": 4,
            "Ability": {
                "Infernal Blaze": {"Power": 8, "Description": "The Fire Guardian conjures fiery devastation!"},
                "Scorching Heat": {"Power": 10, "Description": "The Fire Guardian is raising the temperature!"},
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Radiant Blade": {"Type": "Equipment"},
            }
        }
        actual = generate_special_foe(
            {(0, 0): "Fire Guardian Room"},
            {"X-coordinate": 0, "Y-coordinate": 0}
        )
        self.assertEqual(expected, actual)

    def test_time_warden_player_in_final_room(self):
        expected = {
            "Name": "Time Warden",
            "Attack": 15,
            "Max HP": 100,
            "Current HP": 100,
            "Defence": 5,
            "Ability": {
                "Hasten": {"Power": 12, "Description": "The Time Warden hastens itself and attacks rapidly!"},
                "Temporal Shift": {"Power": 15, "Description": "The Time Warden releases time-warping energy!"},
            },
            "Special Ability": {
                "Chrono Stasis": {"Power": 25, "Description": "The Time Warden tries to control your flow of time!"},
            },
            "Special Ability Counter": 0,
            "Gold": 1000,
            "Experience Points": 1000,
            "Loot": {
                "Orb of Time": {"Type": "Special"},
            }
        }
        actual = generate_special_foe(
            {(0, 0): "Final Room"},
            {"X-coordinate": 0, "Y-coordinate": 0}
        )
        self.assertEqual(expected, actual)
