import random as r
import string as s
import datetime as dt
from faker import Faker

# --- 🌟 Exercise 1: Currencies ---
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return f"{str(self.amount)} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise Exception(f"Cannot add between Currency type {self.currency} and {other.currency}")
        return self.amount + other if type(other) != Currency else self.amount + other.amount

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise ValueError("Cannot add different currencies")
            self.amount += other.amount
        else:
            self.amount += other
        return self

    #Your code starts HERE

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

# print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>
#comment the print above before you run the file for next exercises (since the error will crash your file)
print("--------------------------")

# --- 🌟 Exercise 3: String module ---
print("".join([r.choice(s.ascii_lowercase) for l in range(5)]))
print("--------------------------")

# --- 🌟 Exercise 4: Current Date ---
curr_date = dt.datetime.now()
print(curr_date)
print("--------------------------")

# --- 🌟 Exercise 5: Amount of time left until January 1st ---
curr_date = dt.datetime.now()
a_date = dt.datetime(curr_date.year+1, 1, 1)
print(a_date - curr_date)
print("--------------------------")

# --- 🌟 Exercise 6: Birthday and minutes ---
# Create a function that accepts a birthdate as an argument (in the format of your choice),
# then displays a message stating how many minutes the user lived in his life.
def get_minutes_lives(bd:str):
    bd_list = bd.split("/")
    curr_date = dt.datetime.now()
    bd_date = dt.datetime(int(bd_list[2]), int(bd_list[1]), int(bd_list[0]))
    minutes_lives = curr_date - bd_date
    return f"{int(minutes_lives.total_seconds() // 60)} minutes"

print(get_minutes_lives("20/08/1992"))
print("--------------------------")

# --- 🌟 Exercise 7: Faker Module ---
fake = Faker()
faker_list = []

def add_users(nb_users:int):
    for i in range(nb_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        faker_list.append(user)

add_users(20)
for user in faker_list:
    print(user)
print("--------------------------")
