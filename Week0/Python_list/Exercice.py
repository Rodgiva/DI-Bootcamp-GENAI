# --- 1 ---
input_list = [1,2,3,4]
[print(n) for n in input_list]
print("----------------")

# --- 2 ---
input_list = [1,2,3,4]
[print(n*20) for n in input_list]
print("----------------")

# --- 3 ---
input_list = ["Elie", "Tim", "Matt"]
print([i[0] for i in input_list])
print("----------------")

# --- 4 ---
input_list = [1,2,3,4,5,6]
print([n for n in input_list if n % 2 == 0])
print("----------------")

# --- 5 ---
input_list1 = [1,2,3,4]
input_list2 = [3,4,5,6]
print([n for n in input_list1 if n in input_list2])
print("----------------")

# --- 6 ---
input_list = ["Elie", "Tim", "Matt"]
print([i.lower()[::-1] for i in input_list])
print("----------------")

# --- 7 ---
str1 , str2 = "first", "third"
input_str = str1 + str2
print("".join([x for x in input_str if x in ["i", "r", "t"]]))
print("----------------")

# --- 8 ---
print([x for x in range(1, 100) if x % 12 == 0])
print("----------------")

# --- 9 ---
print([x for x in "amazing"if x not in ["a", "i", "e", "o", "u"]])
print("----------------")

# --- 10 ---
input_list = []
print([[i for i in range(0,3)] for j in range(0, 3)])
print("----------------")

# --- 11 ---
input_list = []
print([[i for i in range(0,10)] for j in range(0, 10)])