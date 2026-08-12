import random as r
import os
import json


# --- 🌟 Exercise 1: Random Sentence Generator ---
def get_words_from_file (path):
    with open(path) as f: 
        txt = f.read()
    return txt

def get_random_sentence(path:str, length:int):
    words = get_words_from_file(path)
    words_list = words.split("\n")
    return " ".join([r.choice(words_list) for i in range(length)])

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "..", "words", "words.txt")

    words = get_words_from_file(path)
    print(words)

    nb_word = int(input("Give me the length you want: (between 2 and 20) "))
    while not 2 <= nb_word <= 20:
        nb_word = int(input("The length is out of range, please try again between 2 and 20: "))

    random_sentence = get_random_sentence(path, nb_word)
    print(random_sentence)

main()
print("--------------------------")

# --- 🌟 Exercise 2: Working with JSON ---
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sample_dict = json.loads(sampleJson)
salary = sample_dict["company"]["employee"]["payable"]["salary"]
sample_dict["company"]["employee"]["birth_date"] = "2026-08-12"
with open("result.txt", "w") as f:
    json.dump(sample_dict, f, indent=4)

print("--------------------------")
