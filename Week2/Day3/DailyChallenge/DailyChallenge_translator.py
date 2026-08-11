from googletrans import Translator

def translate(txt_list:list):
    translator = Translator()
    a_dict = {}
    for word in txt_list:
        translated_word = translator.translate(word)
        print(translated_word.text)
        a_dict[word] = translated_word.text
    return a_dict

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

print(translate(french_words))