from utility import (
    clear,
    draw_box,
    draw,
)


def add_equipment(character, item_name, item_power, item_type):
    """
    Equip the character with a new weapon or armour.

    This function checks if the character already has the item in their inventory. If they do, the function will return.
    If the character does not have the item, the function will check if the item is a weapon or armour. If it is, the
    function will replace the existing weapon or armour in the character's inventory with the new item and adjust the
    character's attack or defence stat accordingly.

    :param character: a dictionary representing the player character
    :param item_name: a string representing the name of the item.
    :param item_power: an integer representing the power of the item.
    :param item_type: a string representing the type of the item ("Weapon" or "Armour").
    :precondition: character must be a dictionary with stats and an inventory.
    :precondition: item_name must be a string.
    :precondition: item_power must be an integer.
    :precondition: item_type must be a string and either "Weapon" or "Armour".
    :precondition: character must have more than 0 health.
    :postcondition: prints the status of the item added, replaced, or already in the inventory.
    :postcondition: updates the character's inventory and stats based on the item added.
    :return: a string representing the description of the item added, replaced, or already in the inventory.
    :return: an updated character dictionary.

    >>> character_test = {"Inventory": {"1": {"Name": "Bronze Sword", "Power": 1, "Type": "Weapon"}},\
 "Attack": 1, "Defence": 0}
    >>> add_equipment(character_test, "Iron Sword", 2, "Weapon")
    Replacing Bronze Sword with Iron Sword in your inventory.

    >>> character_test = {"Inventory": {"1": {"Name": "Bronze Sword", "Power": 1, "Type": "Weapon"}},\
 "Attack": 1, "Defence": 0}
    >>> add_equipment(character_test, "Bronze Sword", 1, "Weapon")
    You already have Bronze Sword in your inventory.
    """
    for key, value in character['Inventory'].items():
        if value['Name'] == item_name:
            print(f"You already have {item_name} in your inventory.")
            return

        elif item_type == "Weapon" and value['Type'] == "Weapon":
            print(f"Replacing {value['Name']} with {item_name} in your inventory.")
            character['Attack'] -= value['Power']
            value['Name'] = item_name
            value['Power'] = item_power
            character['Attack'] += item_power

        elif item_type == "Armour" and value['Type'] == "Armour":
            print(f"Replacing {value['Name']} with {item_name} in your inventory.")
            character['Defence'] -= value['Power']
            value['Name'] = item_name
            value['Power'] = item_power
            character['Defence'] += item_power


def add_inventory(character, item_name, item_power, item_quantity, item_type, item_price=0):
    """
    Add an item to the character's inventory.

    This function checks if the character already has the item in their inventory. If they do, the function will return.
    If the character does not have the item, the function will add the item to the character's inventory.

    :param character: a dictionary representing the player character
    :param item_name: a string representing the name of the item.
    :param item_power: an integer representing the power of the item.
    :param item_quantity: an integer representing the quantity of the item.
    :param item_type: a string representing the type of the item
    :param item_price: an optional integer representing the price of the item. Default is 0.
    :precondition: character must be a dictionary with an 'Inventory' key.
    :precondition: item_name must be a string.
    :precondition: item_power must be an integer.
    :precondition: item_quantity must be an integer.
    :precondition: item_type must be a string and either "Special", "Consumable", or "Miscellaneous".
    :precondition: item_price must be an integer.
    :precondition: character must have more than 0 health.
    :postcondition: prints the status of the item added or already in the inventory.
    :postcondition: updates the character's inventory based on the item added.
    :return: a string representing the description of the item added or already in the inventory.
    :return: an updated character dictionary.

    >>> character_test = {"Inventory": {"1": {"Name": "Health Potion", "Power": 15,\
"Quantity": 1, "Type": "Consumable"}}}
    >>> add_inventory(character_test, "Health Potion", 15, 1, "Consumable")
    You added 1 Health Potion(s) to your inventory!

    >>> character_test = {"Inventory": {"1": {"Name": "Frozen Orb", "Power": 0, "Quantity": 1, "Type": "Special"}}}
    >>> add_inventory(character_test, "Frozen Orb", 0, 1, "Special")
    You already have Frozen Orb in your inventory.
    """
    for key, value in character['Inventory'].items():
        if value['Name'] == item_name and value['Type'] == "Special":
            print(f"You already have {item_name} in your inventory.")
            return
        elif value['Name'] == item_name and value['Type'] == "Consumable":
            print(f"You added {item_quantity} {item_name}(s) to your inventory!")
            value['Quantity'] += item_quantity
            return
        elif value['Name'] == item_name and value['Type'] == "Miscellaneous":
            print(f"You added {item_quantity} {item_name}(s) to your inventory!")
            value['Quantity'] += item_quantity
            return

    # If the item is not in the inventory or is a non-consumable, add a new entry
    inventory_key_count = len(character['Inventory']) + 1
    new_item = {"Name": item_name, "Power": item_power, "Price": item_price, "Quantity": item_quantity,
                "Type": item_type}
    character['Inventory'][str(inventory_key_count)] = new_item
    print(f'You added {item_quantity} {item_name}(s) to your inventory!')


def battle_rewards(character, foe):
    """
    Handle the rewards after a battle.

    This function calculates the rewards after a battle, including gold and experience points. It also checks the foe's
    loot for any special items, miscellaneous items, or equipment, and adds them to the character's inventory.

    :param character: a dictionary representing the player character
    :param foe: a dictionary representing the foe
    :precondition: character must be a dictionary with stats and an inventory.
    :precondition: foe must be a dictionary with stats and loot.
    :precondition: character must have more than 0 health.
    :precondition: foe must have equal to or less than 0 health.
    :postcondition: updates the character's experience points and gold based on the foe's rewards.
    :postcondition: updates the character's inventory based on the foe's loot.
    :return: a string representing the description of the rewards.
    :return: an updated character dictionary.

    >>> character_test = {"Experience Points": 0, "Gold": 0, "Inventory": {}}
    >>> foe_test = {"Name": "Orc", "Gold": 10, "Experience Points": 10,\
 "Loot": {"Cheap Trinket": {"Price": 8, "Type": "Miscellaneous"}}}
    >>> battle_rewards(character_test, foe_test)
    xX------------------------------------------------------Xx
    You defeated the Orc and earned 10 gold!
    You gained 10 experience points!
    Your total gold is now 10.
    You obtained a sellable miscellaneous item: Cheap Trinket!
    You added 1 Cheap Trinket(s) to your inventory!

    >>> character_test = {"Experience Points": 0, "Gold": 0, "Inventory": {}}
    >>> foe_test = {"Name": "Ice Guardian", "Gold": 50, "Experience Points": 50,\
    "Loot": {"Frozen Orb": {"Type": "Special"}}}
    >>> battle_rewards(character_test, foe_test)
    xX------------------------------------------------------Xx
    You defeated the Ice Guardian and earned 50 gold!
    You gained 50 experience points!
    Your total gold is now 50.
    +▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔+
    |  You obtained a special item: Frozen Orb!  |
    +▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁+
    You added 1 Frozen Orb(s) to your inventory!
    """
    draw()
    print(f"You defeated the {foe['Name']} and earned {foe['Gold']} gold!")
    character["Experience Points"] += foe['Experience Points']
    print(f"You gained {foe['Experience Points']} experience points!")
    character['Gold'] += foe['Gold']
    print(f"Your total gold is now {character['Gold']}.")

    # Check for miscellaneous item in foe's inventory
    foe_inventory = foe.get('Loot', {})  # Returns an empty dictionary if 'Loot' key does not exist

    for item_name, item_info in foe_inventory.items():
        item_type = item_info.get('Type', '')
        item_price = item_info.get('Price', 0)

        if item_type == 'Special':
            print(draw_box(f"You obtained a special item: {item_name}!"))
            add_inventory(character, item_name, 0, 1, item_type)

        elif item_type == 'Miscellaneous':
            print(f"You obtained a sellable miscellaneous item: {item_name}!")
            add_inventory(character, item_name, 0, 1, item_type, item_price=item_price)

        elif item_type == 'Equipment':
            if item_name == "Radiant Blade":
                print(draw_box(f"You obtained a special weapon: {item_name}!"))
                add_equipment(character, item_name, 10, "Weapon")

            elif item_name == "Guardian Armour":
                print(draw_box(f"You obtained special armor: {item_name}!"))
                add_equipment(character, item_name, 6, "Armour")


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
            print("1. Health Potion $5\n2. AP Potion $10")
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
