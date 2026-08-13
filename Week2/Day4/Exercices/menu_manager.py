import json

class MenuManager():
    def __init__(self):
        self.menu = None
        with open("restaurant_menu.json", "r") as f:
            self.menu = json.load(f)

    # def __new__(cls):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #     return cls.instance

    def add_item(self, name, price):
        self.menu[name] = price

    def remove_item(self, name):
        if self.menu[name]:
            del self.menu[name]
            return True
        else:
            return False

    def save_to_file(self):
        with open("restaurant_menu.json", "w") as f:
            json.dump(self.menu, f, indent=4)
a_menu_manager = MenuManager()
print(a_menu_manager.menu["items"])