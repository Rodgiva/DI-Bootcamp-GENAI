# --- 🌟 Exercise 1: Favorite Numbers ---
my_fav_numbers = set({5,6,7})
my_fav_numbers.add(1)
my_fav_numbers.add(2)
my_fav_numbers.remove(2)

friend_fav_numbers = set({8,9,0})
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
print("--------------------------")

# --- 🌟 Exercise 2: Tuple ---
# Done
print("--------------------------")

# --- 🌟 Exercise 3: List Manipulation ---
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
print(basket)
basket.clear()
print(basket)
print("--------------------------")

# --- 🌟 Exercise 4: Floats ---
# integer are numbers without decimals
# floats are numbers with decimals

lst = []
i: int = 1.5
while i <= 5:
    if i % 1 == 0:
        lst.append(int(i))
    else:
        lst.append(i)
    i += .5
print(lst)
print("--------------------------")

# --- 🌟 Exercise 5: For Loop ---
print([i for i in range(1,21)])
# print([i for i in range(1,21) if i%2==0])
print([i[1] for i in enumerate(range(1,21)) if i[0]%2==0])
print("--------------------------")

# --- 🌟 Exercise 6: While Loop ---
inp_name = input("What is your name? ")
def name_checker(txt):
    if txt.isdigit():
        return True
    elif len(txt) < 3:
        return True
    return False
while name_checker(inp_name):
    inp_name = input("Give the correct name: ")
print("Thank you!")

print("--------------------------")

# --- 🌟 Exercise 7: Favorite Fruits ---
inp_fruits = input("Tell me ALL your favorites fruits (separated by speces): ")
lst_fruits = inp_fruits.split(" ")
inp_fruit = input("Now give me a fruit: ")
if inp_fruit in lst_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

print(lst_fruits)
print("--------------------------")

# --- 🌟 Exercise 8: Pizza Toppings ---
inp_topping = None
toppings = set()
while inp_topping != "quit":
    print(inp_topping)
    if inp_topping:
        toppings.add(inp_topping)
    inp_topping = input("What topping do you want on your pizza? (one by one, tape quit to finish): ")
print(toppings)
price = 10 + (len(toppings)-1) * 2.5
print(f"{price}$")
print("--------------------------")

# --- 🌟 Exercise 9: Cinemax Tickets ---
price = 0
inp_age = input("What is the age of each person? (one by one, type quit to finish): ")

while inp_age != "quit":
    age = int(inp_age)
    if 3 <= age <= 12:
        price += 10
    elif age > 12:
        price += 15
    inp_age = input("What is the age of each person? (one by one, type quit to finish): ")
print(f"{price}$")

# Bonus
group = []
inp_age = input("What is the age of each person? (one by one, type quit to finish): ")

while inp_age != "quit":
    if not inp_age.isdigit():
        if inp_age == "":
            print("Please enter a valid number")
        else:
            print("Empty input, please try again")
    elif 16 <= int(inp_age) <= 21:
        group.append(int(inp_age))
    inp_age = input("Next! (type quit to finish): ")

print(group)

print("--------------------------")

