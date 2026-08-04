import sys

# --- Exercise 1: Formula ---
C = 50
H = 30
inp_nb_lst = input("Give me a comma-separated string of numbers: ").split(",")
res_lst = []
for D in inp_nb_lst:
    Q = ((2*C*int(D))/H)**0.5
    res_lst.append(int(Q))
print(res_lst)
print("--------------------------")

# --- Exercise 2 : List of integers ---
#1
lst = [3, 47, 99, -80, 22, 97, 3, 7, 54, -23, 5, 7]
#2
print(*lst)
lst.sort(reverse=True)
print(lst)
print(sum(lst))
#3
lst1 = [lst[0], lst[-1]]
print(lst1)
#4
lst2 = [i for i in lst if i > 50]
print(lst2)
#5
lst3 = [i for i in lst if i < 10]
print(lst3)
#6
lst4 = [i**2 for i in range(1,4)]
print(lst4)
#7
lst5 = list(set(lst))
print(len(lst5))
#8
lst_avg = sum(lst)/len(lst)
print(lst_avg)
#9
lst_max = max(lst)
print(lst_max)
#10
lst_min = min(lst)
print(lst_min)
#11 sum, average, largest and smallest
lst_sum = 0
for i in lst:
    lst_sum += i
print(lst_sum)

lst_avg = sum(lst)/len(lst)
print(lst_avg)

lst_max = -(sys.maxsize)
for i in lst:
    if i > lst_max:
        lst_max = i
print(lst_max)

lst_min = sys.maxsize
for i in lst:
    if i < lst_min:
        lst_min = i
print(lst_min)
print("--------------------------")

# --- Exercise 3: Working on a paragraph ---
#1, 2
txt = "I spent too many nights filling in the blanks\nI turned too many drafts into paper planes\nI always rack my brain but I know in the end\nThey will never notice, they won't give a Booooop\nAlways overthinking, I'm the one to blame\nI want to sound smart, they just want to dance\nSo let me try for once, let me grab my pen\nLet me write you down what I think of it\nBiiiiiip the lyrics yeah\nBiiiiiip the lyrics yeah\nBiiiiiip the lyrics yeah\nCome on Biiiiiip the lyrics\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics\nCause no one cares\nCause no one cares\nBut you\nI've always found it hard to remember the words\nEven my own songs, I always mess it up\nLet me tell you what: I think it's over\nForget it, that's the answer\nYou can't forget the lyrics if there are no lyrics\nOh, smart\nShakespeare\nAh mais oui\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics\nCause no one cares\nCause no one cares\nBut you\nNo one cares\nI spent too many nights filling in the blanks\nI turned too many drafts into paper planes\nI always rack my brain, but I know in the end\nThey will never notice, they won't give a Booooop\nAlways overthinking, I'm the one to blame\nI wanted to sound smart, they just wanted to dance\nSo let me try for once, let me grab my pen\nLet me write you down what I think of it\nYeah\nCome on yeah\nBiiiiiip the lyrics, Biiiiiip the lyrics\nYeah\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip the lyrics, Biiiiiip the lyrics\nBiiiiiip it"
#3
print(f"*********************************************\n{txt}\n*********************************************")
#4
chars = txt.replace("\n", " ")
print(len(chars))
#5
sentence_list = txt.split("\n")
print(len(sentence_list))
#6
words_list = txt.replace("\n", " ").split(" ")
print(len(words_list))
#7
unique_words_list = set(words_list)
print(len(unique_words_list))
#8
char_list2 = chars.replace(" ", "")
print(len(char_list2))
#9
count_words = 0
for words in sentence_list:
    count_words += len(words.split(" "))
avg_words = count_words/len(sentence_list)
print(avg_words)
#10
words = txt.lower().split()
# print(words)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
non_unique_word = sum(1 for count in word_count.values() if count > 1)
print(non_unique_word)

print("--------------------------")

# --- Exercise 4 : Frequency Of The Words ---
input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = input.lower().replace(".", "").replace("?", "").split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
for k, v in word_count.items():
    print(f"{k}:{v}")
print("--------------------------")

