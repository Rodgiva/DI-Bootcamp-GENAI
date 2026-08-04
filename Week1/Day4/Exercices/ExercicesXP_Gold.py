import random as r

# --- Exercise 1 : When will I retire ? ---
def get_age(year:str, month:str, day:str)-> int:
    curr_year = 2026
    curr_month = 8
    curr_day = 4

    age = curr_year - int(year)
    if curr_month <= int(month) and curr_day <= int(day):
        age += 1
    return age

def can_retire(gender:str, date_of_birth:str):
    year_birth_date, month_birth_date, day_birth_date = date_of_birth.split("/")
    age = get_age(year_birth_date, month_birth_date, day_birth_date)
    if gender == "m" and age >= 67:
        print("Yes")
    elif gender == "f" and age >= 62:
        print("Yes")
    else:
        print("No")
can_retire("m", "1992/08/20")
print("--------------------------")

# --- Exercise 2 : Sum ---
def a_func(x:int):
    x1 = x
    x2 = int(str(x1) + str(x1))
    x3 = int(str(x2) + str(x1))
    x4 = int(str(x3) + str(x1))
    return x1 + x2 + x3 + x4
print(a_func(3))
print("--------------------------")

# --- Exercise 3 : Double Dice ---
#1
def throw_dice()->int:
    return r.randint(1,6)
#2
def throw_until_doubles()->int:
    throw1 = throw_dice()
    throw2 = throw_dice()
    count = 0
    while throw1 != throw2:
        count += 1
        throw1 = throw_dice()
        throw2 = throw_dice()
    return count
print(throw_until_doubles())
#3
def main():
    res = []
    for i in range(100):
        res.append(throw_until_doubles())
    avg = sum(res)/len(res)
    print(f"It took in total {sum(res)} throws to reach 100 doubles")
    print(f"Also, the average of this result is {round(avg, 2)}")
main()
print("--------------------------")
