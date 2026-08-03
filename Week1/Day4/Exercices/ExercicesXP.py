import random as r

# --- 🌟 Exercise 1: What Are You Learning? ---
def display_message():
    print("“I am learning about functions in Python.”")
display_message()
print("--------------------------")

# --- 🌟 Exercise 2: What’s Your Favorite Book? ---
def favorite_book(title: str):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")
print("--------------------------")

# --- 🌟 Exercise 3: Some Geography ---
def describe_city(city: str, country: str = "Unknown"):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
print("--------------------------")

# --- Exercise 4: Random ---
def a_func(nb: int):
    rand_nb = r.randint(1,100)
    if nb == rand_nb:
        print("success")
    else:
        print(f"Fail. The number to guess: {rand_nb}, and your number: {nb}")
a_func(50)
print("--------------------------")

# --- 🌟 Exercise 5: Let’s Create Some Personalized Shirts! ---
def make_shirt(size: str = "large", text: str = "I love Python"):
    print(f"The shirt’s size: {size}\n{text}")
make_shirt("M", "This is the commentaire that everyone doesn't care")

make_shirt()
make_shirt("medium")
make_shirt("small", "This is a message")
make_shirt(size="small", text="Hello!")
print("--------------------------")

# --- 🌟 Exercise 6: Magicians… ---
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names: list):
    for i in magician_names:
        print(i)

def make_great(magician_names: list):
    for i in magician_names:
        print(f"The Great {i}")

show_magicians(magician_names)
make_great(magician_names)
print("--------------------------")

# --- 🌟 Exercise 7: Temperature Advice ---
def get_random_temp():
    # return r.randint(-10, 40)
    return r.uniform(-10, 40)

def main():
    rand_temp = get_random_temp()
    print(f"The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= rand_temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= rand_temp < 23:
        print("Nice weather.")
    elif 23 <= rand_temp < 32:
        print("“A bit warm, stay hydrated..")
    elif 32 <= rand_temp < 40:
        print("It’s really hot! Stay cool.")

# Step 5: Month-Based Seasons (Bonus)
def get_season(month: int):
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"
    else:
        return None

def get_random_temp_modified(season: str):
    ranges_season = {
        "winter": (-10, 5),
        "spring": (5, 20),
        "summer": (20, 40),
        "autumn": (5, 20),
    }
    low, high = ranges_season[season]
    return r.uniform(low, high)

def main():
    inp_month = int(input("Give me a month: (1-12) "))
    rand_temp = get_random_temp_modified(get_season(inp_month))
    print(f"The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= rand_temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= rand_temp < 23:
        print("Nice weather.")
    elif 23 <= rand_temp < 32:
        print("“A bit warm, stay hydrated..")
    elif 32 <= rand_temp < 40:
        print("It’s really hot! Stay cool.")

main()
print("--------------------------")
