import random

def number_guessing_game():
    nb_user = -1
    max_attempts = 7
    random_number = random.randint(0, 100)
    for i in range(max_attempts):
        # while 0 <= nb_user <= 100:
        nb_user = int(input("Give me a number between 0 and 100:"))
            # if nb_user > 100 or nb_user < 0:
            #     print("Not in range, try again!")
        if nb_user < random_number:
            print("Too low!")
        elif nb_user > random_number:
            print("Too high!")
        elif nb_user == random_number:
            print("Congratulations! You guessed the right number!")
            return
    print("Game Over")
    return
    
number_guessing_game()