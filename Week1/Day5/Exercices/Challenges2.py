# --- Exercise 1 ---
def pattern_drawer1(length:int):
    for i in range(1, length+1, 2):
        line = ("*"*i).center(length)
        print(line)
pattern_drawer1(5)

def pattern_drawer2(length:int):
    for i in range(1, length+1):
        line = ("*"*i).rjust(length)
        print(line)
pattern_drawer2(5)

def pattern_drawer3(length:int):
    for i in range(1, length+1):
        line = ("*"*i).ljust(length)
        print(line)
    for i in range(length, 0, -1):
        line = ("*"*i).rjust(length)
        print(line)
pattern_drawer3(5)
print("--------------------------")

# --- Exercise 2 ---
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
# This is an ascending sorting algorithm 