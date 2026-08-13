# --- Exercise 1: Quizz ---
# -> a class is something where we define all the variables(properties) and functions before instanciate it
# -> an instance is an object with attributate values
# -> encapsulation is a practice of encapsulating datas inside a class only, and will not be accessible outside that class. Usefull when we want to protect the datas of an instance: the user will not be able to modify the datas
# -> abstraction: a way to show only the usefull interfaces for the user
# -> inheritance: a way to give all the properties and methods from a class to another one
# -> multiple inheritance: a way to give all the properties and methods from a multiple class to another one
# -> polymorphism: a function from a children class can have a different behavior than his parent class
# -> MRO: this is the order of executions/priorities of methods that is determined for inherances/multiple inheritances

# --- Exercise 2: Create a deck of cards class ---
import random as r
class Card():
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self, suit:str, value:str):
        self.suit = suit
        self.value = value

class Deck():
    def __init__(self, deck = None):
        self.deck = [] if deck == None else list(deck)
        for s in Card.suit:
            for v in Card.value:
                self.deck.append(Card(s, v))

    def shuffle(self):
        if len(self.deck) != 52:
            print(f"{52 - len(self.deck)} are missing from the deck.")
        else:
            r.shuffle(self.deck)

    def deal(self)->Card:
        card = self.deck[0]
        self.deck.pop(0)
        return card

    def show(self):
        for d in self.deck:
            print(f"{d.suit} {d.value}")

a_deck = Deck()
a_deck.show()
print("***")
a_deck.shuffle()
a_deck.show()
print("***")
a_card = a_deck.deal()
print(f"{a_card.suit} - {a_card.value}")
print("***")
a_deck.show()

