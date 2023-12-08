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


def add_inventory(character, item_name, item_power, item_quantity, item_type, item_price=0):
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

        if item_type == 'Miscellaneous':
            print(f"You obtained a sellable miscellaneous item: {item_name}!")
            add_inventory(character, item_name, 0, 1, item_type, item_price=item_price)

        elif item_type == 'Special':
            print(f"You obtained a special item: {item_name}!")
            add_inventory(character, item_name, 0, 1, item_type)

        elif item_type == 'Equipment':
            if item_name == "Radiant Blade":
                print(f"You obtained a special weapon: {item_name}!")
                add_equipment(character, item_name, 8, "Weapon")

            elif item_name == "Guardian Armour":
                print(f"You obtained special armor: {item_name}!")
                add_equipment(character, item_name, 5, "Armour")


def visit_shop(character):
    """
    """
    print("Welcome to the Shop!")

    while True:
        print("1. Buy Weapon")
        print("2. Buy Armour")
        print("3. Buy Potions")
        print("4. Sell Items")
        print("5. Rest for 15 gold")
        print("6. Leave Shop")
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
            print("\"What are you selling, stranger?\"")
            miscellaneous_items = [(key, value) for key, value in character['Inventory'].items()
                                   if value.get('Type') == 'Miscellaneous']
            for item_key, item_details in miscellaneous_items:
                price = item_details.get('Price', 0)
                quantity = item_details.get('Quantity', 0)

                if not quantity:
                    print("\"You've got nothing to sell!\"")
                    continue

                elif quantity > 0:
                    total_item_value = price * quantity
                    character["Gold"] += total_item_value
                    item_details['Quantity'] -= quantity
                    print(f"You sold {quantity} {item_details['Name']}(s) for {total_item_value} gold.")

        elif choice == "5":
            clear()
            if character['Gold'] < 15:
                print("\"You don't have enough gold to rest.\"")
                continue

            else:
                character['Gold'] -= 15
                character['Current Health'] = character['Max HP']
                character['Ability Points'] = character['Max AP']
                print("\"Eat something while you rest, traveler.\"")
                print("You feel refreshed! Your HP and AP are full.")

        elif choice == "6":
            clear()
            print(f"\"Thanks for visiting the Shop! Come again.\"")
            break

        else:
            clear()
            print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")

    return character
