from utility import clear


def add_equipment(character, item_name, item_power, item_type):
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


def add_inventory(character, item_name, item_power, item_quantity, item_type):
    for key, value in character['Inventory'].items():
        if value['Name'] == item_name and value['Type'] == "Consumable":
            print(f"You added {item_quantity} {item_name}(s) to your inventory!")
            value['Quantity'] += item_quantity
            return
        elif value['Name'] == item_name and value['Type'] == "Special":
            print(f"You already have {item_name} in your inventory.")
            return

    # If the item is not in the inventory or is a non-consumable, add a new entry
    inventory_key_count = len(character['Inventory']) + 1
    new_item = {"Name": item_name, "Power": item_power, "Quantity": item_quantity, "Type": item_type}
    character['Inventory'][str(inventory_key_count)] = new_item
    print(f'You added {item_quantity} {item_name}(s) to your inventory!')


def battle_rewards(character, foe):
    print(f"You defeated the {foe['Name']} and earned {foe['Gold']} gold!")
    character["Experience Points"] += foe['Experience Points']
    print(f"You gained {foe['Experience Points']} experience points!")
    character['Gold'] += foe['Gold']
    print(f"Your total gold is now {character['Gold']}.")

    # Check for special item in foe's inventory
    special_item = foe.get('Special Item')
    if special_item:
        print(f"You obtained a special item: {special_item}!")
        add_inventory(character, special_item, 0, 1, "Special")

    # Check for equipment item in foe's inventory
    equipment_item = foe.get('Equipment Item')
    if equipment_item == "Radiant Blade":
        print(f"You obtained a special item: {equipment_item}!")
        add_equipment(character, equipment_item, 8, "Weapon")
    elif equipment_item == "Guardian Armour":
        print(f"You obtained a special item: {equipment_item}!")
        add_equipment(character, equipment_item, 5, "Armour")


def visit_shop(character):
    """
    """
    print("Welcome to the Shop!")

    while True:
        print("1. Buy Weapon")
        print("2. Buy Armour")
        print("3. Buy Potions")
        print("4. Leave Shop")
        print(f"You currently have {character['Gold']} gold.")
        choice = input("Choose an option (1, 2, 3, or 4): ")

        if choice == "1":  # Buying a weapon
            clear()
            print(f"1. Iron Sword $10\n2. Steel Sword $30")
            weapon_choice = input("Enter the number of the weapon you want to buy: ")

            if weapon_choice == "1":
                weapon_cost = 15
                weapon_name = "Iron Sword"
                weapon_power = 2

            elif weapon_choice == "2":
                weapon_cost = 30
                weapon_name = "Steel Sword"
                weapon_power = 4

            else:
                clear()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < weapon_cost:
                clear()
                print("Not enough gold to buy the weapon.")

            elif any(item.get('Name') == weapon_name for item in character['Inventory'].values()):
                clear()
                print(f"You already have {weapon_name} in your inventory.")
                continue

            elif any(value['Power'] >= weapon_power for value in character['Inventory'].values() if
                     value['Type'] == 'Weapon'):
                clear()
                print("\"You already have a powerful weapon!\"")
                continue

            else:
                clear()
                print(f"You bought {weapon_name}!")
                character['Gold'] -= weapon_cost
                add_equipment(character, weapon_name, weapon_power, "Weapon")

        elif choice == "2":  # Buying armour
            clear()
            print(f"1. Leather Armour $10\n2. Iron Armour $30")
            armour_choice = input("Enter the number of the armour you want to buy: ")

            if armour_choice == "1":
                armour_cost = 15
                armour_name = "Leather Armour"
                armour_power = 1

            elif armour_choice == "2":
                armour_cost = 30
                armour_name = "Iron Armour"
                armour_power = 2

            else:
                clear()
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < armour_cost:
                clear()
                print("Not enough gold to buy the armour.")

            elif any(item.get('Name') == armour_name for item in character['Inventory'].values()):
                clear()
                print(f"You already have {armour_name} in your inventory.")
                continue

            elif any(value['Power'] >= armour_power for value in character['Inventory'].values() if
                     value['Type'] == 'Armour'):
                clear()
                print("\"You already have a magnificent suit of armour!\"")
                continue

            else:
                clear()
                print(f"You bought {armour_name}!")
                character['Gold'] -= armour_cost
                add_equipment(character, armour_name, armour_power, "Armour")

        elif choice == "3":
            clear()
            print("1. Health Potion $5\n2. AP Potion $10")
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
                print("Invalid choice. Please enter a valid option.")
                continue

            if character['Gold'] < potion_cost:
                clear()
                print("Not enough gold to buy the potion.")

            else:
                clear()
                print(f"You bought a {potion_name}!")
                character['Gold'] -= potion_cost
                add_inventory(character, potion_name, potion_power, 1, "Consumable")

        elif choice == "4":
            clear()
            print(f"\"Thanks for visiting the Shop! Come again.\"")
            break

        else:
            clear()
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    return character
