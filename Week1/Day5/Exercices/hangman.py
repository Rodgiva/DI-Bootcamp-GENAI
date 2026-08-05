import random


def rand_word()->str:
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    return random.choice(wordslist)

def init_word(word:str)->str:
    return "*" * len(word)

def is_letter_in_word(hidden_word:str, letter:str)->bool:
    return letter in hidden_word

def place_letters(hidden_word:str, guess_word:str, letter:str)->str:
    lst_word = list(guess_word)
    for i in range(len(hidden_word)):
        if hidden_word[i] == letter:
            lst_word[i] = letter
    return "".join(lst_word)

def check_win(hidden_word:str, guess_word:str)->bool:
    if hidden_word == guess_word:
        return True
    return False

def display_hangman(life:int):
    state = ["  O", "\n /", "|", "\\", "\n /", " \\\n------"]
    if (life < 6):
        print("------\n  |")
        print("".join(state[:(6-life)]))

# Notes for me:
# hidden_word: the word to find
# guess_word: the word we actually know

def game_loop():
    hidden_word = rand_word()
    guess_word = init_word(hidden_word)
    guessed_letter = []
    win = False
    life = 6
    while life > 0 and not win:
        print("\nLife:" + ("\u2764\ufe0f " * life))
        print(guess_word)
        print(f"Letter used: {",".join(guessed_letter)}\n")
        inp_letter = input("Give me a letter: ")

        while inp_letter in guessed_letter:
            inp_letter = input("You have already used, try another letter: ")

        guessed_letter.append(inp_letter)
        if is_letter_in_word(hidden_word, inp_letter):
            guess_word = place_letters(hidden_word, guess_word, inp_letter)
            win = check_win(hidden_word, guess_word)
        else:
            print("Wrong! ")
            life -= 1
            display_hangman(life)
    if win:
        print("You win!")
    else:
        print("You loose...")
        print(f"The word was: {hidden_word}")

game_loop()