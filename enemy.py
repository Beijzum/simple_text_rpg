import random


def check_for_foes():
    """
    Check for foes at a rate of 1 in 4 (25%).

    :param: N/A
    :precondition: character must be alive with greater than 0 HP
    :postcondition: checks for the probability of encountering a challenge
    :return: returns True at a rate of 25%, otherwise False at a rate of 75%
    """
    if random.random() <= 0.25:
        print("Watch out! Something has seen you!")
        return True

    else:
        print("You managed to avoid enemies.")
        return False


def generate_foe():
    foe_types = ["Goblin", "Orc", "Skeleton", "Ghoul"]
    random_foe = random.choice(foe_types)

    if random_foe == "Goblin":
        return {
            "Name": "Goblin",
            "Attack": 1,
            "Current HP": 3,
            "Defence": 0,
            "Gold": 5,
            "Experience Points": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Orc":
        return {
            "Name": "Orc",
            "Attack": 2,
            "Current HP": 6,
            "Defence": 1,
            "Gold": 10,
            "Experience Points": 15,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Skeleton":
        return {
            "Name": "Skeleton",
            "Attack": 2,
            "Current HP": 3,
            "Defence": 1,
            "Gold": 5,
            "Experience Points": 5,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Ghoul":
        return {
            "Name": "Ghoul",
            "Attack": 1,
            "Current HP": 8,
            "Defence": 0,
            "Gold": 5,
            "Experience Points": 10,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
            }
        }


def generate_stronger_foe():
    foe_types = ["Hobgoblin", "High Orc", "Armoured Skeleton", "Draugr", "Wyvern"]
    random_foe = random.choice(foe_types)

    if random_foe == "Hobgoblin":
        return {
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
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "High Orc":
        return {
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
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Iron-Clad Skeleton":
        return {
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
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Draugr":
        return {
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
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }
    elif random_foe == "Wyvern":
        return {
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
                "Rare Relic": {"Price": 16, "Type": "Miscellaneous"},
            }
        }


def generate_special_foe(board, character):
    x = character["X-coordinate"]
    y = character["Y-coordinate"]
    coordinate = (x, y)

    if board.get(coordinate) == "Winter Sanctum":
        return {
            "Name": "Abominable Snowman",
            "Attack": 4,
            "Current HP": 30,
            "Defence": 2,
            "Ability": {
                "Snowball": {"Power": 4, "Description": "The Abominable Snowman throws a giant snowball at you!"},
            },
            "Gold": 50,
            "Experience Points": 50,
            "Loot": {
                "Frozen Orb": {"Type": "Special"},
            }

        }
    elif board.get(coordinate) == "Inferno Lair":
        return {
            "Name": "Dragon",
            "Attack": 6,
            "Current HP": 50,
            "Defence": 3,
            "Ability": {
                "Flame Breath": {"Power": 4, "Description": "The Dragon unleashes a fiery breath!"},
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Flame Orb": {"Type": "Special"},
            }
        }
    elif board.get(coordinate) == "Ice Guardian Room":
        return {
            "Name": "Ice Guardian",
            "Attack": 12,
            "Current HP": 80,
            "Defence": 4,
            "Ability": {
                "Snowstorm": {"Power": 8, "Description": "The Ice Guardian is creating a snowstorm!"}
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Guardian Armour": {"Type": "Equipment"},
            }
        }
    elif board.get(coordinate) == "Fire Guardian Room":
        return {
            "Name": "Fire Guardian",
            "Attack": 12,
            "Current HP": 80,
            "Defence": 4,
            "Ability": {
                "Infernal Blaze": {"Power": 8, "Description": "The Fire Guardian conjures fiery devastation!"}
            },
            "Gold": 100,
            "Experience Points": 50,
            "Loot": {
                "Radiant Blade": {"Type": "Equipment"},
            }
        }
    elif board.get(coordinate) == "Final Room":
        return {
            "Name": "Brain Devourer",
            "Attack": 15,
            "Max HP": 100,
            "Current HP": 100,
            "Defence": 5,
            "Ability": {
                "Ethereal Blast": {"Power": 12, "Description": "A mystic force surges through the fabric of reality!"}
            },
            "Special Ability": {
                "Supernova": {"Power": 25, "Description": "The Brain Devourer is channeling cosmic energy!"},
            },
            "Special Ability Counter": 0,
            "Gold": 1000,
            "Experience Points": 1000,
            "Loot": {
                "Chocolate Orb": {"Type": "Special"},
            }
        }
