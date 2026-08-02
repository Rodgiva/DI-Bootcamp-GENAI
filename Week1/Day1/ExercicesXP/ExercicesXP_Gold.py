# --- Exercise 1 : Hello World-I love Python ---
lst = ['Hello world', "I love python"]
for elem in lst:
    for i in range(4):
        print(elem)
print("--------------------------")

# --- Exercise 2 : What is the Season ? ---
monts_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
inp_month = input("Choose a number of month between 1 to 12")
print(f"You chosed {monts_list[inp_month]}")
if 3 <= inp_month <= 5:
    print("Spring")
elif 6 <= inp_month <= 8:
    print("Summer")
elif 9 <= inp_month <= 11: 
    print("Autumn")
elif 12 == inp_month or inp_month <= 2: 
    print("Winter")
print("--------------------------")