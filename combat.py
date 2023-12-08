import random

from utility import clear


def enemy_attack(character, foe):
    """
    """
    # If the foe has a special ability and is below half health
    if 'Special Ability' in foe and foe['Current HP'] < foe['Max HP'] / 2 and foe['Special Ability Counter'] == 0:

        foe_special_ability_name = next(iter(foe['Special Ability']))
        foe_special_ability = foe['Special Ability'][foe_special_ability_name]
        ability_power = foe_special_ability.get('Power')
        foe_attack = foe['Attack'] + random.randint(-1, 1)

        total_damage = max(0, foe_attack + ability_power - character['Defence'])
        character['Current HP'] -= total_damage
        foe['Special Ability Counter'] += 1
        print(f"{foe_special_ability.get('Description')}")
        print(f"Your Radiant Blade and Guardian Armour are reacting to the {foe['Name']}'s special ability!")
        print(f"Your special items mitigate {foe_special_ability_name} and it only deals {total_damage} damage!")
        print(f"You sense that the creature is weakening.")

    # 25% to use ability
    elif random.random() < 0.25 and 'Ability' in foe:
        foe_ability_name = next(iter(foe['Ability']))
        foe_ability = foe['Ability'][foe_ability_name]
        ability_power = foe_ability.get('Power')
        foe_attack = foe['Attack'] + random.randint(-1, 1)

        total_damage = max(0, foe_attack + ability_power - character['Defence'])
        character['Current HP'] -= total_damage
        print(f"{foe_ability.get('Description')}")
        print(f"The {foe['Name']} uses {foe_ability_name} and deals {total_damage} damage!")

    else:
        foe_attack = foe['Attack'] + random.randint(-1, 1)
        total_damage = max(0, foe_attack - character['Defence'])
        character['Current HP'] -= total_damage
        print(f"The {foe['Name']} counterattacks and deals {total_damage} damage!")


def use_item(character, item_key):
    """
    """
    try:
        selected_item = character['Inventory'][item_key]

        if selected_item['Quantity'] <= 0:
            clear()
            print(f"You don't have any {selected_item['Name']} left.")
            return False

        if "Health Potion" in selected_item["Name"]:
            clear()
            # Will add the lowest amount to character health. If character is already at max HP, nothing will be added.
            healing_amount = min(selected_item["Power"], character['Max HP'] - character['Current HP'])
            character['Current HP'] += healing_amount
            selected_item['Quantity'] -= 1

            print(f"You used a {selected_item['Name']} and healed {healing_amount} health!")
            return True

        elif "AP Potion" in selected_item["Name"]:
            clear()
            # Will add the lowest amount to character AP. If character is already at max AP, nothing will be added.
            ap_amount = min(selected_item["Power"], character['Max AP'] - character['Ability Points'])
            character['Ability Points'] += ap_amount
            selected_item['Quantity'] -= 1

            print(f"You used a {selected_item['Name']} and restored {ap_amount} AP!")
            return True

        print(f"You can't use {selected_item['Name']} in combat.")
        clear()
        return False

    except KeyError:
        print("Invalid item selection.")
        return False


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
            "Gold": 10,
            "Experience Points": 5,
        }
    elif random_foe == "Orc":
        return {
            "Name": "Orc",
            "Attack": 2,
            "Current HP": 6,
            "Defence": 1,
            "Gold": 25,
            "Experience Points": 20,
        }
    elif random_foe == "Skeleton":
        return {
            "Name": "Skeleton",
            "Attack": 2,
            "Current HP": 3,
            "Defence": 1,
            "Gold": 15,
            "Experience Points": 10,
        }
    elif random_foe == "Ghoul":
        return {
            "Name": "Ghoul",
            "Attack": 1,
            "Current HP": 8,
            "Defence": 0,
            "Gold": 15,
            "Experience Points": 15,
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
