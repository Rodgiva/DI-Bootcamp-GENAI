import random as r

class Game():
    _rock_paper_scissors_list = ["rock", "paper", "scissors"]
    _win_rules = {
        "win": [
            (1, 0),
            (2, 1),
            (0, 2),
        ],
        "draw": [
            (1, 1),
            (2, 2),
            (0, 0),
        ],
        "loss": [
            (0, 1),
            (1, 2),
            (2, 0),
        ],
    }

    def __init__(self):
        self.win:int = 0
        self.draw:int = 0
        self.loss:int = 0

    @staticmethod
    def get_user_item()->str:
        choice = int(input(f"What is your move?\n1. Rock\n2. Paper\n3. Scissors\n"))
        return Game._rock_paper_scissors_list[choice-1]

    @staticmethod
    def get_computer_item()->str:
        return r.choice(Game._rock_paper_scissors_list)

    def get_game_result(self, user_item:str, computer_item:str):
        key_item_user = Game._rock_paper_scissors_list.index(user_item)
        key_item_computer = Game._rock_paper_scissors_list.index(computer_item)
        if (key_item_user, key_item_computer) in Game._win_rules["win"]:
            self.win += 1
            return "win"
        elif (key_item_user, key_item_computer) in Game._win_rules["loss"]:
            self.loss += 1
            return "loss"
        else:
            self.draw += 1
            return "draw"

    def play(self):
        user_item = Game.get_user_item()
        computer_item = Game.get_computer_item()

        print(f"{user_item}(you) - {computer_item}(computer)")
        print(self.get_game_result(user_item, computer_item))

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