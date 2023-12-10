from character import is_alive
from combat import (
    enemy_attack,
    multi_strike,
    use_item
)
from utility import (
    draw,
    clear
)
from loot import battle_rewards


def combat_loop(character, foe):
    """
    Handle the combat loop between the character and a foe.

    :param character: a non-empty dictionary representing the player character
    :param foe: a non-empty dictionary representing the foe
    :precondition: character must be alive with greater than 0 HP
    :precondition: foe must be alive with greater than 0 HP
    :postcondition: conducts the combat loop until either the character or the foe is defeated
    :postcondition: prints the result of the combat loop
    :postcondition: updates the character's inventory and experience points
    :postcondition: calls the battle_rewards function
    :postcondition: calls the level_up function if the conditions are met
    :return: updates the character's inventory and experience points
    :return: True if the character wins, otherwise False if the character loses
    """
    while is_alive(character) and is_alive(foe):

        print(f"Your HP: {character['Current HP']}")
        print(f"Your AP: {character['Ability Points']}")
        draw()
        print("Options:")
        print("1. Attack")
        print("2. Use Ability")
        print("3. Use Items")
        print("4. Check Enemy Stats")
        print("5. Run Away")

        action = input("Choose an option (1, 2, 3, 4, or 5): ")

        if action == "1":
            clear()
            draw()
            damage_dealt = max(0, character['Attack'] - foe['Defence'])
            foe['Current HP'] -= damage_dealt
            print(f"You dealt {damage_dealt} damage to the {foe['Name']}!")

            # Foe counterattacks
            if is_alive(foe):
                enemy_attack(character, foe)

        elif action == "2":
            clear()
            draw()
            try:
                print("Choose an ability: ")
                for key, value in character['Abilities'].items():
                    print(f"{key}. \"{value['Name']}\" | Power: {value.get('Power', 0)} |"
                          f" AP Cost: {value.get('AP Cost', 0)}")
                draw()
                skill_choice = input("Enter the number of the skill you want to use: ")

                if skill_choice in character['Abilities']:
                    clear()
                    draw()
                    ability = character['Abilities'][skill_choice]
                    ability_cost = ability.get('AP Cost', 0)

                    if character['Ability Points'] < ability_cost:
                        print("Insufficient Ability Points to use this skill.")
                        continue

                    if ability['Name'] == "Multi-Strike":
                        multi_strike_power = ability['Power']
                        ability_result = multi_strike(multi_strike_power)
                    else:
                        ability_result = ability['Power']

                    damage_dealt = max(0, character['Attack'] + ability_result - foe['Defence'])
                    foe['Current HP'] -= damage_dealt
                    print(f"You used {ability['Name']} and dealt {damage_dealt} damage to the {foe['Name']}!")
                    character['Ability Points'] -= ability_cost

                else:
                    clear()
                    draw()
                    raise ValueError("Invalid skill choice")

                if is_alive(foe):
                    enemy_attack(character, foe)

            except ValueError:
                clear()
                draw()
                print("Please enter a valid skill number.")
                continue

        elif action == "3":
            clear()
            draw()
            try:
                # Check if there are any consumables in the inventory
                consumables_exist = any(item.get('Type') == "Consumable" for item in character['Inventory'].values())
                if consumables_exist:
                    print("Your Inventory:")
                    for key, value in character['Inventory'].items():
                        if value.get('Type') == "Consumable":
                            print(f"{key}. {value['Name']} x{value.get('Quantity', 0)}")
                    draw()
                else:
                    raise ValueError("No consumables in inventory")

            except ValueError as e:
                clear()
                draw()
                print(e)
                continue

            try:
                item_choice = input("Choose an item to use: ")
                use_item_success = use_item(character, item_choice)

                if not use_item_success:
                    continue

            except ValueError:
                clear()
                draw()
                print("Invalid input. Please enter a valid item number.")

        elif action == "4":
            clear()
            draw()
            print(f"{foe['Name']}'s HP: {foe['Current HP']}")
            print(f"{foe['Name']}'s Attack: {foe['Attack']}")
            print(f"{foe['Name']}'s Defence: {foe['Defence']}")
            continue

        elif action == "5":
            clear()
            draw()
            # Player chooses to run away
            print("You run away from the battle.")
            return False, character

        else:
            clear()
            draw()
            print("Invalid choice. Please choose a valid option (1, 2, 3, 4, or 5).")

    if is_alive(foe) and not is_alive(character):
        print("You lost all your HP!")
        print(f"You were defeated by the {foe['Name']}. Game over!")
        draw()
        return False
    else:
        battle_rewards(character, foe)

        return True, character
