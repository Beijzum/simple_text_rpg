import random
from itertools import cycle
from utility import (
    clear,
    draw,
)
from unittest.mock import patch


def enemy_attack(character, foe):
    """
    Handle the enemy's attack during the combat loop.

    This function will handle the enemy's attack calculations and print the results. It will also check if the enemy
    has a special ability and use it if the conditions are met. If the enemy has an ability, it will use it 25% of the
    time. If the enemy has a special ability, it will use it when it is below half health. The special ability will
    only be used once per combat.

    :param character: a dictionary representing the player character
    :param foe: a dictionary representing the enemy
    :precondition: character must be a dictionary with stats.
    :precondition: foe must be a dictionary with stats and a name.
    :postcondition: updates the character's 'Current HP' based on the foe's attack
    :postcondition: prints the foe's attack and damage dealt
    :return: a string representing the description of the foe's attack and damage dealt

    >>> with patch('random.randint', return_value=1):
    ...     character_test = {"Defence": 2, "Current HP": 10}
    ...     foe_test = {"Name": "Orc", "Attack": 2,}
    ...     enemy_attack(character_test, foe_test)
    The Orc counterattacks and deals 1 damage!

    >>> with patch('random.randint', return_value=1), patch('random.random', return_value=0.2):
    ...     character_test = {"Defence": 2, "Current HP": 10}
    ...     foe_test = {"Name": "High Orc", "Attack": 2, "Max HP": 10,
    ...                  "Ability": {"Spear Throw": {"Power": 4, "Description": "The High Orc aims its spear at you!"}}}
    ...     enemy_attack(character_test, foe_test)
    The High Orc aims its spear at you!
    The High Orc uses Spear Throw and deals 5 damage!
    """
    # If the foe has a special ability and is below half health
    if 'Special Ability' in foe and foe['Current HP'] < foe['Max HP'] / 2 and foe['Special Ability Counter'] == 0:

        foe_special_ability_name = next(iter(foe['Special Ability'].keys()))
        foe_special_ability = foe['Special Ability'][foe_special_ability_name]
        ability_power = foe_special_ability.get('Power')
        foe_attack = foe['Attack'] + random.randint(-1, 1)

        total_damage = max(0, foe_attack + ability_power - character['Defence'])
        character['Current HP'] -= total_damage
        foe['Special Ability Counter'] += 1
        print(f"{foe_special_ability.get('Description')}")
        print(f"Your Radiant Blade and Guardian Armour are reacting to the {foe['Name']}'s special ability!")
        print(f"You are able to withstand its manipulation of time!")
        print(f"Your special items mitigate {foe_special_ability_name} and it only deals {total_damage} damage!")
        print(f"You sense that the {foe['Name']} is nearing defeat.")

    # 25% to use ability
    elif random.random() < 0.25 and 'Ability' in foe:
        foe_ability_name = random.choice(list(foe['Ability'].keys()))
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
    Use a consumable item from the character's inventory.

    This function will handle the item's effect and print the results. It will also check if the character has any of
    the item left and use it if the conditions are met. If the character has an item, it will use it and decrease the
    quantity by 1. If the character has no items left, it will print a message and return False. Consumables will only
    heal up until the character's max HP or AP.

    :param character: adictionary representing the player character
    :param item_key: a string representing the key of the item in the character's inventory.
    :raises: KeyError if the item_key is not in the character's inventory.
    :precondition: character must be a dictionary with an inventory.
    :precondition: item_key must be a string and a valid key in the character's 'Inventory'.
    :postcondition: updates the character's stats based on the item used
    :postcondition: prints the item used and the effect
    :return: True if the item was used successfully, otherwise False.
    :return: a string representing the description of the item used.

    >>> character_test = {"Inventory": {"1": {"Name": "Health Potion", "Power": 15, "Quantity": 1}}, "Max HP": 10,\
 "Current HP": 5, "Max AP": 5, "Ability Points": 5}
    >>> use_item(character_test, "1")
    xX------------------------------------------------------Xx
    You used a Health Potion and healed 5 health!
    True

    >>> character_test = {"Inventory": {"1": {"Name": "Health Potion", "Power": 5, "Quantity": 0}}, "Max HP": 10,\
 "Current HP": 5, "Max AP": 5, "Ability Points": 5}
    >>> use_item(character_test, "1")
    xX------------------------------------------------------Xx
    You don't have any Health Potion left.
    False
    """
    try:
        selected_item = character['Inventory'][item_key]

        if selected_item['Quantity'] <= 0:
            clear()
            draw()
            print(f"You don't have any {selected_item['Name']} left.")
            return False

        if "Health Potion" in selected_item["Name"]:
            clear()
            draw()
            # Will add the lowest amount to character health. If character is already at max HP, nothing will be added.
            healing_amount = min(selected_item["Power"], character['Max HP'] - character['Current HP'])
            character['Current HP'] += healing_amount
            selected_item['Quantity'] -= 1

            print(f"You used a {selected_item['Name']} and healed {healing_amount} health!")
            return True

        elif "AP Potion" in selected_item["Name"]:
            clear()
            draw()
            # Will add the lowest amount to character AP. If character is already at max AP, nothing will be added.
            ap_amount = min(selected_item["Power"], character['Max AP'] - character['Ability Points'])
            character['Ability Points'] += ap_amount
            selected_item['Quantity'] -= 1

            print(f"You used a {selected_item['Name']} and restored {ap_amount} AP!")
            return True

        print(f"You can't use {selected_item['Name']} in combat.")
        clear()
        draw()
        return False

    except KeyError:
        clear()
        draw()
        print("Invalid item selection.")
        return False


def multi_strike(power):
    """
    Calculate the hits and total power of the multi-strike ability.

    This function calculates the number of hits and total power for the multi-strike ability.
    The number of hits is determined randomly: there's a 30% chance for the attack to hit 3, 4, or 5 times,
    and a 70% chance for the attack to hit 2 times. The total power of the attack is the product of the
    number of hits and the power parameter.

    :param power: an integer representing the base power of the attack
    :precondition: character must have a 'Multi-Strike' ability
    :precondition: character must have enough AP to use the ability
    :precondition: character must have greater than 0 health
    :precondition: power must be a positive integer
    :postcondition: prints the number of hits
    :postcondition: calculates the total power of the attack
    :return: an integer representing the total power of the multi-strike attack
    :return: the number of hits

    >>> multi_strike(2)
    Your attack hits 2 times!
    4

    >>> with patch('random.random', return_value=0.2):
    ...     multi_strike(2)
    Your attack hits 3 times!
    6
    """
    multipliers = [3, 4, 5]
    multipliers_cycle = cycle(multipliers)

    if random.random() < 0.3:
        hits = next(multipliers_cycle)
        print(f"Your attack hits {hits} times!")
        return power * hits
    else:
        print("Your attack hits 2 times!")
        return power * 2
