# --- Exercise 1 : What’s your name ? ---
def get_full_name(first_name:str, last_name:str, middle_name :str = ""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))
print("--------------------------")

# --- Exercise 2 : From English to Morse ---
def morse_convert(txt:str, mode:bool = True)->str:
    txt = txt.upper()
    morse_code = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", " ": "/"
    }
    translated_txt = ""
    if mode == True: # letter to morse
        for c in txt:
            translated_txt += morse_code[c] + " "
    else: # morse to letter
        txt = txt.split(" ")
        inverted_morse_code = {v:k for k,v in morse_code.items()}
        for c in txt:
            translated_txt += inverted_morse_code[c]
        
    return translated_txt

print(morse_convert(".... . .-.. .-.. --- / - .... . .-. .", False))
# print(morse_convert("Hello there"))
print("--------------------------")

#Exercise 3 : Box of stars
def box_printer(*words):
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    max_len += 2
    
    print("".ljust(max_len, "*"))
    for word in words:
        word = word.center(len(word) + 2, " ")
        left_word = word.ljust(max_len - 2, " ")
        line_word = left_word.center(max_len, "*")
        print(line_word)
    print("".ljust(max_len, "*"))
    return
box_printer("Hello", "World", "in", "reallyLongword", "a", "frame")
print("--------------------------")

# --- Exercise 4 : What is the purpose of this code? ---

def insertion_sort(alist):
   for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)

# This program will do an ascendinf sort of numbers