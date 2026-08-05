import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
paired = []

for i in range(len(list_of_numbers)-1):
    # an indicator to confirm that de program is running
    if i % 100 == 0:
        print(f"i:{i}")
    for j in range(i+1, len(list_of_numbers)):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            paired.append((list_of_numbers[i], list_of_numbers[j]))
print(paired)