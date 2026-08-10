import random as r

# --- 🌟 Exercise 1: Pets ---
class Cat():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def talk(self, txt:str = ""):
        print(txt)

    def walk(self):
        return f'{self.name} is walking!'

class Bengal(Cat):
    def talk(self):
        print("Hum wouf, hehe...")

class Chartreux(Cat):
    def talk(self):
        print("Eh je dirais... wouf.")

class Siamese(Cat):
    def talk(self):
        print("Eh... wouf! Hehehe...")

class Pets():
    def __init__(self, animals = None):
        self.animals = [] if animals == None else list(animals)

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

all_cats = [Bengal("Bangbang", 2), Chartreux("Baguette", 3), Siamese("Minou", 4)]
sara_pets = Pets(all_cats)
sara_pets.walk()
print("--------------------------")

# --- 🌟 Exercise 2: Dogs ---
class Dog():
    def __init__(self, name:str, age:int, weight:int):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog:Dog):
        if other_dog.run_speed() * other_dog.weight > self.run_speed() * self.weight:
            return f"{other_dog.name} won the fight"
        else:
            return f"{self.name} won the fight"


dog1 = Dog("Kiwi", 6, 9)
dog2 = Dog("Rantampla", 15, 40)

dog1.bark()
print(dog2.run_speed())
print(dog1.fight(dog2))
print("--------------------------")

# --- 🌟 Exercise 3: Dogs Domesticated ---
class PetDog(Dog):
    def __init__(self, name:str, age:int, weight:int, trained:bool = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        print(f"{", ".join(args)} all play together")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            print(f"{self.name} {r.choice(tricks)}")
# dogs = [dog1, dog2]

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()
print("--------------------------")

# --- 🌟 Exercise 4: Family and Person Classes ---
class Person():
    def __init__(self, first_name:str, age:int, last_name:str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_18(self)->bool:
        return True if self.age >= 18 else False

class Family():
    def __init__(self, last_name:str, members = None):
        self.last_name = last_name 
        self.members = [] if members == None else list(members)

    def born(self, first_name:str, age:int):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        # return filter(lambda x: x.is_18(), self.members)
        for member in self.members:
            if first_name == member.first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        print(f"Welcome the the {self.last_name}' family")
        for member in self.members:
            print(f" * {member.first_name} {member.age} years old")

partouche = Family("Partouche")
persons = [
    Person("Avigdor", 33),
    Person("Naomi", 30),
    Person("Noa", 28),
    Person("Kiwi", 6),
]

for person in persons:
    partouche.born(person.first_name, person.age)

for person in partouche.members:
    partouche.check_majority(person.first_name)

partouche.family_presentation()
print("--------------------------")

