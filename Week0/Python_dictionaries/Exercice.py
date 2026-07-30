# --- 1 ---
input_list = [("name", "Elie"), ("job", "Ininput_structor")]
print({item[0]:item[1] for item in input_list})
# print(dict(input_list))
print("----------------")

# # --- 2 ---
input_list1 = ["CA", "NJ", "RI"]
input_list2 = ["California", "New Jersey", "Rhode Island"]
print(dict(zip(input_list1, input_list2)))
# print({ input_list1[i]: input_list2[i] for i in range(len(input_list1))})
print("----------------")

# # --- 3 ---
input_list = ["a", "e", "i", "o", "u"]
input_dict = {i: 0 for i in input_list}
print(input_dict)
print("----------------")

# # --- 4 ---
input_dict = {
    k + 1:chr(65 + k)
    for k in range(26)
}
print(input_dict)
print("----------------")

# # --- 5 ---
input_str = "awesome sauce"
voy = "aeiou"
input_dict = {
    k: input_str.count(k) for k in voy
}
print(input_dict)
print("----------------")
