class AnagramChecker():
    def __init__(self):
        with open("words.txt", "r") as f:
            self.words = f.read().lower().split("\n")

    def is_valid_word(self, word:str)->bool:
        return True if word in self.words else False

    @staticmethod
    def is_anagram(word1:str, word2:str)->bool:
        word1_list = list(word1)
        word1_list.sort()

        word2_list = list(word2)
        word2_list.sort()

        return True if "".join(word1_list) == "".join(word2_list) else False

    def get_anagrams(self, word)->list:
        anagrams = []
        words = self.words
        for w in words:
            if AnagramChecker.is_anagram(w, word) and w != word:
                anagrams.append(w)
        return anagrams