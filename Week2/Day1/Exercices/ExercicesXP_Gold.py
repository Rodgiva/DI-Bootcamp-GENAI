import math as m
import random as r

# --- Exercise 1 : Geometry ---
class Circle():
    def __init__(self, radius:float = 1.0):
        self.radius = radius

    def perimeter(self)->float:
        return self.radius * 2 * m.pi

    def area(self)->float:
        return self.radius**2 * m.pi

    def definition(self):
        print("A circle is the set of all points in the plane that are a fixed distance (the radius) from a fixed point (the centre). Any interval joining a point on the circle to the centre is called a radius. By the definition of a circle, any two radii have the same length")
print("--------------------------")

# --- Exercise 2 : Custom List Class ---
class MyList():
    def __init__(self, letters:list = None):
        self.letters = [] if letters == None else list(letters)

    def reverse(self)->list:
        res = []
        for i in range(self.letters, 0, -1):
            res.append(self.letters[i])
        return res

    def sorted(self)->list:
        res = list(self.letters)
        res.sort()
        return res

    def bonus(self)->list:
        return [r.randint for i in self.letters]
print("--------------------------")

# --- Exercise 3 : Restaurant Menu Manager ---
class MenuManager():
    def __init__(self, menu = None):
        self.menu = [] if menu == None else list(menu)

    def add_item(self, name:str, price:int, spice:str, gluten:bool)->MenuManager:
        self.menu.append({
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        })
        print("New dish added successfully")
        return self

    def update_item(self, name:str, price:int, spice:str, gluten:bool)->MenuManager:
        for dish in self.menu:
            if dish["name"] == name:
                dish.update({"name": name, "price": price, "spice": spice, "gluten": gluten})
                print(f"Dish {name} updated successfully")
                return self
        print("The dish is not in the menu.")
        return self

    def remove_item(self, name: str) -> MenuManager:
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"Dish {name} deleted successfully")
                return self
        print("The dish is not in the menu.")
        return self

    def show(self):
        for dish in self.menu:
            if dish:
                print("************")
                for k,v in dish.items():
                    print(f"{k} - {v}")
        print("************")
        

a_menu = MenuManager()
a_menu.show()
a_menu.add_item("Soup",10, "B", False).add_item("Hamburger", 15, "A", True).add_item("Salad", 18, "A", False).add_item("French Fries", 5, "C", False).add_item("Beef bourguignon", 25, "B", True)
a_menu.show()
a_menu.update_item("Soup",12, "C", True)
a_menu.show()
a_menu.remove_item("Beef bourguignon")
a_menu.show()

print("--------------------------")