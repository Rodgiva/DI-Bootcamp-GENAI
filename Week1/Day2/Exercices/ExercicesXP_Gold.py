import random as r

# --- Exercise 1: Concatenate lists ---
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst = [*lst1, *lst2]
print(lst)
print("--------------------------")

# --- Exercise 2: Range of numbers ---
print([i for i in range(1500,2500) if (i%5 == 0 or i%7 == 0)])
print("--------------------------")

# --- Exercise 3: Check the index ---
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
inp_name = input("What is your name? ")
if inp_name in names:
    print(f"Firstoccurence is {names.index(inp_name)}")
print("--------------------------")

# --- Exercise 4: Greatest Number ---
lst = []
for i in range(1, 4):
    inp = input(f"Input the {i}st number: ")
    lst.append(int(inp))
print(max(lst))
print("--------------------------")

# --- Exercise 5: The Alphabet ---
alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
print(alphabet)
vowels = ["a", "e", "i", "o", "u", "y"]
for c in alphabet:
    if c in vowels:
        print("The letter is a vowel")
    else:
        print("The letter is a consonant")
print("--------------------------")

# --- Exercise 6: Words and letters ---
words = []
for i in range(1,8):
    inp_word = input(f"Give me a word: ({i}) ")
    words.append(inp_word)
letter = input(f"Now give me a letter: ")
for w in words:
    try:
        print(f"First occurence: {w.index(letter)}")
    except:
        print(f"No occurence fount with the letter {letter} in {w}")
print("--------------------------")

# --- Exercise 7: Min, Max, Sum ---
lst = [i for i in range(1,1000001)]
lst_min = min(lst)
lst_max = max(lst)
lst_sum = sum(lst)
print(lst_min)
print(lst_max)
print(lst_sum)
print("--------------------------")

# --- Exercise 8 : List and Tuple ---
inp_nbs = input("Write a sequence of comma-separated numbers: ")
lst_nbs = inp_nbs.split(",")
tpl_nbs = tuple(lst_nbs)
print(lst_nbs)
print(tpl_nbs)
print("--------------------------")

# --- Exercise 9 : Random number ---
inp_nb = int(input("Give me a number betwenn 1 and 9: "))
rnd_nb = r.randint(1,9)
if inp_nb == rnd_nb:
    print("Winner winner! Chicken Dinner!")
else:
    print("Loooooooooooooooooser")

# Bonus
inp_nb = input("Give me a number between 1 and 9: ")
rnd_nb = r.randint(1,9)
while inp_nb != "quit" and int(inp_nb) != rnd_nb:
    print("Nope, try again")
    inp_nb = input("Give me another number between 1 and 9: (tape quit to exit) ")
print("Winner!")

# Bonus2
inp_nb = input("Give me a number between 1 and 9: ")
rnd_nb = r.randint(1,9)
wins = 0
loss = 0
while inp_nb != "quit":
    if int(inp_nb) == rnd_nb:
        print("Winner! Lets continue!")
        rnd_nb = r.randint(1,9)
        wins += 1
    else:
        print("Nope, try again")
        loss += 1
    inp_nb = input("Give me another number between 1 and 9: (tape quit to exit) ")
print(f"Wins: {wins} / Loss: {loss}")

print("--------------------------")
