from  ExercicesXp import Dog
import random as r

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