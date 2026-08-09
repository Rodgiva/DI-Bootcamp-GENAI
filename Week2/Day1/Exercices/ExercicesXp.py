# --- 🌟 Exercise 1: Cats ---
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

riri = Cat("Riri", 2)
fifi = Cat("Fifi", 3)
loulou = Cat("Loulou", 4)

cats = (riri, fifi, loulou)

def find_oldest_cat(*cats:Cat)->Cat:
    oldest_cat:Cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(*cats)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
print("--------------------------")

# --- 🌟 Exercise 2 : Dogs ---
class Dog():
    def __init__(self, name:str, height:int):
        self.name:str = name
        self.height:int = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Moka", 70)
sarahs_dog  = Dog("Kiwi", 7)

print(davids_dog.name)
print(sarahs_dog.name)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is higher than {sarahs_dog.name}")
else:
    print(f"{sarahs_dog.name} is higher than {davids_dog.name}")

print("--------------------------")

# --- 🌟 Exercise 3 : Who’s the song producer? ---
class Song():
    def __init__(self, lyrics:list):
        self.lyrics:list = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

lyrics = ("I'll build the coziest lantern","To help you cross the ocean","I want to keep you dry, I want to keep the spark","And if the storm is hitting","I'll try to keep you steady","And if I feel I'm shaking, I would return to practice","And if my arm is hurting","And I if I need to rest","We'd have to switch positions","And you would do it well","We'd light the darkest forest","Brighten our darkest sins","We'd light the deepest cave and","Enlight the deepest meanings","You know I gave my breath, so I could feed it","I blew too hard I thought I killed it","I saw an ember hidden in the ashes","I'll blow again if it can be ignited","I'd build the strongest walls","(So you could feel protected)","Made of the purest glass","('Cause you simply deserve it)","I'll build the coziest home","(And we would learn to live in)","Made of the purest love","('Cause you simply deserve it)","And you could hear the rain banging the ceiling","And not a single drop could stain our feelings","And you could hear the rain banging the ceiling","And not a single drop could stain our feelings","You gave me your trust 'cause you knew I could keep it","The fire's so pure we could learn how to drink it","You gave me your heart cause you knew I could light it","'Cause you know, 'cause you know","'Cause you know, 'cause you know","'Cause you know, 'cause you know","Oh, 'cause you know, 'cause you know")
ember = Song(lyrics)

ember.sing_me_a_song()
print("--------------------------")

# --- 🌟 Exercise 4 : Afternoon at the Zoo ---
class Zoo():
    def __init__(self, zoo_name:str, animals:list=None ):
        self.zoo_name:str = zoo_name
        self.animals:list = [] if animals == None else list(animals)

    def add_animal(self, new_animal:str):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added successfully")
        else:
            print(f"{new_animal} already in the list")
        return self

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold:str):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} sold successfully")
        else:
            print(f"{animal_sold} not found in the list")

    def sort_animals(self) -> dict:
        self.animals.sort()
        sorted_animals = {}
        for animal in self.animals:
            letter = animal[0].upper()
            sorted_animals.setdefault(letter, []).append(animal)
        print("Animals sorted")
        return sorted_animals

    def get_groups(self):
        for k,v in self.sort_animals().items():
            print(f"{k}: {v}")

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Cougar").add_animal("Baboon").add_animal("Cat").add_animal("Zebra").add_animal("Lion").add_animal("Bear").add_animal("Giraffe")

brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Lion")
brooklyn_safari.get_animals()

print("***")
brooklyn_safari.sort_animals()
print("***")
brooklyn_safari.get_groups()
print("--------------------------")
