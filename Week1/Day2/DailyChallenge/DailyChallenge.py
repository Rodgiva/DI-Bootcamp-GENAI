# # --- Challenge 1: Multiples of a Number ---

# inp_nb = int(input("Give me a number: "))
# inp_length = int(input("Give me a length: "))

# def multiples(nb, length):
#     res = []
#     for i in range(1,length + 1):
#         res.append(nb*i)
#     return res
# print(multiples(inp_nb, inp_length))

# --- Challenge 2: Remove Consecutive Duplicate Letters ---
inp_str = input("Give me a string: ")
def rmv_dup_letters(txt):
    res = ""
    for i in range(len(txt)):
        if i == 0 or txt[i] != txt[i-1]:
            res += txt[i]
    return res
print(rmv_dup_letters(inp_str))