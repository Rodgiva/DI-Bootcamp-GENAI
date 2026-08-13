from game import Game

def get_user_menu_choice()->int:
    while True:
        try:
            choice = int(input("*** Rock/Paper/Scissors's Menu ***\n1. Play a new game\n2. Show scores\n3. Quit\n"))
        except ValueError:
            continue
        else:
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please chose an option between 1 and 3")
        

def print_results(results:dict):
    print(f"*****\nWins: {results['wins']}\nLoss: {results['loss']}\nDraw: {results['draw']}\n*****")

def main():
    user_choice = int(get_user_menu_choice())
    scores = {
        "wins": 0,
        "loss": 0,
        "draw": 0,
    }
    a_game = Game()
    while user_choice != 3:
        if user_choice == 1:
            a_game.play()
            scores = {
                "wins": a_game.win,
                "loss": a_game.loss,
                "draw": a_game.draw,
            }
        elif user_choice == 2:
            print_results(scores)

        user_choice = get_user_menu_choice()

    print("Thanks for playing!")
    
if __name__ == "__main__":
    main()