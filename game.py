"""
Jason Chow
A00942129
"""
import json
import sys
from unittest.mock import patch
from itertools import count
from character import (
    get_character_inventory,
    get_character_stats,
    make_character,
    level_up,
    is_alive,
)
from combat import (
    use_item,
    enemy_attack,
    multi_strike,
)
from enemy import (
    generate_foe,
    generate_special_foe,
    check_for_foes,
    generate_stronger_foe,
)
from exploration import (
    show_map,
    make_board,
    describe_current_location,
    validate_move,
    move_character,
    check_win_condition,
    check_stronger_foe,
)
from loot import (
    battle_rewards,
    visit_shop,
)
from utility import (
    clear,
    draw_box,
    draw,
)


def start_menu():
    """
    Display the start menu with a choice of starting a new game, loading a game, or quitting.

    :param: N/A
    :precondition: user must start the program
    :postcondition: displays the start menu and prompts the user to make a choice
    :postcondition: calls the game function, load_game function, or exits the program
    :return: a call to the game function, load_game function, or exits the program
    """

    while True:
        print(draw_box("Quest for the Orb of Time"))
        draw()
        print("1. Start a New Game")
        print("2. Load Game")
        print("3. Quit")
        draw()

        choice = input("Enter your choice 1, 2, or 3: ")

        if choice == "1":
            clear()
            game()
            break
        elif choice == "2":
            clear()
            load_game()
            break
        elif choice == "3":
            clear()
            draw()
            print("Goodbye! Thanks for playing.")
            draw()
            sys.exit(0)
        else:
            clear()
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue


def save_game(character):
    """
    Save the current game state to a JSON file.

    This function takes the current game state, represented by the character dictionary, and saves it to a JSON file.
    The JSON file is named "save.json" and is saved in the same directory as the game.py file. The JSON file is
    formatted with indentation of 4 spaces.

    :param character: a dictionary representing the current game state.
    :precondition: character must be a valid dictionary.
    :precondition: character must be alive with greater than 0 HP.
    :postcondition: saves the game state to a JSON file.
    :postcondition: prints a message to the console indicating that the game was saved successfully.
    :return: a JSON file named "save.json" containing the current game state.
    :return: a string indicating that the game was saved successfully.
    """
    with open("save.json", "w") as game_file:
        json.dump(character, game_file, indent=4)

    print("Game saved successfully!")


def load_game():
    """
    Load an existing game and continue.

    This function loads a saved game state from a JSON file named "save.json".


    :param: N/A
    :precondition: "save.json" file should exist if there is a saved game.
    :precondition: "save.json" file should be formatted correctly.
    :postcondition: loads the game state from the JSON file.
    :postcondition: prints a message to the console indicating that the game was loaded successfully.
    :return: a call to the game function.
    :return: a string indicating that the game was loaded successfully.
    """
    try:
        with open("save.json", "r") as game_file:
            character = json.load(game_file)

        print("Game loaded successfully!")
        game(character)

    except FileNotFoundError:
        print("No saved game found.")
        start_menu()


def get_user_choice(rows, columns, character, board):
    """
    Prompt user for input to choose a direction from a numbered list.

    :param: N/A
    :precondition: user must input a number between 1 and 4
    :precondition: character must be alive with greater than 0 HP
    :precondition: character must not be in the winning room
    :postcondition: prompts user to choose a direction and returns the input as a string
    :return: returns a string consisting of "up", "down", "left", or "right"

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> with patch('builtins.input', return_value='2'):
    ...     get_user_choice(5, 5, character_test, {(0, 0): "Starting Room"})
    xX------------------------------------------------------Xx
    1. Up
    2. Down
    3. Left
    4. Right
    xX------------------------------------------------------Xx
    You chose to go down...
    'down'

    >>> with patch('builtins.input', return_value='4'):
    ...     get_user_choice(5, 5, character_test, {(0, 0): "Starting Room"})
    xX------------------------------------------------------Xx
    1. Up
    2. Down
    3. Left
    4. Right
    xX------------------------------------------------------Xx
    You chose to go right...
    'right'
    """
    while True:
        draw()
        print("1. Up")
        print("2. Down")
        print("3. Left")
        print("4. Right")
        user_input = input("Please choose a direction (1, 2, 3, or 4) or show map(5), character stats(6), "
                           "inventory(7), save game(8), start menu(0): ")

        if user_input == "1":
            clear()
            draw()
            print("You chose to go up...")
            return "up"

        elif user_input == "2":
            clear()
            draw()
            print("You chose to go down...")
            return "down"

        elif user_input == "3":
            clear()
            draw()
            print("You chose to go left...")
            return "left"

        elif user_input == "4":
            clear()
            draw()
            print("You chose to go right...")
            return "right"

        elif user_input == "5":
            clear()
            draw()
            show_map(rows, columns, character)

        elif user_input == "6":
            clear()
            draw()
            get_character_stats(character)

        elif user_input == "7":
            clear()
            draw()
            get_character_inventory(character)

        elif user_input == "8":
            clear()
            draw()
            save_game(character)

        elif user_input == "0":
            clear()
            start_menu()

        else:
            clear()
            draw()
            print("Invalid choice.")
            describe_current_location(board, character)


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


def game(character=None):
    """
    Initialize and run the game.

    This function sets up the game board and character, then enters the main game loop. It will ask the player for
    input to move the character around the board, and will call other functions to handle combat, inventory, and
    other game mechanics. The game will end when the character's health drops to 0 or the win condition is met.

    :param character: a dictionary representing the player character. If None, a new character is created.
    :precondition: if the character is provided, must be a dictionary with stats and inventory.
    :precondition: character must be alive with greater than 0 HP.
    :postcondition: runs the game until the character's health drops to 0 or the win condition is met.
    :postcondition: prints a message to the console indicating that the game is over.
    :postcondition: prints a message to the console indicating that the character has won the game.
    :return: a string indicating that the game is over.
    :return: a string indicating that the character has won the game.
    """
    achieved_goal = False

    if character is None:
        rows = 5
        columns = 5
        board = make_board(rows, columns)
        character = make_character()

    else:
        rows = 5
        columns = 5
        board = make_board(rows, columns)

    draw()
    describe_current_location(board, character)
    while not achieved_goal:
        direction = get_user_choice(rows, columns, character, board)
        valid_move = validate_move(board, character, direction)
        achieved_goal = check_win_condition(board, character)

        if valid_move:
            clear()
            draw()
            move_character(character, direction)
            player_location = (character["X-coordinate"], character["Y-coordinate"])
            describe_current_location(board, character)

            if board.get(player_location) in ["Winter Sanctum", "Inferno Lair"]:
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

                if character['Experience Points'] >= character['EXP to Level Up']:
                    level_up(character)

            elif (board.get(player_location) == "Ice Guardian Room"
                  and any(item['Name'] == "Frozen Orb" for item in character['Inventory'].values())
                  and character["Stronger Enemies"]):
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

                if character['Experience Points'] >= character['EXP to Level Up']:
                    level_up(character)

            elif (board.get(player_location) == "Fire Guardian Room"
                  and any(item['Name'] == "Flame Orb" for item in character['Inventory'].values())
                  and character["Stronger Enemies"]):
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

                if character['Experience Points'] >= character['EXP to Level Up']:
                    level_up(character)

            elif (board.get(player_location) == "Final Room"
                  and any(item['Name'] == "Radiant Blade" for item in character['Inventory'].values())
                  and any(item['Name'] == "Guardian Armour" for item in character['Inventory'].values())):
                special_foe = generate_special_foe(board, character)
                print(f"You are facing {special_foe['Name']}!")

                combat_result = combat_loop(character, special_foe)

                if not combat_result:
                    break

            elif board.get(player_location) == "Traveling Merchant":
                visit_shop(character)

            else:
                there_is_a_challenger = check_for_foes()
                if there_is_a_challenger and character["Stronger Enemies"]:
                    foe = generate_stronger_foe()
                    print(f"You are facing a {foe['Name']}!")

                    combat_result = combat_loop(character, foe)

                    if not combat_result:
                        break

                    if character['Experience Points'] >= character['EXP to Level Up']:
                        level_up(character)

                elif there_is_a_challenger and not character["Stronger Enemies"]:
                    # Generate a foe
                    foe = generate_foe()
                    print(f"You are facing a {foe['Name']}!")

                    # Combat loop
                    combat_result = combat_loop(character, foe)

                    if not combat_result:
                        break  # Player ran away from combat

                    # Check for level up
                    if character['Experience Points'] >= character['EXP to Level Up']:
                        level_up(character)

            achieved_goal = check_win_condition(board, character)
            check_stronger_foe(character)

        else:
            print("You cannot go that direction.")

        if character["Current HP"] <= 0:
            draw()
            print("You lost all your HP! You lose!")
            break

        if is_alive(character) and achieved_goal:
            draw()
            print(f"You have defeated the Time Warden!")
            print("Congratulations, you have obtained the Orb of Time!")
            break


def main():
    """
    Execute the start_menu function
    """
    clear()
    start_menu()


if __name__ == "__main__":
    main()
