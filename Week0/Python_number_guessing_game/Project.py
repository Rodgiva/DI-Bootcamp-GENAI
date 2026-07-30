import random

def number_guessing_game():
    nb_user = -1
    max_attempts = 7
    random_number = random.randint(1, 100)
    for i in range(max_attempts):
        check = True
        while check:
            try:
                input_user = input("Give me a number between 1 and 100:")
                nb_user = int(input_user)
                if nb_user < 0:
                    print("You picked a number below 0, please try again")
                if nb_user > 100:
                    print("You picked a number above 100, please try again")
                    check = True
                else:
                    check = False
            except Exception as e:
                if input_user == '':
                    print("Empty input, please try again")
                else:
                    print("The input is a string, please put a number")
                check = True

        if nb_user < random_number:
            print("Too low!")
        elif nb_user > random_number:
            print("Too high!")
        else:
            print(random_number)
            print("**********************************************")
            print("Congratulations! You guessed the right number!")
            print(f"Number times of attempt: {i+1}")
            print("**********************************************")
            return
        
    print(f"The right number was {random_number}")
    print("Game Over")
    return
    
number_guessing_game()