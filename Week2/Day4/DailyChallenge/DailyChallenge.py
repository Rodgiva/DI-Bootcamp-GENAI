from functools import reduce
import os
import re
import string

class Text():
    def __init__(self, txt:str):
        self.txt = txt

    def word_frequency(self, word:str)->int:
        words = self.txt.split()
        count = words.count(word)
        return count if count > 0 else None

    def most_common_word(self):
        words = self.txt.split()
        common_words = {}
        for word in words:
            common_words[word] = 1 if word not in common_words else common_words[word] + 1
        res = reduce(lambda a,b: a if a[1] > b[1] else b, common_words.items())
        return res

    def unique_words(self)->set:
        words = self.txt.split()
        unique_words = set(words)
        return unique_words

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as f: 
            txt = f.read()
        return Text(txt)

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "..", "words", "words.txt")
a_txt = Text.from_file(path)
# print(a_txt.unique_words())

class TextModification(Text):
    _stop_words = [
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
        "you", "you're", "you've", "you'll", "you'd", "your", "yours",
        "yourself", "yourselves", "he", "him", "his", "himself", "she",
        "she's", "her", "hers", "herself", "it", "it's", "its", "itself",
        "they", "them", "their", "theirs", "themselves", "what", "which",
        "who", "whom", "this", "that", "that'll", "these", "those", "am",
        "is", "are", "was", "were", "be", "been", "being", "have", "has",
        "had", "having", "do", "does", "did", "doing", "a", "an", "the",
        "and", "but", "if", "or", "because", "as", "until", "while", "of",
        "at", "by", "for", "with", "about", "against", "between", "into",
        "through", "during", "before", "after", "above", "below", "to",
        "from", "up", "down", "in", "out", "on", "off", "over", "under",
        "again", "further", "then", "once", "here", "there", "when",
        "where", "why", "how", "all", "any", "both", "each", "few",
        "more", "most", "other", "some", "such", "no", "nor", "not",
        "only", "own", "same", "so", "than", "too", "very", "s", "t",
        "can", "will", "just", "don", "don't", "should", "should've",
        "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren",
        "aren't", "couldn", "couldn't", "didn", "didn't", "doesn",
        "doesn't", "hadn", "hadn't", "hasn", "hasn't", "haven",
        "haven't", "isn", "isn't", "ma", "mightn", "mightn't", "mustn",
        "mustn't", "needn", "needn't", "shan", "shan't", "shouldn",
        "shouldn't", "wasn", "wasn't", "weren", "weren't", "won",
        "won't", "wouldn", "wouldn't"
    ]

    def __init__(self, txt):
        super().__init__(txt)

    def remove_punctuation(self)->str:
        self.txt = re.sub(f"[{re.escape(string.punctuation)}]", "", self.txt)
        return self.txt

    def remove_stop_words(self)->str:
        words = self.txt.split()
        return " ".join(filter(lambda w: w.lower() not in TextModification._stop_words, words))

    def remove_special_characters(self)->str:
        words = self.txt.split()
        return " ".join(filter(lambda w: w not in string.punctuation, words))


a_modified_txt = TextModification(path)
print(a_modified_txt.remove_punctuation())
