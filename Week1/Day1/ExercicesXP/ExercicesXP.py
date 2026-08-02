# --- Exercise 1: Hello World ---
for i in range(4):
    print("hello world")
print("--------------------------")

# --- Exercise 2: Some Math ---
print((99^3)*8)
print("--------------------------")

# --- Exercise 3: What is the output? ---
print(15 < 8) #False
print(5 < 3) #False
print(3 == 3) #True
# print(3 == "3") #Error
# print("3" > 3) #Error
print("Hello" == "hello") #False
print("--------------------------")

# --- Exercise 4: Your computer brand---
computer_brand = "dell"
print(f"I have a {computer_brand} computer.")
print("--------------------------")

# --- Exercise 5: Your information ---
name = "Avigdor"
age = "33"
shoe_size= "42"
info = f"My name is 0 {name}, I am {age} years old and I am wearing {shoe_size} size shoes."
print(info)
print("--------------------------")

# --- Exercise 6: A & B ---
a = 42
b = 91
if a > b:
    print("Hello World")
print("--------------------------")

# --- Exercise 7: Odd or Even ---
inp = input("Give me a number")
if input % 2:
    print("even")
else:
    print("odd")
print("--------------------------")

# --- Exercise 8: What’s your name? ---
my_name = "Avigdor"
inp_name = input("What is yout name?")
if my_name.lower() == inp_name.lower():
    print("Really? We have the same name!")
print("--------------------------")

# --- Exercise 9: Tall enough to ride a roller coaster ---
inp_height = input("What is your height? (in cm)")
if inp_height > 145:
    print("You are tall enough to ride, have fun!")
else:
    print("You are not tall enough to ride, try again next year.")
print("--------------------------")

