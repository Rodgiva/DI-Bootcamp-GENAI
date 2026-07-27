list = [("name", "Elie"), ("job", "Instructor")]
dict = dict(list)
print(dict)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
dict = {
    list1[i]: list2[i] for i in range(len(list1))
}
print(dict)

list = ["a", "e", "i", "o", "u"]
dict = {i: 0 for i in list}
print(dict)

dict = {
    k + 1:chr(65 + k)
    for k in range(26)
}
print(dict)

str = "awesome sauce"
voy = "aeiou"
dict = {
    k: str.count(k) for k in voy
}
print(dict)