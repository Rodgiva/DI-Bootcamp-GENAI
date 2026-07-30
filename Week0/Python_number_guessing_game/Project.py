import random

def number_guessing_game():
    nb_user = -1
    max_attempts = 7
    random_number = random.randint(1, 100)
    for i in range(max_attempts):
        try:
            nb_user = int(input("Give me a number between 1 and 100:"))
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return
        if nb_user < random_number:
            print("Too low!")
        elif nb_user > random_number:
            print("Too high!")
        elif nb_user == random_number:
            print("Congratulations! You guessed the right number!")
            print(f"Number times of attempt: {i+1}")
            return
        
    print(f"The right number was {random_number}")
    print("Game Over")
    return
    
number_guessing_game()