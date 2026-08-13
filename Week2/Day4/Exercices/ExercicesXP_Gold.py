import json

# --- Exercise 1 : Restaurant Menu Manager ---
a_json = {
    "items": [
        {
            "name": "Vegetable soup",
            "price": 30
        },
        {
            "name": "Hamburger",
            "price": 44.9
        },
        {
            "name": "Milkshake",
            "price": 22.5
        },
        {
            "name": "Artichoke",
            "price": 18
        },
        {
            "name": "Beef stew",
            "price": 52.5
        }
    ]
}

with open("restaurant_menu.json", "w") as f:
    json.dump(a_json, f, indent=4)
print("--------------------------")
