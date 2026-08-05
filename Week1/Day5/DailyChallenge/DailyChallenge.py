# --- Challenge 1: Sorting ---
word = input("Give me some word separated by commas: ")
lst_word = word.split(",")
lst_word.sort()
sorted_word = ",".join(lst_word)
print(sorted_word)
print("--------------------------")

# --- Challenge 2: Longest Word ---
def longest_word(sentence:str)->str:
    lst_words = sentence.split(" ")
    longest = ""
    for w in lst_words:
        if len(w) > len(longest):
            longest = w
    return longest
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))