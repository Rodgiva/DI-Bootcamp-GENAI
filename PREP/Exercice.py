list = [1,2,3,4]
for i in list:
    print(i)

list = [1,2,3,4]
for i in list:
    print(i*20)

list = ["Elie", "Tim", "Matt"]
for i in list:
    print(i.title())

list = [1,2,3,4,5,6]
res = []
for i in list:
    if i % 2 == 0:
        res.append(i)
print(res)

list1 = [1,2,3,4]
list2 = [3,4,5,6]

print([
    x
    for x in list1
    if x in list2
])

list = ["Elie", "Tim", "Matt"]
res = []
for i in list:
    res.append(i.lower()[::-1])
print(res)

str1 , str2 = "first", "third"
str = str1 + str2
print([
    x
    for x in str
    if x in ["i", "r", "t"]
])

print([
    x
    for x in range(1, 100)
    if x % 12 == 0
])

print([
    x
    for x in "amazing"
    if x not in ["a", "i", "e", "o", "u"]
])

list = []
for i in range(0, 3):
    list_ = []
    for j in range(0, 3):
        list_.append(j)
    list.append(list_)
print(list)

list = []
for i in range(10):
    list_ = []
    for j in range(10):
        list_.append(j)
    list.append(list_)
print(list)