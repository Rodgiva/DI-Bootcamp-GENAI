# --- Daily Challenge: Coffee Shop Menu Manager ---

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict: dict):
    if len(menu_dict) == 0:
        print("The menu is empty.")
    else:
        print("*************")
        print("Current menu:")
        for k,v in menu_dict.items():
            print(f"{k} - {v}₪")
        print("*************")
        
def add_item(menu_dict:dict):
    drink_name = input("Give me the name of the drink you want to add: ")
    if drink_name in menu_dict:
        print("Item already exists!")
        return
    drink_price = int(input("And give me the price of the drink: "))
    if drink_price < 0:
        print("Invalid price.")
        return
    menu_dict[drink_name] = drink_price
    show_menu(menu)
    print(f"{drink_name.capitalize()} added!")

def update_price(menu_dict:dict):
    show_menu(menu)
    inp_drink = input("Which drink you want to update? ")
    if inp_drink not in menu_dict:
        print("Item not found.")
        return
    inp_price = input("Give me a new price of this drink: ")
    if inp_price < 0:
        print("Invalid price.")
        return
    menu_dict[inp_drink] = inp_price
    show_menu(menu)
    print("Price updated!")

def delete_item(menu_dict:dict):
    show_menu(menu)
    inp_drink = input("Which drink you want to remove? ")
    if inp_drink not in menu_dict:
        print("Item not found.")
        return
    menu_dict.pop(inp_drink)
    show_menu(menu)
    print("Item deleted.")

def show_options():
    print("What would you like to do?\n1. Show menu\n2. Add item\n3. Update price\n4. Delete item\n5. Search item\n6. Exit")

def search_item(menu_dict:dict):
    inp_drink = input("Name of drink you want to find: ")
    if inp_drink not in menu_dict:
        print("Not in the menu.")
        return
    price_found = menu_dict[inp_drink]
    print(f"{inp_drink} - {price_found}₪")

def run_coffee_shop():
    show_options()
    command = input("Please choose a command: (1-6) ")
    while command != "6":
        if command == "1":
            show_menu(menu)
        elif command == "2":
            add_item(menu)
        elif command == "3":
            update_price(menu)
        elif command == "4":
            delete_item(menu)
        elif command == "5":
            search_item(menu)
        else:
            print("Invalid choice, try again.")
        command = input("Please choose a command: (1-6) ")
    print("Goodbye!")

def apply_discount(menu_dict:dict, percent:int):
    # menu_dict = {k : (v * (1 - percent/100)) for k, v in menu_dict.items()}
    for k in menu_dict:
        menu_dict[k] = round(menu_dict[k] * (1 - percent/100), 2)
    print(f"A discount of {percent}% has been applied to all the drinks!")
apply_discount(menu, 10)
run_coffee_shop()

print("--------------------------")