from datetime import date, datetime
import math

def get_age(birth_date: date):
    now = date.today()
    age = now.year  - birth_date.year
    if now.month <= birth_date.month and now.day <= birth_date.day:
        age -= 1
    return age

def is_leap_year(birth_date: date):
    if birth_date.year % 400 == 0:
        return True
    elif birth_date.year % 100 == 0:
        return False
    elif birth_date.year % 4 == 0:
        return True

def cake(age):
    nb_candles = int(str(age)[-1])
    candles = "".join(["i" for i in range(nb_candles)])
    candles = candles.center(len(candles) + 11 - nb_candles).replace(" ", "_")
    layers = []
    layers.append(candles.center(len(candles) + 8))
    layers.append("   |:H:a:p:p:y:|   ")
    layers.append(" __|___________|__ ")
    layers.append("|^^^^^^^^^^^^^^^^^|")
    layers.append("|:B:i:r:t:h:d:a:y:|")
    layers.append("|                 |")
    layers.append("~~~~~~~~~~~~~~~~~~~")
    print("".join([i + "\n" for i in layers]))

inp_bd = input("What is your birthday? (DD/MM/YYYY) ")
birth_date = datetime.strptime(inp_bd, "%d/%m/%Y")


age = get_age(birth_date)
cake(age)
if is_leap_year:
    cake(age)