# --- Exercise 1 : Cars ---
#
cars1, cars2, cars3, cars4, cars5 = "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet"
#2
list_cars = [cars1, cars2, cars3, cars4, cars5]
print(list_cars)
#3
print(f"There is {len(list_cars)} manufacturers/companies")
#4
list_cars.sort(reverse=True)
print(list_cars)
#5
manufacturers_containing_o = [car for car in list_cars if "o" in car.lower()]
print(f"There is {len(manufacturers_containing_o)} manufacters with the letter O in there name")
manufacturers_containing_o = [car for car in list_cars if "i" not in car.lower()]
print(f"There is {len(manufacturers_containing_o)} manufacters with the letter i not in there name")
#6
list_cars = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
list_cars = list(set(list_cars))
print(", ".join(list_cars))
print(f"There is {len(list_cars)} companies in the list")
#7
list_reversed_cars = []
for car in list_cars:
    reversed_car = ""
    for c in reversed(car):
        reversed_car += c
    list_reversed_cars.append(reversed_car)
list_reversed_cars.sort()
print(list_reversed_cars)

print("--------------------------")