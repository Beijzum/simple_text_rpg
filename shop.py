"""
Jason Chow
A00942129
"""
from loot import (
    add_equipment,
    add_inventory
)
from utility import (
    draw,
    clear
)


def visit_shop(character):
    """
    Visit the traveling merchant to buy weapons, armour, potions, sell items, or rest.

    This function allows the character to interact with the traveling merchant. The character can buy weapons, armour,
    and potions, sell miscellaneous items, or rest to recover health and ability points. The character's gold is used
    to buy items and rest, and is gained by selling items.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary with stats and an inventory.
    :precondition: character must have more than 0 health.
    :postcondition: prints the status of the item added or already in the inventory.
    :postcondition: updates the character's stats, gold, and inventory based on the actions taken in the shop.
    :return: the updated character dictionary.
    """
    print("Welcome to the Shop!")
    while True:
        draw()
        print("1. Buy Weapon")
        print("2. Buy Armour")
        print("3. Buy Potions")
        print("4. Sell Items")
        print("5. Rest for 15 gold")
        print("6. Leave Shop")
        print(f"You currently have {character['Gold']} gold.")
        choice = input("Choose an option (1, 2, 3, 4, 5, or 6): ")

        if choice == "1":  # Buying a weapon
            clear()
            draw()
            print(f"1. Iron Sword $10\n2. Steel Sword $30\n3. Obsidian Blade $75\n4. Runic Greatsword $150")
            draw()
            weapon_choice = input("Enter the number of the weapon you want to buy: ")

            if weapon_choice == "1":
                weapon_cost = 15
                weapon_name = "Iron Sword"
                weapon_power = 2

            elif weapon_choice == "2":
                weapon_cost = 30
                weapon_name = "Steel Sword"
                weapon_power = 4

            elif weapon_choice == "3":
                weapon_cost = 75
                weapon_name = "Obsidian Blade"
                weapon_power = 6

            elif weapon_choice == "4":
                weapon_cost = 150
                weapon_name = "Runic Greatsword"
                weapon_power = 8

            else:
                clear()
                draw()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < weapon_cost:
                clear()
                draw()
                print("Not enough gold to buy the weapon.")

            elif any(item.get('Name') == weapon_name for item in character['Inventory'].values()):
                clear()
                draw()
                print(f"You already have {weapon_name} in your inventory.")
                continue

            elif any(value['Power'] >= weapon_power for value in character['Inventory'].values() if
                     value['Type'] == 'Weapon'):
                clear()
                draw()
                print("\"You already have a powerful weapon!\"")
                continue

            else:
                clear()
                draw()
                print(f"You bought {weapon_name}!")
                character['Gold'] -= weapon_cost
                add_equipment(character, weapon_name, weapon_power, "Weapon")

        elif choice == "2":  # Buying armour
            clear()
            draw()
            print(f"1. Leather Armour $10\n2. Iron Armour $30\n3. Steel Armour $75\n4. Dragon Scale Armour $150")
            draw()
            armour_choice = input("Enter the number of the armour you want to buy: ")

            if armour_choice == "1":
                armour_cost = 15
                armour_name = "Leather Armour"
                armour_power = 1

            elif armour_choice == "2":
                armour_cost = 40
                armour_name = "Iron Armour"
                armour_power = 2

            elif armour_choice == "3":
                armour_cost = 75
                armour_name = "Steel Armour"
                armour_power = 3

            elif armour_choice == "4":
                armour_cost = 150
                armour_name = "Dragon Scale Armour"
                armour_power = 4

            else:
                clear()
                draw()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < armour_cost:
                clear()
                draw()
                print("Not enough gold to buy the armour.")

            elif any(item.get('Name') == armour_name for item in character['Inventory'].values()):
                clear()
                draw()
                print(f"You already have {armour_name} in your inventory.")
                continue

            elif any(value['Power'] >= armour_power for value in character['Inventory'].values() if
                     value['Type'] == 'Armour'):
                clear()
                draw()
                print("\"You already have a magnificent suit of armour!\"")
                continue

            else:
                clear()
                draw()
                print(f"You bought {armour_name}!")
                character['Gold'] -= armour_cost
                add_equipment(character, armour_name, armour_power, "Armour")

        elif choice == "3":
            clear()
            draw()
            print("1. Health Potion $10\n2. AP Potion $10")
            draw()
            potion_choice = input("Enter the number of the potion you want to buy: ")

            if potion_choice == "1":
                potion_cost = 10
                potion_name = "Health Potion"
                potion_power = 15

            elif potion_choice == "2":
                potion_cost = 10
                potion_name = "AP Potion"
                potion_power = 10

            else:
                clear()
                draw()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < potion_cost:
                clear()
                draw()
                print("Not enough gold to buy the potion.")

            else:
                clear()
                draw()
                print(f"You bought a {potion_name}!")
                character['Gold'] -= potion_cost
                add_inventory(character, potion_name, potion_power, 1, "Consumable")

        elif choice == "4":
            clear()
            draw()
            print("\"What are you selling, stranger?\"")
            miscellaneous_items = [(key, item) for key, item in character['Inventory'].items()
                                   if item.get('Type') == 'Miscellaneous']
            total_value = sum(item.get('Price', 0) * item.get('Quantity', 0) for key, item in miscellaneous_items)

            if total_value > 0:
                character["Gold"] += total_value

                # Reduce the quantity of all miscellaneous items to zero
                for key, item_detail in miscellaneous_items:
                    item_detail['Quantity'] = 0

                print(f"You sold all miscellaneous items for {total_value} gold.")
            else:
                print("\"You've got nothing to sell, stranger!\"")

        elif choice == "5":
            clear()
            draw()
            if character['Gold'] < 15:
                print("\"You don't have enough gold to rest.\"")
                continue

            else:
                character['Gold'] -= 15
                character['Current Health'] = character['Max HP']
                character['Ability Points'] = character['Max AP']
                print("\"Eat something while you rest, stranger.\"")
                print("You feel refreshed! Your HP and AP are full.")

        elif choice == "6":
            clear()
            draw()
            print(f"\"Thanks for visiting the Shop! Come again.\"")
            break

        else:
            clear()
            draw()
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    return character
