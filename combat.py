import random
from itertools import cycle
from utility import clear, draw


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
    multipliers = [3, 4, 5]
    multipliers_cycle = cycle(multipliers)

    if random.random() < 0.3:
        hits = next(multipliers_cycle)
        print(f"Your attack hits {hits} times!")
        return power * hits
    else:
        print("Your attack hits 2 times!")
        return power * 2
