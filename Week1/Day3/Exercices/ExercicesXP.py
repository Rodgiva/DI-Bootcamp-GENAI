# --- 🌟 Exercise 1: Converting Lists into Dictionaries ---
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
a_dict = dict(zip(keys, values))
print(a_dict)
print("--------------------------")

# --- 🌟 Exercise 2: Cinemax #2 ---
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 0
for k, v in family.items():
    if 3 <= v <= 12:
        price += 10
        print(f"{k}: 10$")
    elif v > 12:
        price += 15
        print(f"{k}: 15$")
    else:
        print(f"{k}: Free!")
print(f"Finale cost: {price}$")
print("--------------------------")

# --- 🌟 Exercise 3: Zara ---
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color":
        {"France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]}
}
brand["number_stores"] = 2
print(f"Zara cleints using clothes for {", ".join(brand["type_of_clothes"])}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)
brand.pop("creation_date")
print(brand)
print(brand["international_competitors"][-1])
print(brand["major_color"].values())
print(len(brand.keys()))
print(", ".join(brand.keys()))

more_on_zara = {"creation_date": 1984,
"number_stores": 3684}
print(brand | more_on_zara)
print("--------------------------")

# --- 🌟 Exercise 4: Disney Characters ---
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#1
dict_users = {}
for i in range(len(users)):
    dict_users[users[i]] = i
print(dict_users)
print("--------------------------")
#2
dict_users2 = {}
for i in range(len(users)):
    dict_users2[i] = users[i]
print(dict_users2)
print("--------------------------")
#3
dict_users3 = {}
users.sort()
for i in range(len(users)):
    dict_users3[users[i]] = i
print(dict_users3)
print("--------------------------")