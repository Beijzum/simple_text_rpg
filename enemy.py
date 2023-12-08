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
            "Experience Points": 20,
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
            "Experience Points": 10,
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
            "Experience Points": 15,
            "Loot": {
                "Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"},
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
            "Special Item": "Frozen Orb",

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
            "Special Item": "Flame Orb",
        }
    elif board.get(coordinate) == "Ice Guardian Room":
        return {
            "Name": "Ice Guardian",
            "Attack": 8,
            "Current HP": 70,
            "Defence": 4,
            "Ability": {
                "Snowstorm": {"Power": 6, "Description": "The Ice Guardian is creating a snowstorm!"}
            },
            "Gold": 100,
            "Experience Points": 50,
            "Equipment Item": "Guardian Armour",
        }
    elif board.get(coordinate) == "Fire Guardian Room":
        return {
            "Name": "Fire Guardian",
            "Attack": 8,
            "Current HP": 70,
            "Defence": 4,
            "Ability": {
                "Infernal Blaze": {"Power": 6, "Description": "The Fire Guardian conjures fiery devastation!"}
            },
            "Gold": 100,
            "Experience Points": 50,
            "Equipment Item": "Radiant Blade",
        }
    elif board.get(coordinate) == "Final Room":
        return {
            "Name": "Brain Devourer",
            "Attack": 10,
            "Max HP": 80,
            "Current HP": 80,
            "Defence": 5,
            "Ability": {
                "Ethereal Blast": {"Power": 8, "Description": "A mystic force surges through the fabric of reality!"}
            },
            "Special Ability": {
                "Supernova": {"Power": 25, "Description": "The Brain Devourer is channeling cosmic energy!"},
            },
            "Special Ability Counter": 0,
            "Gold": 1000,
            "Experience Points": 1000,
            "Special Item": "Chocolate Orb",
        }
