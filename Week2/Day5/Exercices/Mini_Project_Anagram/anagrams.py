from anagram_checker import AnagramChecker

anagram_chk = AnagramChecker()
user_word = input("Give me a word: ('exit' to exit) ").lower()

while user_word != "exit":
    if anagram_chk.is_valid_word(user_word):
        anagrams = anagram_chk.get_anagrams(user_word)
        print(f"Your word: {user_word}\nAnagrams: {anagrams}")
    else:
        print("Word not found")
    user_word = input("Give me another word: ('exit' to exit) ").lower()
