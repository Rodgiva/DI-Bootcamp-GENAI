# --- Exercise 1 : Use the terminal ---
# PATH variable are variables where the paths are stored, it is useful when you want, for example, call python.exe, you just have to call "Python" without calling all the path where he is located

# --- Exercise 2 : Alias ---

# --- Exercise 3 : Outputs ---

print(3 <= 3 < 9) #True
print(3 == 3 == 3) #True
print(bool(0)) #False
print(bool(5 == "5")) #False
print(bool(4 == 4) == bool("4" == "4")) #True
print(bool(bool(None))) #False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x) #True
print("y is", y) #False
print("a:", a) #5
print("b:", b) #10

# --- Exercise 4 : How many characters in a sentence ? ---
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text.split()))

# --- Exercise 5: Longest word without a specific character ---
inp_txt = input("Give me the longest sentence you can without the character “A”:")
if a in inp_txt.lower():
    print("Character “A” found:!")
else:
    print("This is a congratulations message... Good job!!!")