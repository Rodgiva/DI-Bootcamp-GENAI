import random as r
def input_txt(txt):
    if len(txt) < 10:
        print("String not long enough.")
        return True
    elif len(txt) > 10:
        print("String too long.")
        return True
    else:
        print("Perfect string")
        return False
    
inp_txt = input("Give me a string with exactly 10 characters: ")
while input_txt(inp_txt):
    inp_txt = input("Give me a string with exactly 10 characters: ")

print(f"First character: {inp_txt[0]}")
print(f"Last character: {inp_txt[-1]}")

res = ""
for c in inp_txt:
    res += c
    print(res)

lst_txt = list(inp_txt)
r.shuffle(lst_txt)
print("".join(lst_txt))