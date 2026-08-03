# # --- Exercise 1: Birthday Look-up ---
# # --- Exercise 2: Birthdays Advanced ---
# birthdays = {}
# birthdays["Bob"] = "1990/02/05"
# birthdays["Henri"] = "1994/06/20"
# birthdays["Hubert"] = "1991/04/07"
# birthdays["Charles"] = "1993/08/15"
# birthdays["Fred"] = "1996/04/25"

# print(f"Hi and welcome! You can look up the birthdays of the people in the list!")
# print(", ".join(birthdays.keys()))
# inp_name = input("Give me a person's namein the list: ")
# if inp_name in birthdays.keys():
#     bd = birthdays[inp_name]
#     print(f"The birthday of {inp_name} is {bd}")
# else: 
#     print(f"Sorry, we don’t have the birthday information for {inp_name}")
# print("--------------------------")

# # --- Exercise 3: Add Your Own Birthday ---
# birthdays = {}
# birthdays["Bob"] = "1990/02/05"
# birthdays["Henri"] = "1994/06/20"
# birthdays["Hubert"] = "1991/04/07"
# birthdays["Charles"] = "1993/08/15"
# birthdays["Fred"] = "1996/04/25"

# print(f"Hi and welcome! You can look up the birthdays of the people in the list!")
# print(", ".join(birthdays.keys()))

# inp_name = input("Give me a person's name: ")
# if inp_name in birthdays.keys():
#     inp_bd = birthdays[inp_name]
#     print(f"The birthday of {inp_name} is {inp_bd}")
# else: 
#     birth_date = input("Now give me his borth day: (in the format “YYYY/MM/DD”) ")
#     birthdays[inp_name] = birth_date

# print("--------------------------")

# --- Exercise 4: Fruit Shop ---
#1
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for k,v in items.items():
    print(f"{k}: {v}$")
#2
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
total_cost = 0
for k,v in items.items():
    total_cost += v["price"] * v["stock"]
print(f"Total cost: {int(total_cost)}$")
print("--------------------------")