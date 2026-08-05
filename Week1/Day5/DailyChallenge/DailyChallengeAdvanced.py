import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
paired = []
print(len(list_of_numbers))
list_of_numbers = list(set(list_of_numbers))
print(len(list_of_numbers))

for i in range(len(list_of_numbers)-1):
    for j in range(i+1, len(list_of_numbers)):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            paired.append((list_of_numbers[i], list_of_numbers[j]))
print(paired)