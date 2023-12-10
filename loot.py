from utility import (
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
