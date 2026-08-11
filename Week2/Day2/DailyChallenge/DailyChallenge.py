import math as m

class Pagination():
    def __init__(self, page_size:int = 10, items = ""):
        self.page_size = page_size
        if items == "":
            self.items = []
        else:
            self.items = list(items)
        # self.items = [] if items == None else list(items)
        
        self._current_idx = 0
        self._nb_page = m.ceil(len(items)/self.page_size)

    def  get_visible_items(self):
        start = self.page_size*self._current_idx
        end = self.page_size*(self._current_idx+1)
        return self.items[start : end]

    def go_to_page(self, page_num:int):
        if (page_num * self.page_size) + self.page_size-1 > len(self.items):
            raise ValueError("The page number is out of range")
        self._current_idx = page_num - 1
        return self

    def first_page(self):
        self._current_idx = 0
        return self

    def last_page(self):
        self._current_idx = self._nb_page - 1
        return self

    def next_page(self):
        if self._current_idx <= self._nb_page - 1:
            self._current_idx += 1
        return self

    def previous_page(self):
        if self._current_idx > 0:
            self._current_idx -= 1
        return self

    def __str__(a_list:list, length:int):
        return "".join(a_list[:length-1])


alphabetList = [
    "dog", "cat", "elephant", "lion", "tiger",
    "giraffe", "zebra", "horse", "cow", "pig",
    "sheep", "goat", "rabbit", "fox", "wolf",
    "bear", "deer", "monkey", "gorilla", "kangaroo",
    "koala", "panda", "penguin", "eagle", "owl",
    "dolphin", "whale", "shark", "octopus", "crocodile",
]
p = Pagination(4, alphabetList)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

# p.next_page()
# print(p.get_visible_items())
# # ['e', 'f', 'g', 'h']

# p.last_page()
# print(p.get_visible_items())
# # ['y', 'z']

# # p.go_to_page(10)
# # print(p.current_idx + 1)
# # Output: ValueError

# p.go_to_page(0)
# # Raises ValueError

# p.next_page()
# p.next_page()
# p.next_page()
# p.get_visible_items()

# p.next_page().next_page().next_page().get_visible_items()
# print(p.get_visible_items())
